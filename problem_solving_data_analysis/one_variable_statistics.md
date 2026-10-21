# One-Variable Data — distributions, center, spread, and data displays

## 1. Заголовок и краткое описание

One-variable data — официальный skill Problem-Solving and Data Analysis. На SAT нужно интерпретировать **frequency tables, histograms, dot plots и box plots**, сравнивать distributions и работать с mean, median, range, IQR, outliers и standard deviation.

> **Главная идея:** center отвечает «где данные находятся», spread — «насколько они разбросаны», а график показывает форму distribution.

---

## 2. Ключевые понятия и формулы

| Понятие | Смысл |
|---|---|
| mean | сумма / количество |
| median | центральное значение после сортировки |
| mode | наиболее частое значение |
| range | `max-min` |
| quartiles | `Q1`, median=`Q2`, `Q3` |
| IQR | `Q3-Q1` |
| standard deviation | мера разброса вокруг mean |
| outlier | значение, заметно удалённое от основной массы |

### Основные representations

| Представление | Что удобно видеть |
|---|---|
| frequency table | сколько раз встречается значение/интервал |
| dot plot | отдельные значения, clusters, gaps, outliers |
| histogram | shape distribution по intervals/bins |
| box plot | median, quartiles, IQR, общий spread |

### Что устойчиво к outliers?

- mean — чувствителен;
- median — более устойчив;
- standard deviation — чувствителен;
- IQR — более устойчив.

### Shape of distribution

Полезно распознавать:

- symmetric;
- skewed right;
- skewed left;
- clusters;
- gaps;
- outliers.

### Визуальный якорь

**Mean тянется к длинному хвосту и outliers. Median устойчивее.**

---

## 3. Пошаговый разбор — Guided Example

Data set:

```text
4, 5, 5, 6, 30
```

### Шаг 1. Median

Данные уже отсортированы. Центральное значение:

```math
median=5.
```

### Шаг 2. Mean

```math
mean=\frac{4+5+5+6+30}{5}=10.
```

### Шаг 3. Range

```math
range=30-4=26.
```

### Шаг 4. Интерпретируем shape

`30` — far-right value, поэтому distribution имеет сильный right-side outlier. Mean значительно больше median.

### Шаг 5. SAT-style conclusion

Если `30` удалить:

- mean резко уменьшится;
- median изменится гораздо меньше;
- spread/standard deviation уменьшится.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Grid-in

Find the mean of `3, 5, 7, 9`.

### Problem 2 — Easy — Multiple Choice

What is the median of `2, 4, 8, 10, 20`?

**A)** 4  **B)** 8  **C)** 10  **D)** 20

### Problem 3 — Medium — Multiple Choice

Which graph most directly displays median, Q1, and Q3?

**A)** scatterplot  
**B)** box plot  
**C)** line graph  
**D)** circle graph

### Problem 4 — Medium — Grid-in

The mean of five numbers is 12. What is their total sum?

### Problem 5 — Hard — Multiple Choice

Two data sets have the same mean. Set A is tightly clustered around the mean; Set B is much more spread out. Which statement is true?

**A)** A has larger standard deviation  
**B)** B has larger standard deviation  
**C)** they must have equal standard deviation  
**D)** standard deviation depends only on mean

<details>
<summary><strong>Ответы и краткие решения</strong></summary>

1. **6**.  
2. **B**, middle value 8.  
3. **B**, box plot directly shows quartiles and median.  
4. **60**, sum=`mean·count`.  
5. **B**, greater spread → larger standard deviation.

</details>

---

## 5. Common Traps — типичные ловушки

### Ловушка 1. Искать median без сортировки

Median зависит от **position**, поэтому сначала данные должны быть ordered.

### Ловушка 2. Путать histogram и bar chart

Histogram используется для количественных data intervals; соседние bins обычно образуют continuous distribution.

### Ловушка 3. Считать одинаковый mean признаком одинаковых distributions

Одинаковый center не означает одинаковый spread или shape.

---

## 6. Стратегия для Digital SAT

Сначала определите, что можно прочитать **напрямую с графика**, прежде чем считать.

- box plot → quartiles/median;
- dot plot → individual values;
- histogram → shape and frequencies by intervals;
- frequency table → counts.

Desmos умеет вычислять summary statistics для lists, но многие SAT-вопросы концептуальные: «что изменится при добавлении outlier?» или «какой set имеет больший spread?».

---

## 7. Связи с другими темами

**Опирается на:** arithmetic, fractions, percentages.  
**Связано с:**
- `two_variable_data_scatterplots.md`;
- `sampling_margin_of_error.md`;
- `observational_studies_experiments.md`.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я читаю frequency tables, histograms, dot plots и box plots.
- [ ] Я нахожу mean, median, range и IQR.
- [ ] Я понимаю влияние outliers на center и spread.
- [ ] Я сравниваю distributions по shape, center и spread.
