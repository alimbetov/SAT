# One-Variable Data — distributions, center, and spread

## 1. Заголовок и краткое описание

One-variable data — официальный skill Problem-Solving and Data Analysis. На SAT нужно интерпретировать distributions и сравнивать mean, median, range, interquartile range и standard deviation.

> **Главная идея:** center отвечает «где данные находятся», spread — «насколько они разбросаны».

---

## 2. Ключевые понятия и формулы

| Понятие | Смысл |
|---|---|
| mean | сумма / количество |
| median | центральное значение после сортировки |
| mode | наиболее частое значение |
| range | `max-min` |
| IQR | `Q3-Q1` |
| standard deviation | мера разброса вокруг mean |
| outlier | значение, заметно удалённое от остальных |

### Что устойчиво к outliers?

- mean — чувствителен;
- median — более устойчив;
- standard deviation — чувствителен;
- IQR — более устойчив.

### Визуальный якорь

**Mean тянется к outlier. Median обычно остаётся ближе к центру основной массы.**

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

### Шаг 3. Сравниваем

Outlier `30` сильно поднял mean, но почти не повлиял на median.

### Шаг 4. Интерпретируем SAT-style

Если удалить `30`, mean резко уменьшится. Median изменится гораздо меньше.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Grid-in

Find the mean of `3, 5, 7, 9`.

### Problem 2 — Easy — Multiple Choice

What is the median of `2, 4, 8, 10, 20`?

**A)** 4  **B)** 8  **C)** 10  **D)** 20

### Problem 3 — Medium — Multiple Choice

A very large outlier is added to a data set. Which measure is generally affected most?

**A)** median  **B)** mean  **C)** number of values below median  **D)** position of middle observation only

### Problem 4 — Medium — Grid-in

The mean of five numbers is 12. What is their total sum?

### Problem 5 — Hard — Multiple Choice

Two data sets have the same mean. Set A has values tightly clustered around the mean; Set B has values much more spread out. Which statement is true?

**A)** A has larger standard deviation  
**B)** B has larger standard deviation  
**C)** they must have equal standard deviation  
**D)** standard deviation depends only on mean

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **6**.  
2. **B**, middle value 8.  
3. **B**, mean is sensitive to outliers.  
4. **60**, because sum=`mean·count`.  
5. **B**, greater spread → larger standard deviation.

</details>

---

## 5. Common Traps — типичные ловушки

- Искать median без предварительной сортировки.
- Путать range и standard deviation.
- Считать, что одинаковый mean означает одинаковое distribution.

---

## 6. Стратегия для Digital SAT

Не тратьте время на ручное вычисление сложного standard deviation, если вопрос качественный. SAT часто спрашивает, какой набор имеет больший spread. Desmos позволяет вводить списки и вычислять summary statistics, но сначала прочитайте, что именно сравнивается.

---

## 7. Связи с другими темами

**Опирается на:** arithmetic, fractions, percentages.  
**Связано с:** two-variable data, sampling, margin of error, statistical claims.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я нахожу mean и median.
- [ ] Я понимаю влияние outliers.
- [ ] Я различаю center и spread.
- [ ] Я сравниваю distributions по standard deviation/IQR концептуально.
