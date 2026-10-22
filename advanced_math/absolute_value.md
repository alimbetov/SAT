# Absolute Value — модуль числа и функции с модулем

## 1. Зачем эта тема нужна на SAT

Absolute value — это не «смена знака». На SAT он появляется как язык **расстояния**, двух возможных branches, интервалов и V-shaped graphs.

> **Главная идея:** `|x-a|` — расстояние от `x` до `a`.

Если ученик понимает distance model, equations и inequalities с modulus перестают быть набором отдельных правил.

---

## 2. Pattern Map — как распознавать задачу

| Что вы видите | Значение | Что делать |
|---|---|---|
| `|x|` | distance from 0 | result ≥0 |
| `|x-a|=d` | distance = d | two points: `a±d` |
| `|x-a|<d` | distance less than d | inside interval |
| `|x-a|>d` | distance greater than d | outside interval |
| `y=a|x-h|+k` | V-shaped graph | vertex `(h,k)` |
| `|A|=-3` | impossible | no solution |

### Visual Anchor — distance on a number line

```text
      distance 5
<---------|---------|---------|--------->
         -2         3         8
                    center
```

`|x-3|=5` means points 5 units away from 3:

```math
x=-2\quad\text{or}\quad x=8.
```

---

## 3. Учимся решать по паттернам

### Pattern A — Equation means two branches

#### Worked Example

Solve:

```math
|2x-5|=9.
```

**Notice:** absolute value equals a positive number.

So inside can be `9` or `-9`:

```math
2x-5=9
```

or

```math
2x-5=-9.
```

First branch:

```math
2x=14\Rightarrow x=7.
```

Second branch:

```math
2x=-4\Rightarrow x=-2.
```

Answer:

```text
-2 and 7
```

---

### Pattern B — Use distance directly

#### Worked Example

Solve:

```math
|x-4|=6.
```

Think:

> Which points are 6 units from 4?

```math
4-6=-2
```

```math
4+6=10.
```

So:

```math
x=-2,10.
```

This is often faster than formal branch writing.

---

### Pattern C — Less than means inside

#### Worked Example

```math
|x-3|<5.
```

Distance from 3 is less than 5.

Endpoints:

```math
3-5=-2,
```

```math
3+5=8.
```

Therefore:

```math
-2<x<8.
```

### Memory Anchor

```text
LESS THAN  → INSIDE
GREATER THAN → OUTSIDE
```

---

### Pattern D — Greater than means outside

#### Worked Example

```math
|x+1|>4.
```

Center is `-1`.

Distance greater than 4 means outside:

```math
x<-5
```

or

```math
x>3.
```

---

### Pattern E — Impossible negative distance

```math
|3x-1|=-4
```

No solution.

Why? Absolute value is a distance and distance cannot be negative.

---

### Pattern F — Read a V-shaped graph from equation

General form:

```math
y=a|x-h|+k.
```

Vertex:

```math
(h,k).
```

#### Worked Example

```math
y=2|x-5|-3.
```

Vertex:

```math
(5,-3).
```

Since `a=2>0`, graph opens upward.

If `a<0`, V is reflected downward.

---

## 4. Method Selector + SAT Language Decoder

### Decision Tree

```text
|A| = positive number?
  → two branches

|A| = 0?
  → A = 0 only

|A| = negative number?
  → no solution

|x-a| < d?
  → inside interval

|x-a| > d?
  → outside interval

Need graph feature?
  → read vertex from a|x-h|+k
```

### SAT English Decoder

| Phrase | Think |
|---|---|
| `distance from` | absolute value |
| `within 5 units of` | `<` or `≤` absolute-value inequality |
| `more than 5 units from` | `>` absolute-value inequality |
| `vertex of the graph` | `(h,k)` in `a|x-h|+k` |
| `two solutions` | positive distance usually creates two branches |

---

## 5. Guided Practice — fading support

### Example 1 — full support

```math
|x-2|=7
```

Center = `2`, distance = `7`.

```math
x=2±7.
```

Answers:

```math
-5,9.
```

### Example 2 — partial support

```math
|3x+1|=10.
```

Branches:

```math
3x+1=____
```

or

```math
3x+1=____.
```

<details><summary>Answer</summary>

`10` and `-10`; solutions `3` and `-11/3`.

</details>

### Example 3 — interval reasoning

```math
|x|<6.
```

Distance from 0 less than 6:

```math
-6<x<6.
```

### Example 4 — transfer

```math
|x-10|\le3.
```

What interval does this describe?

<details><summary>Solution</summary>

Within 3 units of 10:

```math
7\le x\le13.
```

</details>

---

## 6. Error Clinic + Desmos Strategy

### Error 1 — “absolute value flips the sign”

Not always. `|5|=5` and `|-5|=5`.

Think distance, not sign change.

### Error 2 — forgetting the second branch

`|A|=d` with `d>0` usually gives two equations.

### Error 3 — confusing inside/outside

```text
<  → inside
>  → outside
```

### Error 4 — wrong vertex sign

In

```math
y=|x-4|+2,
```

vertex is `(4,2)`, not `(-4,2)`.

### Desmos

Enter:

```text
y=abs(2x-5)
y=9
```

Intersections show both solutions.

Desmos is especially useful when coefficients are awkward or graph interpretation is asked.

---

## 7. SAT-Style Practice

### Problem 1 — Easy — Multiple Choice

What is

```math
|-12|?
```

**A)** `-12`  
**B)** `0`  
**C)** `12`  
**D)** `24`

### Problem 2 — Easy — Grid-in

Solve

```math
|x-5|=4.
```

Enter the larger solution.

### Problem 3 — Medium — Multiple Choice

Which inequality is equivalent to

```math
|x|<7?
```

**A)** `x<7`  
**B)** `x>-7`  
**C)** `-7<x<7`  
**D)** `x<-7 or x>7`

### Problem 4 — Medium — Multiple Choice

What is the vertex of

```math
y=3|x+2|-5?
```

**A)** `(2,-5)`  
**B)** `(-2,-5)`  
**C)** `(-5,-2)`  
**D)** `(2,5)`

### Problem 5 — Hard — Grid-in

The equation

```math
|4x-3|=13
```

has two solutions. What is the larger solution?

<details><summary><strong>Answers</strong></summary>

1. **C**  
2. `9`  
3. **C**  
4. **B**  
5. `4`

</details>

---

## 8. Мини-чек-лист и Transfer

- [ ] Я понимаю absolute value как distance.
- [ ] Я решаю positive absolute-value equations через two branches.
- [ ] Я мгновенно распознаю no-solution case with negative distance.
- [ ] Я читаю `<` как inside и `>` как outside.
- [ ] Я нахожу vertex `a|x-h|+k`.

### Transfer Question

A measurement must stay within `2.5` units of target `100`. Write an absolute-value inequality.

Answer:

```math
|x-100|\le2.5.
```
