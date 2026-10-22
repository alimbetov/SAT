# Nonlinear Functions — нелинейные функции

## 1. Зачем эта тема нужна на SAT

Это интеграционная тема Advanced Math. Здесь SAT проверяет, умеете ли вы **узнать family функции по equation, table или graph** и выбрать правильный способ чтения информации.

> **Главная идея:** сначала распознай family, потом применяй его язык.

Не нужно решать quadratic как exponential или читать absolute-value graph как parabola. У каждой family есть свои визуальные признаки и «быстрые» свойства.

---

## 2. Pattern Map — узнаём семейство функции

| Family | Equation pattern | Visual / numerical clue |
|---|---|---|
| quadratic | `ax²+bx+c` | parabola, changing slope |
| exponential | `a(b)^x` | constant multiplicative factor |
| polynomial | powers `x^n` | smooth curve, degree controls shape |
| rational | variable in denominator | holes/asymptotes possible |
| radical | `√(...)` | endpoint/domain restriction |
| absolute value | `a|x-h|+k` | V-shape |

### First Question

Перед вычислениями спросите:

> **Какое это семейство?**

Потом:

> **Что эта форма показывает сразу?**

---

## 3. Учимся читать разные families

### Pattern A — Quadratic: read the form

#### Vertex form

```math
f(x)=2(x-3)^2+5.
```

Сразу видно:

- vertex `(3,5)`;
- minimum = `5`, because `a=2>0`.

**Не раскрывайте скобки**, если вопрос просит vertex/minimum.

#### Factored form

```math
f(x)=(x-2)(x-8).
```

Roots:

```math
2,8.
```

Again: use the information already visible.

---

### Pattern B — Exponential: look for multiplicative change

```math
P(t)=500(1.08)^t.
```

Immediately:

- initial value = `500`;
- growth rate = `8%` per period.

If table values multiply by same factor, think exponential.

Example:

```text
100, 120, 144, 172.8
```

Each term ×`1.2`.

---

### Pattern C — Absolute value: V-shape and vertex

```math
y=3|x+2|-4.
```

Vertex:

```math
(-2,-4).
```

Why negative 2? Because inside is `x-(-2)`.

---

### Pattern D — Radical: domain starts somewhere

```math
y=\sqrt{x-4}+2.
```

For real outputs:

```math
x-4\ge0
```

```math
x\ge4.
```

Graph begins at:

```math
(4,2).
```

**Recognition clue:** endpoint often matters more than intercepts.

---

### Pattern E — Rational: denominator controls domain

```math
y=\frac1{x-3}.
```

Undefined at:

```math
x=3.
```

That x-value often corresponds to a vertical asymptote or hole depending on structure.

---

### Pattern F — Transformations

General transformation:

```math
y=f(x-h)+k.
```

- inside `x-h` → right by `h`;
- outside `+k` → up by `k`.

### Memory Anchor

```text
INSIDE = opposite sign
OUTSIDE = same sign
```

Example:

```math
y=(x-4)^2+1
```

means right 4, up 1.

---

## 4. Method Selector + SAT Language Decoder

### Family Recognition Tree

```text
x² dominant?
  → quadratic

constant percent/factor?
  → exponential

variable in denominator?
  → rational

square root?
  → radical

absolute-value bars?
  → absolute value

higher integer powers?
  → polynomial
```

### What the question asks determines the form

```text
Need roots?
  → factored form / intersections

Need vertex/minimum?
  → vertex form / graph

Need initial value?
  → evaluate at x=0 / exponential coefficient

Need domain?
  → denominator/radical restrictions

Need transformations?
  → compare to parent function
```

### SAT English Decoder

| Phrase | Think |
|---|---|
| `minimum value` | vertex / lowest point |
| `zeros` | x-intercepts |
| `initial value` | input `0` |
| `constant percentage change` | exponential |
| `domain` | allowed inputs |
| `shifted right` | replace `x` with `x-h` |

---

## 5. Guided Practice — identify before solving

### Example 1 — Recognition

```math
y=4(1.3)^x
```

Family: exponential.

Why? Variable appears in exponent.

### Example 2 — Read without algebra

```math
y=-2(x+5)^2+7.
```

- family: quadratic;
- vertex: `(-5,7)`;
- opens downward;
- maximum = `7`.

No expansion needed.

### Example 3 — Table recognition

```text
x: 0  1  2  3
y: 5 10 20 40
```

Same difference? No.

Same ratio? Yes, ×2.

Therefore exponential.

### Example 4 — Domain transfer

```math
f(x)=\sqrt{2x-6}.
```

Require:

```math
2x-6\ge0
```

```math
x\ge3.
```

---

## 6. Error Clinic + Desmos Strategy

### Error 1 — expanding useful forms

If vertex is already visible, expansion may hide useful structure.

### Error 2 — confusing constant difference and constant ratio

```text
+5 each step → linear
×1.05 each step → exponential
```

### Error 3 — wrong horizontal-shift sign

`f(x-3)` shifts right 3.

### Error 4 — treating all nonlinear graphs the same

A parabola, V-shape and radical graph have different signatures.

### Desmos

Desmos is especially useful for:

- recognizing family shape;
- checking transformations;
- finding extrema;
- locating roots/intersections.

But first identify the family. Otherwise graphing becomes blind button-pushing.

---

## 7. SAT-Style Practice

### Problem 1 — Easy — Multiple Choice

Which function is exponential?

**A)** `y=4x+1`  
**B)** `y=x²+1`  
**C)** `y=5(1.2)^x`  
**D)** `y=√x`

### Problem 2 — Easy — Grid-in

If

```math
f(x)=x^2+6,
```

what is `f(4)`?

### Problem 3 — Medium — Multiple Choice

What is the vertex of

```math
y=2(x-5)^2-3?
```

**A)** `(-5,-3)`  
**B)** `(5,-3)`  
**C)** `(5,3)`  
**D)** `(-3,5)`

### Problem 4 — Medium — Multiple Choice

Which table is most likely exponential?

**A)** `10, 15, 20, 25`  
**B)** `3, 6, 12, 24`  
**C)** `1, 4, 9, 16`  
**D)** `8, 8, 8, 8`

### Problem 5 — Hard — Grid-in

For

```math
f(x)=a(x-2)^2+7,
```

the point `(4,15)` lies on the graph. Find `a`.

<details><summary><strong>Answers</strong></summary>

1. **C**  
2. `22`  
3. **B**  
4. **B**  
5. `2`

</details>

---

## 8. Мини-чек-лист и Transfer

- [ ] Я узнаю основные nonlinear families по equation/table/graph.
- [ ] Я читаю полезную информацию из текущей формы, не делая лишних преобразований.
- [ ] Я различаю constant difference и constant ratio.
- [ ] Я понимаю basic transformations.
- [ ] Я выбираю algebra vs graph vs Desmos по типу вопроса.

### Transfer Question

Почему для функции

```math
y=(x-7)^2+4
```

не стоит сначала раскрывать скобки, если SAT спрашивает minimum value?

Потому что vertex form уже показывает minimum value `4` напрямую.
