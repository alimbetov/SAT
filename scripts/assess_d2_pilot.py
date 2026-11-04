#!/usr/bin/env python3
"""Aggregate D2 blind-confirmation results locally, without student-level output.

This evaluates provisional diagnostic GAP detection, NOT student performance
nor a certified score. The input CSV MUST remain private and outside Git.
Usage:
  python scripts/assess_d2_pilot.py local_pilot_confirmation.csv
  python scripts/assess_d2_pilot.py --self-test
"""
from __future__ import annotations

import argparse
import csv
import io
import sys

REQUIRED = {
    "student_code", "topic_id", "attempt_id", "diagnostic_status",
    "confirmation_label", "error_cause_confirmed",
    "recommendation_confirmed", "hint_used",
}
DIAG = {"GAP", "VERIFY", "PROVISIONAL_SECURE", "INCOMPLETE", "NOT_ASSESSED", "ASSISTED"}
GOLD = {"GAP", "NO_GAP", "INDETERMINATE", ""}
YN = {"yes", "no", "unknown", ""}

def ratio(num, den):
    return None if den == 0 else num / den

def evaluate(rows):
    tally = {"TP":0,"FP":0,"FN":0,"TN":0,"verify":0,"indeterminate":0,
             "excluded":0,"with_hints":0,"total":0,
             "cause_yes":0,"cause_no":0,"recommend_yes":0,"recommend_no":0}
    seen = set()
    for row in rows:
        tally["total"] += 1
        attempt = (row["student_code"].strip(), row["topic_id"].strip(), row["attempt_id"].strip())
        if not all(attempt) or attempt in seen:
            raise ValueError("Missing or duplicate student/topic/attempt identifier")
        seen.add(attempt)
        status = row["diagnostic_status"].strip().upper()
        label = row["confirmation_label"].strip().upper()
        help_used = row["hint_used"].strip().lower()
        cause = row["error_cause_confirmed"].strip().lower()
        recommendation = row["recommendation_confirmed"].strip().lower()
        if status not in DIAG or label not in GOLD or help_used not in {"yes","no"}:
            raise ValueError("Unexpected diagnostic/gold status or hint flag")
        if cause not in YN or recommendation not in YN:
            raise ValueError("Unexpected cause/recommendation review flag")
        if help_used == "yes":
            tally["with_hints"] += 1
        if cause in {"yes","no"}:
            tally[f"cause_{cause}"] += 1
        if recommendation in {"yes","no"}:
            tally[f"recommend_{recommendation}"] += 1
        if status in {"INCOMPLETE","NOT_ASSESSED","ASSISTED"} or help_used == "yes":
            tally["excluded"] += 1
        elif status == "VERIFY":
            tally["verify"] += 1
        elif label in {"INDETERMINATE",""}:
            tally["indeterminate"] += 1
        elif status == "GAP":
            tally["TP" if label == "GAP" else "FP"] += 1
        else:
            tally["FN" if label == "GAP" else "TN"] += 1
    n = tally
    n["binary_evaluated"] = n["TP"] + n["FP"] + n["FN"] + n["TN"]
    n["precision_gap"] = ratio(n["TP"],n["TP"]+n["FP"])
    n["recall_gap"] = ratio(n["TP"],n["TP"]+n["FN"])
    n["specificity"] = ratio(n["TN"],n["TN"]+n["FP"])
    n["cause_agreement"] = ratio(n["cause_yes"], n["cause_yes"]+n["cause_no"])
    n["recommendation_agreement"] = ratio(n["recommend_yes"], n["recommend_yes"]+n["recommend_no"])
    return n

def self_test():
    source = io.StringIO(
        "student_code,topic_id,attempt_id,diagnostic_status,confirmation_label,error_cause_confirmed,recommendation_confirmed,hint_used\n"
        "P001,ALG-01,A1,GAP,GAP,yes,yes,no\n"
        "P001,ALG-02,A1,GAP,NO_GAP,no,yes,no\n"
        "P002,ALG-01,A1,PROVISIONAL_SECURE,GAP,no,no,no\n"
        "P002,ALG-02,A1,PROVISIONAL_SECURE,NO_GAP,unknown,unknown,no\n"
        "P003,ALG-01,A1,VERIFY,INDETERMINATE,unknown,unknown,no\n"
        "P003,ALG-02,A1,GAP,GAP,unknown,unknown,yes\n"
    )
    data = evaluate(csv.DictReader(source))
    assert [data[k] for k in ("TP","FP","FN","TN","verify","excluded","binary_evaluated")] == [1,1,1,1,1,1,4]
    assert data["precision_gap"] == data["recall_gap"] == data["specificity"] == 0.5
    assert data["cause_agreement"] == 1/3
    assert data["recommendation_agreement"] == 2/3
    try:
        evaluate([{"student_code":"","topic_id":"ALG-01","attempt_id":"A1",
            "diagnostic_status":"GAP","confirmation_label":"GAP","hint_used":"no",
            "error_cause_confirmed":"","recommendation_confirmed":""}])
    except ValueError:
        pass
    else:
        raise AssertionError("missing student code must fail")
    print("PASS: D2 aggregate metrics, exclusions, duplicate/missing-ID validation (synthetic only).")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("csv_file", nargs="?", help="private local confirmation CSV")
    p.add_argument("--self-test",action="store_true")
    args = p.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not args.csv_file:
        p.error("provide a local private CSV path or --self-test")
    try:
        with open(args.csv_file,newline="",encoding="utf-8-sig") as stream:
            reader = csv.DictReader(stream)
            if not REQUIRED.issubset(set(reader.fieldnames or [])):
                p.error(f"missing columns: {sorted(REQUIRED-set(reader.fieldnames or []))}")
            data = evaluate(reader)
    except (OSError, ValueError) as exc:
        p.error(str(exc))
    print("D2 blinded validation — aggregate only; no individual data printed")
    print(f"Attempts: {data['total']}; binary evaluated: {data['binary_evaluated']}; "
          f"VERIFY: {data['verify']}; gold uncertain/missing: {data['indeterminate']}; "
          f"excluded/helped: {data['excluded']}")
    print("Confusion matrix (GAP detection): TP={TP}, FP={FP}, FN={FN}, TN={TN}".format(**data))
    for key in ("precision_gap","recall_gap","specificity","cause_agreement","recommendation_agreement"):
        value = data[key]
        print(f"{key}: {'n/a' if value is None else f'{100*value:.1f}%'}")
    print("Interpretation: descriptive pilot evidence, not psychometric validation or CEFR/SAT score.")
    if data["binary_evaluated"] < 30:
        print("CAUTION: very small binary sample; do not generalize results.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
