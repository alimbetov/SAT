# Probability and Conditional Probability — вероятность и условная вероятность

## 1. Зачем эта тема нужна на SAT

Probability questions на Digital SAT часто выглядят простыми, но проверяют один критический навык: **правильно выбрать denominator**.

Особенно это важно в conditional probability и two-way tables.

Перед вычислением всегда спросите:

```text
Из какой группы сейчас выбирают?
```

> **Главная идея:** probability = favorable outcomes / relevant possible outcomes. В conditional probability слово **given that** меняет relevant group.

---

## 2. Pattern Map — какие probability patterns встречаются

| Формулировка | Pattern | Denominator |
|---|---|---|
| `randomly selected from all` | basic probability | whole group |
| `not A` | complement | `1-P(A)` |
| `A and B` | intersection | both conditions |
| `given that B` | conditional probability | only B group |
| independent events | multiplication | `P(A)P(B)` |
| two-way table | table probability | depends on wording |

### Pattern 1. Basic probability

```math
P(A)=\frac{favorable}{total}
```

Example: fair die, event = roll 5.

```math
P(5)=\frac16
```

### Pattern 2. Complement

If:

```math
P(A)=0.35
```

then:

```math
P(not\ A)=1-0.35=0.65
```

> **Memory anchor:** event + not event = whole universe = 1.

### Pattern 3. Conditional probability

```math
P(A|B)=\frac{P(A\cap B)}{P(B)}
```

Но на SAT часто проще не использовать formula mechanically.

Read it as:

```text
Among only B, what fraction are also A?
```

> **Given that = shrink the room.**

### Pattern 4. Two-way table

Suppose:

| | Soccer | No Soccer | Total |
|---|---:|---:|---:|
| Grade 11 | 18 | 12 | 30 |
| Grade 12 | 10 | 20 | 30 |
| Total | 28 | 32 | 60 |

Questions:

#### P(Soccer)

Whole group denominator:

```math
28/60
```

#### P(Soccer | Grade 11)

Condition = Grade 11 → denominator 30:

```math
18/30
```

#### P(Grade 11 | Soccer)

Condition = Soccer → denominator 28:

```math
18/28
```

Same intersection `18`, different denominators.

### Pattern 5. Independent events

Events A and B are independent if occurrence of one does not change probability of the other.

Then:

```math
P(A\cap B)=P(A)P(B)
```

Example:

```math
P(A)=0.4,\quad P(B)=0.5
```

```math
P(A\cap B)=0.2
```

### Pattern 6. Independent ≠ mutually exclusive

**Independent:** events can occur together; one does not affect the other.

**Mutually exclusive:** cannot occur together.

For mutually exclusive events:

```math
P(A\cap B)=0
```

If two events with positive probabilities are mutually exclusive, they are generally **not independent**.

### Pattern 7. “At least one” often invites complement

If two independent attempts each fail with probability 0.2, probability of at least one success:

Instead of listing cases:

```math
1-P(both\ fail)
```

```math
1-(0.2)(0.2)=0.96
```

> **At least one = often easier through none.**

---

## 3. Guided Learning — denominator first

### Decision Tree

```text
Does question say "given that" / "among" / "of those"?
        │
        ├─ YES → condition defines denominator
        │
        └─ NO  → denominator usually whole relevant group

Does it ask "not"?
        → complement

Are events independent and asks "and"?
        → multiply probabilities

Does it ask "at least one"?
        → consider complement
```

### Worked Example 1 — conditional probability

In a group of 40 students:

- 24 study Spanish;
- 15 of those 24 play on a school team.

Find probability a student plays on a team **given that** the student studies Spanish.

#### Step 1. Circle the condition

```text
given that ... Spanish
```

Relevant group = 24 Spanish students.

#### Step 2. Favorable among that group

15 play on team.

#### Step 3. Probability

```math
\frac{15}{24}=\frac58
```

Why denominator not 40?

Because condition has already restricted sample space.

---

### Worked Example 2 — reverse condition

Same data: 15 students both study Spanish and play team. Suppose total team players = 20.

Find:

```math
P(Spanish|Team)
```

Now condition is **Team**, so denominator = 20.

```math
P(Spanish|Team)=15/20=3/4
```

Compare:

```math
P(Team|Spanish)=15/24
```

These are not equal in general.

> **Order around the vertical bar matters.**

---

### Worked Example 3 — complement

A machine produces defective item with probability `0.03`.

Probability item is not defective:

```math
1-0.03=0.97
```

No need to build a separate ratio.

---

### Worked Example 4 — independent repeated events

A fair coin is flipped twice.

Probability of two heads:

```math
\frac12\cdot\frac12=\frac14
```

Why multiply?

We need both events (`and`) and flips are independent.

---

### Worked Example 5 — at least one

Probability of at least one head in two fair flips.

Harder route: HH, HT, TH → 3/4.

Faster pattern:

```text
at least one head
= 1 - no heads
```

```math
1-P(TT)=1-\frac14=\frac34
```

---

### Worked Example 6 — two-way table logic

| | Passed | Not Passed | Total |
|---|---:|---:|---:|
| Took Course | 36 | 9 | 45 |
| No Course | 24 | 31 | 55 |
| Total | 60 | 40 | 100 |

#### Probability passed overall

```math
60/100=0.60
```

#### Probability passed given took course

```math
36/45=0.80
```

#### Probability took course given passed

```math
36/60=0.60
```

Again: same cell, different denominator.

---

## 4. Practice Ladder

### A. Denominator Recognition Drill

Do not calculate. Write denominator only.

1. `P(red)` from 3 red + 7 blue balls → denominator `____`  
2. `P(physics | junior)` where 20 juniors, 8 take physics → denominator `____`  
3. `P(junior | physics)` where 14 total physics students → denominator `____`  
4. `P(not A)` → denominator concept replaced by `__________`

<details>
<summary><strong>Answers</strong></summary>

1. 10  
2. 20  
3. 14  
4. complement `1-P(A)`

</details>

### B. Faded Example

There are 50 students. 30 are seniors. Of the seniors, 18 take calculus.

```math
P(Calculus|Senior)=\frac{\boxed{\phantom{18}}}{\boxed{\phantom{30}}}
```

<details>
<summary><strong>Solution</strong></summary>

`18/30=3/5`.

</details>

### C. SAT-style Independent Practice

#### Problem 1 — Easy — Multiple Choice

A fair die is rolled. What is probability of rolling a 5?

**A)** `1/2`  
**B)** `1/5`  
**C)** `1/6`  
**D)** `5/6`

#### Problem 2 — Easy — Grid-in

A bag contains 3 red and 7 blue balls. What is probability of selecting red? Enter decimal.

#### Problem 3 — Medium — Multiple Choice

If `P(A)=0.35`, what is `P(not A)`?

**A)** 0.35  
**B)** 0.50  
**C)** 0.65  
**D)** 1.35

#### Problem 4 — Medium — Multiple Choice

In a class, 20 students are juniors. Of those juniors, 8 take physics. If a student is selected from the juniors, what is probability the student takes physics?

**A)** `8/30`  
**B)** `8/20`  
**C)** `20/8`  
**D)** `12/20`

#### Problem 5 — Hard — Grid-in

Two independent events have `P(A)=0.4` and `P(B)=0.5`. Find `P(A and B)`.

#### Problem 6 — Hard Transfer — Multiple Choice

A two-way table shows that among 80 students, 50 study French, 32 play an instrument, and 20 do both. What is `P(French | Instrument)`?

**A)** `20/80`  
**B)** `20/50`  
**C)** `20/32`  
**D)** `32/50`

<details>
<summary><strong>Ответы и решения</strong></summary>

1. **C**. `1/6`.  
2. **0.3**. `3/10`.  
3. **C**. `1-0.35=0.65`.  
4. **B**. Condition restricts denominator to 20 juniors.  
5. **0.2**. `0.4·0.5`.  
6. **C**. Given Instrument → denominator 32; both = 20.

</details>

---

## 5. Error Clinic — denominator traps

### Ошибка 1. Always use grand total

Conditional question:

```text
Given that student is a junior...
```

Grand total is irrelevant after conditioning.

#### Fix

Rewrite:

```text
Among juniors only...
```

---

### Ошибка 2. Confuse `P(A|B)` with `P(B|A)`

They share numerator intersection but denominator changes.

```math
P(A|B)=\frac{A\cap B}{B}
```

```math
P(B|A)=\frac{A\cap B}{A}
```

---

### Ошибка 3. Independent = mutually exclusive

Incorrect.

Independent positive-probability events can happen together.

Mutually exclusive events cannot.

---

### Ошибка 4. Probability outside [0,1]

Any computed probability <0 or >1 is automatically wrong.

Use that as instant sanity check.

---

### Ошибка 5. Add when should multiply

For independent `A and B`, multiplication is common.

For mutually exclusive `A or B`, addition may apply.

Pay attention to logical connector:

```text
AND vs OR
```

---

## 6. Digital SAT Strategy — table-first reasoning

### Two-way table workflow

1. Read condition after `given that`.
2. Cover everything outside that row/column mentally.
3. Denominator = total remaining group.
4. Numerator = favorable inside that group.

### Desmos

Usually unnecessary. Fractions and table reasoning are faster manually.

Use calculator only for awkward decimals if needed.

### Fast sanity checks

- probability between 0 and 1;
- favorable ≤ denominator;
- conditioning should change denominator;
- if event is rare, answer near 0 is plausible.

---

## 7. SAT Language Decoder и связи

### Language Decoder

| Phrase | Meaning |
|---|---|
| `randomly selected` | probability from relevant group |
| `given that` | conditional denominator |
| `among` | restrict group |
| `of those` | denominator becomes referenced subgroup |
| `and` | intersection |
| `or` | union |
| `not` | complement |
| `at least one` | often use complement |
| `independent` | one event does not change probability of other |

### Connections

**Опирается на:** fractions, ratios, percentages.  
**Используется в:**

- sampling;
- inference;
- two-way tables;
- experiment interpretation.

### Transfer Question

If `P(A)=0.6` and `P(A|B)=0.6`, what does that suggest about A and B?

<details>
<summary><strong>Reasoning</strong></summary>

Knowing B did not change probability of A, which is consistent with independence (assuming probabilities are well-defined).

</details>

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я выбираю denominator до вычислений.
- [ ] Я перевожу `given that` в restricted sample space.
- [ ] Я различаю `P(A|B)` и `P(B|A)`.
- [ ] Я использую complement rule.
- [ ] Я понимаю independence.
- [ ] Я не путаю independent и mutually exclusive events.
- [ ] Я читаю two-way tables без использования grand total по привычке.
- [ ] Я проверяю probability на диапазон `[0,1]`.

> **Mastery test:** при conditional probability вы должны уметь сначала назвать denominator словами, а только потом смотреть на числа.