# Equivalent Expressions — эквивалентные выражения

## 1. Заголовок и краткое описание

**Equivalent expressions** — официальный skill домена Advanced Math. На SAT нужно узнавать одинаковые выражения в разных формах, раскрывать скобки, факторизовать, сокращать дроби и использовать структуру выражения для быстрого решения.

> **Главная идея:** форма меняется, значение — нет.

---

## 2. Ключевые понятия и формулы

| Приём | Правило | Пример |
|---|---|---|
| distributive property | `a(b+c)=ab+ac` | `3(x+2)=3x+6` |
| factoring | `ab+ac=a(b+c)` | `6x+12=6(x+2)` |
| difference of squares | `a²-b²=(a-b)(a+b)` | `x²-9=(x-3)(x+3)` |
| square of sum | `(a+b)²=a²+2ab+b²` | `(x+4)²=x²+8x+16` |
| square of difference | `(a-b)²=a²-2ab+b²` | `(x-5)²=x²-10x+25` |
| exponent product | `a^m a^n=a^(m+n)` | `x²x³=x⁵` |

### Визуальный якорь

**Expand** = «распаковать».  
**Factor** = «упаковать».

Это обратные процессы.

### Быстрый вопрос

Какое выражение удобнее для поиска zeros: `x²-5x+6` или `(x-2)(x-3)`? Почему?

---

## 3. Пошаговый разбор — Guided Example

### Задача

Which expression is equivalent to

```math
3x^2-12x+12?
```

### Шаг 1. Ищем общий множитель

Все члены делятся на `3`:

```math
3(x^2-4x+4).
```

Почему начинаем с GCF? Он упрощает структуру и позволяет увидеть знакомый шаблон.

### Шаг 2. Распознаём perfect square

```math
x^2-4x+4=(x-2)^2.
```

Потому что `4=2²`, а средний член равен `-2·x·2=-4x`.

### Шаг 3. Записываем итог

```math
3(x-2)^2.
```

### Шаг 4. Проверяем обратным раскрытием

```math
3(x^2-4x+4)=3x^2-12x+12.
```

Форма изменилась, значение осталось тем же.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

Which expression is equivalent to `4(x+3)-2x`?

**A)** `2x+3`  
**B)** `2x+12`  
**C)** `6x+12`  
**D)** `2x+6`

### Problem 2 — Easy — Multiple Choice

Which is equivalent to `x²-16`?

**A)** `(x-4)²`  
**B)** `(x-4)(x+4)`  
**C)** `(x-8)(x+2)`  
**D)** `(x+4)²`

### Problem 3 — Medium — Grid-in

If

```math
2x^2+10x=2x(x+k),
```

what is `k`?

### Problem 4 — Medium — Multiple Choice

Which expression is equivalent to

```math
\frac{x^2-25}{x-5}
```

for `x≠5`?

**A)** `x-5`  
**B)** `x+5`  
**C)** `x²+5`  
**D)** `1`

### Problem 5 — Hard — Grid-in

If

```math
(x+a)^2=x^2+14x+49,
```

what is the positive value of `a`?

<details>
<summary><strong>Ответы и краткие решения</strong></summary>

1. **B.** `4x+12-2x=2x+12`.  
2. **B.** Difference of squares.  
3. **5.** `2x²+10x=2x(x+5)`.  
4. **B.** `(x²-25)=(x-5)(x+5)`, затем сокращаем.  
5. **7.** В `(x+a)²=x²+2ax+a²`, поэтому `2a=14`.

</details>

---

## 5. Common Traps — типичные ловушки

### Ловушка 1. Ошибка в квадрате суммы

Неверно:

```math
(a+b)^2=a^2+b^2
```

Правильно:

```math
(a+b)^2=a^2+2ab+b^2.
```

### Ловушка 2. Незаконное сокращение

В дроби можно сокращать **множители**, а не отдельные слагаемые.

### Ловушка 3. Потерять ограничение domain

После сокращения `(x-5)` исходное выражение всё равно не определено при `x=5`.

---

## 6. Стратегия для Digital SAT

Desmos полезен для **проверки** эквивалентности: постройте два выражения как `y=`. Если графики полностью совпадают, это сильная проверка.

Но основной SAT-навык здесь — видеть структуру вручную. Factoring и special products часто быстрее калькулятора.

---

## 7. Связи с другими темами

**Опирается на:** distributive property, exponent rules, linear algebra.

**Дальше используется в:**
- `quadratics.md`;
- `rational_expressions_equations.md`;
- `radicals_and_radical_equations.md`;
- `nonlinear_equations_systems.md`.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я умею раскрывать и выносить множитель.
- [ ] Я узнаю difference of squares и perfect-square trinomial.
- [ ] Я умею безопасно сокращать rational expressions.
- [ ] Я могу выбрать форму выражения, которая делает задачу проще.
