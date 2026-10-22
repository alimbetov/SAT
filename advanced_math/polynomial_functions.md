# Polynomial Functions — полиномы и полиномиальные функции

## 1. Зачем эта тема нужна на SAT

Polynomial questions проверяют не вычислительную выносливость, а умение видеть структуру: degree, zeros, factors, remainder, end behavior и связь между algebra и graph.

> **Главная идея:** `root ↔ factor ↔ x-intercept` — три языка для одной идеи.

На экзамене ученик должен быстро распознавать, что именно дано:

- polynomial expression;
- factored form;
- zero;
- graph intercept;
- value `f(a)`;
- parameter inside a factorization.

---

## 2. Pattern Map — что вижу и что делать

| Что дано | Что это значит | Следующий шаг |
|---|---|---|
| `f(r)=0` | `r` — root | `(x-r)` factor |
| `(x-r)` is a factor | `r` — root | `f(r)=0` |
| graph crosses x-axis at `r` | x-intercept | root `r` |
| divide by `(x-r)` | remainder theorem | compute `f(r)` |
| factored polynomial | roots visible | set each factor = 0 |
| expanded polynomial | coefficients visible | compare / factor if needed |
| parameter in factorization | identity | expand and match coefficients |
| highest exponent | degree | read directly |

### Core connection

```text
root r
  ⇅
f(r)=0
  ⇅
factor (x-r)
  ⇅
x-intercept (r,0)
```

Это один из самых полезных SAT-паттернов Advanced Math.

---

## 3. Учимся решать по паттернам

### Pattern A — Degree and leading term

#### Worked Example

For

```math
f(x)=7x^4-3x^2+8,
```

- degree = `4`;
- leading coefficient = `7`;
- leading term = `7x^4`.

**Ловушка:** degree — это exponent, а не самый большой coefficient.

---

### Pattern B — Root → Factor

#### Worked Example

If `x=5` is a zero of `f(x)`, which factor must divide `f(x)`?

Root `5` означает:

```math
f(5)=0.
```

По Factor Theorem:

```math
(x-5)
```

is a factor.

### Visual Anchor

```text
root +5  → factor (x-5)
root -5  → factor (x+5)
```

Знак внутри factor всегда противоположный root.

---

### Pattern C — Factor → Root

#### Worked Example

```math
f(x)=2(x+3)(x-7)
```

Roots:

```math
x=-3,
```

```math
x=7.
```

**Почему?** Product equals zero only when at least one factor equals zero.

---

### Pattern D — Remainder theorem

If a polynomial is divided by `(x-a)`, remainder = `f(a)`.

#### Worked Example

For

```math
f(x)=x^3-2x+5,
```

find the remainder when divided by `(x-2)`.

Не нужно polynomial long division.

Просто:

```math
f(2)=8-4+5=9.
```

Remainder = `9`.

### Pattern Recognition

Если вопрос содержит:

> remainder when divided by `(x-4)`

ваша первая мысль должна быть:

```text
Compute f(4).
```

---

### Pattern E — Factor by grouping

#### Worked Example

Factor completely:

```math
x^3-4x^2-x+4.
```

Group:

```math
x^2(x-4)-1(x-4)
```

Common factor:

```math
(x^2-1)(x-4)
```

Difference of squares:

```math
(x-1)(x+1)(x-4).
```

Roots:

```text
1, -1, 4
```

Здесь сразу работают два знакомых паттерна: grouping + difference of squares.

---

### Pattern F — Parameter through coefficient matching

#### Worked Example

If

```math
(x+3)(x+k)=x^2+10x+21,
```

find `k`.

Expand left:

```math
x^2+(k+3)x+3k.
```

Compare coefficients:

```math
k+3=10
```

```math
k=7.
```

Check constant:

```math
3(7)=21.
```

---

## 4. Method Selector + SAT Language Decoder

### Быстрый выбор метода

```text
Question says zero/root?
  → think factor

Question says factor?
  → think root

Question says remainder after division by (x-a)?
  → compute f(a)

Polynomial already factored?
  → do NOT expand unless necessary

Need coefficients?
  → expanded form is often better

Need roots?
  → factored form is often better
```

### SAT English Decoder

| Phrase | Translation into action |
|---|---|
| `zero of f` | `f(x)=0` |
| `root` | same as zero |
| `x-intercept` | root on graph |
| `factor of f(x)` | corresponding root makes function zero |
| `remainder when divided by (x-a)` | compute `f(a)` |
| `degree` | highest exponent |

---

## 5. Guided Practice — faded examples

### Example 1 — full support

If `(x-4)` is a factor of `f(x)`, what is `f(4)`?

Pattern: factor theorem.

```math
f(4)=0.
```

### Example 2 — less support

If `f(-2)=0`, name a factor.

Think: root `-2` means factor with opposite sign.

<details><summary>Answer</summary>

```math
x+2
```

</details>

### Example 3 — transfer

For

```math
f(x)=x^3+3x^2-4x-12,
```

show that `x=2` is a root.

Compute:

```math
f(2)=8+12-8-12=0.
```

Therefore `(x-2)` is a factor.

### Example 4 — independent

Find remainder when

```math
f(x)=2x^3-x+1
```

is divided by `(x+1)`.

<details><summary>Solution</summary>

`x+1 = x-(-1)`, so compute:

```math
f(-1)=2(-1)^3-(-1)+1=-2+1+1=0.
```

Remainder = `0`.

</details>

---

## 6. Error Clinic + Desmos Strategy

### Error 1 — wrong sign in factor

Root `3` → factor `(x-3)`, not `(x+3)`.

### Error 2 — unnecessary long division

If denominator is `(x-a)` and question asks remainder, use `f(a)` first.

### Error 3 — expand too early

From

```math
(x-2)(x+5)(x-7),
```

roots are already visible. Expanding only creates work.

### Desmos

Use graphing to verify roots:

```text
y=(x-2)(x+5)(x-7)
```

Look for x-intercepts.

But for factor/remainder theorem, substitution is usually faster than graphing.

---

## 7. SAT-Style Practice

### Problem 1 — Easy — Multiple Choice

What is the degree of

```math
5x^6-2x^3+1?
```

**A)** 3  
**B)** 5  
**C)** 6  
**D)** 8

### Problem 2 — Easy — Grid-in

If `(x-7)` is a factor of `f(x)`, what is `f(7)`?

### Problem 3 — Medium — Multiple Choice

If `x=-4` is a zero of `f(x)`, which must be a factor?

**A)** `x-4`  
**B)** `x+4`  
**C)** `x²-4`  
**D)** `4x+1`

### Problem 4 — Medium — Grid-in

For

```math
f(x)=x^3-3x+6,
```

find the remainder when divided by `(x-2)`.

### Problem 5 — Hard — Grid-in

If

```math
(x+4)(x+k)=x^2+11x+28,
```

find `k`.

<details><summary><strong>Answers</strong></summary>

1. **C**, degree 6.  
2. **0**.  
3. **B**.  
4. `f(2)=8-6+6=8`.  
5. `k=7`.

</details>

---

## 8. Мини-чек-лист и Transfer

- [ ] Я связываю root, factor и x-intercept.
- [ ] Я использую Factor Theorem без лишних вычислений.
- [ ] Я использую Remainder Theorem вместо long division, когда можно.
- [ ] Я понимаю, когда factored form полезнее expanded form.
- [ ] Я умею находить parameter через coefficient matching.

### Transfer Question

Если график polynomial function пересекает x-axis в `x=-2`, что вы можете сказать об одном из factors?

Ответ:

```math
(x+2)
```

must be a factor.
