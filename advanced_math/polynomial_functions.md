# Polynomial Functions — полиномы и полиномиальные функции

## 1. Заголовок и краткое описание

Polynomial questions на SAT проверяют работу со степенями, коэффициентами, zeros, factorization и структурой выражений. Чаще всего встречаются квадратичные полиномы, но навыки распространяются и на выражения более высокой степени.

> **Главная идея:** если `f(r)=0`, то `(x-r)` — фактор полинома.

---

## 2. Ключевые понятия и формулы

| Понятие | Смысл |
|---|---|
| polynomial | сумма членов `a_n x^n` с целыми неотрицательными степенями |
| degree | наибольшая степень переменной |
| leading coefficient | коэффициент при члене наибольшей степени |
| zero / root | значение `x`, при котором `f(x)=0` |
| factor theorem | `f(r)=0` ⇔ `(x-r)` является фактором |
| remainder theorem | остаток при делении на `(x-r)` равен `f(r)` |

### Операции

```math
(x+2)(x+5)=x^2+7x+10
```

```math
x^3\cdot x^2=x^5
```

### Визуальный якорь

**Root `r` ↔ factor `(x-r)` ↔ x-intercept `(r,0)`.**

---

## 3. Пошаговый разбор — Guided Example

### Задача

For

```math
f(x)=x^3-4x^2-x+4,
```

show that `x=1` is a zero and factor the polynomial completely.

### Шаг 1. Проверяем zero

```math
f(1)=1-4-1+4=0.
```

По factor theorem `(x-1)` — фактор.

### Шаг 2. Используем grouping

```math
x^3-4x^2-x+4=x^2(x-4)-1(x-4).
```

### Шаг 3. Выносим общий binomial

```math
=(x^2-1)(x-4).
```

### Шаг 4. Difference of squares

```math
x^2-1=(x-1)(x+1).
```

Итог:

```math
f(x)=(x-1)(x+1)(x-4).
```

Zeros: `-1`, `1`, `4`.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

What is the degree of `4x^5-2x^2+7`?

**A)** 2  **B)** 4  **C)** 5  **D)** 7

### Problem 2 — Easy — Grid-in

If `(x-3)` is a factor of `f(x)`, what is `f(3)`?

### Problem 3 — Medium — Multiple Choice

Which is a factor of `x²-7x+12`?

**A)** `x+3`  **B)** `x-3`  **C)** `x+4`  **D)** `x-12`

### Problem 4 — Medium — Grid-in

For `f(x)=x³-2x+5`, what is the remainder when divided by `(x-2)`?

### Problem 5 — Hard — Multiple Choice

If `x²+kx+18=(x+3)(x+6)`, what is `k`?

**A)** 3  **B)** 9  **C)** 18  **D)** 24

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **C**, degree 5.  
2. **0**, по factor theorem.  
3. **B**, `x²-7x+12=(x-3)(x-4)`.  
4. **9**, потому что `f(2)=8-4+5=9`.  
5. **B**, раскрытие даёт `x²+9x+18`.

</details>

---

## 5. Common Traps — типичные ловушки

- Root `3` соответствует фактору `(x-3)`, а не `(x+3)`.
- Degree определяется степенью, а не величиной коэффициента.
- При умножении степеней одинакового основания показатели складываются; при сложении членов — нет.

---

## 6. Стратегия для Digital SAT

Desmos быстро показывает zeros графика `y=f(x)`. Но если вопрос спрашивает factor или coefficient, algebraic structure обычно быстрее. Для проверки factor подставьте соответствующий root: если результат 0, фактор подходит.

---

## 7. Связи с другими темами

**Опирается на:** exponent rules, equivalent expressions, quadratics.  
**Дальше:** nonlinear functions, rational expressions, systems with nonlinear equations.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я нахожу degree и leading coefficient.
- [ ] Я связываю zero с factor.
- [ ] Я использую factor/remainder theorem.
- [ ] Я умею раскрывать и факторизовать polynomial expressions.
