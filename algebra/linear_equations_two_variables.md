# Linear Equations in Two Variables — линейные уравнения с двумя переменными

> **Цель урока:** понять, что equation with two variables описывает **целую прямую**, и научиться читать эту прямую через slope, intercepts, points, parallel/perpendicular relationships.

Главная идея:

> **One equation in x and y = infinitely many points on one line.**

---

# 1. Pattern Map

| Что вижу | Паттерн | Что делаю |
|---|---|---|
| `y=mx+b` | slope-intercept form | читаю slope и y-intercept |
| `Ax+By=C` | standard form | удобно искать intercepts |
| point `(x,y)` | point check | подставляю coordinates |
| две points | line from points | slope → equation |
| line through point parallel to given line | parallel | same slope |
| line perpendicular to given line | perpendicular | negative reciprocal slope |
| x-intercept | `y=0` | solve for x |
| y-intercept | `x=0` | solve for y |

Перед вычислением спросите:

> **«Какую информацию о линии мне уже показывает эта форма?»**

---

# 2. Что означает equation с двумя variables

Рассмотрим:

```math
y=2x+1
```

Подставим разные x:

| x | y |
|---:|---:|
| 0 | 1 |
| 1 | 3 |
| 2 | 5 |
| 3 | 7 |

Получаем points:

```text
(0,1), (1,3), (2,5), (3,7), ...
```

Все они лежат на одной line.

В отличие от equation with one variable, здесь обычно не один solution, а infinitely many ordered pairs.

---

# 3. PATTERN 1 — Check whether a point lies on a line

Очень простой, но частый SAT skill.

## Worked Example

Does `(2,7)` lie on

```math
y=3x+1?
```

Подставляем:

```math
7\stackrel{?}{=}3(2)+1
```

```math
7=7
```

Да.

### Pattern

```text
point given
→ substitute x and y
→ true equality = point is on line
```

---

# 4. PATTERN 2 — Intercepts from standard form

Standard form:

```math
Ax+By=C
```

очень удобна для intercepts.

## X-intercept

На x-axis:

```text
y=0
```

## Y-intercept

На y-axis:

```text
x=0
```

---

## Worked Example

```math
2x+3y=12
```

### x-intercept

Set `y=0`:

```math
2x=12
```

```math
x=6
```

Point:

```text
(6,0)
```

### y-intercept

Set `x=0`:

```math
3y=12
```

```math
y=4
```

Point:

```text
(0,4)
```

---

# 5. Visual Anchor — intercept = where one coordinate becomes zero

```text
x-axis → y = 0

y-axis → x = 0
```

Это проще, чем заучивать два отдельных правила.

---

# 6. PATTERN 3 — Convert standard form to slope-intercept form

Иногда SAT даёт:

```math
2x+3y=12
```

а спрашивает slope.

Тогда нужно выразить `y`.

```math
3y=-2x+12
```

```math
y=-\frac23x+4
```

Теперь видно:

```text
slope = -2/3
y-intercept = 4
```

---

# 7. PATTERN 4 — Parallel lines

Parallel lines имеют одинаковый slope.

```math
y=3x-4
```

Любая parallel line имеет:

```math
m=3
```

но другой intercept, если это действительно другая line.

---

## Worked Example

A line passes through `(2,5)` and is parallel to

```math
y=3x-4
```

### Step 1 — copy slope

```math
m=3
```

### Step 2 — use point-slope form

```math
y-5=3(x-2)
```

### Step 3 — simplify

```math
y=3x-1
```

### Check

Same slope `3` → parallel.

Point `(2,5)`:

```math
5=6-1
```

Correct.

---

# 8. PATTERN 5 — Perpendicular lines

For nonvertical lines, perpendicular slopes are **negative reciprocals**.

If:

```math
m=\frac23
```

then perpendicular slope:

```math
-\frac32
```

Якорь:

```text
flip fraction
change sign
```

или:

```math
m_1m_2=-1
```

---

## Worked Example 1

Given:

```math
y=-4x+7
```

Slope is `-4`, or:

```math
-\frac41
```

Flip:

```math
-\frac14
```

Change sign:

```math
\frac14
```

Perpendicular slope:

```math
\frac14
```

---

## Error Clinic

Students often think perpendicular means just change sign:

```text
2 → -2
```

Wrong.

Correct:

```text
2 = 2/1
flip → 1/2
change sign → -1/2
```

---

# 9. PATTERN 6 — Equation from two points

This overlaps with Linear Functions and is worth mastering.

Given:

```text
(2,5), (6,13)
```

### Step 1 — slope

```math
m=\frac{13-5}{6-2}=2
```

### Step 2 — use `y=mx+b`

```math
5=2(2)+b
```

```math
b=1
```

Equation:

```math
y=2x+1
```

---

# 10. Pattern: recognize same line in different forms

These may look different:

```math
2x+y=7
```

and

```math
y=-2x+7
```

But they are the same line.

SAT may hide simple relationships through rearrangement.

Always simplify before deciding whether lines are parallel, perpendicular, or identical.

---

# 11. Method Selector

```text
Need point check?
→ substitute coordinates

Need x-intercept?
→ set y=0

Need y-intercept?
→ set x=0

Need slope from Ax+By=C?
→ solve for y

Parallel?
→ same slope

Perpendicular?
→ negative reciprocal slope

Need equation from points?
→ slope → intercept
```

---

# 12. Desmos Strategy

Desmos is useful when you want to see line relationships quickly.

Enter:

```text
y=2x+1
y=2x-5
```

You immediately see parallel lines.

Enter:

```text
y=2x+1
y=-0.5x+4
```

Slopes multiply to `-1`, so lines are perpendicular.

But for a question asking simply:

> What is the slope of `y=5x-3`?

manual reading is instant.

---

# 13. Error Clinic

## Error 1 — x-intercept vs y-intercept

```text
x-intercept → y=0
y-intercept → x=0
```

---

## Error 2 — perpendicular = negative only

Need reciprocal **and** sign change.

---

## Error 3 — assume same intercept for parallel line

Parallel fixes slope, not intercept.

---

## Error 4 — not simplify before comparing

```math
2y=4x+6
```

must become:

```math
y=2x+3
```

before comparing slopes/intercepts.

---

# 14. Guided Practice

## Level A — point check

Does `(3,10)` lie on

```math
y=3x+1?
```

<details><summary>Answer</summary>

Yes:

```math
10=3(3)+1
```

</details>

---

## Level B — intercept

Find x-intercept of:

```math
3x+2y=18
```

<details><summary>Solution</summary>

Set `y=0`:

```math
3x=18
```

```math
x=6
```

</details>

---

## Level C — perpendicular

What is slope of line perpendicular to slope `3/5`?

<details><summary>Answer</summary>

```math
-\frac53
```

</details>

---

## Level D — build equation

Find equation of line parallel to `y=-2x+7` and passing through `(3,1)`.

<details><summary>Solution</summary>

Slope `-2`.

```math
y-1=-2(x-3)
```

```math
y=-2x+7
```

Interesting: this is actually the same line because `(3,1)` lies on the original line.

This is a useful check: "parallel" can collapse to "same line" if point is already on it.

</details>

---

# 15. SAT-style Practice

## 1 — Easy — Multiple Choice

Which point lies on

```math
y=2x+1?
```

**A)** `(1,2)`  
**B)** `(1,3)`  
**C)** `(2,4)`  
**D)** `(3,8)`

## 2 — Easy — SPR

For

```math
3x+2y=18,
```

what is x-coordinate of x-intercept?

## 3 — Medium — Multiple Choice

Which line is parallel to

```math
y=-2x+5?
```

**A)** `y=2x+1`  
**B)** `y=-2x-7`  
**C)** `y=(1/2)x+3`  
**D)** `y=-(1/2)x+3`

## 4 — Medium — Multiple Choice

Which slope is perpendicular to `2/3`?

**A)** `3/2`  
**B)** `-3/2`  
**C)** `-2/3`  
**D)** `2/3`

## 5 — Hard — SPR

A line passes through `(4,11)` and has slope `2`. Find its y-intercept.

## 6 — 750–800 — Multiple Choice

Line `L` is perpendicular to

```math
4x-2y=10.
```

What is the slope of `L`?

**A)** `2`  
**B)** `-2`  
**C)** `1/2`  
**D)** `-1/2`

<details>
<summary><strong>Answers</strong></summary>

1. **B** — `3=2(1)+1`.
2. **`6`**.
3. **B** — same slope `-2`.
4. **B** — negative reciprocal.
5. **`3`** — `11=2(4)+b`, so `b=3`.
6. **D** — rewrite original: `-2y=-4x+10 → y=2x-5`; perpendicular slope `-1/2`.

</details>

---

# 16. Transfer Questions

1. Почему одно equation in two variables имеет infinitely many solutions?
2. Почему x-intercept требует `y=0`?
3. Почему parallel lines share slope?
4. Почему perpendicular slope — negative reciprocal?
5. Зачем иногда переводить standard form в slope-intercept form?
6. Как проверить, что point действительно лежит на line?
7. Когда Desmos полезнее algebra?

---

# 17. Checklist

- [ ] Я понимаю equation in two variables как line.
- [ ] Я проверяю point подстановкой.
- [ ] Я нахожу x- и y-intercepts.
- [ ] Я перевожу `Ax+By=C` в `y=mx+b`.
- [ ] Я нахожу slope из equation.
- [ ] Я строю equation по points.
- [ ] Я понимаю parallel = same slope.
- [ ] Я понимаю perpendicular = negative reciprocal.
- [ ] Я упрощаю equation перед сравнением lines.
- [ ] Я могу объяснить геометрический смысл каждого шага.
