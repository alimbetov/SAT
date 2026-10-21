# Radicals and Radical Equations — корни и уравнения с радикалами

## 1. Заголовок и краткое описание

Radical expressions и radical equations относятся к Advanced Math. На SAT проверяются упрощение корней, связь radical/exponent forms, решение уравнений и обязательная проверка на **extraneous solutions**.

> **Главная идея:** возведение в квадрат помогает убрать корень, но может создать лишний ответ.

---

## 2. Ключевые понятия и формулы

| Правило | Формула |
|---|---|
| product rule | `√(ab)=√a·√b` для допустимых значений |
| fractional exponent | `a^(1/2)=√a` |
| nth root | `a^(1/n)=ⁿ√a` |
| power of root | `a^(m/n)=ⁿ√(a^m)` |
| square | `(√a)²=a` для `a≥0` |

Пример:

```math
\sqrt{72}=\sqrt{36\cdot2}=6\sqrt2.
```

### Визуальный якорь

Ищите внутри radical **самый большой perfect-square factor**.

### Вопрос к читателю

Почему после squaring both sides нужно обязательно вернуть найденное значение в исходное уравнение?

---

## 3. Пошаговый разбор — Guided Example

Solve:

```math
\sqrt{x+5}=x-1.
```

### Шаг 1. Замечаем ограничение

Левая часть неотрицательна, поэтому правая тоже должна быть неотрицательной:

```math
x-1\ge0\Rightarrow x\ge1.
```

### Шаг 2. Возводим обе части в квадрат

```math
x+5=(x-1)^2.
```

### Шаг 3. Получаем quadratic equation

```math
x+5=x^2-2x+1
```

```math
x^2-3x-4=0
```

```math
(x-4)(x+1)=0.
```

Candidates: `x=4` и `x=-1`.

### Шаг 4. Проверяем исходное уравнение

`x=4`:

```math
\sqrt9=3=4-1.
```

Подходит.

`x=-1` нарушает `x≥1` и исходное равенство. Это extraneous solution.

**Ответ: `4`.**

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

Simplify `√50`.

**A)** `5√2`  **B)** `10√5`  **C)** `25√2`  **D)** `2√25`

### Problem 2 — Easy — Multiple Choice

Which is equivalent to `x^(1/2)` for `x≥0`?

**A)** `x/2`  **B)** `2x`  **C)** `√x`  **D)** `x²`

### Problem 3 — Medium — Grid-in

Solve `√(x+1)=5`.

### Problem 4 — Medium — Multiple Choice

Which expression equals `∛(x²)`?

**A)** `x^(2/3)`  **B)** `x^(3/2)`  **C)** `x²/3`  **D)** `x^6`

### Problem 5 — Hard — Grid-in

Solve `√(2x+3)=x` for the valid real solution.

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **A**, `√50=√25·√2=5√2`.  
2. **C**.  
3. **24**, `x+1=25`.  
4. **A**.  
5. **3**, после squaring: `2x+3=x²` → `(x-3)(x+1)=0`; `-1` не подходит исходному уравнению.

</details>

---

## 5. Common Traps — типичные ловушки

- Ошибочно писать `√(a+b)=√a+√b`.
- Забывать ограничения domain для even roots.
- Не проверять candidates после squaring.

---

## 6. Стратегия для Digital SAT

Desmos удобно использовать для radical equations: постройте обе стороны как функции и найдите intersections. Это особенно полезно для проверки extraneous solutions, но algebraic reasoning всё равно нужно для понимания domain.

---

## 7. Связи с другими темами

**Опирается на:** exponents, quadratics, equivalent expressions.  
**Связано с:** nonlinear equations, geometry distance formulas, right triangles.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я упрощаю radicals.
- [ ] Я перевожу между radical и fractional exponent forms.
- [ ] Я решаю radical equations.
- [ ] Я проверяю extraneous solutions.
