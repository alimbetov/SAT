# Equivalent Expressions — эквивалентные выражения

## 1. Зачем эта тема нужна на SAT

На SAT редко спрашивают: «Раскрой скобки». Чаще дают две разные формы выражения и проверяют, умеете ли вы увидеть **одну и ту же структуру под разной записью**.

> **Главная идея:** форма может меняться, но значение выражения — нет.

Ученик должен научиться отвечать не только «как преобразовать?», но и:

1. **что я вижу?**
2. **какой паттерн здесь спрятан?**
3. **какая форма полезнее именно для вопроса?**

---

## 2. Pattern Map — как распознавать тип задачи

| Что вы видите | Паттерн | Что обычно делать |
|---|---|---|
| `a(b+c)` | distributive property | expand |
| `ab+ac` | common factor | factor |
| `x²-a²` | difference of squares | `(x-a)(x+a)` |
| `x²±2ax+a²` | perfect square | `(x±a)²` |
| `(x+a)(x+b)` | product of binomials | expand / read roots structure |
| fraction with polynomial numerator | hidden factor | factor before canceling |
| same base powers | exponent rule | add/subtract exponents |
| parameter in an identity | coefficient matching | compare corresponding terms |

### Mental model: «распаковать» и «упаковать»

```text
FACTORED FORM  --expand-->  EXPANDED FORM
FACTORED FORM  <--factor--  EXPANDED FORM
```

Это обратные процессы.

### Почему разные формы полезны по-разному

```math
x^2-5x+6
```

и

```math
(x-2)(x-3)
```

эквивалентны, но:

- expanded form удобна для чтения коэффициентов;
- factored form удобна для roots;
- vertex-like form удобна для maximum/minimum.

**SAT-паттерн:** сначала спросите, **что просит вопрос**, и только потом выбирайте форму.

---

## 3. Учимся решать по паттернам

### Pattern A — Distribute and combine like terms

#### Worked Example

Simplify:

```math
4(x+3)-2x
```

**Notice:** есть скобки и like terms.

**Decision:** сначала expand, затем combine.

```math
4x+12-2x
```

```math
2x+12
```

**Check:** подставим `x=1`.

Исходное:

```math
4(4)-2=14
```

Новое:

```math
2+12=14
```

Совпало.

#### Faded Example

```math
5(2x-1)+3x
```

1. Expand: `__________`
2. Combine like terms: `__________`

<details><summary>Проверка</summary>

`10x-5+3x=13x-5`.

</details>

---

### Pattern B — Factor out the GCF

#### Worked Example

```math
6x^2+18x
```

**Notice:** оба terms делятся на `6x`.

```math
6x(x+3)
```

**Почему это полезно?**

Если дальше нужно решать

```math
6x^2+18x=0,
```

то factored form сразу даёт:

```math
6x(x+3)=0.
```

---

### Pattern C — Difference of squares

Запомните визуальный шаблон:

```math
a^2-b^2=(a-b)(a+b)
```

#### Worked Example

```math
x^2-49
```

Это:

```math
x^2-7^2
```

поэтому:

```math
(x-7)(x+7).
```

#### Recognition Question

Что из этого является difference of squares?

- `x²+25`
- `x²-25`
- `x²-10x+25`

Ответ: `x²-25`.

**Ключевой признак:** subtraction между двумя perfect squares.

---

### Pattern D — Perfect-square trinomial

```math
(a+b)^2=a^2+2ab+b^2
```

```math
(a-b)^2=a^2-2ab+b^2
```

#### Worked Example

Factor:

```math
x^2-12x+36
```

**Notice:**

- `36=6²`;
- middle term `-12x = -2·6·x`.

Значит:

```math
(x-6)^2.
```

#### Pattern Check

Для

```math
x^2+14x+49
```

половина `14` — это `7`, а `7²=49`.

Значит:

```math
(x+7)^2.
```

---

### Pattern E — Cancel only factors

#### Worked Example

Simplify:

```math
\frac{x^2-25}{x-5}
```

Сначала factor numerator:

```math
\frac{(x-5)(x+5)}{x-5}
```

Теперь можно сократить **factor** `(x-5)`:

```math
x+5,
```

но исходное выражение имеет restriction:

```math
x\ne5.
```

### Error Clinic

Нельзя делать так:

```math
\frac{x+5}{x} \cancel{=} 5.
```

Почему? Потому что `x+5` — сумма, а не произведение factors.

> **Правило:** сокращаем factors, а не terms.

---

### Pattern F — Parameter by coefficient matching

#### Worked Example

If

```math
(x+a)^2=x^2+14x+49,
```

find positive `a`.

Expand шаблон:

```math
(x+a)^2=x^2+2ax+a^2.
```

Сравниваем middle coefficients:

```math
2a=14
```

```math
a=7.
```

Проверка constant:

```math
7^2=49.
```

Совпадает.

---

## 4. Method Selector + SAT Language Decoder

### Как выбрать действие

```text
Есть скобки?
  └─ Нужно упростить → expand

Есть общий множитель?
  └─ Нужно увидеть структуру → factor GCF

Вижу a²-b²?
  └─ difference of squares

Вижу x²±2ax+a²?
  └─ perfect square

Есть дробь?
  └─ factor first, cancel factors only

Есть parameter и identity?
  └─ compare coefficients
```

### SAT English → математическое действие

| SAT phrase | Что это обычно значит |
|---|---|
| `Which expression is equivalent to...` | transform without changing value |
| `Which form reveals the zeros?` | factor |
| `Which form reveals the minimum/maximum?` | vertex form |
| `for all x` | identity; compare coefficients |
| `simplify` | reduce structure safely |
| `factor` | rewrite as product |

---

## 5. Guided Practice — подсказки постепенно исчезают

### Example 1 — с полной опорой

Simplify:

```math
3(x+4)+2x
```

**Pattern:** distribute + combine.

```math
3x+12+2x=5x+12.
```

### Example 2 — с частичной подсказкой

Factor:

```math
x^2-81
```

Подсказка: `81=9²`.

Ответ:

```math
(x-9)(x+9).
```

### Example 3 — почти самостоятельно

Factor:

```math
x^2+18x+81
```

Спросите себя:

1. Является ли `81` квадратом?
2. Равен ли middle term `2·9·x`?

<details><summary>Ответ</summary>

```math
(x+9)^2
```

</details>

### Example 4 — transfer

If

```math
4x^2+20x=4x(x+k),
```

find `k`.

<details><summary>Решение</summary>

Factor left side:

```math
4x(x+5),
```

поэтому `k=5`.

</details>

---

## 6. Common Traps + Desmos Strategy

### Trap 1 — `(a+b)²=a²+b²`

Неверно.

Правильно:

```math
(a+b)^2=a^2+2ab+b^2.
```

### Trap 2 — потерять domain restriction

После сокращения выражение может выглядеть проще, но запрещённое значение из исходного denominator остаётся запрещённым.

### Trap 3 — использовать не ту форму

Иногда ученик умеет преобразовать, но делает это в неудобную сторону.

Например, если спрашивают roots, переходить из factored form в expanded form — шаг назад.

### Desmos

Desmos полезен как **verification tool**.

Введите:

```text
y=(x-3)(x+5)
y=x^2+2x-15
```

Если графики совпадают, expressions эквивалентны.

Но на простых identities ручное распознавание быстрее.

---

## 7. SAT-Style Practice

### Problem 1 — Easy — Multiple Choice

Which expression is equivalent to

```math
5(x+2)-3x?
```

**A)** `2x+2`  
**B)** `2x+10`  
**C)** `8x+10`  
**D)** `2x+7`

### Problem 2 — Easy — Multiple Choice

Which expression is equivalent to

```math
x^2-64?
```

**A)** `(x-8)^2`  
**B)** `(x-8)(x+8)`  
**C)** `(x-32)(x+2)`  
**D)** `(x+8)^2`

### Problem 3 — Medium — Grid-in

If

```math
3x^2+15x=3x(x+k),
```

what is `k`?

### Problem 4 — Medium — Multiple Choice

Which expression is equivalent to

```math
\frac{x^2-36}{x-6}
```

for `x≠6`?

**A)** `x-6`  
**B)** `x+6`  
**C)** `x²+6`  
**D)** `1`

### Problem 5 — Hard — Grid-in

If

```math
(x+a)^2=x^2+22x+121,
```

what is the positive value of `a`?

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **B.** `5x+10-3x=2x+10`.  
2. **B.** Difference of squares.  
3. **5.** `3x²+15x=3x(x+5)`.  
4. **B.** `(x²-36)=(x-6)(x+6)`.  
5. **11.** `2a=22`.

</details>

---

## 8. Мини-чек-лист и Transfer

- [ ] Я различаю `expand` и `factor` и понимаю, зачем нужен каждый.
- [ ] Я мгновенно узнаю difference of squares.
- [ ] Я узнаю perfect-square trinomial.
- [ ] Я сокращаю только factors.
- [ ] Я умею выбрать форму выражения под конкретный вопрос.
- [ ] Я могу найти parameter через coefficient matching.

### Transfer Question

Почему выражение

```math
2(x-4)^2+7
```

может быть полезнее expanded form, если SAT спрашивает minimum value?

Ответ: потому что в этой форме сразу видно vertex; minimum value равно `7`.
