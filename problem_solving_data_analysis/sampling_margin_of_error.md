# Sampling, Inference, and Margin of Error — выборки, выводы и погрешность

## 1. Зачем эта тема нужна на SAT

Эта тема проверяет статистическое мышление, а не сложную математику. SAT спрашивает:

- кого именно исследовали;
- о ком хотят сделать вывод;
- была ли sample selected appropriately;
- можно ли generalize;
- что означает margin of error;
- как sample size влияет на precision.

Главный workflow:

```text
TARGET POPULATION
      ↓
HOW SAMPLE WAS CHOSEN
      ↓
IS SAMPLE REPRESENTATIVE?
      ↓
WHAT STATISTIC WAS ESTIMATED?
      ↓
HOW PRECISE IS THE ESTIMATE?
      ↓
WHAT CLAIM IS JUSTIFIED?
```

> **Главная идея:** **random selection** отвечает за качество generalization; **sample size** главным образом влияет на precision. Большая biased sample остаётся biased.

---

## 2. Pattern Map — как читать sampling questions

| Что видите | Pattern | Главный вопрос |
|---|---|---|
| `all students in school` | population | о ком хотят знать? |
| `200 selected students` | sample | кого реально измерили? |
| `random sample from roster` | probability sampling | можно ли generalize? |
| `volunteers / convenience` | possible bias | кто систематически excluded? |
| `estimate ± margin of error` | interval | какой plausible range? |
| larger random sample | precision | margin of error tends smaller |
| huge biased sample | bias remains | size does not cure selection bias |

### Pattern 1. Population vs sample

**Population** = whole target group.

**Sample** = subset actually observed.

Example:

> Researchers survey 300 randomly selected students to estimate average sleep of all 2,000 students at a school.

Population:

```text
all 2,000 students
```

Sample:

```text
300 surveyed students
```

### Pattern 2. Statistic vs parameter

A **sample statistic** is calculated from sample.

A **population parameter** is the unknown true value for population.

Example:

```text
sample says 54% support proposal
```

54% is an estimate of population support percentage.

### Pattern 3. Random sample supports generalization

If sample is randomly selected from target population, it is more defensible to use sample statistic to estimate population parameter.

But random does not mean perfectly representative every time. Sampling variability still exists.

### Pattern 4. Bias beats sample size

Compare:

```text
A: 200 random students from full roster
B: 10,000 volunteers from SAT club
```

For generalizing to all students, A may be much better despite being smaller.

> **Memory anchor:** `large ≠ representative`.

### Pattern 5. Margin of error

If estimate is `p` and margin is `m`:

```math
p-m\le plausible\ population\ value\le p+m
```

Example:

```text
54% ± 4 percentage points
```

gives:

```text
50% to 58%
```

### Pattern 6. Larger random sample → usually smaller margin of error

All else equal:

```text
n ↑ → sampling variability ↓ → margin of error ↓
```

But:

```text
n ↑ does NOT automatically remove bias
```

### Pattern 7. Margin of error is not “percent of wrong respondents”

If survey reports:

```text
48% ± 3 percentage points
```

3 does not mean 3% respondents lied or answered incorrectly.

It quantifies uncertainty in estimate due to sampling.

---

## 3. Guided Learning — claim first, calculation second

### Decision Tree

```text
What population does claim target?
       ↓
Was sample selected from that population?
       │
       ├─ random / representative mechanism
       │      → generalization more defensible
       │
       └─ convenience / voluntary / restricted subgroup
              → generalization limited

Then:
Does question ask precision?
       → sample size / margin of error
```

### Worked Example 1 — identify population and sample

A district wants to estimate average homework time of all 12,000 high-school students. It randomly selects 600 students from district enrollment records.

Population:

```text
12,000 high-school students
```

Sample:

```text
600 randomly selected students
```

Because selection comes from district records randomly, sample design supports generalization better than convenience sampling.

---

### Worked Example 2 — convenience sample bias

A school asks students leaving the gym whether they exercise at least four times per week.

Can result estimate exercise frequency for all students?

Problem:

```text
location of sampling = gym
```

Gym users are more likely to exercise.

This is selection bias.

A large number of gym respondents would not fix target mismatch.

---

### Worked Example 3 — margin of error interval

A random sample of 500 voters finds 54% support. Margin of error = 4 percentage points.

Lower endpoint:

```math
54-4=50
```

Upper endpoint:

```math
54+4=58
```

Plausible interval:

```text
50% to 58%
```

Interpretation:

> 54% is estimate, not guaranteed exact population value.

---

### Worked Example 4 — compare sample sizes

Two polls use same random-sampling method.

```text
Poll A: n=100
Poll B: n=1600
```

Which generally has smaller margin of error?

Poll B.

Why?

Larger sample reduces sampling variability.

Do we need to calculate exact margin? No. SAT often asks only direction.

---

### Worked Example 5 — large biased sample

A news website posts voluntary poll. 50,000 readers answer.

Can it automatically represent all adults in country?

No.

Problems:

- only website readers;
- self-selection;
- voluntary response bias.

> **50,000 biased observations can still be less useful than a much smaller random sample.**

---

### Worked Example 6 — population mismatch

Researchers randomly sample 800 university students and estimate preference for online learning.

Can they generalize to all adults?

No, not automatically.

Random selection was within **university students**, so target population supported by design is that sampling frame, not all adults.

---

### Worked Example 7 — use margin to evaluate claim

Survey estimate:

```text
48% ± 5 percentage points
```

Interval:

```text
43% to 53%
```

Claim:

> “A majority definitely supports the proposal.”

Not justified because interval includes values below 50%.

This is a classic SAT inference pattern:

```text
estimate interval
→ compare claim threshold
```

---

## 4. Practice Ladder

### A. Recognition Drill

Identify issue/idea.

1. `first 100 people entering a mall` → `__________ sample`  
2. `random names from complete roster` → supports `__________`  
3. `n increases from 100 to 1000` → margin of error generally `__________`  
4. `52% ± 4` → plausible interval `__________`

<details>
<summary><strong>Answers</strong></summary>

1. convenience  
2. generalization to roster population  
3. decreases  
4. 48%–56%

</details>

### B. Faded Example

Estimate = 62%, margin of error = 3 percentage points.

Lower:

```math
62-3=\boxed{\phantom{59}}
```

Upper:

```math
62+3=\boxed{\phantom{65}}
```

<details>
<summary><strong>Solution</strong></summary>

59% to 65%.

</details>

### C. SAT-style Independent Practice

#### Problem 1 — Easy — Multiple Choice

A study wants to estimate average height of all students at a school. What is population?

**A)** only surveyed students  
**B)** all students at school  
**C)** tallest students  
**D)** all schools in city

#### Problem 2 — Easy — Grid-in

An estimate is 62% with margin of error 3 percentage points. What is lower endpoint?

#### Problem 3 — Medium — Multiple Choice

Which sample best supports generalization to all students at a school?

**A)** first 50 students entering gym  
**B)** 50 volunteers from chess club  
**C)** random sample from full student roster  
**D)** 50 highest-scoring students

#### Problem 4 — Medium — Multiple Choice

Two random samples use same method. Sample A has 100 people; Sample B has 1,000. Which generally has smaller margin of error?

**A)** A  
**B)** B  
**C)** always equal  
**D)** impossible

#### Problem 5 — Hard — Multiple Choice

A survey reports 48% support with margin of error 5 percentage points. Which population value is consistent?

**A)** 39%  
**B)** 42%  
**C)** 51%  
**D)** 56%

#### Problem 6 — Hard Transfer — Multiple Choice

A voluntary online poll of 20,000 visitors and a random telephone sample of 800 residents produce different estimates. Which statement is best?

**A)** online poll must be better because larger  
**B)** random sample may support better population inference despite smaller size  
**C)** both are automatically unbiased  
**D)** sample size is the only design feature that matters

<details>
<summary><strong>Ответы и решения</strong></summary>

1. **B**. Population is target group.  
2. **59**.  
3. **C**. Random sampling from full roster best matches target population.  
4. **B**. Larger random sample generally has smaller sampling variability.  
5. **C**. Interval `43%–53%`.  
6. **B**. Selection quality can matter more than raw sample size.

</details>

---

## 5. Error Clinic — inference traps

### Ошибка 1. “Big sample = good sample”

False.

Large sample reduces random sampling variability, but does not repair systematic selection bias.

### Ошибка 2. Random assignment confused with random sampling

Random **sampling**:

```text
Who gets into study?
→ generalization
```

Random **assignment**:

```text
Who gets which treatment?
→ causation
```

Do not swap them.

### Ошибка 3. Margin of error interpreted as response mistakes

Margin of error describes uncertainty of population estimate, not honesty/accuracy of individual respondents.

### Ошибка 4. Claim broader than sampling frame

Random sample of one school supports inference to that school, not automatically whole country.

### Ошибка 5. Interval contains threshold but student claims certainty

If support interval includes both sides of 50%, cannot confidently say majority/minority based only on that interval.

---

## 6. Digital SAT Strategy — inference without overcalculation

These questions are mostly verbal logic.

### Four-word scan

Look for:

```text
population
sample
random
margin
```

Then ask:

```text
Generalization question?
→ inspect sampling

Precision question?
→ inspect sample size / margin
```

### Desmos

Usually unnecessary.

Simple interval arithmetic can be done mentally:

```text
57 ± 4 → 53 to 61
```

### Exam shortcut

When answer choice says **“definitely”**, **“proves”**, or generalizes beyond sampled population, inspect it skeptically.

Statistical evidence usually supports bounded claims, not absolute certainty.

---

## 7. SAT Language Decoder и связи

### Language Decoder

| Phrase | Meaning |
|---|---|
| `population` | target whole group |
| `sample` | observed subset |
| `random sample` | probability-based selection |
| `representative` | resembles target population relevantly |
| `generalize` | extend sample conclusion to population |
| `estimate` | sample-based approximation |
| `margin of error` | uncertainty band around estimate |
| `plausible value` | value within reasonable interval |
| `voluntary response` | self-selected sample, bias risk |

### Connections

**Опирается на:** percentages, probability, one-variable statistics.  
**Следующий логический урок:** `observational_studies_experiments.md`.

### Master distinction

```text
RANDOM SAMPLE
→ external validity / generalization

RANDOM ASSIGNMENT
→ causal comparison
```

### Transfer Question

A study randomly selects 1,200 registered voters from one state. Can result be generalized to all adults in every country?

<details>
<summary><strong>Reasoning</strong></summary>

No. Random selection improves inference for the sampled target frame (registered voters in that state), not arbitrary external populations.

</details>

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я различаю population и sample.
- [ ] Я различаю statistic и population parameter.
- [ ] Я понимаю, зачем нужен random sampling.
- [ ] Я распознаю convenience/voluntary-response bias.
- [ ] Я строю interval `estimate ± margin of error`.
- [ ] Я понимаю effect of larger sample on precision.
- [ ] Я знаю, что большой sample не исправляет selection bias.
- [ ] Я проверяю, не выходит ли claim за sampling frame.
- [ ] Я отличаю random sampling от random assignment.

> **Mastery test:** перед любым statistical claim вы должны уметь ответить: **«Кого реально sampled и на кого пытаются перенести вывод?»**