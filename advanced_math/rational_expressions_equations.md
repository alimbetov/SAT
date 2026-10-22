# Rational Expressions and Equations — рациональные выражения и уравнения

## 1. Зачем эта тема нужна на SAT

Rational expressions содержат переменную в denominator. Главная сложность SAT здесь — не арифметика, а дисциплина:

1. увидеть запрещённые значения;
2. понять, что можно сокращать;
3. выбрать LCD или cross multiplication;
4. проверить, не появился ли invalid / extraneous answer.

> **Главная идея:** сначала domain restrictions, потом algebra.

---

## 2. Pattern Map — как распознавать задачу

| Что вы видите | Паттерн | Что делать |
|---|---|---|
| variable in denominator | domain restriction | denominator `≠0` |
| factor appears top and bottom | simplification | factor, then cancel |
| two simple fractions equal | proportion | cross multiply |
| several denominators | rational equation | use LCD |
| solution equals forbidden value | extraneous/invalid | reject |
| hole after cancellation | removable discontinuity | original restriction stays |

### Visual Anchor

```text
DENOMINATOR = DANGER ZONE
```

Перед любыми преобразованиями спросите:

> При каких x denominator становится 0?

---

## 3. Учимся решать по паттернам

### Pattern A — Domain restriction

#### Worked Example

For

```math
\frac{5}{x-7},
```

find the forbidden value.

Set denominator equal to zero:

```math
x-7=0
```

```math
x=7.
```

Therefore:

```math
x\ne7.
```

---

### Pattern B — Factor before canceling

#### Worked Example

Simplify:

```math
\frac{x^2-16}{x-4}.
```

**Notice:** numerator is difference of squares.

```math
x^2-16=(x-4)(x+4).
```

So:

```math
\frac{(x-4)(x+4)}{x-4}=x+4,
```

but original restriction remains:

```math
x\ne4.
```

### Error Clinic

Wrong:

```math
\frac{x+4}{x}=4.
```

Why wrong? `x+4` is a sum, not a product of factors.

> **Rule:** cancel factors, never terms inside addition/subtraction.

---

### Pattern C — Cross multiplication for a proportion

#### Worked Example

Solve:

```math
\frac{3}{x-1}=\frac{6}{x+2}.
```

#### Step 1 — restrictions

```math
x\ne1,-2.
```

#### Step 2 — cross multiply

```math
3(x+2)=6(x-1).
```

#### Step 3 — solve

```math
3x+6=6x-6
```

```math
12=3x
```

```math
x=4.
```

#### Step 4 — check restriction

`4` is allowed.

---

### Pattern D — LCD for several fractions

#### Worked Example

Solve:

```math
\frac1x+\frac1{x+2}=\frac34.
```

Restrictions:

```math
x\ne0,-2.
```

LCD:

```math
4x(x+2).
```

Multiply every term by LCD:

```math
4(x+2)+4x=3x(x+2).
```

Then solve the resulting quadratic.

**Key idea:** LCD is not magic. It clears denominators by multiplying **every term**.

---

### Pattern E — Candidate is forbidden

Suppose after solving you obtain:

```math
x=3,
```

but original denominator contains `(x-3)`.

Then `x=3` is invalid even if later simplified algebra seems to accept it.

> Original expression controls the domain.

---

## 4. Method Selector + SAT Language Decoder

### Choose the method

```text
One denominator?
  → note restriction

Same factor top/bottom?
  → factor, cancel, keep restriction

Fraction = fraction?
  → cross multiply

Several different denominators?
  → use LCD

Found candidate?
  → check original restrictions
```

### SAT English Decoder

| Phrase | What to think |
|---|---|
| `undefined` | denominator = 0 |
| `equivalent for x ≠ ...` | cancellation with restriction |
| `solve the equation` | clear denominators safely |
| `which value must be excluded` | domain restriction |
| `least common denominator` | product of necessary denominator factors |

---

## 5. Guided Practice — fading support

### Example 1 — full support

Simplify:

```math
\frac{x^2-25}{x-5}.
```

Factor numerator:

```math
(x-5)(x+5).
```

Cancel common factor:

```math
x+5,
```

with `x≠5`.

### Example 2 — partial support

Solve:

```math
\frac2x=\frac69.
```

1. Restriction: `x≠___`
2. Cross multiply: `2·9=6x`
3. Solution: `x=___`

<details><summary>Answer</summary>

`x=3`.

</details>

### Example 3 — transfer

Solve:

```math
\frac{x+1}{x-2}=2.
```

<details><summary>Solution</summary>

Restriction `x≠2`.

```math
x+1=2x-4
```

```math
x=5.
```

Valid.

</details>

### Example 4 — recognition only

What must you do **before** simplifying

```math
\frac{(x-3)(x+7)}{x-3}?
```

Answer: record `x≠3`.

---

## 6. Error Clinic + Desmos Strategy

### Error 1 — forgetting original restrictions

After cancellation, simplified expression may be defined where original one was not.

### Error 2 — canceling terms instead of factors

You can cancel:

```math
\frac{(x+2)(x-5)}{x+2}
```

but not:

```math
\frac{x+2}{x}.
```

### Error 3 — multiplying only one term by LCD

LCD multiplication applies to **every term in the equation**.

### Desmos

For an equation such as:

```math
\frac3{x-1}=\frac6{x+2},
```

enter both sides as graphs and inspect intersections.

But Desmos can visually hide forbidden x-values, so domain reasoning must still be done manually.

---

## 7. SAT-Style Practice

### Problem 1 — Easy — Multiple Choice

For which value is

```math
\frac{7}{x+4}
```

undefined?

**A)** `-4`  
**B)** `0`  
**C)** `4`  
**D)** `7`

### Problem 2 — Easy — Multiple Choice

Simplify

```math
\frac{x^2-9}{x-3}
```

for `x≠3`.

**A)** `x-3`  
**B)** `x+3`  
**C)** `x²+3`  
**D)** `1`

### Problem 3 — Medium — Grid-in

Solve:

```math
\frac4x=\frac8{10}.
```

### Problem 4 — Medium — Multiple Choice

What is an LCD of

```math
\frac1x\quad\text{and}\quad\frac1{x-5}?
```

**A)** `x-5`  
**B)** `x(x-5)`  
**C)** `2x-5`  
**D)** `x²-5`

### Problem 5 — Hard — Grid-in

Solve:

```math
\frac{x+2}{x-1}=3.
```

<details><summary><strong>Answers</strong></summary>

1. **A**  
2. **B**  
3. `5`  
4. **B**  
5. `5/2`

</details>

---

## 8. Мини-чек-лист и Transfer

- [ ] Я нахожу forbidden values до преобразований.
- [ ] Я сокращаю только factors.
- [ ] Я выбираю cross multiplication для simple proportion.
- [ ] Я использую LCD для нескольких denominators.
- [ ] Я проверяю кандидаты в original equation/domain.

### Transfer Question

Почему выражения

```math
\frac{x^2-4}{x-2}
```

и

```math
x+2
```

не имеют полностью одинаковый domain?

Потому что первое выражение undefined at `x=2`, даже после algebraic cancellation.
