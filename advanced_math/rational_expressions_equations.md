# Rational Expressions and Equations — рациональные выражения и уравнения

## 1. Заголовок и краткое описание

Rational expressions содержат переменную в знаменателе. На SAT нужно уметь факторизовать, сокращать допустимые множители, находить ограничения domain и решать rational equations без потери логики.

> **Главная идея:** сначала найди запрещённые значения, потом упрощай.

---

## 2. Ключевые понятия и формулы

| Понятие | Смысл |
|---|---|
| rational expression | отношение двух polynomial expressions |
| domain restriction | знаменатель не может быть 0 |
| LCD | least common denominator |
| extraneous solution | значение, появившееся при преобразованиях, но не подходящее исходному уравнению |

Пример:

```math
\frac{x^2-9}{x-3}=\frac{(x-3)(x+3)}{x-3}=x+3,
```

но только при

```math
x\ne3.
```

### Визуальный якорь

**Сокращаем множители, не слагаемые.**

Нельзя сокращать `x` в `(x+2)/x`.

---

## 3. Пошаговый разбор — Guided Example

### Задача

Solve:

```math
\frac{3}{x-1}=\frac{6}{x+2}.
```

### Шаг 1. Ограничения

```math
x\ne1,\quad x\ne-2.
```

Почему сначала? Эти значения никогда не могут быть ответами.

### Шаг 2. Cross multiplication

```math
3(x+2)=6(x-1).
```

### Шаг 3. Решаем linear equation

```math
3x+6=6x-6
```

```math
12=3x
```

```math
x=4.
```

### Шаг 4. Проверяем restriction

`4` не запрещено, значит решение допустимо.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

For which value is `5/(x-7)` undefined?

**A)** -7  **B)** 0  **C)** 5  **D)** 7

### Problem 2 — Easy — Multiple Choice

Simplify `(x²-16)/(x-4)` for `x≠4`.

**A)** `x-4`  **B)** `x+4`  **C)** `x²+4`  **D)** `1`

### Problem 3 — Medium — Grid-in

Solve `2/x = 6/9`.

### Problem 4 — Medium — Multiple Choice

Which is the least common denominator of `1/x` and `1/(x+2)`?

**A)** `2x`  **B)** `x+2`  **C)** `x(x+2)`  **D)** `x²+2`

### Problem 5 — Hard — Grid-in

Solve

```math
\frac{x+1}{x-2}=2.
```

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **D**, denominator zero at 7.  
2. **B**, difference of squares.  
3. **3**, `18=6x`.  
4. **C**.  
5. **5**, `x+1=2x-4`, значит `x=5`.

</details>

---

## 5. Common Traps — типичные ловушки

- Забыть domain restriction после сокращения.
- Сокращать отдельные terms вместо factors.
- Не проверить solution, если при решении умножали на выражение с переменной.

---

## 6. Стратегия для Digital SAT

Desmos может решить rational equation через пересечение двух графиков. Но обязательно проверьте, не находится ли найденная x-coordinate в точке, где исходный denominator равен нулю.

---

## 7. Связи с другими темами

**Опирается на:** factoring, equivalent expressions, linear equations.  
**Связано с:** nonlinear equations, asymptotic behavior, domain questions.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я нахожу domain restrictions.
- [ ] Я сокращаю только factors.
- [ ] Я решаю rational equations через LCD/cross multiplication.
- [ ] Я проверяю ответы в исходном уравнении.
