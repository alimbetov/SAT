# Nonlinear Functions — нелинейные функции

## 1. Заголовок и краткое описание

**Nonlinear functions** — официальный skill Advanced Math. На SAT под этим названием объединяются quadratic, exponential, polynomial, rational, radical, absolute-value и другие модели. Главное — уметь переходить между equation, table и graph и интерпретировать параметры.

> **Главная идея:** если rate of change не постоянен, функция обычно nonlinear.

---

## 2. Ключевые понятия и формулы

| Тип | Пример | Ключевой признак |
|---|---|---|
| quadratic | `y=x²` | parabola |
| exponential | `y=2^x` | постоянный multiplicative factor |
| polynomial | `y=x³-2x` | целые неотрицательные степени |
| rational | `y=1/x` | переменная в denominator |
| radical | `y=√x` | radical |
| absolute value | `y=|x|` | V-shaped graph |

### Что SAT часто спрашивает

- значение функции `f(a)`;
- zeros / x-intercepts;
- maximum/minimum;
- domain или range;
- смысл параметра;
- преобразование графика;
- сравнение двух моделей.

### Transformations

Для

```math
y=f(x-h)+k
```

график `f(x)` сдвигается:

- вправо на `h`;
- вверх на `k`.

### Визуальный якорь

**Внутри функции знак работает наоборот, снаружи — как написано.**

`f(x-3)` → вправо 3.  
`f(x)+3` → вверх 3.

---

## 3. Пошаговый разбор — Guided Example

### Задача

The function

```math
f(x)=2(x-3)^2+5
```

models a quantity. Identify the vertex and minimum value.

### Шаг 1. Узнаём vertex form

Quadratic vertex form:

```math
a(x-h)^2+k.
```

Здесь `h=3`, `k=5`.

### Шаг 2. Находим vertex

```math
(3,5).
```

### Шаг 3. Определяем направление

`a=2>0`, парабола открывается вверх.

### Шаг 4. Интерпретируем

Следовательно, `5` — minimum value функции.

Почему не нужно раскрывать скобки? Потому что текущая форма уже показывает нужную информацию напрямую.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

Which function is nonlinear?

**A)** `y=3x+2`  
**B)** `y=-5x`  
**C)** `y=x²+1`  
**D)** `y=7`

### Problem 2 — Easy — Grid-in

If `f(x)=x²+4`, what is `f(3)`?

### Problem 3 — Medium — Multiple Choice

What transformation changes `y=x²` into `y=(x-4)²+1`?

**A)** left 4, down 1  
**B)** right 4, up 1  
**C)** right 1, up 4  
**D)** left 1, down 4

### Problem 4 — Medium — Multiple Choice

Which model has a constant percentage rate of change?

**A)** `y=5x+10`  
**B)** `y=10(1.2)^x`  
**C)** `y=x²`  
**D)** `y=√x`

### Problem 5 — Hard — Grid-in

For `f(x)=a(x-2)²+7`, the point `(4,15)` lies on the graph. What is `a`?

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **C**.  
2. **13**.  
3. **B**.  
4. **B**.  
5. **2**: `15=a(2²)+7`, значит `8=4a`.

</details>

---

## 5. Common Traps — типичные ловушки

- Считать любую кривую «сложной», но не распознавать конкретный family type.
- Ошибаться со знаком horizontal shift.
- Раскрывать выражение, когда исходная форма уже показывает vertex, roots или initial value.

---

## 6. Стратегия для Digital SAT

Desmos особенно силён именно для nonlinear functions:

- строит график мгновенно;
- показывает intersections и extrema;
- позволяет сравнивать модели;
- помогает проверить transformation.

Но сначала определите, **какую характеристику спрашивает задача**. Иногда нужное значение видно прямо из формы функции и график только замедлит решение.

---

## 7. Связи с другими темами

Этот файл объединяет навыки из:
- `quadratics.md`;
- `exponential_functions.md`;
- `polynomial_functions.md`;
- `rational_expressions_equations.md`;
- `radicals_and_radical_equations.md`;
- `absolute_value.md`.

Следующий шаг: `nonlinear_equations_systems.md`.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я распознаю основные families nonlinear functions.
- [ ] Я читаю полезную информацию из формы уравнения.
- [ ] Я понимаю basic graph transformations.
- [ ] Я выбираю между algebraic и graphical solution method.
