# Nonlinear Equations and Systems — нелинейные уравнения и системы

## 1. Заголовок и краткое описание

**Nonlinear equations in one variable and systems of equations in two variables** — официальный skill Advanced Math. На SAT встречаются quadratic, radical, rational, exponential equations и системы, где хотя бы одно уравнение нелинейное.

> **Главная идея:** solution системы — точка, которая одновременно удовлетворяет обоим уравнениям; на графике это intersection.

---

## 2. Ключевые понятия и формулы

| Тип | Пример | Частый метод |
|---|---|---|
| quadratic equation | `x²-5x+6=0` | factoring / formula / graph |
| radical equation | `√(x+1)=x-1` | isolate radical, square, check |
| rational equation | `1/x=2/(x+3)` | restrictions + LCD |
| exponential equation | `2^x=8` | common base / graph |
| linear-quadratic system | `y=x+2`, `y=x²` | substitution / intersections |

### Количество решений системы

Графически:

- 0 intersections → 0 real solutions;
- 1 intersection → 1 solution;
- 2 intersections → 2 solutions;
- иногда больше для higher-degree curves.

### Визуальный якорь

**System = одновременно.** Точка должна лежать на обоих графиках.

---

## 3. Пошаговый разбор — Guided Example

Solve the system:

```math
y=x+2
```

```math
y=x^2-4.
```

### Шаг 1. Используем равенство двух выражений для `y`

Так как обе правые части равны одному и тому же `y`:

```math
x+2=x^2-4.
```

### Шаг 2. Переносим всё в одну сторону

```math
x^2-x-6=0.
```

### Шаг 3. Factor

```math
(x-3)(x+2)=0.
```

Отсюда:

```math
x=3\quad\text{или}\quad x=-2.
```

### Шаг 4. Находим `y`

Для `x=3`:

```math
y=5.
```

Для `x=-2`:

```math
y=0.
```

Solutions:

```math
(3,5),\quad(-2,0).
```

Почему substitution здесь эффективна? Потому что `y` уже выражен в обоих уравнениях.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

How many real solutions does `x²=9` have?

**A)** 0  **B)** 1  **C)** 2  **D)** 3

### Problem 2 — Easy/Medium — Grid-in

Solve `3^x=27`.

### Problem 3 — Medium — Multiple Choice

The graphs `y=x²` and `y=4` intersect at which x-values?

**A)** `0 only`  
**B)** `2 only`  
**C)** `-2 and 2`  
**D)** `-4 and 4`

### Problem 4 — Medium — Grid-in

For the system `y=x+1` and `y=x²-1`, what is the positive x-coordinate of an intersection?

### Problem 5 — Hard — Multiple Choice

A line and a parabola have exactly one point of intersection. After substitution, the resulting quadratic equation must have:

**A)** `D<0`  
**B)** `D=0`  
**C)** `D>0`  
**D)** `a=0`

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **C**, `x=±3`.  
2. **3**, потому что `27=3³`.  
3. **C**.  
4. **2**: `x+1=x²-1` → `x²-x-2=0` → `(x-2)(x+1)=0`.  
5. **B**, один real root означает discriminant zero.

</details>

---

## 5. Common Traps — типичные ловушки

- Найти только x-coordinate и забыть, что solution системы — пара `(x,y)`.
- Не проверить extraneous solution после squaring или rational manipulation.
- Предполагать, что система всегда имеет один solution.

---

## 6. Стратегия для Digital SAT

Это одна из тем, где Desmos особенно эффективен. Введите оба уравнения и найдите точки пересечения. Если SAT спрашивает только число решений, иногда достаточно просто посчитать intersections.

Однако parameter questions могут требовать algebra: например, «при каком `k` line касается parabola?» Тогда условие tangent часто превращается в `D=0`.

---

## 7. Связи с другими темами

**Опирается на:** systems of linear equations, quadratics, exponential/radical/rational equations.  
**Связано с:** parameter problems, graph interpretation, modeling.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я решаю основные nonlinear equations.
- [ ] Я решаю linear–nonlinear systems substitution методом.
- [ ] Я интерпретирую solutions как intersections.
- [ ] Я использую discriminant для вопросов о числе intersections.
