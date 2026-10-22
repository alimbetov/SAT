# Two-Variable Data — scatterplots, models, regression, and residuals

## 1. Зачем эта тема нужна на SAT

Two-variable data — официальный skill **Problem-Solving and Data Analysis**. На SAT вам могут показать scatterplot, table или regression equation и спросить:

- есть ли association;
- positive она или negative;
- какая model подходит лучше — linear, quadratic или exponential;
- что означает slope/intercept;
- насколько observed value отличается от prediction;
- можно ли делать causal conclusion.

Главная ошибка — начинать с формулы. Правильный порядок:

```text
DIRECTION → SHAPE → STRENGTH → MODEL → RESIDUAL → INTERPRETATION
```

> **Главная идея:** сначала распознай pattern данных, потом выбирай equation.

---

## 2. Pattern Map — как читать scatterplot

| Что видно | Pattern | Вероятная идея |
|---|---|---|
| точки идут вверх слева направо | positive association | x↑ → y обычно↑ |
| точки идут вниз | negative association | x↑ → y обычно↓ |
| точки около прямой | linear | constant additive trend |
| curve ускоряется | exponential candidate | multiplicative trend |
| U / inverted U | quadratic candidate | turning point |
| точки без pattern | weak/no association | model может быть плохой |
| point far from trend | outlier | investigate residual/influence |

### Pattern 1. Direction

Positive association:

```text
x increases
→ y tends to increase
```

Negative association:

```text
x increases
→ y tends to decrease
```

No association:

```text
knowing x gives little useful information about y
```

### Pattern 2. Strength

**Strong association**: points tightly follow a pattern.  
**Weak association**: points widely scattered.

Strength is not the same as slope.

A steep but scattered line can be weak. A shallow but tight line can be strong.

### Pattern 3. Shape determines model family

#### Linear

Look for approximately constant additive change:

```text
+4, +4, +4, ...
```

Equation:

```math
y=mx+b
```

#### Exponential

Look for approximately constant multiplicative/percent change:

```text
×1.2, ×1.2, ×1.2, ...
```

Equation:

```math
y=a(b)^x
```

#### Quadratic

Look for:

- U-shape;
- inverted U;
- one turning point.

### Pattern 4. Residual

```math
residual=observed-predicted
```

#### Sign meaning

```text
positive residual → point above model
negative residual → point below model
zero residual     → model hits point exactly
```

> **Memory anchor:** `actual minus expected`.

### Pattern 5. Residual plot

A good model tends to leave residuals that look **random around 0**.

If residuals form a clear curve:

```text
pattern remains unexplained
→ current model is missing structure
```

### Pattern 6. Interpolation vs extrapolation

**Interpolation**: predict inside observed x-range. Usually safer.

**Extrapolation**: predict far outside observed range. More uncertain.

### Pattern 7. Association ≠ causation

A scatterplot can show a strong relationship without proving one variable causes the other.

Example:

```text
ice cream sales ↑
drowning incidents ↑
```

Possible lurking variable: hot weather.

---

## 3. Guided Learning — model selection step by step

### Decision Tree

```text
What does the pattern look like?
      │
      ├─ straight-ish
      │    → linear candidate
      │
      ├─ constant percent / accelerating one direction
      │    → exponential candidate
      │
      ├─ U / inverted-U
      │    → quadratic candidate
      │
      └─ no stable pattern
           → weak/no useful model

Then:
→ interpret coefficients
→ predict
→ compute residual if asked
→ check whether conclusion is association or causation
```

### Worked Example 1 — read linear model

A model for hours studied `x` and score `y` is:

```math
y=4.5x+62
```

Interpret slope.

Slope = 4.5.

Correct interpretation:

> For each additional hour studied, the model predicts an increase of about **4.5 score points**.

Not:

> Every student definitely gains 4.5 points.

A regression model describes a trend, not a guarantee.

---

### Worked Example 2 — residual

Same model:

```math
y=4.5x+62
```

A student studies 6 hours and scores 86.

Predicted:

```math
4.5(6)+62=89
```

Observed:

```math
86
```

Residual:

```math
86-89=-3
```

Interpretation:

> The observed score was 3 points **below** the model's prediction.

---

### Worked Example 3 — choose model from changes

Table:

| x | y |
|---:|---:|
| 0 | 100 |
| 1 | 120 |
| 2 | 144 |
| 3 | 172.8 |

Differences:

```text
+20, +24, +28.8
```

not constant.

Ratios:

```math
120/100=1.2
```

```math
144/120=1.2
```

```math
172.8/144=1.2
```

Constant multiplier → exponential.

Model:

```math
y=100(1.2)^x
```

---

### Worked Example 4 — quadratic pattern

Suppose data approximately follow:

```text
x:  -2  -1   0   1   2
y:   4   1   0   1   4
```

This is symmetric around `x=0` and has a minimum.

Recognize:

```math
y=x^2
```

Pattern = quadratic.

### Why linear is wrong

Linear data should not reverse direction from decreasing to increasing.

---

### Worked Example 5 — residual pattern rejects model

Suppose linear model residuals are:

```text
x small: positive
x middle: negative
x large: positive
```

That creates a curved residual pattern.

Conclusion:

> Linear model probably misses curvature; consider quadratic.

You do not need a complex statistic to make this decision.

---

### Worked Example 6 — extrapolation trap

Data were collected for temperatures from `10°C` to `30°C`.

A line predicts behavior at `120°C`.

Even if arithmetic is correct, prediction may be unreliable because `120°C` is far outside observed range.

> SAT can test **validity of prediction**, not just calculation.

---

## 4. Practice Ladder

### A. Recognition Drill

Identify likely model/pattern.

1. Points tightly follow an upward straight line → `__________`  
2. Values multiply by about 1.08 each step → `__________`  
3. Scatterplot forms an inverted U → `__________`  
4. Residual plot shows random scatter around 0 → model is likely `__________`

<details>
<summary><strong>Answers</strong></summary>

1. positive linear association  
2. exponential  
3. quadratic  
4. reasonable/appropriate

</details>

### B. Faded Example

Model:

```math
y=7+2.5x
```

At `x=4`, predicted value:

```math
7+2.5(4)=\boxed{\phantom{17}}
```

Observed value = 20.

Residual:

```math
20-\boxed{\phantom{17}}=\boxed{\phantom{3}}
```

<details>
<summary><strong>Solution</strong></summary>

Prediction = 17. Residual = 3, so observed is 3 units above model.

</details>

### C. SAT-style Independent Practice

#### Problem 1 — Easy — Multiple Choice

If points generally rise from left to right, the association is:

**A)** positive  
**B)** negative  
**C)** none  
**D)** impossible

#### Problem 2 — Easy — Grid-in

For `y=3x+10`, what value is predicted when `x=5`?

#### Problem 3 — Medium — Multiple Choice

A scatterplot forms a clear U-shaped pattern. Which model is most plausible?

**A)** constant  
**B)** linear  
**C)** quadratic  
**D)** no model

#### Problem 4 — Medium — Multiple Choice

A quantity increases by roughly the same percentage for each equal increase in `x`. Which model is most appropriate?

**A)** linear  
**B)** exponential  
**C)** constant  
**D)** random

#### Problem 5 — Hard — Grid-in

A model `y=12-0.8x` predicts a value for `x=5`. If observed value is 10, what is the residual?

#### Problem 6 — Hard Transfer — Multiple Choice

A linear model fits data for `1≤x≤10`. Which prediction should be treated with the greatest caution?

**A)** x=4  
**B)** x=7  
**C)** x=9  
**D)** x=100

<details>
<summary><strong>Ответы и решения</strong></summary>

1. **A**.  
2. **25**.  
3. **C**.  
4. **B**.  
5. **2**. Prediction `12-0.8(5)=8`; residual `10-8=2`.  
6. **D**. Extreme extrapolation is least reliable.

</details>

---

## 5. Error Clinic — ошибки распознавания модели

### Ошибка 1. Choose linear because equation is familiar

Familiarity is not evidence.

Check pattern:

```text
constant difference → linear
constant ratio      → exponential
turning point       → quadratic
```

---

### Ошибка 2. Reverse residual sign

Wrong:

```math
predicted-observed
```

SAT convention here:

```math
observed-predicted
```

Use phrase:

```text
actual minus model
```

---

### Ошибка 3. Strong correlation means causation

No.

Possible problems:

- lurking variable;
- reverse causality;
- selection bias.

Causal inference requires experiment design logic, not a prettier scatterplot.

---

### Ошибка 4. Interpreting intercept outside meaningful context

If model:

```math
salary=5000+2000(years)
```

intercept may represent salary at 0 years and be meaningful.

But in another model, `x=0` may be outside observed range and interpretation may be nonsensical.

---

## 6. Digital SAT Strategy — Desmos as model lab

### For linear regression

With lists `x1`, `y1`:

```text
y1 ~ m x1 + b
```

Desmos estimates `m` and `b`.

### Compare models

You may compare:

```text
y1 ~ m x1+b
```

```text
y1 ~ a*b^(x1)
```

or inspect shape directly.

### But do not outsource recognition

Before opening regression, ask:

```text
What pattern do I expect?
```

Otherwise calculator output becomes meaningless numbers.

### Fast residual check

If predicted = 42 and observed = 39:

```text
39-42=-3
```

Negative → point below model.

---

## 7. SAT Language Decoder и связи

### Language Decoder

| Phrase | Meaning |
|---|---|
| `association` | statistical relationship |
| `positive association` | x↑, y tends↑ |
| `negative association` | x↑, y tends↓ |
| `line of best fit` | linear trend model |
| `predicted` | model output |
| `observed` | actual data value |
| `residual` | observed - predicted |
| `best models the data` | choose family matching pattern |
| `extrapolate` | predict outside data range |
| `correlation` | association, not necessarily causation |

### Connections

**Опирается на:**

- linear functions;
- quadratics;
- exponential functions;
- one-variable statistics.

**Дальше:**

- experiments and causal claims;
- residual analysis;
- statistical inference.

### Transfer Question

A table has constant first differences in y for equal x-steps. What model should you test first, and why?

<details>
<summary><strong>Reasoning</strong></summary>

Linear model, because constant first difference indicates constant additive rate of change.

</details>

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я читаю direction, shape и strength scatterplot.
- [ ] Я различаю linear, exponential и quadratic patterns.
- [ ] Я интерпретирую slope как predicted change per unit x.
- [ ] Я вычисляю residual как observed-predicted.
- [ ] Я использую residual pattern для оценки model fit.
- [ ] Я отличаю interpolation от extrapolation.
- [ ] Я не делаю causal conclusion только из association.
- [ ] Я могу выбрать model до использования Desmos.

> **Mastery test:** видя table или scatterplot без формул, вы должны сначала назвать pattern, а уже затем выбирать equation.