# Systems of Equations — системы линейных уравнений

> **Цель урока:** научиться видеть систему как **две условия, которые должны выполняться одновременно**, и быстро выбирать между substitution, elimination и graphing.

Главная идея:

> **Solution of a system = точка, которая подходит обоим уравнениям сразу.**

---

# 1. Pattern Map

| Что вижу | Паттерн | Лучший старт |
|---|---|---|
| `y=...` уже выражено | substitution-ready | подставить выражение |
| коэффициенты `+y` и `-y` | elimination-ready | сложить equations |
| коэффициенты можно легко сделать opposite | scale + elimination | умножить одно equation |
| две lines на graph | intersection | читать точку пересечения |
| same slope, different intercept | parallel | no solution |
| same line written differently | same line | infinitely many solutions |
| two quantities + total/count constraints | word-problem system | определить variables и написать 2 equations |

Перед вычислениями спросите:

> **«Какой variable проще всего убрать?»**

---

# 2. Что означает system

Пример:

```math
\begin{cases}
2x+y=11\\
x-y=1
\end{cases}
```

Нужно найти такие `x` и `y`, которые делают **оба** равенства верными.

Геометрически каждое equation — линия.

Solution system — их intersection.

```text
line 1  \ /
         X   ← solution
line 2  / \
```

---

# 3. Три геометрических случая

| Lines | Solutions | Почему |
|---|---:|---|
| пересекаются | 1 | одна общая point |
| parallel | 0 | никогда не встречаются |
| same line | infinitely many | каждая point общая |

Якорь:

```text
CROSS → ONE
PARALLEL → NONE
SAME → INFINITE
```

---

# 4. PATTERN 1 — Substitution

## Когда выбирать

Одна variable уже выражена:

```math
y=2x+1
```

или её очень легко выразить.

---

## Worked Example 1

```math
\begin{cases}
y=2x+1\\
3x+y=16
\end{cases}
```

### Notice

Первое equation уже говорит, чему равен `y`.

### Decision

Вместо `y` во втором equation подставляем `2x+1`.

```math
3x+(2x+1)=16
```

```math
5x+1=16
```

```math
5x=15
```

```math
x=3
```

Теперь возвращаемся:

```math
y=2(3)+1=7
```

Solution:

```math
(3,7)
```

### Check

Second equation:

```math
3(3)+7=16
```

Correct.

---

## Worked Example 2 — express first

```math
\begin{cases}
x+y=10\\
2x+3y=24
\end{cases}
```

Из первого equation очень легко:

```math
y=10-x
```

Подставляем:

```math
2x+3(10-x)=24
```

```math
2x+30-3x=24
```

```math
-x=-6
```

```math
x=6
```

```math
y=4
```

---

# 5. PATTERN 2 — Elimination

## Когда выбирать

Coefficients уже opposite или легко становятся opposite.

Пример:

```math
\begin{cases}
2x+y=9\\
3x-y=6
\end{cases}
```

`+y` и `-y` уничтожатся при сложении.

---

## Worked Example 1

Складываем equations:

```math
5x=15
```

```math
x=3
```

Подставляем в первое:

```math
2(3)+y=9
```

```math
y=3
```

Solution:

```math
(3,3)
```

---

## PATTERN CARD — elimination

```text
1. choose variable to eliminate
2. make coefficients opposite if needed
3. add equations
4. solve one variable
5. back-substitute
6. check both equations
```

---

## Worked Example 2 — сначала умножить

```math
\begin{cases}
2x+3y=12\\
4x-y=10
\end{cases}
```

### Notice

`y` coefficients: `3` and `-1`.

Если второе equation умножить на `3`:

```math
12x-3y=30
```

Теперь:

```math
\begin{cases}
2x+3y=12\\
12x-3y=30
\end{cases}
```

Складываем:

```math
14x=42
```

```math
x=3
```

Подставляем:

```math
4(3)-y=10
```

```math
y=2
```

---

# 6. Method Selector — substitution или elimination?

```text
Variable already isolated?
→ substitution

Coefficients already opposite?
→ elimination

One coefficient = 1 or -1?
→ substitution often easy

Can multiply one equation by small number to eliminate?
→ elimination

Graph/intersection given?
→ graphing / Desmos
```

Не существует «всегда лучшего» метода.

SAT проверяет гибкость выбора.

---

# 7. PATTERN 3 — No solution / infinitely many solutions

## Case A — parallel lines

```math
y=2x+3
```

```math
y=2x-5
```

Same slope, different intercept.

```text
parallel → no solution
```

---

## Case B — same line

```math
y=2x+3
```

и

```math
2y=4x+6
```

Второе делим на `2`:

```math
y=2x+3
```

Это одна и та же line.

```text
same line → infinitely many solutions
```

---

## Algebraic signal

При elimination variable может исчезнуть.

Если осталось:

```math
0=7
```

→ no solution.

Если:

```math
0=0
```

→ infinitely many solutions.

Это тот же pattern, что в linear equations.

---

# 8. PATTERN 4 — Word Problems: count + value

Очень частый SAT pattern:

```text
number of items total
+
value/cost total
```

Например tickets, coins, products, memberships.

---

## Worked Example — tickets

A school sold `120` tickets.
Student tickets cost `$6`, adult tickets `$10`.
Total revenue was `$920`.
How many student tickets?

### Step 1 — define variables

```text
s = student tickets
a = adult tickets
```

### Step 2 — count equation

```math
s+a=120
```

### Step 3 — money equation

```math
6s+10a=920
```

System:

```math
\begin{cases}
s+a=120\\
6s+10a=920
\end{cases}
```

### Step 4 — choose method

First equation makes substitution easy:

```math
a=120-s
```

### Step 5

```math
6s+10(120-s)=920
```

```math
6s+1200-10s=920
```

```math
-4s=-280
```

```math
s=70
```

Then:

```math
a=50
```

### Check

```math
6(70)+10(50)=420+500=920
```

Correct.

---

# 9. SAT Language Decoder for systems

| Phrase | Model clue |
|---|---|
| `a total of 120 items` | count equation |
| `total revenue/cost/value` | weighted value equation |
| `combined` | often sum |
| `both plans cost the same` | set outputs equal |
| `intersection` | common solution |
| `satisfies both equations` | system solution |

---

# 10. PATTERN 5 — Compare two linear models

Suppose:

```math
A(x)=5x+40
```

```math
B(x)=8x+10
```

When are costs equal?

System perspective:

```math
y=5x+40
```

```math
y=8x+10
```

At intersection:

```math
5x+40=8x+10
```

```math
30=3x
```

```math
x=10
```

This is both:

- solving an equation;
- solving a system;
- finding graph intersection.

SAT often tests the same concept through different representations.

---

# 11. Desmos Strategy

For:

```math
\begin{cases}
y=2x+1\\
y=-x+7
\end{cases}
```

enter:

```text
y=2x+1
y=-x+7
```

Click intersection.

You get:

```text
(2,5)
```

## When Desmos is strong

- messy coefficients;
- both equations already in graph form;
- question asks intersection;
- nonlinear system later in Advanced Math.

## When manual is faster

```math
\begin{cases}
x+y=10\\
x-y=2
\end{cases}
```

Add equations instantly:

```math
2x=12
```

No reason to graph.

---

# 12. Error Clinic

## Error 1 — solve one equation only

System solution must satisfy **both** equations.

Always check pair `(x,y)`.

---

## Error 2 — substitution without parentheses

If:

```math
y=5-x
```

and second equation has `3y`, then:

```math
3(5-x)
```

not

```math
15-x
```

---

## Error 3 — elimination changes only one term

If multiplying equation by `3`, multiply **every term**.

```math
2x-y=4
```

becomes:

```math
6x-3y=12
```

---

## Error 4 — confuse no solution with `(0,0)`

Parallel lines do not intersect.

No solution does **not** mean `(0,0)`.

---

# 13. Guided Practice

## Level A — method given

Use elimination:

```math
\begin{cases}
x+y=9\\
x-y=3
\end{cases}
```

<details><summary>Solution</summary>

Add:

```math
2x=12
```

```math
x=6
```

Then `y=3`.

</details>

---

## Level B — choose method

```math
\begin{cases}
y=3x-2\\
2x+y=13
\end{cases}
```

Write first:

```text
Best method: __________
Why: __________________
```

<details><summary>Solution</summary>

Substitution, because `y` is already isolated.

```math
2x+(3x-2)=13
```

```math
5x=15
```

```math
x=3,\quad y=7
```

</details>

---

## Level C — classify without solving

```math
y=-4x+2
```

```math
y=-4x-9
```

How many solutions?

<details><summary>Answer</summary>

No solution: same slope, different intercepts.

</details>

---

## Level D — word problem

There are `40` coins, all quarters and dimes, worth `$7.00` total.

Define variables and write a system before solving.

<details><summary>Setup</summary>

Let `q` quarters, `d` dimes.

```math
q+d=40
```

```math
0.25q+0.10d=7
```

</details>

---

# 14. SAT-style Practice

## 1 — Easy — Multiple Choice

Solve:

```math
\begin{cases}
x+y=10\\
x-y=2
\end{cases}
```

What is `x`?

**A)** `4`  
**B)** `5`  
**C)** `6`  
**D)** `8`

## 2 — Medium — SPR

```math
\begin{cases}
y=2x+1\\
y=-x+10
\end{cases}
```

Find `x`.

## 3 — Medium — Multiple Choice

Which system has no solution?

**A)** `y=2x+1`, `y=-2x+1`  
**B)** `y=3x+4`, `y=3x-2`  
**C)** `y=x`, `y=2x`  
**D)** `y=5`, `x=5`

## 4 — Medium/Hard — SPR

```math
\begin{cases}
2x+3y=19\\
2x-y=7
\end{cases}
```

Find `y`.

## 5 — Hard — Multiple Choice

The system

```math
\begin{cases}
y=kx+4\\
y=3x-8
\end{cases}
```

has no solution. Which value could `k` be?

**A)** `-3`  
**B)** `0`  
**C)** `3`  
**D)** `8`

## 6 — 750–800 — SPR

A theater sold `200` tickets. Adult tickets cost `$12`, student tickets `$8`, and total revenue was `$2,080`. How many adult tickets were sold?

<details>
<summary><strong>Answers</strong></summary>

1. **C, 6** — add equations.
2. **`3`** — `2x+1=-x+10`.
3. **B** — same slope, different intercept.
4. **`3`** — subtract/eliminate `x`: `4y=12`.
5. **C** — parallel requires same slope `3`; intercepts differ.
6. **`120`** — `a+s=200`, `12a+8s=2080`; substitute `s=200-a`: `12a+1600-8a=2080 → 4a=480 → a=120`.

</details>

---

# 15. Transfer Questions

1. Почему solution system должна удовлетворять обоим equations?
2. Когда substitution быстрее elimination?
3. Когда elimination очевидно лучше?
4. Как same slope помогает определить no solution?
5. Почему system word problem обычно требует двух независимых условий?
6. Как intersection двух cost functions интерпретируется в реальной задаче?
7. Когда Desmos действительно сокращает решение?

---

# 16. Checklist

- [ ] Я понимаю system как одновременное выполнение двух условий.
- [ ] Я выбираю substitution, когда variable уже isolated.
- [ ] Я выбираю elimination, когда coefficients удобно сократить.
- [ ] Я умею масштабировать equation перед elimination.
- [ ] Я различаю one/no/infinite solutions.
- [ ] Я понимаю solution как graph intersection.
- [ ] Я строю systems из count + value word problems.
- [ ] Я проверяю найденную pair в обоих equations.
- [ ] Я знаю, когда использовать Desmos.
- [ ] Я могу объяснить выбор метода до вычислений.
