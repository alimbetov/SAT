# Observational Studies and Experiments — наблюдательные исследования и эксперименты

## 1. Зачем эта тема нужна на SAT

Эта тема проверяет не вычисления, а **границы допустимого вывода**.

SAT часто даёт описание исследования и спрашивает:

- это observational study или experiment;
- есть ли random sampling;
- есть ли random assignment;
- можно ли generalize;
- можно ли утверждать causation;
- какую роль играет control group;
- есть ли confounding.

Самая важная карта:

```text
HOW PEOPLE ENTER STUDY?   → generalization
HOW TREATMENT IS ASSIGNED? → causation
```

> **Главная идея:** **random sampling** помогает отвечать «для кого?», а **random assignment** — «из-за чего?». Это две разные задачи.

---

## 2. Pattern Map — распознаём design за 20 секунд

| Что описано | Pattern | Что можно заключать |
|---|---|---|
| researchers only observe | observational study | association, not causation |
| researchers assign treatment | experiment | possible causal inference |
| random sample from population | random sampling | supports generalization |
| random assignment to groups | randomized experiment | supports causation |
| volunteers only | self-selected sample | limited generalization |
| control group | baseline comparison | isolates treatment effect |
| third variable affects both | confounding | causal interpretation weakened |

### Pattern 1. Observational study

Researchers measure existing behavior without assigning treatment.

Example:

> Record sleep hours and grades of students.

They observe:

```text
sleep ↔ grades
```

but do not make students sleep specific amounts.

Conclusion:

```text
association possible
causation not established
```

### Pattern 2. Experiment

Researchers actively assign treatment.

Example:

> Assign one group new tutoring method, another standard method.

Now researcher controls treatment exposure.

If assignment is random and design is sound, causal claim becomes much stronger.

### Pattern 3. Random sampling

Question:

```text
Who gets into the study?
```

Random sampling from target population helps sample represent population.

Purpose:

```text
generalization / external validity
```

### Pattern 4. Random assignment

Question:

```text
Once participants are in study, who gets which treatment?
```

Random assignment helps balance lurking/confounding variables across groups.

Purpose:

```text
causal comparison / internal validity
```

### Pattern 5. Control group

A treatment group alone tells little.

Control group provides baseline:

```text
Treatment result - Control result
```

This does not magically remove every bias, but gives meaningful comparison.

### Pattern 6. Confounding variable

Suppose observational data show:

```text
students who exercise more have higher grades
```

Possible confounder:

```text
sleep
health
socioeconomic factors
study habits
```

A third variable may affect both exercise and grades.

### Pattern 7. Correlation/association ≠ causation

Even strong association does not prove cause.

> **Memory anchor:** `moves together` ≠ `makes happen`.

---

## 3. Guided Learning — two-axis inference model

Use this 2×2 mental model:

| | No random assignment | Random assignment |
|---|---|---|
| **No random sample** | limited association claim | causation for participants may be supported; generalization limited |
| **Random sample** | association can generalize better | strongest design: causal inference + broader generalization |

This table is a powerful SAT pattern.

### Worked Example 1 — random assignment, volunteers

Researchers recruit 200 volunteers and randomly assign them:

- Group A: new study method;
- Group B: standard method.

Group A scores higher.

#### Step 1. Experiment or observational?

Treatment assigned → experiment.

#### Step 2. Random assignment?

Yes.

#### Step 3. Causation?

Reasonably supported for participants under study design.

#### Step 4. Generalization to all students?

Limited, because participants were volunteers, not random sample of all students.

> **Correct nuanced conclusion:** causal inference can be stronger than generalization.

---

### Worked Example 2 — random sample, no assignment

A random sample of 1,000 adults is surveyed about coffee consumption and sleep duration. Heavy coffee consumption is associated with less sleep.

#### Generalization

Because sampling is random from target population, association may generalize reasonably.

#### Causation

No. Researchers did not assign coffee intake.

Possible confounders:

- work schedules;
- stress;
- health;
- age.

---

### Worked Example 3 — neither random sampling nor assignment

A fitness influencer asks followers whether supplement users feel more energetic.

Problems:

- followers are not representative of all adults;
- voluntary response;
- no treatment assignment;
- placebo/confounding possible.

Conclusion should be very limited.

---

### Worked Example 4 — why control group matters

A company gives 50 employees a productivity app. Average output rises 8% after one month.

Can app be credited?

Not confidently.

Other possibilities:

- seasonal demand;
- new manager;
- learning curve;
- incentive changes.

A comparable control group without app would help distinguish app effect from background changes.

---

### Worked Example 5 — random assignment role

Suppose highly motivated students choose new tutoring program voluntarily and then outperform others.

Observed difference may reflect motivation, not tutoring.

Random assignment would reduce this self-selection imbalance.

> **Random assignment attacks confounding between treatment groups.**

---

### Worked Example 6 — blind wording trap

SAT may not use phrase `random assignment` directly.

Look for verbs:

```text
randomly assigned
randomly divided
randomly placed into groups
allocated at random
```

These all indicate same design feature.

Likewise observational clues:

```text
surveyed
recorded
observed
measured existing behavior
```

---

## 4. Practice Ladder

### A. Recognition Drill

Identify design feature.

1. Researchers record diet and blood pressure, no intervention → `__________`  
2. Participants randomly divided between drug/placebo → `__________`  
3. Names randomly selected from city registry → `__________`  
4. One group receives no new treatment → `__________`

<details>
<summary><strong>Answers</strong></summary>

1. observational study  
2. random assignment / experiment  
3. random sampling  
4. control group

</details>

### B. Faded Example

Researchers randomly sample 500 students, then only observe hours of sleep and test scores.

Random sampling supports: `__________`

No random assignment means causation is: `__________`

<details>
<summary><strong>Solution</strong></summary>

Generalization of association is better supported; causation is not established.

</details>

### C. SAT-style Independent Practice

#### Problem 1 — Easy — Multiple Choice

Researchers record students' sleep hours and grades without changing behavior. This is:

**A)** experiment  
**B)** observational study  
**C)** random assignment  
**D)** controlled treatment

#### Problem 2 — Easy — Multiple Choice

Which feature most directly supports causal conclusion?

**A)** large graph  
**B)** random assignment to treatments  
**C)** high correlation only  
**D)** voluntary survey

#### Problem 3 — Medium — Multiple Choice

A random sample of city residents is surveyed about exercise and health. More exercise is associated with better health. Which conclusion is justified?

**A)** exercise definitely causes better health  
**B)** there is an association in population  
**C)** all residents who exercise are healthy  
**D)** survey is an experiment

#### Problem 4 — Medium — Multiple Choice

What is main purpose of control group?

**A)** guarantee larger sample  
**B)** create comparison baseline  
**C)** remove every source of error  
**D)** make all variables equal

#### Problem 5 — Hard — Multiple Choice

A randomized experiment uses volunteers recruited from one sports club. Which statement is strongest?

**A)** causal inference may be possible for participants, but broad generalization is limited  
**B)** results automatically apply to all adults  
**C)** no causal inference is ever possible  
**D)** random assignment guarantees representative sampling

#### Problem 6 — Hard Transfer — Multiple Choice

A study randomly samples 2,000 adults, then asks about screen time and anxiety. High screen time is associated with higher anxiety. What is strongest justified conclusion?

**A)** screen time causes anxiety in all adults  
**B)** anxiety causes screen time  
**C)** association may generalize to target population, but causation is not established  
**D)** random sampling is equivalent to random assignment

<details>
<summary><strong>Ответы и решения</strong></summary>

1. **B**. No treatment assigned.  
2. **B**. Random assignment supports causal comparison.  
3. **B**. Random sample supports population association, not causation.  
4. **B**. Control group gives baseline.  
5. **A**. Random assignment helps causation; volunteer recruitment limits generalization.  
6. **C**. Good sampling does not turn observational association into causation.

</details>

---

## 5. Error Clinic — четыре критические ловушки

### Ошибка 1. Correlation = causation

Wrong reasoning:

```text
A and B strongly associated
→ A causes B
```

Missing possibilities:

- B causes A;
- third variable C causes both;
- selection effects.

---

### Ошибка 2. Random sampling = random assignment

Keep questions separate:

```text
sampling → who enters?
assignment → who gets what?
```

This distinction solves many SAT questions instantly.

---

### Ошибка 3. Large sample proves causation

Sample size affects precision, not causal design.

A million observational records can show strong association and still not establish cause.

---

### Ошибка 4. Random assignment means representative population

No.

You can randomly assign a very unrepresentative volunteer group.

Then causal effect among participants may be credible, but broad population generalization remains limited.

---

### Ошибка 5. Control group eliminates all confounding automatically

Not automatically. Quality also depends on assignment, compliance, measurement and other design features.

Control group is necessary in many experiments but not magical.

---

## 6. Digital SAT Strategy — classify verbs before reading answers

### Verb scan

Look for:

```text
selected
sampled
surveyed
observed
assigned
given treatment
randomly divided
```

Then classify:

```text
Selection verb → sampling issue
Assignment verb → experiment/causation issue
```

### Two-question shortcut

Before answer choices:

1. **Can I generalize?** → inspect sampling.
2. **Can I say cause?** → inspect assignment.

This prevents attractive but overstrong answer choices.

### Desmos

Usually irrelevant. This is a reasoning domain.

Time should be spent on claim boundaries, not calculations.

---

## 7. SAT Language Decoder и связи

### Language Decoder

| Phrase | What it signals |
|---|---|
| `observed` | observational study likely |
| `surveyed` | observational, sampling matters |
| `assigned to` | experiment |
| `randomly assigned` | causal inference support |
| `randomly selected` | population generalization support |
| `control group` | comparison baseline |
| `treatment group` | receives intervention |
| `associated with` | correlation, not necessarily causation |
| `caused` / `led to` | causal claim |
| `generalize` | sampling question |
| `confounding variable` | alternative explanation |

### Connections

**Опирается на:**

- sampling and margin of error;
- probability;
- scatterplots/association.

### Core matrix to memorize conceptually

```text
random sample?      → WHO can conclusion describe?
random assignment?  → WHY can difference be attributed?
```

### Transfer Question

A nationally representative random sample participates in an observational nutrition survey. Can researchers claim a food causes longer life?

<details>
<summary><strong>Reasoning</strong></summary>

No. Sampling may support broad association estimates, but without random assignment/treatment experiment, causal claim remains unsupported.

</details>

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я различаю observational study и experiment.
- [ ] Я определяю, был ли treatment assigned.
- [ ] Я понимаю роль random sampling.
- [ ] Я понимаю роль random assignment.
- [ ] Я могу отдельно оценить generalization и causation.
- [ ] Я понимаю control group и confounding.
- [ ] Я не делаю causal claim из association.
- [ ] Я распознаю overclaim в answer choices.
- [ ] Я умею пользоваться 2×2 mental model sampling × assignment.

> **Mastery test:** по любому описанию исследования вы должны суметь закончить две фразы: **«Этот дизайн позволяет обобщать на…»** и **«Этот дизайн позволяет/не позволяет говорить, что X caused Y, потому что…»**.