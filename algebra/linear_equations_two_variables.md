# Linear Equations in Two Variables — линейные уравнения с двумя переменными

## 1. Заголовок и краткое описание

Линейные уравнения с двумя переменными — отдельный официальный skill домена **Algebra**. На Digital SAT нужно читать equations, graphs и tables, находить slope/intercepts, писать equation of a line и работать с **parallel/perpendicular lines**.

> **Главная идея:** одно линейное уравнение с двумя переменными описывает целую прямую, а slope определяет её направление.

---

## 2. Ключевые понятия и формулы

| Понятие | Формула / смысл | Якорь |
|---|---|---|
| standard form | `Ax+By=C` | две переменные → одна прямая |
| slope-intercept form | `y=mx+b` | `m` slope, `b` y-intercept |
| slope | `m=(y₂-y₁)/(x₂-x₁)` | **rise over run** |
| x-intercept | установить `y=0` | пересечение x-axis |
| y-intercept | установить `x=0` | пересечение y-axis |
| point-slope form | `y-y₁=m(x-x₁)` | линия через point с slope `m` |
| parallel lines | одинаковые slopes | идут в одном направлении |
| perpendicular lines | `m₁m₂=-1` для nonvertical lines | negative reciprocals |

### Проверка точки

Для

```math
y=3x+2
```

точка `(1,5)` подходит:

```math
5=3(1)+2.
```

### Intercepts

Для

```math
2x+3y=12
```

x-intercept: `y=0` → `x=6`.  
y-intercept: `x=0` → `y=4`.

### Parallel lines

```math
y=2x+1
```

и

```math
y=2x-7
```

parallel, потому что slope обеих линий равен `2`.

### Perpendicular lines

Если одна линия имеет slope `2/3`, perpendicular slope:

```math
-\frac32.
```

Проверка:

```math
\frac23\cdot\left(-\frac32\right)=-1.
```

### Вопрос к читателю

Какой slope имеет линия, perpendicular к линии `y=-4x+7`?

---

## 3. Пошаговый разбор — Guided Example

### Задача

A line passes through `(2,5)` and is parallel to

```math
y=3x-4.
```

Find the equation of the new line.

### Шаг 1. Используем parallel condition

Parallel lines имеют одинаковый slope.

Значит:

```math
m=3.
```

### Шаг 2. Используем point-slope form

```math
y-y_1=m(x-x_1).
```

Подставляем `(2,5)`:

```math
y-5=3(x-2).
```

### Шаг 3. Упрощаем

```math
y-5=3x-6
```

```math
y=3x-1.
```

### Шаг 4. Проверяем

- slope нового уравнения = 3 → линии parallel;
- точка `(2,5)` удовлетворяет: `5=6-1`.

Почему нельзя просто взять исходный y-intercept `-4`? Parallel condition фиксирует slope, но intercept обычно меняется.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

Which point lies on

```math
y=2x+1?
```

**A)** `(1,2)`  
**B)** `(1,3)`  
**C)** `(2,4)`  
**D)** `(3,8)`

### Problem 2 — Easy — Grid-in

For

```math
3x+2y=18,
```

what is the x-coordinate of the x-intercept?

### Problem 3 — Medium — Multiple Choice

A line passes through `(2,5)` and `(6,13)`. What is its slope?

**A)** `1/2`  
**B)** `2`  
**C)** `4`  
**D)** `8`

### Problem 4 — Medium — Multiple Choice

Which line is parallel to `y=-2x+5`?

**A)** `y=2x+1`  
**B)** `y=-2x-7`  
**C)** `y=(1/2)x+3`  
**D)** `y=-(1/2)x+3`

### Problem 5 — Hard — Grid-in

A line is perpendicular to `y=(1/4)x+9`. What is the slope of the perpendicular line?

<details>
<summary><strong>Ответы и краткие решения</strong></summary>

1. **B**, `3=2(1)+1`.  
2. **6**, при `y=0`: `3x=18`.  
3. **B**, `(13-5)/(6-2)=2`.  
4. **B**, same slope `-2`.  
5. **-4**, negative reciprocal of `1/4`.

</details>

---

## 5. Common Traps — типичные ловушки

### Ловушка 1. Перепутать slope и intercept

В `y=mx+b`, `m` — rate of change, `b` — значение `y` при `x=0`.

### Ловушка 2. Перепутать parallel и perpendicular slopes

- parallel → same slope;
- perpendicular → negative reciprocal.

### Ловушка 3. Неверно найти intercept

- x-intercept → `y=0`;
- y-intercept → `x=0`.

---

## 6. Стратегия для Digital SAT

Desmos удобно использовать для проверки:

```text
y=2x+1
```

и второй candidate line. По графику легко увидеть parallel/perpendicular relationship.

Но для slope questions algebra обычно быстрее:

1. приведите equation к `y=mx+b`;
2. прочитайте `m`;
3. примените same slope или negative reciprocal.

---

## 7. Связи с другими темами

**Опирается на:**
- `linear_equations.md`;
- coordinate plane;
- ratios/rates.

**Связано с:**
- `linear_functions.md`;
- `systems_of_equations.md` — intersections;
- `linear_inequalities.md` — boundary lines;
- geometry — perpendicular/parallel relationships.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я проверяю, лежит ли point на line.
- [ ] Я нахожу slope и intercepts.
- [ ] Я пишу equation по point и slope.
- [ ] Я нахожу equations/slopes parallel и perpendicular lines.
