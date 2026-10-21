# Sampling, Inference, and Margin of Error — выборки, выводы и погрешность

## 1. Заголовок и краткое описание

**Inference from sample statistics and margin of error** — официальный SAT skill. Здесь проверяется не сложное вычисление, а статистическое мышление: можно ли обобщать результат выборки на population, насколько точна estimate и как sample size влияет на margin of error.

> **Главная идея:** хорошая выборка должна представлять population; больший random sample обычно даёт более точную estimate.

---

## 2. Ключевые понятия и формулы

| Понятие | Смысл |
|---|---|
| population | вся группа, о которой хотят сделать вывод |
| sample | часть population, реально исследованная |
| random sample | выборка, где элементы population имеют случайный механизм отбора |
| representative sample | выборка, адекватно отражающая population |
| sample statistic | число, рассчитанное по sample |
| margin of error | диапазон неопределённости вокруг estimate |

Если estimate равна `p` с margin of error `m`, разумный interval:

```math
p-m\le true\ value\le p+m.
```

### Sample size

При прочих равных:

> larger random sample → smaller margin of error.

### Визуальный якорь

**Random selection помогает generalization. Large sample помогает precision.**

---

## 3. Пошаговый разбор — Guided Example

A random sample of 500 voters finds that 54% support a proposal. The margin of error is 4 percentage points. What interval is plausible for the population percentage?

### Шаг 1. Определяем estimate

```math
54\%.
```

### Шаг 2. Вычитаем margin

```math
54-4=50.
```

### Шаг 3. Прибавляем margin

```math
54+4=58.
```

### Шаг 4. Интерпретируем

Plausible interval:

```text
50% to 58%
```

Это не означает, что 54% «точно» истинное population value. Это sample-based estimate с неопределённостью.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

A study wants to estimate the average height of all students at a school. What is the population?

**A)** only surveyed students  
**B)** all students at the school  
**C)** only tallest students  
**D)** all schools in the city

### Problem 2 — Easy — Grid-in

An estimate is 62% with a margin of error of 3 percentage points. What is the lower endpoint, in percent?

### Problem 3 — Medium — Multiple Choice

Which sample best supports generalization to all students at a school?

**A)** first 50 students entering the gym  
**B)** 50 volunteers from the chess club  
**C)** a random sample from the full student roster  
**D)** the 50 highest-scoring students

### Problem 4 — Medium — Multiple Choice

Two random samples use the same method. Sample A has 100 people; Sample B has 1,000 people. Which generally has the smaller margin of error?

**A)** A  **B)** B  **C)** always equal  **D)** impossible to compare

### Problem 5 — Hard — Multiple Choice

A survey reports 48% support with a margin of error of 5 percentage points. Which population value is consistent with the interval?

**A)** 39%  **B)** 42%  **C)** 51%  **D)** 56%

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **B**.  
2. **59**.  
3. **C**, random sampling from the target population best supports generalization.  
4. **B**, larger sample generally reduces sampling variability.  
5. **C**, interval is 43%–53%.

</details>

---

## 5. Common Traps — типичные ловушки

- Путать sample с population.
- Считать большой, но biased sample автоматически хорошим.
- Интерпретировать margin of error как процент «ошибочных ответов» респондентов.

---

## 6. Стратегия для Digital SAT

Эти вопросы чаще логические, чем вычислительные. Desmos почти не нужен. Ищите ключевые слова: **random sample**, **representative**, **margin of error**, **generalize**.

При сравнении одинаково организованных surveys обычно выбирайте larger sample как более precise.

---

## 7. Связи с другими темами

**Опирается на:** percentages, one-variable statistics, probability.  
**Связано с:** observational studies, experiments, evaluating statistical claims.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я различаю sample и population.
- [ ] Я понимаю роль random sampling.
- [ ] Я строю interval из estimate ± margin of error.
- [ ] Я понимаю, как sample size влияет на precision.
