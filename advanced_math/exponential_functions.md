# Exponential Functions — экспоненциальные функции

## 1. Зачем эта тема нужна на SAT

Экспоненциальные задачи появляются, когда величина меняется на **одинаковый процент** за каждый период. Главный навык — не запомнить формулу, а научиться быстро отличать exponential growth от linear growth и правильно читать параметры модели.

> **Главная идея:** linear добавляет одно и то же число; exponential умножает на один и тот же factor.

---

## 2. Pattern Map — что вижу и что это значит

| Что в условии | Модель | Что делать |
|---|---|---|
| `increases by 8 each year` | linear | add 8 |
| `increases by 8% each year` | exponential | multiply by `1.08` |
| `decreases by 20%` | exponential decay | factor `0.80` |
| `doubles every 3 hours` | exponential | factor `2` per 3 hours |
| `halves every 5 days` | exponential decay | factor `0.5` per 5 days |
| `a(b)^x` | exponential model | `a` initial, `b` factor |
| exponent `t/k` | period = `k` units | factor applies every `k` units |

### Mental model

```text
LINEAR:
100 → 110 → 120 → 130
add +10 each step

EXPONENTIAL:
100 → 110 → 121 → 133.1
multiply ×1.10 each step
```

Если изменение считается от **нового текущего значения**, это главный сигнал exponential model.

---

## 3. Учимся решать по паттернам

### Pattern A — Convert percent to factor

Growth by `r%`:

```math
1+\frac{r}{100}
```

Decay by `r%`:

```math
1-\frac{r}{100}
```

#### Worked Example

Increase by `12%`:

```math
1+0.12=1.12.
```

Decrease by `12%`:

```math
1-0.12=0.88.
```

### Visual Anchor

```text
1.12 → 112% remains → +12%
0.88 → 88% remains  → -12%
```

---

### Pattern B — Build the model

General form:

```math
y=a(b)^t
```

where:

- `a` = initial value;
- `b` = growth/decay factor;
- `t` = number of periods.

#### Worked Example

A bacteria population starts at `800` and grows by `25%` each hour.

Initial value:

```math
a=800.
```

Growth factor:

```math
b=1.25.
```

Model:

```math
P(h)=800(1.25)^h.
```

After 2 hours:

```math
P(2)=800(1.25)^2=1250.
```

---

### Pattern C — Read a model backwards

#### Worked Example

```math
V(t)=24000(0.82)^t.
```

What does `0.82` mean?

`82%` remains each period.

So decrease is:

```math
100%-82%=18%.
```

**SAT trap:** factor `0.82` does **not** mean decrease of 82%.

---

### Pattern D — Period hidden in the exponent

#### Worked Example

```math
P(t)=1200(1.5)^{t/3}.
```

The exponent increases by `1` whenever `t` increases by `3`.

Therefore the population multiplies by `1.5` every **3 time units**.

Growth every 3 units:

```math
50%.
```

### Recognition rule

```text
(b)^(t/k)
→ b is the factor for k units of time
```

---

### Pattern E — Doubling and halving

#### Worked Example

A quantity starts at `300` and doubles every 4 hours.

After `t` hours:

```math
Q(t)=300\cdot2^{t/4}.
```

Why `t/4`?

Because every 4 hours counts as one doubling period.

---

### Pattern F — Linear or exponential?

#### Worked Example

Which is exponential?

1. A tank loses 5 liters per minute.
2. A car loses 15% of its value per year.

Case 1: same amount → linear.

Case 2: same percentage → exponential.

### Fast recognition

```text
same AMOUNT     → linear
same PERCENT    → exponential
same MULTIPLIER → exponential
```

---

## 4. Method Selector + SAT Language Decoder

### Decision Tree

```text
Does the quantity change by a fixed amount?
  → linear

Does it change by a fixed percent/factor?
  → exponential

Does it double/halve?
  → exponential

Is exponent t/k?
  → factor applies every k units

Need unknown time?
  → algebra if simple; Desmos intersection if messy
```

### SAT English Decoder

| Phrase | Meaning |
|---|---|
| `increases by 7%` | factor `1.07` |
| `decreases by 7%` | factor `0.93` |
| `is 80% of its previous value` | factor `0.80` |
| `doubles every 5 years` | factor `2`, period 5 |
| `halves every 3 hours` | factor `0.5`, period 3 |
| `initial value` | `a` in `a(b)^t` |
| `growth factor` | `b` |

---

## 5. Guided Practice — от полной опоры к самостоятельности

### Example 1 — full support

A value starts at `500` and grows by `6%` each year.

Pattern: percent growth.

Factor:

```math
1.06.
```

Model:

```math
V(t)=500(1.06)^t.
```

### Example 2 — partial support

A machine worth `$20,000` loses `12%` of its value each year.

1. Initial value = `__________`
2. Decay factor = `__________`
3. Model = `__________`

<details><summary>Answer</summary>

```math
V(t)=20000(0.88)^t
```

</details>

### Example 3 — recognition

Which is exponential?

- `C=50+8t`
- `P=50(1.08)^t`

Answer: second model, because output is repeatedly multiplied by `1.08`.

### Example 4 — transfer

```math
A(t)=900(1.21)^{t/2}.
```

By what percent does the quantity grow every 2 time units?

<details><summary>Solution</summary>

Factor `1.21` → growth `21%` every 2 units.

</details>

---

## 6. Error Clinic + Desmos Strategy

### Error 1 — using `0.08` for 8% growth

Wrong:

```math
y=a(0.08)^t.
```

Right:

```math
y=a(1.08)^t.
```

### Error 2 — reading factor as percent change

`0.75` means 75% remains, so decrease = 25%.

### Error 3 — ignoring the period

In

```math
2^{t/6},
```

factor `2` applies every 6 units, not every 1 unit.

### Desmos

Use Desmos when target value is given and time is unknown.

Example:

```text
y=1000(1.08)^x
y=1500
```

Intersection gives the time when the population reaches 1500.

For simple factor interpretation, manual reasoning is faster.

---

## 7. SAT-Style Practice

### Problem 1 — Easy — Multiple Choice

A quantity increases by `9%` per year. What is the growth factor?

**A)** `0.09`  
**B)** `0.91`  
**C)** `1.09`  
**D)** `1.90`

### Problem 2 — Easy — Multiple Choice

For

```math
f(x)=400(0.7)^x,
```

what percent decrease occurs per unit increase in `x`?

**A)** 7%  
**B)** 30%  
**C)** 70%  
**D)** 130%

### Problem 3 — Medium — Grid-in

A population starts at `600` and grows by `20%` for one period. What is the new population?

### Problem 4 — Medium — Multiple Choice

Which situation is exponential?

**A)** salary increases by `$1000` each year  
**B)** tank loses `3` liters each minute  
**C)** investment grows by `5%` each year  
**D)** taxi costs `$5 + $2/mile`

### Problem 5 — Hard — Grid-in

```math
P(t)=500(1.4)^{t/5}.
```

By what percent does `P` increase every 5 time units?

<details><summary><strong>Answers</strong></summary>

1. **C**  
2. **B**  
3. `720`  
4. **C**  
5. `40`

</details>

---

## 8. Мини-чек-лист и Transfer

- [ ] Я мгновенно различаю fixed amount и fixed percent.
- [ ] Я перевожу percentage change в growth/decay factor.
- [ ] Я читаю initial value и factor из `a(b)^t`.
- [ ] Я понимаю exponent `t/k` как период.
- [ ] Я умею строить модель по тексту.
- [ ] Я знаю, когда Desmos быстрее ручного решения.

### Transfer Question

Почему

```math
100(1.1)^t
```

и

```math
100+10t
```

дают одинаковое значение при `t=1`, но дальше расходятся?

Потому что в первой модели 10% каждый раз берутся от нового текущего значения, а во второй каждый шаг добавляется фиксированное число 10.
