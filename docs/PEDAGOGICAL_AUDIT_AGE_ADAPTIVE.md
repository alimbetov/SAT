# Pedagogical Audit — age-adaptive SAT Math delivery

## Context

The repository now has strong topic coverage, Pedagogy V2 lessons, Practice V2 drills, diagnostic maps, and timed modules. The remaining pedagogical risk is not missing SAT content. It is **learner fit**.

Two target learners require different instructional pacing:

- **Foundation learner (примерно 6 класс):** concrete models, arithmetic-first explanations, fewer new terms at once, more visual representations, more worked examples, and delayed exposure to advanced SAT abstractions.
- **SAT Bridge learner (примерно 9 класс):** explicit prerequisite checks, deeper explanation of why a method works, contrast between methods, and gradual transition to SAT language, time pressure, and Desmos.

A single linear path is therefore not sufficient.

---

# Executive assessment

| Area | Current state | Risk | Priority |
|---|---|---|---|
| SAT topic coverage | Strong | low | maintain |
| Pattern recognition | Strong | low | maintain |
| Method selection | Strong | low | maintain |
| Worked examples | Good but uneven | some central topics still move too quickly | P1 |
| Explanation of *why* | Medium/strong | some rules still appear before intuition | P1 |
| Age adaptation | Weak | same lesson assumes too much prior knowledge | **P0** |
| Prerequisite routing | Weak | learner can open a lesson before being ready | **P0** |
| Foundation numeracy bridge | Missing | 6th-grade learner can hit algebraic abstraction too early | **P0** |
| SAT English load | Medium | terminology can compete with math comprehension | P1 |
| Practice sequencing | Strong for SAT | too hard too early for younger learner | P0 |
| Timed practice | Appropriate for SAT learner | inappropriate as early goal for foundation learner | P0 |

## Overall conclusion

The repository is now a strong **SAT preparation system**, but not yet a fully differentiated **learning system for two school-age levels**.

The correct fix is **not** to make every lesson longer. The correct fix is to add:

1. learner tracks;
2. prerequisite gates;
3. foundation bridge modules;
4. three-level worked-example ladders;
5. Russian-first explanation before SAT English for younger learners;
6. different mastery gates for Foundation and SAT Bridge.

---

# P0 findings

## P0-1 — No explicit learner routing

The root course currently presents all 25 SAT lessons as one system. A learner can move from basic linear equations to quadratics, rational expressions, radians, unit circle, inference, and margin of error without an explicit readiness gate.

### Why this matters

For a younger learner, inability to solve an advanced topic can reflect **missing prerequisite knowledge**, not inability in the topic itself.

### Required correction

Add two routes:

```text
FOUNDATION TRACK
concrete arithmetic
→ ratios / percent
→ equation balance
→ coordinates / patterns
→ geometry meaning
→ algebra bridge

SAT BRIDGE TRACK
prerequisite diagnostic
→ Algebra
→ Advanced Math
→ PSDA
→ Geometry / Trig
→ mixed practice
→ timed modules
```

---

## P0-2 — Concrete → visual → symbolic progression is inconsistent

Several lessons start well with a mental model, but central formulas may still appear before enough concrete examples.

### Required teaching sequence

For foundational concepts:

```text
CONCRETE
real objects / money / distance / tiles
    ↓
VISUAL
bar, table, balance, number line, diagram
    ↓
SYMBOLIC
x, y, formula, equation
    ↓
SAT LANGUAGE
English exam wording
```

For a sixth-grade learner, reversing this order increases cognitive load.

---

## P0-3 — Practice V2 is still SAT-calibrated

Practice V2 correctly uses Recognition → Core → Variation → Trap → Transfer. However, even `Easy` SAT questions can be too abstract for a learner who has not yet automated prerequisite arithmetic and algebra.

### Required correction

Add a **Foundation Practice layer** before Topic Drill 01:

```text
Warm-up A — understand the idea
Warm-up B — do the arithmetic
Worked Together — complete example
Your Turn — same pattern
Bridge — first SAT-style wording
```

Only then enter `Drill 01`.

---

# P1 findings

## P1-1 — Worked examples need a stronger three-pass ladder

Central patterns should have three example types:

### Example A — Teacher Think-Aloud

Every decision is explicit:

```text
What do I notice?
What does the question want?
Which fact connects them?
Why is this operation legal?
How will I check?
```

### Example B — Same Pattern, New Clothes

Different numbers or context; fewer hints.

### Example C — Student Completes the Reasoning

Only the first decision is given.

This creates a smoother release of responsibility.

---

## P1-2 — Some mathematical vocabulary should be staged

For a younger learner, terms such as:

- coefficient;
- parameter;
- domain restriction;
- discriminant;
- residual;
- margin of error;
- congruence criterion

should be introduced after the intuitive idea, not before it.

Recommended format:

> **По-простому:** число перед `x`.
>
> **Math term:** coefficient.

---

## P1-3 — SAT English should be a second representation, not the first obstacle

For the younger track:

```text
Russian meaning
→ mathematical model
→ short English phrase
```

For the SAT Bridge track:

```text
English phrase
→ pattern recognition
→ model
```

The same topic therefore needs different language emphasis.

---

# P2 findings

## P2-1 — Add parent/teacher prompts

A short prompt after a worked example can reveal whether understanding is real:

- «Почему здесь делим, а не умножаем?»
- «Как ты понял, что 80 — это 100%?»
- «Что изменится, если знак будет минус?»
- «Покажи эту же идею рисунком или таблицей.»

## P2-2 — Add confidence labels separate from difficulty

`Easy/Medium/Hard` describes exam difficulty, not learning readiness.

Add optional labels:

- `FOUNDATION` — idea is accessible before formal SAT work;
- `BRIDGE` — school algebra connection;
- `SAT CORE` — expected SAT application;
- `STRETCH` — hard/750–800.

---

# Topic-level audit

## Linear equations

### Strengths

- balance model is excellent;
- undo-operations model is effective;
- multiple worked examples already exist;
- errors are explained rather than merely listed.

### Gap

For a 6th-grade learner the lesson still starts with `x` and formal pattern names too quickly.

### Needed bridge

```text
□ + 7 = 12
3□ = 18
3□ + 7 = 25
3x + 7 = 25
```

The symbol changes; the reasoning does not.

---

## Ratios, rates, units

### Strengths

- units are treated as mathematical information;
- `per` and denominator direction are taught explicitly.

### Gap

Need more visual grouping before dimensional analysis.

### Needed bridge

Use tables, repeated groups, recipes, price tags, and `for every` diagrams before formal fractions.

---

## Percentages

### Strengths

- excellent `100% = what?` question;
- base/rate/part model is correct;
- reverse percentage and successive changes are well represented.

### Gap

For younger learner, decimal multipliers arrive too early.

### Needed bridge

Teach first:

```text
10% = divide by 10
1%  = divide by 100
50% = half
25% = quarter
5%  = half of 10%
```

Then connect to `0.10`, `0.25`, `1.15`, etc.

---

## Lines, angles, triangles

### Strengths

- diagram ≠ proof is an excellent habit;
- visual anchors and relationship classification are strong.

### Gap

Need an earlier no-algebra phase where the learner identifies angle relationships before equations with `x`.

### Needed bridge

```text
vertical? → equal
straight line? → 180°
triangle? → 180°
```

Only after mastery introduce `3x+10` and `5x-30`.

---

## Quadratics

### Strengths

- method selection is excellent;
- representation-based reasoning is strong.

### Gap

This is not a foundation-start topic. A younger learner needs squares/area, square roots, distributive property, factoring, and coordinate graphs first.

### Required readiness gate

Do not begin Quadratics until the learner can comfortably:

- evaluate `x²`;
- find simple square roots;
- expand `(x+a)(x+b)`;
- factor simple integer quadratics;
- plot/read points and intercepts.

---

## Rational expressions, radians, unit circle, statistical inference

These should be clearly marked **SAT Bridge / later**, not early Foundation material.

The lesson quality can remain SAT-focused; the fix is routing and prerequisite gating.

---

# Definition of Done — age-adaptive lesson

A central lesson is age-adaptive when:

- [ ] prerequisites are explicit;
- [ ] there is a `Foundation Bridge` where needed;
- [ ] intuitive Russian explanation comes before formal terminology;
- [ ] at least one concrete or visual representation is present;
- [ ] at least two worked examples explain decision-making;
- [ ] one faded example requires the learner to finish reasoning;
- [ ] SAT English is introduced after the mathematical meaning for Foundation learners;
- [ ] the lesson says when a younger learner should stop and review prerequisites;
- [ ] practice has a bridge before SAT-calibrated Drill 01 when necessary;
- [ ] timed work is not used as an early mastery gate.

---

# Recommended implementation order

```text
P0
1. learner tracks
2. foundation bridge modules
3. prerequisite gates
4. gateway topics: equations, ratios, percentages, geometry

P1
5. coordinates / linear functions
6. systems / inequalities
7. squares → quadratics bridge
8. vocabulary staging

P2
9. parent prompts
10. confidence labels
11. progress tracker by learner track
```

This audit treats the current SAT curriculum as the target destination, while adding a safer and more understandable road to that destination for younger learners.