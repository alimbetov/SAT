#!/usr/bin/env python3
"""Build and validate Kazakh-school SAT diagnostic starter packets.

No external libraries and no child data. Source: diagnostic/kz_school/*.json.
Student papers have NO answer keys or explanations. The teacher-only papers are
generated separately. Kazakh is the primary math-test language; Russian is an
optional parallel version, and English grammar questions remain in English.

Usage:
  python scripts/build_kz_school_pilot.py
  python scripts/build_kz_school_pilot.py --grade grade6 --locale kk
  python scripts/build_kz_school_pilot.py --check-only
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "diagnostic" / "kz_school"
SOURCE_FILES = ["foundation_questions.json", "sat_math_questions.json", "english_questions.json"]
TRACKS = {
    "grade6": ["KZ-FND-01", "KZ-FND-02", "PSD-01", "EN-A1-01", "EN-A1-02"],
    "grade9": ["ALG-01", "ALG-02", "PSD-02", "EN-A2-01", "EN-B1-02"],
}
EXPECTED_IDS = {
    "KZ-FND-01", "KZ-FND-02", "ALG-01", "ALG-02", "PSD-01", "PSD-02",
    "EN-A1-01", "EN-A1-02", "EN-A2-01", "EN-B1-02",
}

def load_bank():
    bank = {}
    seen_ids = set()
    for file_name in SOURCE_FILES:
        content = json.loads((D / file_name).read_text(encoding="utf-8"))
        if content.get("schema_version") != "kz-school-pilot/1":
            raise ValueError(f"Bad schema_version in {file_name}")
        if content.get("bank_revision") != "kz-pilot-0.1":
            raise ValueError(f"Unexpected bank revision in {file_name}")
        subject = content["subject"]
        if subject not in {"math", "english"}:
            raise ValueError("Unknown subject")
        for topic in content["topics"]:
            tid = topic["topic_id"]
            if tid in bank:
                raise ValueError(f"Duplicate topic {tid}")
            if len(topic["questions"]) != 5:
                raise ValueError(f"{tid}: expected 5 questions")
            for j, q in enumerate(topic["questions"], 1):
                qid = f"{tid}-Q{j}"
                if q["id"] != qid or qid in seen_ids:
                    raise ValueError(f"Invalid/duplicate question ID {qid}")
                seen_ids.add(qid)
                if q["key"] not in "ABCD" or len(q["key"]) != 1:
                    raise ValueError(f"{qid}: key must be A–D")
                if subject == "math":
                    for lang in ["kk", "ru"]:
                        if not q.get(f"stem_{lang}"):
                            raise ValueError(f"{qid}: missing {lang} stem")
                        options = q[f"options_{lang}"]
                        if len(options) != 4 or len(set(options)) != 4:
                            raise ValueError(f"{qid}: invalid {lang} options")
                else:
                    if not q.get("stem_en"):
                        raise ValueError(f"{qid}: English stem missing")
                    options = q["options_en"]
                    if len(options) != 4 or len(set(options)) != 4:
                        raise ValueError(f"{qid}: English options invalid")
                for lang in ["kk", "ru"]:
                    if len(q[f"explanation_{lang}"].strip()) < 30:
                        raise ValueError(f"{qid}: explanation_{lang} too short")
            bank[tid] = dict(topic, subject=subject)
    if set(bank) != EXPECTED_IDS or len(seen_ids) != 50:
        raise ValueError(f"Expected 10 topics/50 questions, got {len(bank)} topics/{len(seen_ids)} questions")
    for grade, ids in TRACKS.items():
        if not set(ids).issubset(bank) or len(ids) != 5 or len(set(ids)) != 5:
            raise ValueError(f"Bad track {grade}")
    return bank

def label(grade, locale):
    grade_number = 6 if grade == "grade6" else 9
    if locale == "kk":
        return f"{grade_number}-сынып — SAT-қа дайындықтың бастапқы диагностикасы"
    return f"{grade_number} класс — стартовая диагностика для подготовки к SAT"

def student_sheet(bank, grade, locale):
    header = [
        "# " + label(grade, locale),
        "",
        "**Revision:** kz-pilot-0.1 | **5 тақырып × 5 сұрақ = 25 / 5 тем × 5 вопросов = 25**",
        "",
        ("**Оқушы коды:** ______  **Күні:** ______  **Сеанс:** ______" if locale=="kk" else "**Код ученика:** ______  **Дата:** ______  **Сеанс:** ______"),
        "",
        ("**Нұсқау:** әр тапсырмаға A–D ішінен бір жауап таңда. Жауабыңды кейін өзгертпе. "
         "Математика қазақ тілінде, ағылшын грамматикасы ағылшын тілінде. "
         "Таймер тек бақылау үшін: уақыт ұпайды төмендетпейді."
         if locale=="kk" else
         "**Инструкция:** выбери один ответ A–D. Не исправляй ответы после сдачи. "
         "Математика на русском, английская грамматика на английском. "
         "Время фиксируется, но не уменьшает оценку."),
        "",
    ]
    for topic_id in TRACKS[grade]:
        topic = bank[topic_id]
        title = topic["title_kk" if locale=="kk" else "title_ru"]
        header.extend([
            f"## {topic_id} — {title}", "",
            ("Басталды: ______  Аяқталды: ______  Үзіліс (сек): ______" if locale=="kk" else "Начало: ______  Окончание: ______  Паузы (сек): ______"), "",
        ])
        for q in topic["questions"]:
            stem = q["stem_en"] if topic["subject"] == "english" else q[f"stem_{locale}"]
            opts = q["options_en"] if topic["subject"] == "english" else q[f"options_{locale}"]
            header.extend([f"**{q['id']}**", "", stem, ""])
            for letter, opt in zip("ABCD",opts):
                header.append(f"{letter}) {opt}  ")
            header.append("")
        header.extend([
            "| ID | A/B/C/D | " + ("Сенімділік 1–3" if locale=="kk" else "Уверенность 1–3") + " |",
            "|---|---|---|",
        ])
        for q in topic["questions"]:
            header.append(f"| {q['id']} | ______ | ______ |")
        header.append("")
    output = "\n".join(header) + "\n"
    if re.search(r"<u>|<strong>|<details>|answer key|teacher-only|дұрыс жауап:|правильный ответ:",output,re.I):
        raise ValueError("Student sheet leaks key")
    return output

def teacher_sheet(bank, grade):
    out = [
        "# Мұғалімге / преподавателю — жабық жауаптар / закрытые ключи",
        "",
        f"**Трек:** {grade} | **Revision:** kz-pilot-0.1",
        "",
        "Оқушы бес жауабын жазып болғанға дейін ашпау / не показывать до сдачи пяти ответов.",
        "",
    ]
    for topic_id in TRACKS[grade]:
        topic=bank[topic_id]
        out.extend([f"## {topic_id} — {topic['title_kk']} / {topic['title_ru']}", ""])
        for q in topic["questions"]:
            option = q["options_en"] if topic["subject"]=="english" else q["options_kk"]
            index = "ABCD".index(q["key"])
            out.extend([
                f"**{q['id']}** — <u>**{q['key']}) {option[index]}**</u>", "",
                f"**Түсіндірме (қаз.):** {q['explanation_kk']}", "",
                f"**Объяснение (рус.):** {q['explanation_ru']}", "",
            ])
        out.extend([
            "**SAT terms / терминдер:** " + ", ".join(topic["sat_terms"]), "",
        ])
    out.extend([
        "## Интерпретация / нәтиже",
        "",
        "0–2/5 → GAP, 3/5 → VERIFY, 4–5/5 → PROVISIONAL_SECURE. "
        "Это предварительная оценка, не официальный SAT/CEFR результат.",
        "",
        "Алдымен баланың қателесу себебін оның өз сөзімен нақтылаңыз. "
        "Сначала уточните ход мысли ребёнка; неверная буква не доказывает причину.",
        "",
    ])
    return "\n".join(out)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--grade", choices=["grade6","grade9","all"],default="all")
    p.add_argument("--locale",choices=["kk","ru","both"],default="both")
    p.add_argument("--out-dir",type=Path,default=ROOT/"build"/"kz_school")
    p.add_argument("--check-only",action="store_true")
    args=p.parse_args()
    bank=load_bank()
    grades=list(TRACKS) if args.grade=="all" else [args.grade]
    locales=["kk","ru"] if args.locale=="both" else [args.locale]
    if not args.check_only:
        for grade in grades:
            directory = args.out_dir/grade
            directory.mkdir(parents=True,exist_ok=True)
            for locale in locales:
                (directory/f"student_{locale}.md").write_text(student_sheet(bank,grade,locale),encoding="utf-8")
            (directory/"teacher_key_kk_ru.md").write_text(teacher_sheet(bank,grade),encoding="utf-8")
    # Build in memory also during --check-only so leakage is tested on CI.
    for grade in grades:
        for locale in locales:
            doc = student_sheet(bank,grade,locale)
            if len(re.findall(rf"^\*\*(?:KZ-FND|ALG|PSD|EN-)[A-Z0-9-]*-Q[1-5]\*\*$",doc,re.M)) != 25:
                raise ValueError(f"{grade}/{locale}: expected 25 student questions")
        if len(re.findall(r"^\\*\\*(?:KZ-FND|ALG|PSD|EN-)", teacher_sheet(bank,grade),re.M)) != 25:
            # Teacher keys each have one bold question header; fail on missing.
            raise ValueError(f"{grade}: teacher key incomplete")
    print(f"PASS: 10 topics/50 localized items; {len(grades)} learner tracks, no student answer leakage.")
    if not args.check_only:
        print("Created student KK/RU and separate teacher keys under", args.out_dir)

if __name__=="__main__":
    main()
