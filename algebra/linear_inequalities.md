# Linear Inequalities — линейные неравенства

> **Цель урока:** научиться видеть inequality как **диапазон допустимых значений**, переводить SAT-фразы `at least / at most / no more than` в математические знаки и не забывать переворачивать знак при делении на negative number.

Главная идея:

> **Equation ищет точку. Inequality описывает область или диапазон.**

---

# 1. Pattern Map

| Что вижу | Паттерн | Что делаю |
|---|---|---|
| `3x+5<20` | simple inequality | решаю почти как equation |
| `-4x≥20` | divide by negative | переворачиваю знак |
| `2<x≤7` | compound inequality | держу два ограничения одновременно |
| `at least 18` | language → symbol | `x≥18` |
| `at most 50` | language → symbol | `x≤50` |
| budget / maximum / minimum | constraint model | строю inequality |
| `y>2x+1` | two-variable region | boundary + shading |
| greatest integer satisfying... | endpoint reasoning | найти boundary и выбрать integer |

Перед решением спросите:

> **«Я ищу одно значение или множество допустимых значений?»**

---

# 2. Language Decoder — слова, которые решают половину задачи

| English phrase | Symbol | Русский смысл |
|---|---|---|
| `greater than` | `>` | больше |
| `less than` | `<` | меньше |
| `at least` | `≥` | не меньше / минимум |
| `at most` | `≤` | не больше / максимум |
| `no more than` | `≤` | не более |
| `no less than` | `≥` | не менее |
| `minimum of 10` | `≥10` | как минимум 10 |
| `maximum of 10` | `≤10` | не больше 10 |
| `between 3 and 8` | зависит от включения endpoints | между 3 и 8 |

Эти фразы нужно узнавать автоматически.

---

# 3. PATTERN 1 — Solve like an equation

Большинство операций такие же, как в equation.

Пример:

```math
3x+5<20
```

Вычитаем `5`:

```math
3x<15
```

Делим на positive `3`:

```math
x<5
```

### Что означает ответ?

Не только `4`.

Подходит **любое** число меньше 5:

```text
4, 0, -100, 4.9, ...
```

---

# 4. PATTERN 2 — Negative flips the sign

Критическое правило:

> При умножении или делении обеих частей inequality на negative number знак **переворачивается**.

---

## Почему?

Мы знаем:

```math
2<5
```

Умножим на `-1`:

```math
-2>-5
```

На number line отрицательные числа идут в обратном порядке.

---

## Визуальный якорь

```text
÷ positive → sign stays
÷ negative → sign flips
```

или коротко:

> **Minus turns the arrow around.**

---

## Worked Example 1

```math
-4x\ge20
```

Делим на `-4`:

```math
x\le-5
```

Знак `≥` стал `≤`.

---

## Error Clinic

Неверно:

```math
-2x>8 \Rightarrow x> -4
```

Правильно:

```math
x<-4
```

### Проверка числом

Возьмём `x=-5`:

```math
-2(-5)=10>8
```

Работает.

Возьмём `x=0`:

```math
0>8
```

Не работает.

Значит направление `x<-4` логично.

---

# 5. PATTERN 3 — Endpoints: open или closed

```math
x>3
```

`3` не входит.

```text
open circle
```

```math
x\ge3
```

`3` входит.

```text
closed circle
```

Якорь:

```text
< or >   → endpoint excluded
≤ or ≥   → endpoint included
```

---

# 6. PATTERN 4 — Compound inequalities

Пример:

```math
2<x\le7
```

означает одновременно:

```math
x>2
```

и

```math
x\le7
```

То есть:

```text
2 < x ≤ 7
```

### Визуально

```text
2  ○────────●  7
```

- open at 2;
- closed at 7.

---

## Worked Example

```math
3<2x+1\le11
```

В compound inequality можно выполнять одну операцию со **всем тремя частями**.

Вычитаем `1`:

```math
2<2x\le10
```

Делим на positive `2`:

```math
1<x\le5
```

---

# 7. PATTERN 5 — Budget / capacity word problems

Это один из главных SAT patterns.

Фраза:

> cannot spend more than `$120`

означает:

```math
\text{cost}\le120
```

---

## Worked Example

A student has `$120`.
Calculator costs `$48`.
Each notebook costs `$9`.
What is the greatest number of notebooks the student can buy?

### Step 1 — translate language

```text
cannot spend more than 120
→ total cost ≤ 120
```

### Step 2 — build model

Let `n` = notebooks.

```math
48+9n\le120
```

### Step 3 — solve

```math
9n\le72
```

```math
n\le8
```

### Step 4 — interpret question

Asked for **greatest number**.

So:

```text
8 notebooks
```

---

# 8. PATTERN 6 — Greatest / least integer

Suppose:

```math
x<6.7
```

Question asks greatest integer value of `x`.

Numbers below `6.7` include:

```text
..., 4, 5, 6
```

Greatest integer:

```text
6
```

---

## Important trap

If:

```math
x\le6.7
```

greatest integer is still `6`.

But if:

```math
x\le7
```

greatest integer is `7`, because endpoint is included.

---

# 9. PATTERN 7 — Two-variable inequalities

Example:

```math
y>2x+1
```

Equation

```math
y=2x+1
```

is the **boundary line**.

But inequality includes an entire region.

---

## Boundary rule

```text
< or >   → dashed boundary
≤ or ≥   → solid boundary
```

Why?

If equality is allowed, points on line are included.

---

## Which side to shade?

For:

```math
y>2x+1
```

`y` must be greater than line value → shade **above**.

For:

```math
y<2x+1
```

shade **below**.

---

## Test-point method

If equation is not written conveniently, test `(0,0)` if it is not on boundary.

Example:

```math
2x+y>5
```

Test `(0,0)`:

```math
0>5
```

False.

So shade the side **not containing** `(0,0)`.

---

# 10. Method Selector

```text
Simple inequality?
→ solve like equation

Dividing/multiplying by negative?
→ flip sign

Compound inequality?
→ apply operations to all parts

Word phrase at least/at most?
→ translate phrase before algebra

Greatest/least integer?
→ solve boundary, then inspect integers

Two-variable inequality?
→ draw boundary + decide shading
```

---

# 11. Desmos Strategy

For one-variable inequalities, manual work is usually faster.

But for regions:

```text
y>2x+1
y≤-x+7
```

Desmos immediately shows overlapping feasible region.

This is useful for systems of inequalities and visual questions.

Do not use Desmos for:

```math
3x+5<20
```

That is a few seconds by hand.

---

# 12. Error Clinic

## Error 1 — forget sign flip

If divide by negative, always pause and say:

> «Negative division — arrow flips.»

---

## Error 2 — confuse at least / at most

```text
at least 10 → x ≥ 10
at most 10  → x ≤ 10
```

Use meaning, not memorized word shape.

---

## Error 3 — answer boundary instead of greatest integer

If solution:

```math
x<8.4
```

and asks greatest integer, answer `8`, not `8.4`.

---

## Error 4 — solid line for strict inequality

`>` and `<` exclude equality → dashed boundary.

---

# 13. Guided Practice

## Level A

Solve:

```math
4x-3\le17
```

<details><summary>Solution</summary>

```math
4x\le20
```

```math
x\le5
```

</details>

---

## Level B

Solve:

```math
-3x+2>14
```

Before solving, write:

```text
Will the sign flip? yes / no
Why? __________________
```

<details><summary>Solution</summary>

```math
-3x>12
```

Divide by `-3` → flip:

```math
x<-4
```

</details>

---

## Level C — language

Translate only; do not solve:

> A student must score at least 70 points.

<details><summary>Answer</summary>

```math
s\ge70
```

</details>

---

## Level D — word problem

A concert ticket costs `$30` and each snack costs `$6`. A student can spend at most `$54` total. What is the greatest number of snacks?

<details><summary>Solution</summary>

```math
30+6s\le54
```

```math
6s\le24
```

```math
s\le4
```

Greatest number: `4`.

</details>

---

# 14. SAT-style Practice

## 1 — Easy — Multiple Choice

Solve:

```math
3x+5<20
```

**A)** `x<5`  
**B)** `x>5`  
**C)** `x<15`  
**D)** `x>15`

## 2 — Medium — SPR

If

```math
-4x\ge20,
```

what is the greatest possible integer value of `x`?

## 3 — Medium — Multiple Choice

Which inequality means "x is at least 12"?

**A)** `x>12`  
**B)** `x≥12`  
**C)** `x<12`  
**D)** `x≤12`

## 4 — Medium — SPR

Solve:

```math
5<2x+1\le13
```

What is the greatest integer `x` satisfying the compound inequality?

## 5 — Hard — Multiple Choice

A store has a budget of `$200`. A fixed setup fee is `$35`, and each item costs `$11`. Which inequality models the maximum number `n` of items?

**A)** `35+11n≥200`  
**B)** `35+11n≤200`  
**C)** `11+35n≤200`  
**D)** `35n≤200`

## 6 — Hard — Multiple Choice

For the inequality

```math
y\ge-2x+3,
```

which statement is true?

**A)** dashed boundary, shade below  
**B)** dashed boundary, shade above  
**C)** solid boundary, shade above  
**D)** solid boundary, shade below

<details>
<summary><strong>Answers</strong></summary>

1. **A** — `3x<15 → x<5`.
2. **`-5`** — `x≤-5`; greatest integer is `-5`.
3. **B**.
4. `5<2x+1≤13 → 4<2x≤12 → 2<x≤6`; greatest integer `6`.
5. **B** — cannot exceed budget.
6. **C** — `≥` includes boundary and `y greater` means above.

</details>

---

# 15. Transfer Questions

1. Почему inequality solution обычно не одно число?
2. Почему negative multiplication меняет order?
3. Как различить `at least` и `at most` смыслом?
4. Что значит open vs closed endpoint?
5. Как boundary line связана с two-variable inequality?
6. Когда нужно искать greatest integer, а не просто boundary value?
7. Когда Desmos полезен для inequalities?

---

# 16. Checklist

- [ ] Я перевожу verbal constraints в `> < ≥ ≤`.
- [ ] Я решаю simple inequalities.
- [ ] Я всегда flip sign при умножении/делении на negative.
- [ ] Я понимаю open/closed endpoints.
- [ ] Я решаю compound inequalities.
- [ ] Я строю budget/capacity models.
- [ ] Я нахожу greatest/least integer solutions.
- [ ] Я понимаю boundary + shading для two-variable inequalities.
- [ ] Я умею использовать test point.
- [ ] Я могу объяснить, почему выбранный знак inequality правильный.
