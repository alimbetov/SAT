# Systems of Equations — системы линейных уравнений

## 1. Зачем эта тема нужна на SAT

Системы двух линейных уравнений входят в официальный домен **Algebra**. На SAT нужно уметь находить точку пересечения двух линий, выбирать между substitution и elimination, распознавать отсутствие решения или бесконечно много решений и строить систему по текстовой ситуации.

> **Главная идея:** решение системы — значение, которое одновременно удовлетворяет обоим уравнениям.

**Вопрос перед началом:** если две прямые пересекаются в одной точке, сколько решений имеет соответствующая система?

---

## 2. Ключевые понятия и формулы

Система обычно записывается так:

```math
\begin{cases}
2x+y=11\\
x-y=1
\end{cases}
```

### Что означает решение

Если решение равно `(x,y)=(4,3)`, то эта пара должна сделать **оба** уравнения верными.

### Три метода

| Метод | Когда удобен | Идея |
|---|---|---|
| **substitution** | одна переменная уже выражена | подставить одно выражение в другое уравнение |
| **elimination** | коэффициенты легко сократить | сложить/вычесть уравнения и убрать переменную |
| **graphing** | нужен быстрый визуальный ответ | найти точку пересечения графиков |

### Substitution

```math
\begin{cases}
y=2x+1\\
3x+y=16
\end{cases}
```

Подставляем `y=2x+1` во второе уравнение:

```math
3x+(2x+1)=16
```

```math
5x=15
```

```math
x=3
```

Затем:

```math
y=2(3)+1=7
```

### Elimination

```math
\begin{cases}
2x+y=9\\
3x-y=6
\end{cases}
```

Складываем уравнения:

```math
5x=15
```

```math
x=3
```

Потом находим `y`.

### Геометрический смысл

| Линии | Число решений системы |
|---|---:|
| пересекаются | 1 |
| параллельны | 0 |
| совпадают | бесконечно много |

Визуальный якорь:

```text
пересеклись → ONE
параллельны → NONE
совпали → INFINITE
```

### Одинаковый slope

Если две линии имеют одинаковый slope, но разные intercepts:

```math
y=2x+3
```

```math
y=2x-5
```

они параллельны → **no solution**.

Если совпадают и slope, и intercept:

```math
y=2x+3
```

```math
2y=4x+6
```

это одна и та же линия → **infinitely many solutions**.

---

## 3. Пошаговый разбор — Guided Example

### Задача

A school sold `120` tickets to a performance. Student tickets cost `$6` and adult tickets cost `$10`. Total revenue was `$920`. How many student tickets were sold?

Пусть:

- `s` — число student tickets;
- `a` — число adult tickets.

### Шаг 1. Строим уравнение количества

Всего продано 120 билетов:

```math
s+a=120
```

**Почему?**

Потому что каждая продажа относится либо к student, либо к adult ticket.

### Шаг 2. Строим уравнение стоимости

Доход от student tickets:

```math
6s
```

Доход от adult tickets:

```math
10a
```

Общий доход:

```math
6s+10a=920
```

Получаем систему:

```math
\begin{cases}
s+a=120\\
6s+10a=920
\end{cases}
```

### Шаг 3. Выбираем метод

Из первого уравнения легко выразить:

```math
a=120-s
```

Поэтому substitution здесь естественнее.

### Шаг 4. Подставляем

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

### Шаг 5. Проверяем

Adult tickets:

```math
a=120-70=50
```

Доход:

```math
6(70)+10(50)=420+500=920
```

**Ответ: `70` student tickets.**

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

What is the solution to the system?

```math
\begin{cases}
x+y=9\\
x-y=3
\end{cases}
```

**A)** `(3,6)`  
**B)** `(6,3)`  
**C)** `(9,3)`  
**D)** `(6,6)`

---

### Problem 2 — Medium — Grid-in

```math
\begin{cases}
y=3x-2\\
2x+y=18
\end{cases}
```

What is the value of `x`?

Enter your answer: `_____`

---

### Problem 3 — Medium — Multiple Choice

Which system has **no solution**?

**A)**

```math
\begin{cases}
y=2x+1\\
y=-x+7
\end{cases}
```

**B)**

```math
\begin{cases}
y=4x+3\\
y=4x-5
\end{cases}
```

**C)**

```math
\begin{cases}
x+y=8\\
2x-y=4
\end{cases}
```

**D)**

```math
\begin{cases}
y=x\\
y=2x
\end{cases}
```

---

### Problem 4 — Hard — Grid-in

A café sold `50` drinks. Small drinks cost `$3` and large drinks cost `$5`. Total sales were `$190`. How many large drinks were sold?

Enter your answer: `_____`

---

### Problem 5 — Hard — Multiple Choice

For what value of `k` does the system have infinitely many solutions?

```math
\begin{cases}
2x+4y=10\\
kx+8y=20
\end{cases}
```

**A)** `2`  
**B)** `4`  
**C)** `8`  
**D)** `10`

<details>
<summary><strong>Ответы и краткие решения</strong></summary>

### Problem 1

**Ответ: B) `(6,3)`**

Складываем уравнения:

```math
2x=12
```

```math
x=6
```

Тогда `y=3`.

### Problem 2

**Ответ: `4`**

```math
2x+(3x-2)=18
```

```math
5x=20
```

```math
x=4
```

### Problem 3

**Ответ: B**

Обе линии имеют slope `4`, но разные y-intercepts: `3` и `-5`. Они параллельны.

### Problem 4

**Ответ: `20`**

Пусть `s` — small, `l` — large:

```math
s+l=50
```

```math
3s+5l=190
```

Из `s=50-l`:

```math
3(50-l)+5l=190
```

```math
150+2l=190
```

```math
l=20
```

### Problem 5

**Ответ: B) `4`**

Чтобы второе уравнение было удвоением первого:

```math
2(2x+4y=10)
```

получаем:

```math
4x+8y=20
```

Следовательно `k=4`.

</details>

---

## 5. Common Traps — типичные ловушки

### Ловушка 1. Найти только `x` и забыть про `y`

Если вопрос просит ordered pair, ответ должен быть `(x,y)`, а не только одно число.

### Ловушка 2. Ошибка знака при elimination

Если вычитаете целое уравнение, знак меняется у **каждого** члена.

Например:

```math
-(2x-3y=5)
```

становится:

```math
-2x+3y=-5
```

### Ловушка 3. Считать одинаковый slope признаком бесконечных решений

Одинаковый slope означает либо:

- параллельные линии → no solution;
- одну и ту же линию → infinitely many solutions.

Нужно проверить intercept или эквивалентность всего уравнения.

---

## 6. Стратегия для Digital SAT

### Desmos — сильный инструмент для систем

Введите оба уравнения:

```text
y = 2x + 3
y = -x + 9
```

Точка пересечения показывает решение системы.

Это особенно удобно, если коэффициенты дробные или десятичные.

### Но elimination часто быстрее

Для системы

```math
\begin{cases}
4x+y=12\\
2x-y=6
\end{cases}
```

достаточно сложить уравнения. Здесь Desmos будет медленнее ручного решения.

### Как выбирать метод

```text
переменная уже выражена? → substitution
коэффициенты легко сокращаются? → elimination
неудобные числа / нужен визуальный контроль? → Desmos
```

### SAT word problems

В текстовой задаче сначала определите две неизвестные и найдите **два независимых факта**. Именно они обычно превращаются в два уравнения.

---

## 7. Связи с другими темами

### Предыдущие темы

- [Linear Equations](./linear_equations.md)
- [Linear Functions](./linear_functions.md)

Система объединяет сразу две линейные модели.

### Следующая тема

[Linear Inequalities](./linear_inequalities.md)

В inequalities вместо одной точки решения часто появляется целый диапазон или область допустимых значений.

### Связь с Advanced Math

Позже системы встречаются и с нелинейными функциями, например:

```math
\begin{cases}
y=x^2\\
y=2x+3
\end{cases}
```

Тогда решения — точки пересечения параболы и прямой.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я умею решать систему методом substitution.
- [ ] Я умею решать систему методом elimination.
- [ ] Я понимаю геометрический смысл one/no/infinite solutions.
- [ ] Я умею составить систему из текстовой задачи и проверить ответ.

### Контрольная микро-задача

```math
\begin{cases}
3x+y=14\\
x-y=2
\end{cases}
```

Найдите `(x,y)`.

<details>
<summary><strong>Проверка</strong></summary>

Складываем:

```math
4x=16
```

```math
x=4
```

Подставляем:

```math
4-y=2
```

```math
y=2
```

Ответ:

```math
(4,2)
```

</details>
