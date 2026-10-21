# Linear Functions — линейные функции

> **Цель урока:** научиться видеть в линейной функции не формулу `y=mx+b`, а **историю о начальном значении и постоянной скорости изменения**.

Главная идея:

> **Linear function = старт + одинаковое изменение за каждый шаг.**

Это одна из самых полезных идей всего SAT Math.

---

# 1. Pattern Map

| Что вижу | Паттерн | Что делаю |
|---|---|---|
| `y=3x+7` | read slope/intercept | `m=3`, `b=7` |
| две точки | slope from points | `Δy/Δx` |
| таблица с постоянным изменением | linear table | сравниваю changes |
| slope + одна point | build equation | point-slope или `y=mx+b` |
| две points | build equation | slope → then intercept |
| `initial fee + per unit` | linear model | `output = rate·input + initial` |
| function notation `f(4)` | evaluate function | подставить `x=4` |
| сравнение двух plans | compare functions | понять смысл slope/intercept или найти intersection |

Перед вычислениями спрашивайте:

> **«Что здесь является стартом, а что — изменением за единицу?»**

---

# 2. Якорь: slope = изменение, intercept = старт

Основная форма:

```math
y=mx+b
```

или

```math
f(x)=mx+b
```

где:

```text
m = slope = change per 1 unit of x
b = y-intercept = starting value when x=0
```

Визуально:

```text
output = rate × input + start

   y   =  m   ×   x   +  b
```

Это та же структура, которую вы уже видели в word problems:

```text
total = fixed + rate × quantity
```

---

# 3. PATTERN 1 — Read `y=mx+b`

## Worked Example 1

```math
y=-3x+11
```

Сразу читаем:

```text
slope       = -3
y-intercept = 11
```

Что означает negative slope?

Когда `x` увеличивается на `1`, `y` уменьшается на `3`.

---

## Worked Example 2 — смысл в контексте

```math
C(h)=12h+25
```

где `C` — стоимость в долларах, `h` — количество часов.

```text
25 = начальная fixed fee
12 = $12 за каждый час
```

Не просто называйте `12` slope.

На SAT лучше мыслить:

> **«12 долларов на один дополнительный час».**

Units часто помогают понять ответ.

---

# 4. PATTERN 2 — Slope from two points

Формула:

```math
m=\frac{y_2-y_1}{x_2-x_1}
```

Визуальный якорь:

```text
slope = rise / run
      = vertical change / horizontal change
```

Главное: используйте **одинаковый порядок** сверху и снизу.

---

## Worked Example

Points:

```text
(2,5) and (6,13)
```

### Notice

Нужно найти rate of change между двумя points.

### Action

```math
m=\frac{13-5}{6-2}
```

```math
m=\frac84=2
```

### Meaning

Когда `x` растёт на `1`, `y` в среднем растёт на `2`.

---

## Error Clinic — смешать порядок

Неверно:

```math
\frac{13-5}{2-6}
```

Почему? Сверху идём `point 1 → point 2`, а снизу вдруг наоборот.

Используйте правило:

```text
same order / same order
```

Например:

```math
\frac{13-5}{6-2}
```

или

```math
\frac{5-13}{2-6}
```

Оба дадут `2`.

---

# 5. PATTERN 3 — Slope from a table

## Как узнать linear table

У linear function одинаковому изменению `x` соответствует одинаковое изменение `y`.

Пример:

| x | y |
|---:|---:|
| 1 | 5 |
| 2 | 8 |
| 3 | 11 |
| 4 | 14 |

Каждый раз:

```text
x +1
y +3
```

Значит:

```math
m=3
```

---

## Важная ловушка

Если `x` меняется не на `1`, slope — не просто change in y.

| x | y |
|---:|---:|
| 2 | 7 |
| 5 | 19 |

```math
\Delta x=3
```

```math
\Delta y=12
```

Поэтому:

```math
m=\frac{12}{3}=4
```

Не пишите slope `12`.

---

# 6. PATTERN 4 — Build a function from slope + point

Если известны slope `m` и point `(x₁,y₁)`, удобно использовать:

```math
y-y_1=m(x-x_1)
```

Это point-slope form.

---

## Worked Example

A line has slope `3` and passes through `(2,5)`.

### Step 1

Подставляем:

```math
y-5=3(x-2)
```

### Step 2

Упрощаем:

```math
y-5=3x-6
```

```math
y=3x-1
```

### Check

При `x=2`:

```math
y=6-1=5
```

Point подходит.

---

# 7. PATTERN 5 — Build a function from two points

Алгоритм:

```text
1. slope
2. choose one point
3. find b
4. write equation
5. check with second point
```

---

## Worked Example

Points:

```text
(2,5), (6,13)
```

### Step 1 — slope

```math
m=\frac{13-5}{6-2}=2
```

### Step 2 — write `y=mx+b`

```math
y=2x+b
```

### Step 3 — use one point

Using `(2,5)`:

```math
5=2(2)+b
```

```math
b=1
```

### Step 4

```math
y=2x+1
```

### Step 5 — check second point

At `x=6`:

```math
y=2(6)+1=13
```

Correct.

---

# 8. PATTERN 6 — Linear word problem

## Самый важный шаблон

```math
\text{output}=\text{rate}\times\text{input}+\text{initial value}
```

### SAT Language Decoder

| Phrase | Math meaning |
|---|---|
| `initially` | intercept / start |
| `at time 0` | intercept |
| `per hour` | slope |
| `each month` | slope |
| `increases by` | positive slope |
| `decreases by` | negative slope |
| `constant rate` | linear relationship |

---

## Worked Example 1 — water tank

A water tank contains `120` liters. Water is added at a constant rate of `8` liters per minute.

Find `W(t)`.

### Translate before writing formula

```text
initial = 120 liters
rate    = +8 liters/minute
input   = t minutes
```

Therefore:

```math
W(t)=8t+120
```

### Check

At `t=0`:

```math
W(0)=120
```

At `t=5`:

```math
W(5)=160
```

Both make sense.

---

## Worked Example 2 — decreasing quantity

A tank starts with `500` liters and loses `12` liters per minute.

```text
initial = 500
rate    = -12
```

So:

```math
V(t)=500-12t
```

Why negative slope?

Because output decreases as time increases.

---

# 9. PATTERN 7 — Function notation

`f(x)` is not multiplication.

It means:

> value of function `f` at input `x`.

If:

```math
f(x)=3x+7
```

then:

```math
f(4)=3(4)+7=19
```

---

## Reverse question

If:

```math
f(x)=3x+7
```

and

```math
f(x)=25,
```

then solve:

```math
3x+7=25
```

```math
x=6
```

Функции и equations — не отдельные миры. Они постоянно переходят друг в друга.

---

# 10. PATTERN 8 — Compare two linear models

Пример:

```math
A(x)=5x+20
```

```math
B(x)=8x+5
```

### Что можно понять без вычислений?

Plan A:

```text
higher starting cost: 20
lower rate: 5
```

Plan B:

```text
lower starting cost: 5
higher rate: 8
```

Если спрашивают, когда costs equal:

```math
5x+20=8x+5
```

```math
15=3x
```

```math
x=5
```

Это точка пересечения двух lines.

### Большая идея

```text
same output
→ set functions equal
→ solve intersection
```

---

# 11. Method Selector

```text
Вижу y=mx+b?
→ read m and b directly

Даны two points?
→ slope first

Дана table?
→ compare Δy/Δx

Дан slope + point?
→ point-slope form

Даны two points и нужно equation?
→ slope → find b

Word problem with initial/per?
→ rate × input + initial

Two plans become equal?
→ set equations equal

Graphical/intersection question?
→ Desmos may be fastest
```

---

# 12. Desmos Strategy

## Find slope/intercept visually

Введите:

```text
y=2x+1
```

Вы увидите:

- y-intercept `(0,1)`;
- line rising 2 for each 1 right.

## Compare plans

Введите:

```text
y=5x+20
y=8x+5
```

Intersection gives the input where costs are equal.

## Когда вручную быстрее

Если вопрос просто:

> What is the slope of `y=-4x+7`?

Ответ `-4` уже виден. Desmos только замедлит.

---

# 13. Error Clinic

## Ошибка 1 — спутать slope и intercept

```math
y=7x-3
```

```text
slope = 7
intercept = -3
```

Не наоборот.

---

## Ошибка 2 — считать y-intercept как `x=b`

Y-intercept всегда имеет:

```text
x=0
```

Поэтому point:

```text
(0,b)
```

---

## Ошибка 3 — читать `per` как intercept

`$12 per hour` → slope, потому что это change per unit.

`$25 initial fee` → intercept.

---

## Ошибка 4 — не смотреть на units

Slope может быть:

```text
dollars/hour
liters/minute
miles/hour
points/game
```

Units часто раскрывают смысл коэффициента.

---

# 14. Guided Practice

## Level A

For

```math
y=4x-9,
```

fill in:

```text
slope = ____
y-intercept = ____
```

<details><summary>Answer</summary>

`slope=4`, `y-intercept=-9`.

</details>

---

## Level B

A line passes through `(1,4)` and `(5,12)`.

Before calculating, write:

```text
Δx = ____
Δy = ____
```

<details><summary>Solution</summary>

```math
\Delta x=4
```

```math
\Delta y=8
```

```math
m=2
```

</details>

---

## Level C

A phone plan costs `$30` initially and `$6` per GB used.

Fill in:

```text
initial = ____
rate = ____
input variable = ____
```

Then write the function.

<details><summary>Solution</summary>

```math
C(g)=6g+30
```

</details>

---

## Level D — transfer

Plan A costs `$20` plus `$8` per month.
Plan B costs `$50` plus `$5` per month.

When do the plans cost the same?

<details><summary>Solution</summary>

```math
8m+20=5m+50
```

```math
3m=30
```

```math
m=10
```

</details>

---

# 15. SAT-style Practice

## 1 — Easy — Multiple Choice

What is the slope of

```math
y=-3x+11?
```

**A)** `-3`  
**B)** `3`  
**C)** `11`  
**D)** `-11`

## 2 — Easy — SPR

What is the y-intercept of

```math
y=5x-7?
```

## 3 — Medium — Multiple Choice

The line through `(2,5)` and `(6,13)` has slope:

**A)** `1/2`  
**B)** `2`  
**C)** `4`  
**D)** `8`

## 4 — Medium — SPR

A line has slope `4` and passes through `(3,14)`. Find its y-intercept.

## 5 — Medium/Hard — Multiple Choice

A gym charges `$40` to join and `$15` per month. Which function models total cost `C(m)`?

**A)** `C(m)=40m+15`  
**B)** `C(m)=15m+40`  
**C)** `C(m)=55m`  
**D)** `C(m)=15m`

## 6 — Hard — SPR

Functions `A(x)=7x+10` and `B(x)=4x+31` have the same output for what value of `x`?

## 7 — Hard — Multiple Choice

A linear function has `f(2)=9` and `f(5)=18`. What is `f(0)`?

**A)** `1`  
**B)** `3`  
**C)** `5`  
**D)** `9`

## 8 — 750–800 — SPR

A linear function satisfies `f(3)=11` and `f(8)=26`. Find `f(20)`.

<details>
<summary><strong>Answers and patterns</strong></summary>

1. **A** — read `m` directly.
2. **`-7`** — `b=-7`.
3. **B** — `(13-5)/(6-2)=2`.
4. **`2`** — `14=4(3)+b → b=2`.
5. **B** — fixed 40, rate 15.
6. **`7`** — `7x+10=4x+31`.
7. **B** — slope `(18-9)/(5-2)=3`; `9=3(2)+b`, so `b=3`.
8. **`62`** — slope `(26-11)/(8-3)=3`; `f(x)=3x+2`; `f(20)=62`.

</details>

---

# 16. Transfer Questions

1. Что физически означает slope в word problem?
2. Почему y-intercept — значение при `x=0`?
3. Как по table доказать, что relationship linear?
4. Почему при двух points сначала удобно искать slope?
5. Что означает intersection двух cost functions?
6. Чем function notation `f(4)` отличается от `f×4`?
7. Когда Desmos полезнее ручного решения?

---

# 17. Checklist

- [ ] Я читаю slope и intercept из `y=mx+b`.
- [ ] Я понимаю slope как change per unit.
- [ ] Я нахожу slope по двум points и table.
- [ ] Я строю equation по slope + point.
- [ ] Я строю equation по two points.
- [ ] Я перевожу `initial` и `per` в linear model.
- [ ] Я понимаю function notation.
- [ ] Я сравниваю две linear models через intersection.
- [ ] Я проверяю units и смысл coefficients.
- [ ] Я могу объяснить, почему выбрал метод.
