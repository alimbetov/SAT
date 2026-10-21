# Two-Variable Data — models and scatterplots

## 1. Заголовок и краткое описание

Two-variable data — официальный skill Problem-Solving and Data Analysis. На SAT нужно читать scatterplots, определять association, использовать line of best fit и интерпретировать slope, intercept и residuals в контексте данных.

> **Главная идея:** scatterplot показывает связь между двумя количественными переменными, но связь сама по себе не доказывает причинность.

---

## 2. Ключевые понятия и формулы

| Понятие | Смысл |
|---|---|
| positive association | `x` растёт → `y` в среднем растёт |
| negative association | `x` растёт → `y` в среднем уменьшается |
| no clear association | устойчивого тренда нет |
| line of best fit | линия, описывающая общий trend |
| predicted value | значение модели |
| residual | `observed - predicted` |
| slope | изменение predicted `y` на единицу `x` |

### Residual

```math
residual=y_{observed}-y_{predicted}
```

- positive residual → точка выше модели;
- negative residual → точка ниже модели.

### Визуальный якорь

**Trend ≠ cause.** Корреляция может быть сильной и всё равно не доказывать причинно-следственную связь.

---

## 3. Пошаговый разбор — Guided Example

A line of best fit for hours studied `x` and test score `y` is

```math
y=4.5x+62.
```

A student studied 6 hours and scored 86. Find and interpret the residual.

### Шаг 1. Находим predicted score

```math
y=4.5(6)+62=89.
```

### Шаг 2. Вычисляем residual

```math
86-89=-3.
```

### Шаг 3. Интерпретируем

Фактический score оказался на 3 points **ниже**, чем предсказывает модель.

Почему знак важен? Потому что он показывает направление ошибки prediction.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

If points generally rise from left to right, the association is:

**A)** positive  **B)** negative  **C)** none  **D)** impossible

### Problem 2 — Easy — Grid-in

For `y=3x+10`, what value is predicted when `x=5`?

### Problem 3 — Medium — Multiple Choice

A model predicts 42, but the observed value is 47. What is the residual?

**A)** -5  **B)** 0  **C)** 5  **D)** 89

### Problem 4 — Medium — Multiple Choice

The slope of a best-fit line is `2.4`. Which interpretation is best?

**A)** `y` is always 2.4  
**B)** predicted `y` increases about 2.4 for each 1-unit increase in `x`  
**C)** `x` causes `y` to increase by 2.4  
**D)** intercept is 2.4

### Problem 5 — Hard — Grid-in

A model `y=12-0.8x` predicts a value for `x=5`. If the observed value is 10, what is the residual?

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **A**.  
2. **25**.  
3. **C**, `47-42=5`.  
4. **B**.  
5. **2**: predicted `8`; residual `10-8=2`.

</details>

---

## 5. Common Traps — типичные ловушки

- Вычислять residual как predicted − observed вместо observed − predicted.
- Интерпретировать slope без units/context.
- Делать causal conclusion только на основании scatterplot.

---

## 6. Стратегия для Digital SAT

Desmos умеет regression. Для введённых списков `x1` и `y1` можно использовать линейную регрессию вида `y1~mx1+b`. На SAT это полезно, когда требуется модель по таблице данных. Но для готовой best-fit equation обычно быстрее просто подставить значение.

---

## 7. Связи с другими темами

**Опирается на:** linear functions, slope, one-variable statistics.  
**Связано с:** observational studies, experiments, statistical claims.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я определяю направление association.
- [ ] Я интерпретирую slope и intercept модели.
- [ ] Я вычисляю и интерпретирую residual.
- [ ] Я не путаю correlation с causation.
