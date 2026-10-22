# Nonlinear Equations and Systems — нелинейные уравнения и системы

## 1. Зачем эта тема нужна на SAT

Это итоговая тема Advanced Math: здесь ученик должен не только уметь решать разные nonlinear equations, но и **выбирать метод по структуре задачи**.

На SAT могут встретиться:

- quadratic equations;
- radical equations;
- rational equations;
- exponential equations;
- linear–quadratic systems;
- parameter questions about number of intersections.

> **Главная идея:** сначала распознай тип equation/system, затем выбери самый короткий надёжный метод.

---

## 2. Pattern Map — тип задачи → метод

| Что вы видите | Тип | Обычно лучший первый метод |
|---|---|---|
| `x²-5x+6=0` | quadratic | factoring if easy |
| ugly quadratic | quadratic | formula / Desmos |
| `√(x+1)=x-1` | radical | isolate, square, check |
| variable in denominator | rational | restrictions + LCD/cross multiply |
| `2^x=8` | exponential | common base |
| `y=x+2`, `y=x²-4` | linear–quadratic system | substitution / intersections |
| exactly one intersection | parameter/tangent | discriminant `D=0` |
| asks only number of solutions | graphical | count intersections |

### Mental model

```text
EQUATION TYPE
    ↓
METHOD
    ↓
CANDIDATES
    ↓
CHECK / INTERPRET
```

---

## 3. Учимся выбирать и применять методы

### Pattern A — Quadratic: factor when structure is friendly

#### Worked Example

Solve:

```math
x^2-7x+12=0.
```

Need two numbers with product `12` and sum `-7`:

```text
-3 and -4
```

So:

```math
(x-3)(x-4)=0.
```

Solutions:

```math
x=3,4.
```

**Method choice:** factoring was faster than quadratic formula.

---

### Pattern B — Exponential: use common base first

#### Worked Example

```math
3^x=27.
```

Recognize:

```math
27=3^3.
```

Therefore:

```math
x=3.
```

No graph or logarithms needed.

---

### Pattern C — Radical: square, then check

#### Worked Example

```math
\sqrt{x+5}=x-1.
```

1. left side ≥0, so `x≥1`;
2. square both sides;
3. solve resulting quadratic;
4. test candidates in original equation.

This is the radical-equation pattern learned earlier.

---

### Pattern D — Rational: domain first

#### Worked Example

```math
\frac1x=\frac2{x+3}.
```

Restrictions:

```math
x\ne0,-3.
```

Cross multiply:

```math
x+3=2x.
```

```math
x=3.
```

Check restriction: valid.

---

### Pattern E — Linear–quadratic system = intersection

Solve:

```math
y=x+2
```

and

```math
y=x^2-4.
```

Since both equal `y`:

```math
x+2=x^2-4.
```

Move all terms:

```math
x^2-x-6=0.
```

Factor:

```math
(x-3)(x+2)=0.
```

So:

```math
x=3,-2.
```

Find corresponding y-values:

```math
(3,5),\quad(-2,0).
```

### Key interpretation

These are exactly the **intersection points** of the line and parabola.

---

### Pattern F — Number of intersections via discriminant

A line and parabola may intersect 0, 1 or 2 times.

After substitution you get a quadratic:

```math
ax^2+bx+c=0.
```

Then:

```text
D < 0 → 0 real intersections
D = 0 → 1 intersection (tangent)
D > 0 → 2 intersections
```

#### Worked Example

For what `k` does

```math
y=x+k
```

meet

```math
y=x^2
```

at exactly one point?

Set equal:

```math
x^2=x+k
```

```math
x^2-x-k=0.
```

Exactly one solution means:

```math
D=0.
```

```math
(-1)^2-4(1)(-k)=0
```

```math
1+4k=0
```

```math
k=-\frac14.
```

---

## 4. Method Selector + SAT Language Decoder

### Decision Tree

```text
Can it factor easily?
  → factor

Same exponential base available?
  → rewrite to common base

Radical present?
  → isolate, square, check

Variable in denominator?
  → restrictions, then clear denominators

System with y already isolated?
  → set expressions equal / substitute

Question asks number of intersections?
  → graph or discriminant

Question asks parameter for one intersection?
  → D = 0
```

### SAT English Decoder

| Phrase | What it signals |
|---|---|
| `solution to the system` | point satisfying both equations |
| `point of intersection` | system solution |
| `exactly one real solution` | often `D=0` |
| `no real solutions` | often `D<0` |
| `valid solution` | check domain/extraneous candidates |
| `how many solutions` | count algebraic roots or graph intersections |

---

## 5. Guided Practice — fading support

### Example 1 — identify method

```math
x^2-9=0.
```

Best method?

Difference of squares / square root.

Solutions:

```math
x=\pm3.
```

### Example 2 — partial support

```math
2^x=32.
```

Rewrite 32 as a power of 2:

```math
32=2^{___}.
```

<details><summary>Answer</summary>

`2^5`, so `x=5`.

</details>

### Example 3 — system

```math
y=x+1
```

```math
y=x^2-1.
```

Set equal:

```math
x+1=x^2-1.
```

Then solve:

```math
x^2-x-2=0.
```

```math
(x-2)(x+1)=0.
```

Intersections have x-values `2` and `-1`.

### Example 4 — transfer

A line and parabola have exactly one common point. After substitution you obtain

```math
x^2+6x+k=0.
```

What condition should you use?

<details><summary>Answer</summary>

```math
D=0.
```

</details>

---

## 6. Error Clinic + Desmos Strategy

### Error 1 — using one method for every equation

Not every quadratic deserves quadratic formula. Not every system deserves substitution. Choose method by structure.

### Error 2 — forgetting y-coordinate

For a system, `x` alone is usually not the complete solution. Return to an equation and find `y`.

### Error 3 — ignoring invalid candidates

Radical and rational equations require checks.

### Error 4 — assuming one intersection

Nonlinear systems may have 0, 1, 2 or more intersections.

### Desmos — where it is strongest

For systems:

```text
y=x+2
y=x^2-4
```

Click intersection points.

For «how many solutions?» problems, Desmos may be the fastest method.

For parameter questions, algebra/discriminant often gives cleaner exact reasoning.

---

## 7. SAT-Style Practice

### Problem 1 — Easy — Multiple Choice

How many real solutions does

```math
x^2=16
```

have?

**A)** 0  
**B)** 1  
**C)** 2  
**D)** 4

### Problem 2 — Easy — Grid-in

Solve:

```math
5^x=125.
```

### Problem 3 — Medium — Multiple Choice

The graphs

```math
y=x^2
```

and

```math
y=9
```

intersect at which x-values?

**A)** `0 only`  
**B)** `3 only`  
**C)** `-3 and 3`  
**D)** `-9 and 9`

### Problem 4 — Medium — Grid-in

For the system

```math
y=x+2,
```

```math
y=x^2,
```

what is the positive x-coordinate of an intersection?

### Problem 5 — Hard — Multiple Choice

A line and parabola have exactly one point of intersection. After substitution, the resulting quadratic must satisfy:

**A)** `D<0`  
**B)** `D=0`  
**C)** `D>0`  
**D)** `a=0`

<details><summary><strong>Answers</strong></summary>

1. **C**  
2. `3`  
3. **C**  
4. `2`  
5. **B**

</details>

---

## 8. Мини-чек-лист и Transfer

- [ ] Я сначала распознаю equation type, а не применяю метод автоматически.
- [ ] Я выбираю factoring / common base / squaring / LCD по структуре.
- [ ] Я понимаю system solutions как intersections.
- [ ] Я нахожу полный ordered pair `(x,y)`.
- [ ] Я использую discriminant для числа quadratic intersections.
- [ ] Я знаю, когда Desmos быстрее algebra.

### Transfer Question

Почему tangent line to a parabola соответствует `D=0` после substitution?

Потому что tangent имеет с parabola ровно одну общую точку, а quadratic equation с exactly one real root имеет discriminant zero.
