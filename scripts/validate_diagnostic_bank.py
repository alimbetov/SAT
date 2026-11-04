#!/usr/bin/env python3
"""Static qualification gate for the 225-item SAT diagnostic Markdown bank.

No third-party dependencies. This verifies format, uniqueness, coverage, answer-key
presence and segregation, NOT independent pedagogical validity or psychometrics.
Run from repository root: python3 scripts/validate_diagnostic_bank.py
"""
from __future__ import annotations

import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
D = ROOT / "diagnostic"

BANK_FILES = {
    "bank/math_algebra.md": 4,
    "bank/math_advanced.md": 9,
    "bank/math_data_analysis.md": 7,
    "bank/math_geometry.md": 4,
    "bank/english_a1.md": 4,
    "bank/english_a2.md": 4,
    "bank/english_b1.md": 4,
    "bank/english_b2.md": 4,
}
TOPIC_RE = r"(?:ALG|ADV|PSD|GEO|EN-[AB][12])-\d\d"
failures: list[str] = []
counts: collections.Counter[str] = collections.Counter()
all_ids: set[str] = set()
seen_topics: set[str] = set()


def check(ok: bool, message: str) -> None:
    if not ok:
        failures.append(message)


def student_options(fragment: str, label: str, required_q: int) -> None:
    """Check exactly four nonduplicated lettered options per question."""
    starts = list(re.finditer(r"^\*\*(?:[A-Z0-9-]+-)?Q[1-5]\*\*[ \t]*$", fragment, re.M))
    check(len(starts) == required_q, f"{label}: student question headings {len(starts)} != {required_q}")
    for i, match in enumerate(starts):
        chunk = fragment[match.end() : (starts[i + 1].start() if i + 1 < len(starts) else len(fragment))]
        options = re.findall(r"^([ABCD])\)\s+(.+)$", chunk, re.M)
        letters = [x[0] for x in options]
        values = [x[1].strip() for x in options]
        check(letters == list("ABCD"), f"{label}: question {i+1} option labels {letters} != ABCD")
        check(len(set(values)) == 4, f"{label}: question {i+1} duplicated answer texts")
    check("<u>" not in fragment and "<strong>" not in fragment, f"{label}: student fragment reveals key markup")


def check_bank(path: str, expected_topic_count: int) -> None:
    content = (D / path).read_text(encoding="utf-8")
    segments = list(re.finditer(rf"^## ({TOPIC_RE}) — .+$", content, re.M))
    check(len(segments) == expected_topic_count, f"{path}: topics {len(segments)} != {expected_topic_count}")
    for idx, heading in enumerate(segments):
        topic = heading.group(1)
        check(topic not in seen_topics, f"{path}: duplicate topic {topic}")
        seen_topics.add(topic)
        body = content[heading.end() : (segments[idx + 1].start() if idx + 1 < len(segments) else len(content))]
        check(body.count("<details>") == 1 and body.count("</details>") == 1, f"{topic}: one closed teacher key required")
        if "<details>" not in body:
            continue
        student, teacher = body.split("<details>", 1)
        ids = re.findall(rf"^\*\*({re.escape(topic)}-Q[1-5])\*\*[ \t]*$", student, re.M)
        expected_ids = [f"{topic}-Q{i}" for i in range(1, 6)]
        check(ids == expected_ids, f"{topic}: question IDs expected {expected_ids}, got {ids}")
        for qid in ids:
            check(qid not in all_ids, f"duplicate question ID {qid}")
            all_ids.add(qid)
        student_options(student, topic, 5)
        keys = re.findall(r"^\d+\.\s+<u>\*\*([ABCD])\)\s+(.+?)\*\*</u>\.\s+(.+)$", teacher, re.M)
        check(len(keys) == 5, f"{topic}: teacher keys {len(keys)} != 5")
        for no, (_, answer, rationale) in enumerate(keys, start=1):
            check(bool(answer.strip()) and len(rationale.strip()) >= 25, f"{topic}: weak rationale Q{no}")
        counts["bank"] += len(ids)


def check_pilot_math() -> None:
    text = (D / "PILOT_MATH_LINEAR_EQUATIONS.md").read_text(encoding="utf-8")
    before, teacher = text.split("<details>", 1)
    # Student test precedes answer sheet.
    student = before.split("## Student test", 1)[1].split("## Answer sheet", 1)[0]
    student_options(student, "math pilot", 5)
    ids = re.findall(r"^\*\*(ALG-01-Q[1-5])\*\*[ \t]*$", student, re.M)
    check(ids == [f"ALG-01-Q{i}" for i in range(1, 6)], "math pilot: Q1–Q5 missing")
    check("ALG-01" not in seen_topics, "math pilot duplicate topic")
    seen_topics.add("ALG-01")
    for qid in ids:
        check(qid not in all_ids, f"duplicate ID {qid}")
        all_ids.add(qid)
    check(len(re.findall(r"\*\*Q[1-5] — <u>[ABCD]\)", teacher)) == 5, "math pilot key count != 5")
    counts["pilot_math"] += len(ids)


def check_pilot_english() -> None:
    text = (D / "PILOT_ENGLISH_A1_B2.md").read_text(encoding="utf-8")
    chunks = list(re.finditer(r"^## (A1|A2|B1|B2) / (EN-[AB][12]-\d\d) —", text, re.M))
    check(len(chunks) == 4, "english pilot: expected 4 topical sections")
    for i, heading in enumerate(chunks):
        topic = heading.group(2)
        body = text[heading.end() : chunks[i + 1].start() if i + 1 < len(chunks) else len(text)]
        check("<details>" in body and "</details>" in body, f"{topic}: missing closed teacher key")
        if "<details>" not in body:
            continue
        student, teacher = body.split("<details>", 1)
        student_options(student, topic, 5)
        check(len(re.findall(r"^\*\*Q[1-5]\*\*[ \t]*$", student, re.M)) == 5, f"{topic}: student Q1–Q5 missing")
        check(topic not in seen_topics, f"english pilot duplicate topic {topic}")
        seen_topics.add(topic)
        for j in range(1, 6):
            qid = f"{topic}-Q{j}"
            check(qid not in all_ids, f"duplicate ID {qid}")
            all_ids.add(qid)
        key_count = len(re.findall(r"^\d+\.\s+<u><strong>[ABCD]\)", teacher, re.M))
        check(key_count == 5, f"{topic}: teacher key count {key_count} != 5")
        counts["pilot_english"] += 5


def main() -> int:
    for path, expected_count in BANK_FILES.items():
        check_bank(path, expected_count)
    check_pilot_math()
    check_pilot_english()
    math_blueprint = (D / "MATH_BLUEPRINT.md").read_text(encoding="utf-8")
    english_blueprint = (D / "ENGLISH_BLUEPRINT.md").read_text(encoding="utf-8")
    math_topics = set(re.findall(r"^\| ((?:ALG|ADV|PSD|GEO)-\d\d) \|", math_blueprint, re.M))
    english_topics = set(re.findall(r"^\| (EN-[AB][12]-\d\d) \|", english_blueprint, re.M))
    expected = math_topics | english_topics
    check(len(math_topics) == 25, f"Math blueprint is {len(math_topics)} topics, expected 25")
    check(len(english_topics) == 20, f"English blueprint is {len(english_topics)} topics, expected 20")
    check(seen_topics == expected, f"topic mismatch: missing {sorted(expected-seen_topics)}, unexpected {sorted(seen_topics-expected)}")
    check(counts["bank"] == 200, f"new bank count {counts['bank']} != 200")
    check(counts["pilot_math"] == 5 and counts["pilot_english"] == 20, "pilot question counts incorrect")
    check(len(all_ids) == 225, f"unique question IDs {len(all_ids)} != 225")
    if failures:
        for problem in failures:
            print("FAIL:", problem, file=sys.stderr)
        print(f"Diagnostic bank FAIL ({len(failures)} errors)", file=sys.stderr)
        return 1
    print("PASS: 45 topics, 225 unique questions (125 Math + 100 English),")
    print("      A–D option structure and 225 teacher-only keys checked.")
    print("NOTE: human subject-matter review, calibration, and child piloting remain pending.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
