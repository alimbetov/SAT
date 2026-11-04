#!/usr/bin/env python3
"""Generate isolated D2 student/teacher sheets and a 225-row blind review ledger.

Usage: python scripts/build_d2_pilot.py [--topics ALG-01,PSD-02,EN-A1-01 | all]
Outputs under ignored build/d2/. No student data is stored in Git.
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    "PILOT_MATH_LINEAR_EQUATIONS.md", "PILOT_ENGLISH_A1_B2.md",
    "bank/math_algebra.md", "bank/math_advanced.md",
    "bank/math_data_analysis.md", "bank/math_geometry.md",
    "bank/english_a1.md", "bank/english_a2.md",
    "bank/english_b1.md", "bank/english_b2.md",
]
TOPIC = r"(?:ALG|ADV|PSD|GEO|EN-[AB][12])-\d\d"
BANK_HEAD = re.compile(rf"^## ({TOPIC}) — (.+)$", re.M)
PILOT_HEAD = re.compile(rf"^## (A1|A2|B1|B2) / ({TOPIC}) — (.+)$", re.M)
QHEAD = re.compile(r"^\*\*((?:[A-Z0-9-]+-)?Q[1-5])\*\*[ \t]*$", re.M)
OPTIONS = re.compile(r"^([ABCD])\)\s+(.+?)\s*$", re.M)
KEY = re.compile(r"^(\d+)\. <u>\*\*([ABCD])\) (.+?)\*\*</u>\. (.+)$", re.M)
PILOT_EN_KEY = re.compile(r"^(\d+)\. <u><strong>([ABCD])\) (.+?)</strong></u>\. (.+)$", re.M)
PILOT_MATH_KEY = re.compile(r"^\*\*Q(\d+) — <u>([ABCD])\) (.+?)</u>\.\*\* (.+)$", re.M)

def parse_topic(topic_id, name, source, body, kind="bank"):
    if "<details>" not in body or "</details>" not in body:
        raise ValueError(f"{topic_id}: missing closed teacher key")
    student, teacher = body.split("<details>", 1)
    if kind == "math_pilot":
        student = student.split("## Answer sheet", 1)[0]
    heads = list(QHEAD.finditer(student))
    if len(heads) != 5:
        raise ValueError(f"{topic_id}: expected five questions, got {len(heads)}")
    answers_re = PILOT_MATH_KEY if kind == "math_pilot" else PILOT_EN_KEY if kind == "english_pilot" else KEY
    keys = answers_re.findall(teacher)
    if len(keys) != 5:
        raise ValueError(f"{topic_id}: expected five answers, got {len(keys)}")
    result = []
    for idx, head in enumerate(heads):
        question_id = head.group(1)
        if question_id.startswith("Q"):
            question_id = f"{topic_id}-{question_id}"
        if question_id != f"{topic_id}-Q{idx + 1}":
            raise ValueError(f"{topic_id}: misnumbered question {question_id}")
        chunk = student[head.end():heads[idx + 1].start() if idx < 4 else len(student)].strip()
        options = OPTIONS.findall(chunk)
        if [o[0] for o in options] != list("ABCD"):
            raise ValueError(f"{question_id}: expected options A/B/C/D")
        num, letter, correct_text, explanation = keys[idx]
        if int(num) != idx + 1:
            raise ValueError(f"{question_id}: key order mismatch")
        option_text = options[ord(letter) - ord("A")][1]
        norm = lambda s: re.sub(r"\s+", " ", s.replace(chr(96), "").strip())
        if norm(option_text) != norm(correct_text):
            raise ValueError(f"{question_id}: key/option text mismatch: {option_text!r} != {correct_text!r}")
        if len(explanation.strip()) < 18:
            raise ValueError(f"{question_id}: rationale missing")
        result.append((question_id, chunk, letter, correct_text, explanation))
    return {"id": topic_id, "name": name, "source": source, "questions": result}

def load_all():
    topics = {}
    for source in FILES:
        text = (ROOT / "diagnostic" / source).read_text(encoding="utf8")
        if source.startswith("PILOT_MATH"):
            sections = [("ALG-01", "Linear equations", text.split("## Student test", 1)[1], "math_pilot")]
        elif source.startswith("PILOT_ENGLISH"):
            matches = list(PILOT_HEAD.finditer(text))
            sections = [(h.group(2), h.group(3), text[h.end():matches[i+1].start() if i+1<len(matches) else len(text)], "english_pilot") for i,h in enumerate(matches)]
        else:
            matches = list(BANK_HEAD.finditer(text))
            sections = [(h.group(1), h.group(2), text[h.end():matches[i+1].start() if i+1<len(matches) else len(text)], "bank") for i,h in enumerate(matches)]
        for topic_id,name,body,kind in sections:
            if topic_id in topics:
                raise ValueError(f"duplicate topic: {topic_id}")
            topics[topic_id] = parse_topic(topic_id, name, source, body, kind)
    if len(topics) != 45 or sum(len(t["questions"]) for t in topics.values()) != 225:
        raise ValueError("incomplete corpus: expected 45 topics, 225 questions")
    return topics

def student_sheet(t):
    out = [f"# Diagnostic: {t['id']} — {t['name']}", "",
        "Student code: ______  Attempt: ______  Date/timezone: ______", "",
        "Topic started: ______  Finished: ______  Pause (seconds): ______", "",
        "Choose one answer A–D. No hints; do not view teacher material.", ""]
    for qid,body,*_ in t["questions"]:
        out += [f"## {qid}", "", body, ""]
    out += ["## Answer record", "", "| ID | Answer A/B/C/D | Confidence 1–3 |", "|---|---|---|"]
    out += [f"| {qid} | ______ | ______ |" for qid,*_ in t["questions"]]
    sheet = "\n".join(out)+"\n"
    if re.search(r"<details>|<u>|<strong>|Teacher-only|answer key", sheet, re.I):
        raise ValueError(f"{t['id']}: answer key leaked to student sheet")
    return sheet

def teacher_sheet(t):
    out = [f"# Teacher-only: {t['id']} — {t['name']}", "", "Only reveal after recording all answers.", ""]
    for qid,_,letter,answer,why in t["questions"]:
        out += [f"## {qid}", "", f"Answer: <u>**{letter}) {answer}**</u>.", "", f"Explanation: {why}", ""]
    return "\n".join(out)+"\n"

def write_ledger(topics, destination):
    names = ["topic_id","question_id","subject","source_file","revision","reviewer_code",
        "blind_answer","key_checked","unique_correct","distractors_plausible",
        "explanation_correct","topic_alignment","age_language_appropriate",
        "decision","issue_code","reviewer_note","reviewed_at"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=names)
        writer.writeheader()
        for t in topics.values():
            for qid,*_ in t["questions"]:
                writer.writerow({"topic_id":t["id"],"question_id":qid,
                    "subject":"English" if t["id"].startswith("EN-") else "Math",
                    "source_file":t["source"],"revision":"v1.0-draft","decision":"PENDING"})

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topics",default="ALG-01,ALG-02,PSD-02,EN-A1-01,EN-A2-01")
    parser.add_argument("--out-dir",type=Path,default=ROOT/"build"/"d2")
    args = parser.parse_args()
    topics = load_all()
    chosen = sorted(topics) if args.topics=="all" else [x.strip() for x in args.topics.split(",") if x.strip()]
    if len(chosen)!=len(set(chosen)) or any(x not in topics for x in chosen):
        parser.error("Invalid or duplicate topic ID")
    for topic_id in chosen:
        t = topics[topic_id]
        for folder,name,contents in [
            ("student",f"{topic_id}.md",student_sheet(t)),
            ("teacher",f"{topic_id}_key.md",teacher_sheet(t))]:
            destination = args.out_dir/folder/name
            destination.parent.mkdir(parents=True,exist_ok=True)
            destination.write_text(contents,encoding="utf-8")
    write_ledger(topics,args.out_dir/"review"/"blind_review_225.csv")
    print(f"PASS: 45 topics/225 questions. {len(chosen)} separated student/teacher packets.")
    print("Generated independent reviewer ledger with 225 PENDING rows.")
    print(f"Output directory: {args.out_dir}")

if __name__=="__main__":
    main()
