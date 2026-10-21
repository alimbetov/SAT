# Quadratics — квадратные уравнения и функции

> **Цель урока:** увидеть quadratic structure и быстро решить, **какой метод здесь выгоднее**: square root, factoring, discriminant, vertex form, quadratic formula или Desmos.

На SAT проблема обычно не в том, что ученик «не знает квадратную формулу». Проблема в другом: он применяет один и тот же метод ко всем задачам и тратит время.

Главная идея:

> **Quadratics — это не один алгоритм. Это семейство паттернов.**

---

# 1. Pattern Map — что я вижу и что делаю

| Что вижу | Паттерн | Лучший первый метод |
|---|---|---|
| `x²=49` | pure square | square root → `x=±7` |
| `x²-7x+12=0` | factorable quadratic | factoring |
| `(x-4)²=25` | square already isolated | square root |
| `y=(x-3)²+5` | vertex form | читать vertex напрямую |
| `y=(x-2)(x-8)` | factored form | читать roots напрямую |
| `x²-8x+k=0` + one real solution | number of roots / parameter | discriminant |
| ugly coefficients | hard-to-factor | quadratic formula или Desmos |
| graph asks intersections/minimum | visual quadratic | Desmos / graph interpretation |

Перед решением задайте себе:

> **«Какая форма передо мной и какую информацию она уже показывает?»**

---

# 2. Три формы quadratic function — три разных «окна»

Одна и та же parabola может быть записана по-разному.

## Standard form

```math
y=ax^2+bx+c
```

Что видно сразу:

```text
c = y-intercept
```

## Factored form

```math
y=a(x-r_1)(x-r_2)
```

Что видно сразу:

```text
roots / zeros / x-intercepts = r₁, r₂
```

## Vertex form

```math
y=a(x-h)^2+k
```

Что видно сразу:

```text
vertex = (h,k)
```

---

# 3. Визуальный якорь: форма — это подсказка

```text
STANDARD  → y-intercept
FACTORED  → roots
VERTEX    → vertex
```

Не преобразуйте функцию автоматически.

Сначала спросите:

> «Что именно спрашивает SAT?»

Если спрашивают roots и перед вами factored form — ответ уже почти виден.

---

# 4. PATTERN 1 — Pure Square

## Как узнать

После простого преобразования получается:

```math
x^2=c
```

или

```math
(x-h)^2=c
```

Главная ловушка:

> square root equation обычно даёт **два** значения.

---

## Worked Example 1

```math
x^2=49
```

### Notice

Это не general quadratic. Никакой quadratic formula не нужен.

### Decision

Берём square root обеих частей.

```math
x=\pm7
```

Почему `±`?

Потому что:

```math
7^2=49
```

и

```math
(-7)^2=49
```

---

## Worked Example 2 — shifted square

```math
(x-3)^2=16
```

Берём square root:

```math
x-3=\pm4
```

Получаем две ветки:

```math
x-3=4\Rightarrow x=7
```

```math
x-3=-4\Rightarrow x=-1
```

**Solutions: `-1` and `7`.**

---

## Recognition Drill

Для какой задачи square-root method самый естественный?

**A)** `x²-5x+6=0`  
**B)** `(x+2)²=81`  
**C)** `2x²+7x+3=0`  
**D)** `x²+6x+4=0`

<details>
<summary>Ответ</summary>

**B.** Square already isolated.

</details>

---

# 5. PATTERN 2 — Factoring

## Как узнать

Quadratic выглядит так:

```math
x^2+bx+c=0
```

и есть хорошие integer factors.

Для monic quadratic `x²+bx+c` ищем числа `p` и `q`, такие что:

```math
pq=c
```

```math
p+q=b
```

Тогда:

```math
x^2+bx+c=(x+p)(x+q)
```

---

## Worked Example 1

```math
x^2-7x+12=0
```

### Notice

Нужно два числа:

```text
product = +12
sum     = -7
```

### Decision

Оба числа должны быть negative, потому что product positive, sum negative.

Подходят `-3` и `-4`.

```math
(x-3)(x-4)=0
```

Zero-product rule:

```math
x-3=0\quad\text{or}\quad x-4=0
```

```math
x=3,4
```

---

## Pattern Card — знаки при factoring

Для

```math
x^2+bx+c
```

быстрая логика:

```text
c positive → factors same sign
c negative → factors opposite signs

b tells which sign dominates
```

Пример:

```math
x^2+x-12
```

`c=-12` → opposite signs.

Нужна сумма `+1` → positive factor по модулю больше.

```math
(x+4)(x-3)
```

---

## Worked Example 2 — difference of squares

```math
x^2-25=0
```

Можно решить square root, но есть ещё мгновенный pattern:

```math
a^2-b^2=(a-b)(a+b)
```

```math
(x-5)(x+5)=0
```

```math
x=\pm5
```

Это один из SAT patterns, который стоит узнавать визуально.

---

# 6. PATTERN 3 — Vertex Form

Форма:

```math
y=a(x-h)^2+k
```

Главное:

```text
vertex = (h,k)
```

Но знак внутри скобок читается «наоборот».

---

## Worked Example 1

```math
y=(x-4)^2+7
```

Сравниваем с:

```math
y=(x-h)^2+k
```

Получаем:

```text
h = 4
k = 7
```

Vertex:

```math
(4,7)
```

---

## Error Clinic — знак vertex

Ученик видит:

```math
(x+3)^2
```

и пишет `h=3`.

Но:

```math
x+3=x-(-3)
```

Значит:

```text
h = -3
```

Визуальный якорь:

```text
inside parentheses → opposite sign
outside             → same sign
```

---

## Worked Example 2 — minimum/maximum

```math
y=2(x-5)^2-8
```

Vertex:

```math
(5,-8)
```

`a=2>0`, parabola opens upward.

Значит vertex — minimum.

```text
minimum value = -8
occurs at x = 5
```

Если бы `a<0`, vertex был бы maximum.

---

# 7. PATTERN 4 — Roots + symmetry → vertex

Если известны roots `r₁` и `r₂`, axis of symmetry находится ровно посередине:

```math
x_{vertex}=\frac{r_1+r_2}{2}
```

---

## Worked Example

```math
f(x)=x^2-6x+5
```

Factor:

```math
(x-1)(x-5)
```

Roots:

```text
1 and 5
```

Vertex x-coordinate:

```math
\frac{1+5}{2}=3
```

Теперь:

```math
f(3)=9-18+5=-4
```

Vertex:

```math
(3,-4)
```

### Визуальный смысл

Парабола симметрична.

Если пересечения с x-axis находятся в `1` и `5`, середина между ними — `3`.

Не нужно заучивать это как отдельную магию.

---

# 8. PATTERN 5 — Discriminant: сколько roots?

Quadratic formula содержит:

```math
\sqrt{b^2-4ac}
```

Выражение под корнем называется **discriminant**:

```math
D=b^2-4ac
```

Оно отвечает на вопрос: сколько real roots?

---

# Визуальный якорь: discriminant = светофор roots

```text
D > 0  → 2 real roots
D = 0  → 1 real root
D < 0  → 0 real roots
```

Почему?

- positive number имеет два square-root направления `±`;
- zero уничтожает `±` различие;
- negative number не имеет real square root.

---

## Worked Example 1 — parameter

```math
x^2-8x+k=0
```

Equation has exactly one real solution. Find `k`.

### Notice

Фраза **exactly one real solution** — сильнейшая подсказка.

Не нужно искать сам root.

### Decision

Use discriminant:

```math
D=0
```

Здесь:

```text
a = 1
b = -8
c = k
```

```math
(-8)^2-4(1)(k)=0
```

```math
64-4k=0
```

```math
k=16
```

---

## SAT Language Decoder

| SAT phrase | Что означает |
|---|---|
| `two distinct real solutions` | `D>0` |
| `exactly one real solution` | `D=0` |
| `no real solutions` | `D<0` |
| `zeros` | roots / x-intercepts |
| `x-intercepts` | zeros / roots |
| `minimum value` | y-coordinate vertex if `a>0` |
| `maximum value` | y-coordinate vertex if `a<0` |

Эти слова могут описывать одну и ту же математику с разных сторон.

---

# 9. PATTERN 6 — Quadratic Formula

Используйте:

```math
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
```

когда factoring не очевиден или нужна exact form.

Но не используйте её автоматически.

---

## Worked Example

```math
2x^2+3x-7=0
```

Подбираемые integer factors неудобны.

Значит quadratic formula разумна.

```text
a=2
b=3
c=-7
```

```math
x=\frac{-3\pm\sqrt{3^2-4(2)(-7)}}{4}
```

```math
x=\frac{-3\pm\sqrt{9+56}}{4}
```

```math
x=\frac{-3\pm\sqrt{65}}{4}
```

Не пытайтесь превратить `√65` в decimal, если SAT просит exact expression.

---

# 10. PATTERN 7 — Factored form + extra information

Hard SAT часто даёт roots, но спрашивает coefficient.

---

## Worked Example

A parabola has zeros at `x=2` and `x=8` and passes through `(0,16)`.

Write:

```math
f(x)=a(x-2)(x-8)
```

### Notice

Roots уже встроены. Не надо строить general form.

### Decision

Используем данную point `(0,16)` для поиска `a`.

```math
16=a(0-2)(0-8)
```

```math
16=16a
```

```math
a=1
```

### Pattern

```text
roots given
→ write factored form
→ substitute one known point
→ solve for a
```

Очень частая структура hard questions.

---

# 11. Method Selector — главный decision tree

```text
Quadratic question
│
├─ Вид x² = number или (x-h)² = number?
│      └─ square root
│
├─ Легко factor?
│      └─ factoring
│
├─ Уже vertex form?
│      └─ read vertex / max / min directly
│
├─ Уже factored form?
│      └─ read roots directly
│
├─ Спрашивают number of real solutions?
│      └─ discriminant
│
├─ Ugly coefficients / exact roots?
│      └─ quadratic formula
│
└─ Graph/intersection/visual question?
       └─ Desmos may be fastest
```

Эту карту нужно научиться воспроизводить мысленно.

---

# 12. Desmos Strategy — не просто «построй график»

Возьмём:

```math
f(x)=x^2-6x+5
```

Введите в Desmos:

```text
y=x^2-6x+5
```

Из одного графика можно прочитать:

```text
x-intercepts → roots = 1, 5
lowest point → vertex = (3,-4)
y-intercept  → 5
axis symmetry → x=3
```

## Когда Desmos особенно хорош

- ugly coefficients;
- nonlinear system;
- intersection question;
- vertex/minimum question;
- approximate solution;
- quick verification.

## Когда вручную быстрее

```math
x^2-9=0
```

или

```math
x^2-7x+12=0
```

Не превращайте 10-секундную задачу в минутную работу с графиком.

---

# 13. Error Clinic

## Ошибка 1 — забыть `±`

```math
x^2=36
```

не только `6`.

Правильно:

```math
x=\pm6
```

---

## Ошибка 2 — знак vertex внутри parentheses

```math
y=(x+5)^2-2
```

Vertex:

```math
(-5,-2)
```

не `(5,-2)`.

---

## Ошибка 3 — quadratic formula при очевидном factoring

```math
x^2-5x+6=0
```

можно решить:

```math
(x-2)(x-3)=0
```

за несколько секунд.

---

## Ошибка 4 — спутать root и vertex

Roots — где:

```math
y=0
```

Vertex — maximum/minimum turning point.

Это разные объекты.

---

## Ошибка 5 — считать весь root, когда спрашивают только число roots

Если вопрос: «how many real solutions?» — discriminant часто достаточно.

Не решайте больше, чем попросили.

---

# 14. Guided Practice — scaffolding постепенно исчезает

## Level A — метод указан

### A1 — Use factoring

```math
x^2-9x+20=0
```

Ищем числа:

```text
product = 20
sum     = -9
```

Какие это числа?

<details>
<summary>Ответ</summary>

`-4` и `-5`.

```math
(x-4)(x-5)=0
```

```math
x=4,5
```

</details>

---

## Level B — сначала выберите метод

### B1

```math
(x-7)^2=36
```

Запишите перед решением:

```text
Best method: __________________
Why: _________________________
```

<details>
<summary>Ответ</summary>

Square root.

```math
x-7=\pm6
```

```math
x=13,1
```

</details>

---

## Level C — language clue

### C1

```math
3x^2-12x+k=0
```

has exactly one real solution.

Какое слово подсказывает метод?

```text
____________________________
```

<details>
<summary>Решение</summary>

`exactly one real solution` → `D=0`.

```math
(-12)^2-4(3)(k)=0
```

```math
144-12k=0
```

```math
k=12
```

</details>

---

## Level D — transfer

A parabola has roots `-2` and `6`. Its y-intercept is `24`. If

```math
f(x)=a(x+2)(x-6),
```

find `a`.

<details>
<summary>Решение</summary>

Y-intercept означает `x=0`, `y=24`.

```math
24=a(2)(-6)
```

```math
24=-12a
```

```math
a=-2
```

</details>

---

# 15. SAT-style Independent Practice

## Problem 1 — Easy — Multiple Choice

What are the solutions to

```math
x^2-16=0?
```

**A)** `4 only`  
**B)** `-4 only`  
**C)** `-4 and 4`  
**D)** `-16 and 16`

---

## Problem 2 — Easy — SPR

For

```math
y=(x+3)^2-5,
```

what is the x-coordinate of the vertex?

---

## Problem 3 — Medium — Multiple Choice

Which expression is equivalent to

```math
x^2+9x+20?
```

**A)** `(x+4)(x+5)`  
**B)** `(x+2)(x+10)`  
**C)** `(x-4)(x-5)`  
**D)** `(x+1)(x+20)`

---

## Problem 4 — Medium — Multiple Choice

The equation

```math
x^2-10x+k=0
```

has exactly one real solution. What is `k`?

**A)** `10`  
**B)** `20`  
**C)** `25`  
**D)** `100`

---

## Problem 5 — Hard — SPR

The zeros of a quadratic are `3` and `9`. What is the x-coordinate of its axis of symmetry?

---

## Problem 6 — Hard — Multiple Choice

Which method is most direct for solving

```math
(x-4)^2=81?
```

**A)** quadratic formula  
**B)** square root  
**C)** discriminant only  
**D)** regression

---

## Problem 7 — 750–800 — SPR

The equation

```math
2x^2-12x+k=0
```

has exactly one real solution. Find `k`.

---

## Problem 8 — 750–800 — Multiple Choice

A quadratic function has roots at `x=-1` and `x=7` and passes through `(0,-14)`. Which function could represent it?

**A)** `f(x)=2(x+1)(x-7)`  
**B)** `f(x)=-2(x+1)(x-7)`  
**C)** `f(x)=(x-1)(x+7)`  
**D)** `f(x)=14(x+1)(x-7)`

<details>
<summary><strong>Ответы и паттерны</strong></summary>

1. **C.** Pure square / difference of squares → `x=±4`.
2. **`-3`.** Vertex form → opposite sign inside parentheses.
3. **A.** `4×5=20`, `4+5=9`.
4. **C, 25.** Exactly one real root → `D=0`: `100-4k=0`.
5. **`6`.** Midpoint roots: `(3+9)/2=6`.
6. **B.** Square already isolated.
7. **`18`.** `D=(-12)^2-4(2)(k)=0 → 144-8k=0 → k=18`.
8. **A.** At `x=0`: `2(1)(-7)=-14`.

</details>

---

# 16. Transfer Questions — без вычислений

1. Почему factored form удобнее standard form, если спрашивают roots?
2. Почему vertex form удобнее standard form, если спрашивают minimum?
3. Как по знаку `a` понять, maximum или minimum находится в vertex?
4. Как фраза `exactly one real solution` подсказывает discriminant?
5. Когда square-root method быстрее quadratic formula?
6. Почему roots `2` и `8` сразу говорят, что axis of symmetry равна `5`?
7. Когда Desmos реально экономит время?
8. Почему SAT иногда выгоднее решить вопрос по structure, а не полностью раскрывать функцию?

---

# 17. Мини-чек-лист

- [ ] Я сначала определяю форму quadratic.
- [ ] Я различаю standard, factored и vertex form.
- [ ] Я умею выбрать square root, factoring, discriminant или quadratic formula по структуре задачи.
- [ ] Я не забываю `±`.
- [ ] Я читаю vertex с правильным знаком.
- [ ] Я понимаю roots как x-intercepts/zeros.
- [ ] Я использую midpoint roots для axis of symmetry.
- [ ] Я понимаю, что `D>0`, `D=0`, `D<0` говорят о числе real roots.
- [ ] Я умею находить coefficient `a` по roots и дополнительной point.
- [ ] Я знаю, когда Desmos быстрее, а когда ручное решение проще.
- [ ] Я могу объяснить, **почему** выбрал конкретный метод.

---

# 18. Связи с другими темами

Quadratics связывает сразу несколько тем:

```text
Equivalent Expressions
        ↓
Factoring
        ↓
Quadratics
   ↙          ↘
Graphs      Nonlinear Systems
   ↓              ↓
Vertex       Intersections
        ↘    ↙
          Desmos
```

Если вы научились не просто решать quadratic equations, а распознавать их форму, большая часть Advanced Math становится намного понятнее.
