# Quadratics — квадратные уравнения и функции

## 1. Заголовок и краткое описание

Квадратные уравнения и функции — один из центральных типов задач домена **Advanced Math**. На SAT нужно уметь решать quadratic equations, читать параболы, находить *roots*, *vertex*, максимум/минимум и выбирать удобную форму записи.

> **Главная идея:** квадратная функция — это парабола, а разные формы одной функции подсвечивают разные свойства.

---

## 2. Ключевые понятия и формулы

| Понятие | Формула | Что показывает |
|---|---|---|
| standard form | `y=ax²+bx+c` | y-intercept = `c` |
| factored form | `y=a(x-r₁)(x-r₂)` | roots `r₁`, `r₂` |
| vertex form | `y=a(x-h)²+k` | vertex `(h,k)` |
| quadratic formula | `x=(-b±√(b²-4ac))/(2a)` | roots |
| discriminant | `D=b²-4ac` | число действительных roots |
| axis of symmetry | `x=-b/(2a)` | x-coordinate vertex |

### Discriminant

- `D>0` → два действительных корня;
- `D=0` → один действительный корень;
- `D<0` → нет действительных корней.

### Визуальный якорь

- **Factored form → roots видно сразу.**
- **Vertex form → вершину видно сразу.**
- **Standard form → y-intercept видно сразу.**

### Вопрос к читателю

Если `a<0`, парабола открывается вверх или вниз? Что тогда представляет vertex: максимум или минимум?

---

## 3. Пошаговый разбор — Guided Example

### Задача

For the function

```math
f(x)=x^2-6x+5,
```

find its zeros and vertex.

### Шаг 1. Ищем roots через factorization

Нужны два числа, произведение которых `5`, а сумма `-6`.

Это `-1` и `-5`:

```math
x^2-6x+5=(x-1)(x-5).
```

Почему factorization удобна? Потому что из произведения сразу видны нули функции.

### Шаг 2. Приравниваем каждый множитель к нулю

```math
x-1=0\Rightarrow x=1
```

```math
x-5=0\Rightarrow x=5
```

Roots: `1` и `5`.

### Шаг 3. Находим axis of symmetry

Она проходит посередине между roots:

```math
x=\frac{1+5}{2}=3.
```

### Шаг 4. Находим y-coordinate vertex

```math
f(3)=9-18+5=-4.
```

Vertex:

```math
(3,-4).
```

### Шаг 5. Проверяем смысл

Так как `a=1>0`, парабола открывается вверх. Значит `-4` — minimum value.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

What are the solutions to

```math
x^2-9=0?
```

**A)** `3 only`  
**B)** `-3 only`  
**C)** `-3 and 3`  
**D)** `-9 and 9`

### Problem 2 — Easy/Medium — Grid-in

For

```math
y=(x-4)^2+7,
```

what is the x-coordinate of the vertex?

### Problem 3 — Medium — Multiple Choice

Which expression is equivalent to

```math
x^2+7x+12?
```

**A)** `(x+2)(x+6)`  
**B)** `(x+3)(x+4)`  
**C)** `(x-3)(x-4)`  
**D)** `(x+1)(x+12)`

### Problem 4 — Medium — Multiple Choice

The equation

```math
x^2-8x+k=0
```

has exactly one real solution. What is `k`?

**A)** `8`  
**B)** `16`  
**C)** `32`  
**D)** `64`

### Problem 5 — Hard — Grid-in

A parabola has zeros at `x=2` and `x=8` and passes through `(0,16)`. If

```math
f(x)=a(x-2)(x-8),
```

what is `a`?

<details>
<summary><strong>Ответы и краткие решения</strong></summary>

1. **C.** `x²=9`, поэтому `x=±3`.  
2. **4.** Vertex form `a(x-h)²+k` даёт `h=4`.  
3. **B.** `3·4=12`, `3+4=7`.  
4. **B.** Один root означает `D=0`: `64-4k=0`, поэтому `k=16`.  
5. **1.** `16=a(-2)(-8)=16a`, значит `a=1`.

</details>

---

## 5. Common Traps — типичные ловушки

### Ловушка 1. Знак vertex в форме `(x-h)²`

В

```math
y=(x-5)^2+2
```

vertex — `(5,2)`, а не `(-5,2)`.

### Ловушка 2. Забыть `±`

Из `x²=25` следуют **два** решения: `x=5` и `x=-5`.

### Ловушка 3. Использовать quadratic formula там, где factoring очевиден

`x²-7x+12=0` быстрее решить как `(x-3)(x-4)=0`.

---

## 6. Стратегия для Digital SAT

### Desmos

Для сложного quadratic equation можно ввести:

```text
y=x^2-6x+5
y=0
```

Точки пересечения дают roots.

Для вопроса на maximum/minimum постройте функцию и найдите vertex.

### Что делать вручную

Если выражение легко факторизуется, factoring обычно быстрее Desmos. Если коэффициенты неудобные или вопрос графический, Desmos экономит время.

---

## 7. Связи с другими темами

**Опирается на:** linear equations, factoring, exponents.

**Связано с:**
- `equivalent_expressions.md`;
- `nonlinear_functions.md`;
- `nonlinear_equations_systems.md`;
- geometry optimization questions.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я умею решать quadratic equation факторизацией и quadratic formula.
- [ ] Я понимаю, что показывает discriminant.
- [ ] Я умею находить roots и vertex.
- [ ] Я умею выбирать между standard, factored и vertex form.
