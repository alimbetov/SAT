# Foundation Bridge 04 — Coordinates and Linear Patterns

**Learner label:** `FOUNDATION`

Цель — понять координаты, изменение и linear pattern до формул `y=mx+b`.

---

# 1. Coordinate plane — адрес точки

Точка `(3,2)` означает:

```text
сначала 3 вправо
потом 2 вверх
```

Порядок всегда:

```text
(x, y)
```

Полезный anchor:

> **x first, y second.**

---

# 2. Table before formula

Рассмотрим стоимость яблок по 400 тг за килограмм.

| kg | cost |
|---:|---:|
| 0 | 0 |
| 1 | 400 |
| 2 | 800 |
| 3 | 1200 |

Что происходит каждый раз, когда `kg` увеличивается на 1?

Стоимость увеличивается на 400.

Это постоянное изменение.

Позже мы запишем:

```math
y=400x
```

Но сначала важен pattern:

```text
+1 по x
→ +400 по y
```

---

# 3. Starting value

Теперь taxi:

- starting fee = 500 тг;
- each km = 200 тг.

| km | cost |
|---:|---:|
| 0 | 500 |
| 1 | 700 |
| 2 | 900 |
| 3 | 1100 |

Что отличается от яблок?

При `x=0` cost уже 500.

Это **starting value**.

Formula later:

```math
C=200x+500
```

Meaning first:

```text
500 = start
200 = change per 1 km
```

---

# 4. Slope without the word slope

Посмотрим на points:

```text
(1, 3)
(2, 5)
(3, 7)
(4, 9)
```

Каждый раз:

```text
x +1
↓
y +2
```

Rate of change = 2.

Только после понимания вводим term:

> **slope** = change in y per change in x.

---

# 5. Worked Example — read a table

| x | y |
|---:|---:|
| 0 | 4 |
| 1 | 7 |
| 2 | 10 |
| 3 | 13 |

### What do we notice?

`y` increases by 3 when `x` increases by 1.

So rate of change = 3.

At `x=0`:

```text
y=4
```

So starting value = 4.

Formula:

```math
y=3x+4
```

### Check

At `x=2`:

```math
3(2)+4=10
```

matches table.

---

# 6. Graph as a picture of a table

The points from the table:

```text
(0,4), (1,7), (2,10), (3,13)
```

all lie on one straight line.

Why?

Because the rate of change is constant.

Mental model:

```text
constant additive change
→ straight line
```

---

# 7. Positive and negative change

Table:

| x | y |
|---:|---:|
| 0 | 20 |
| 1 | 17 |
| 2 | 14 |
| 3 | 11 |

Every +1 in x gives -3 in y.

So slope/rate = -3.

Meaning:

```text
as x goes up, y goes down
```

---

# 8. Faded Example

A water tank starts with 50 liters and fills by 6 liters per minute.

Fill in:

```text
starting value = ______
rate per minute = ______
after 1 min = ______
after 2 min = ______
formula = ______
```

<details><summary>Проверка</summary>

```text
starting value = 50
rate = 6
1 min = 56
2 min = 62
A(t)=50+6t
```

</details>

---

# 9. Compare two plans

Plan A:

```text
start = 1000
+200 each month
```

Plan B:

```text
start = 400
+300 each month
```

Instead of jumping to formulas, make a table:

| month | A | B |
|---:|---:|---:|
| 0 | 1000 | 400 |
| 1 | 1200 | 700 |
| 2 | 1400 | 1000 |
| 3 | 1600 | 1300 |
| 4 | 1800 | 1600 |
| 5 | 2000 | 1900 |
| 6 | 2200 | 2200 |

At month 6 they are equal.

This prepares for systems of equations.

---

# 10. SAT English Bridge

| English | Meaning |
|---|---|
| rate of change | насколько y меняется при изменении x |
| slope | rate on a graph |
| initial value | starting value |
| y-intercept | value when x=0 |
| increases by | прибавляется |
| decreases by | уменьшается |
| per | на каждый |

---

# 11. Check for Understanding

1. What does `(4,2)` mean?
2. If y grows by 5 every time x grows by 1, what is the rate?
3. In `y=3x+8`, which number is the start?
4. What does negative slope mean in words?
5. Why does constant rate produce a straight line?

---

# 12. Foundation Practice

1. Point with x=2, y=7 — write coordinates.
2. Sequence y: 4, 7, 10, 13. Change each step?
3. Starts at 12 and grows by 5 per step. Value after 4 steps?
4. In `y=2x+6`, find y when x=3.
5. A plan costs 300 initially + 50 per month. Cost after 6 months?

<details><summary>Ответы</summary>

1. `(2,7)`
2. `+3`
3. `32`
4. `12`
5. `600`

</details>

---

# Mastery Gate

Готовность к linear equations in two variables / linear functions:

- [ ] coordinates читаются без путаницы;
- [ ] starting value виден в table/context;
- [ ] rate per 1 понятен;
- [ ] positive/negative change объясняется словами;
- [ ] простая formula строится из `start + rate·quantity`;
- [ ] ученик может проверить formula по таблице.
