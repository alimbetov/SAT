# Two-Variable Data — models, scatterplots, and regression

## 1. Заголовок и краткое описание

Two-variable data — официальный skill Problem-Solving and Data Analysis. На SAT нужно читать scatterplots, определять association, использовать residuals и выбирать подходящую **linear, quadratic или exponential model** для данных.

> **Главная идея:** scatterplot показывает pattern двух переменных; задача — распознать форму pattern и выбрать модель, которая её объясняет.

---

## 2. Ключевые понятия и формулы

| Понятие | Смысл |
|---|---|
| positive association | `x` растёт → `y` в среднем растёт |
| negative association | `x` растёт → `y` в среднем уменьшается |
| no clear association | устойчивого trend нет |
| line/curve of best fit | модель общего pattern |
| predicted value | значение, которое даёт model |
| residual | `observed - predicted` |
| linear model | примерно constant additive change |
| exponential model | примерно constant multiplicative / percent change |
| quadratic model | curved pattern с turning point |

### Residual

```math
residual=y_{observed}-y_{predicted}
```

- positive residual → point выше model;
- negative residual → point ниже model.

### Как выбрать модель

**Linear:** точки идут примерно вдоль прямой.  
**Exponential:** рост/decay ускоряется multiplicatively.  
**Quadratic:** U-shape или inverted-U pattern.

### Визуальный якорь

**Straight → linear. Constant percent → exponential. One turn → quadratic.**

---

## 3. Пошаговый разбор — Guided Example

A line of best fit for hours studied `x` and score `y` is

```math
y=4.5x+62.
```

A student studied 6 hours and scored 86. Find and interpret the residual.

### Шаг 1. Predicted score

```math
4.5(6)+62=89.
```

### Шаг 2. Residual

```math
86-89=-3.
```

### Шаг 3. Интерпретация

Observed score на 3 points ниже prediction.

### Шаг 4. Что означал бы pattern residuals?

Если residuals случайно распределены вокруг 0, model может быть разумной. Если residuals образуют заметную curve, linear model, вероятно, не отражает pattern и стоит рассмотреть nonlinear model.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

If points generally rise from left to right, the association is:

**A)** positive  **B)** negative  **C)** none  **D)** impossible

### Problem 2 — Easy — Grid-in

For `y=3x+10`, what value is predicted when `x=5`?

### Problem 3 — Medium — Multiple Choice

A scatterplot forms a clear U-shaped pattern. Which type of model is most plausible?

**A)** constant  **B)** linear  **C)** quadratic  **D)** no model can ever be used

### Problem 4 — Medium — Multiple Choice

A quantity increases by roughly the same percentage for each equal increase in `x`. Which model is most appropriate?

**A)** linear  **B)** exponential  **C)** constant  **D)** random

### Problem 5 — Hard — Grid-in

A model `y=12-0.8x` predicts a value for `x=5`. If the observed value is 10, what is the residual?

<details>
<summary><strong>Ответы и краткие решения</strong></summary>

1. **A**.  
2. **25**.  
3. **C**, U-shape suggests quadratic behavior.  
4. **B**, constant percent/multiplicative change suggests exponential.  
5. **2**: predicted `8`; residual `10-8=2`.

</details>

---

## 5. Common Traps — типичные ловушки

### Ловушка 1. Residual с неправильным знаком

Всегда:

```math
observed-predicted.
```

### Ловушка 2. Выбирать linear model просто потому, что знакома формула `y=mx+b`

Смотрите на pattern. Curve требует nonlinear candidate.

### Ловушка 3. Correlation = causation

Даже сильная association не доказывает cause-and-effect.

---

## 6. Стратегия для Digital SAT

Desmos особенно полезен для regression. После ввода lists `x1` и `y1` можно сравнивать модели, например:

```text
y1 ~ mx1+b
```

или nonlinear regression, если формат задачи это допускает.

Главное — не выбирать model только по красивому графику. Сверяйте context: additive change чаще linear, multiplicative/percent change чаще exponential.

---

## 7. Связи с другими темами

**Опирается на:** linear functions, quadratics, exponential functions, one-variable statistics.  
**Связано с:**
- `observational_studies_experiments.md`;
- model interpretation;
- residual analysis.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я определяю direction and shape of association.
- [ ] Я выбираю linear/quadratic/exponential model по pattern.
- [ ] Я вычисляю и интерпретирую residual.
- [ ] Я не путаю statistical association с causation.
