# D1 Quality Review — diagnostic question bank

**Repository branch:** `feat/diagnostic-assessment-v1`  
**Baseline:** `feat/age-adaptive-pedagogy`  
**Bank revision:** `v1.0-draft` (questions are *not yet externally calibrated*)  
**Scope:** 25 SAT Math topics and 20 English Grammar topics A1–B2.

## 1. Artifact coverage

| Component | Topics | Questions | Location |
|---|---:|---:|---|
| Math pilot: linear equations | 1 | 5 | [pilot Math](PILOT_MATH_LINEAR_EQUATIONS.md) |
| Math Algebra (remaining) | 4 | 20 | [Algebra](bank/math_algebra.md) |
| Math Advanced | 9 | 45 | [Advanced](bank/math_advanced.md) |
| Math Data Analysis | 7 | 35 | [Data Analysis](bank/math_data_analysis.md) |
| Math Geometry & Trig | 4 | 20 | [Geometry](bank/math_geometry.md) |
| English grammar pilots A1/A2/B1/B2 | 4 | 20 | [English pilot](PILOT_ENGLISH_A1_B2.md) |
| English grammar A1 remaining | 4 | 20 | [A1](bank/english_a1.md) |
| English grammar A2 remaining | 4 | 20 | [A2](bank/english_a2.md) |
| English grammar B1 remaining | 4 | 20 | [B1](bank/english_b1.md) |
| English grammar B2 remaining | 4 | 20 | [B2](bank/english_b2.md) |
| **Total** | **45** | **225** | |

## 2. Structural verification

**Automated gate:** `python3 scripts/validate_diagnostic_bank.py`; [workflow](../.github/workflows/diagnostic-bank.yml).

Checks:
- complete mapping of 25 Math + 20 English blueprint topics;
- five uniquely identified questions per topic;
- exactly four answer options A/B/C/D for each question, no duplicates within an item;
- one teacher-only correct key per question with an explanation;
- answer-key markup excluded from student question text;
- question types (recognition, trap, transfer) are not shown beside student questions;
- no duplicate question IDs across files;
- all 225 questions accounted for, 200 newly authored + 25 initial pilots.

**Status:** structurally validated by local connector inspection and CI gate; the latest CI result must be checked on the exact branch SHA before acceptance. CI cannot prove that the indicated answer is academically correct or uniquely best.

## 3. Pedagogical and subject-matter review

Required before declaring D1 *academically closed*:

- [ ] Independent SAT Math expert checks all 125 problems, correct answers, distractors and solution steps.
- [ ] Independent English teacher checks all 100 problems for a single best answer given the context and approximate A1–B2 difficulty.
- [ ] Remove or revise plausible alternative answers, including usage/dialect ambiguity.
- [ ] Check each 5-question set covers five different facets and not only pattern memorization.
- [ ] Check mathematics question language does not unintentionally create a reading test for Foundation.
- [ ] Map answers to root causes **after** observing students, not just by wrong option.
- [ ] Establish unseen transfer/retest sets; current D1 items must not serve as immediate retests.
- [ ] Record review approver, date, question revisions and specific feedback after review.

## 4. Important distinction

- **D1 authored** = 225 diagnostic items exist.
- **D1 structural qualified** = format/coverage CI passes on exact SHA.
- **D1 pedagogically accepted** = expert review + resolution of semantic ambiguities.
- **D2 accepted** = real child pilots with prior consent, captured answers and timing, correct reports and unseen follow-up evidence.

No claim about **validated CEFR level, psychometric reliability, official SAT score, or real child outcome** follows from structural CI.

## 5. Error taxonomy and interpretation

Wrong answers generate an **error hypothesis**, not a diagnosis. The teacher uses response patterns and short follow-up prompts to confirm an error code. Five multiple-choice items support an initial topic triage, not permanent certification.

## 6. Next step

Use [D2 Field Protocol](D2_FIELD_PROTOCOL.md), private [CSV template](templates/session_capture.csv) and [Gap Report template](templates/gap_report_template.md). After real pilots, open review issues for ambiguous items, release question bank `v1.1` and author unseen validation variants before automating D3.
