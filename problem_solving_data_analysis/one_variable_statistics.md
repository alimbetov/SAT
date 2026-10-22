# One-Variable Data — distributions, center, spread, and data displays

## 1. Зачем эта тема нужна на SAT

One-variable data — официальный skill **Problem-Solving and Data Analysis**. На SAT здесь проверяется не столько арифметика, сколько умение **читать distribution**: где находится center, насколько данные spread out, есть ли skew/outliers и какой summary statistic уместен.

Ученик должен научиться смотреть на data display и сначала думать:

```text
SHAPE → CENTER → SPREAD → OUTLIERS
```

а уже потом считать.

> **Главная идея:** одинаковый mean не означает одинаковые данные. Distribution описывается одновременно формой, центром и разбросом.

---

## 2. Pattern Map — что искать в данных

| Что спрашивают | Pattern | Что смотреть |
|---|---|---|
| typical value | center | mean или median |
| middle ordered value | median | position |
| overall spread | range / standard deviation | distance from center |
| middle 50% spread | IQR | `Q3-Q1` |
| effect of extreme value | outlier | mean/SD more sensitive |
| compare two sets | distribution comparison | shape + center + spread |
| read quartiles | box plot | Q1, median, Q3 |
| see clusters/gaps | dot plot/histogram | shape |

### Pattern 1. Mean vs median

#### Mean

```math
mean=\frac{sum}{count}
```

Mean uses **every value**, so extreme values pull it.

#### Median

Median = middle position after sorting.

Median depends mainly on **order**, not magnitude of extremes.

> **Memory anchor:** `mean moves`, `median resists`.

### Pattern 2. Right skew / left skew

For a right-skewed distribution:

```text
long tail → right
mean pulled → right
```

Usually:

```math
mean>median
```

For left-skewed distribution, usually:

```math
mean<median
```

### Pattern 3. Spread

| Measure | Что измеряет | Sensitive to outliers? |
|---|---|---|
| range | max-min | yes |
| IQR | spread middle 50% | less sensitive |
| standard deviation | typical distance from mean | yes |

### Pattern 4. Standard deviation

Не нужно вручную вычислять сложную SD на SAT в большинстве задач. Важно понимать смысл:

```text
points tightly clustered → small SD
points widely spread → large SD
```

Если к каждому значению прибавить 10:

- mean +10;
- median +10;
- SD stays same;
- IQR stays same.

Если каждое значение умножить на 3:

- mean ×3;
- median ×3;
- SD ×3;
- IQR ×3.

### Pattern 5. Data displays

#### Dot plot

Лучше всего показывает:

- individual values;
- repeated values;
- clusters;
- gaps;
- outliers.

#### Histogram

Лучше показывает:

- frequencies by intervals/bins;
- overall shape;
- skew;
- clusters.

Но individual exact values могут быть неизвестны.

#### Box plot

Показывает five-number structure:

```text
min — Q1 — median — Q3 — max
```

и:

```math
IQR=Q3-Q1
```

### Pattern 6. Weighted/frequency mean

Если value встречается несколько раз, нельзя усреднять только distinct values.

Example:

| score | frequency |
|---:|---:|
| 70 | 2 |
| 80 | 3 |
| 90 | 1 |

Mean:

```math
\frac{70(2)+80(3)+90(1)}{2+3+1}
```

---

## 3. Guided Learning — как читать distribution до вычислений

### Decision Tree

```text
Есть extreme value/outlier?
    │
    ├─ Да → mean и SD сильно реагируют
    │       median/IQR устойчивее
    │
    └─ Нет

Спрашивают "typical"?
    │
    ├─ symmetric/no outliers → mean часто хорош
    └─ skew/outliers → median часто лучше

Сравнивают два sets?
    → shape + center + spread
```

### Worked Example 1 — outlier changes mean

Data:

```text
4, 5, 5, 6, 30
```

#### Step 1. Shape

`30` далеко справа → right-side outlier.

#### Step 2. Median

Middle value:

```math
median=5
```

#### Step 3. Mean

```math
mean=\frac{4+5+5+6+30}{5}=10
```

#### Interpretation

Mean = 10, median = 5.

Это не случайность: outlier 30 тянет mean вправо.

> Если задача спрашивает «representative center», median здесь обычно лучше.

---

### Worked Example 2 — remove outlier

Remove 30:

```text
4,5,5,6
```

Mean:

```math
\frac{20}{4}=5
```

Median:

```math
\frac{5+5}{2}=5
```

Effect:

- mean: `10 → 5` big change;
- median: `5 → 5` no change;
- spread decreases strongly.

### Pattern conclusion

```text
remove high outlier
→ mean usually decreases
→ SD usually decreases
→ median often changes little
```

---

### Worked Example 3 — same mean, different spread

Set A:

```text
9, 10, 10, 10, 11
```

Set B:

```text
0, 5, 10, 15, 20
```

Both means = 10.

Но Set B намного шире spread.

Therefore:

```text
SD(B) > SD(A)
```

> SAT часто не требует считать SD — только сравнить.

---

### Worked Example 4 — mean from frequency table

| value | frequency |
|---:|---:|
| 2 | 3 |
| 5 | 2 |
| 8 | 1 |

Total count:

```math
3+2+1=6
```

Total sum:

```math
2(3)+5(2)+8(1)=24
```

Mean:

```math
24/6=4
```

> Frequency table = compressed data set. Multiply first, then divide by total frequency.

---

### Worked Example 5 — box plot reasoning

Suppose:

```text
Q1=12, median=18, Q3=25
```

Then:

```math
IQR=25-12=13
```

Interpretation:

Middle 50% of data lies between 12 and 25.

Do **not** say that 50% of data equals 13. `13` is a distance/spread, not a count.

---

### Worked Example 6 — shift vs scale

Original set has:

```text
mean=20, SD=4
```

Add 7 to every value:

```text
new mean = 27
new SD = 4
```

Why SD unchanged?

Relative distances between points remain exactly the same.

Now multiply every value by 2:

```text
new mean = 40
new SD = 8
```

All distances double.

---

## 4. Practice Ladder

### A. Recognition Drill

For each prompt, identify what concept matters most.

1. `One value is far above all others.` → `__________`  
2. `Two sets have same mean but one is more spread.` → `__________`  
3. `Need Q1, median, Q3 directly.` → `__________`  
4. `Distribution has long right tail.` → compare `__________` and `__________`

<details>
<summary><strong>Answers</strong></summary>

1. outlier  
2. standard deviation/spread  
3. box plot  
4. mean and median

</details>

### B. Faded Example

Data:

```text
2, 4, 4, 5, 25
```

Median:

```math
\boxed{\phantom{4}}
```

Mean:

```math
\frac{2+4+4+5+25}{5}=\boxed{\phantom{8}}
```

Which is more affected by 25? `__________`

<details>
<summary><strong>Solution</strong></summary>

Median = 4. Mean = 8. Mean is more affected by the outlier.

</details>

### C. SAT-style Independent Practice

#### Problem 1 — Easy — Grid-in

Find the mean of `3, 5, 7, 9`.

#### Problem 2 — Easy — Multiple Choice

What is the median of `2, 4, 8, 10, 20`?

**A)** 4  
**B)** 8  
**C)** 10  
**D)** 20

#### Problem 3 — Medium — Multiple Choice

Which graph most directly displays median, Q1, and Q3?

**A)** scatterplot  
**B)** box plot  
**C)** line graph  
**D)** circle graph

#### Problem 4 — Medium — Grid-in

The mean of five numbers is 12. What is their total sum?

#### Problem 5 — Hard — Multiple Choice

Two data sets have the same mean. Set A is tightly clustered around the mean; Set B is much more spread out. Which statement is true?

**A)** A has larger standard deviation  
**B)** B has larger standard deviation  
**C)** they must have equal standard deviation  
**D)** standard deviation depends only on mean

#### Problem 6 — Hard Transfer — Multiple Choice

Every value in a data set is increased by 50. Which quantity must remain unchanged?

**A)** mean  
**B)** median  
**C)** standard deviation  
**D)** maximum

<details>
<summary><strong>Ответы и решения</strong></summary>

1. **6**. `(3+5+7+9)/4=6`.  
2. **B.** Middle ordered value is 8.  
3. **B.** Box plot.  
4. **60.** `sum=mean·count=12·5`.  
5. **B.** More spread → larger SD.  
6. **C.** Adding same constant shifts center but does not change distances between observations.

</details>

---

## 5. Error Clinic — частые логические ошибки

### Ошибка 1. Median without sorting

Data:

```text
10, 2, 8, 4, 6
```

Нельзя брать третье записанное число 8.

Sort:

```text
2,4,6,8,10
```

Median = 6.

---

### Ошибка 2. Same mean = same distribution

Два sets могут иметь:

- same mean;
- different SD;
- different range;
- different shape.

Mean описывает только center.

---

### Ошибка 3. Histogram interpreted as exact individual data

Histogram показывает counts внутри intervals.

Если bin `10–20` contains 8 values, мы не знаем exact value каждого observation.

---

### Ошибка 4. Confusing IQR with range

```math
range=max-min
```

```math
IQR=Q3-Q1
```

IQR ignores outer 50% and therefore is less sensitive to extremes.

---

### Ошибка 5. Outlier always changes median greatly

False.

Median depends on position. One extreme value can move mean dramatically while median stays unchanged.

---

## 6. Digital SAT Strategy — как быстро читать график

### 10-second scan

Before calculations, ask:

```text
1. What display is this?
2. What can I read directly?
3. Is there skew/outlier?
4. Is question about center or spread?
```

### Use display strengths

| Display | Read first |
|---|---|
| dot plot | exact values, clusters, gaps |
| histogram | shape and interval frequencies |
| box plot | median, quartiles, IQR |
| frequency table | counts / weighted calculations |

### Desmos

For a list:

```text
L=[3,5,7,9]
mean(L)
median(L)
```

Desmos can reduce arithmetic mistakes, but conceptual questions about outliers and spread are usually faster by reasoning.

### Exam shortcut

If answer choices describe qualitative effects such as:

- mean increases;
- median unchanged;
- standard deviation decreases;

do not calculate everything unless needed. Use structure first.

---

## 7. SAT Language Decoder и связи

### Language Decoder

| Phrase | Meaning |
|---|---|
| `mean` | average |
| `median` | middle ordered value |
| `spread` | variability |
| `standard deviation` | spread around mean |
| `interquartile range` | `Q3-Q1` |
| `middle 50 percent` | between Q1 and Q3 |
| `outlier` | unusually distant observation |
| `distribution` | whole pattern of data |
| `skewed right` | long tail to right |
| `clustered` | observations close together |

### Connections

**Опирается на:** arithmetic, ratios, percentages.  
**Дальше используется в:**

- `two_variable_data_scatterplots.md`;
- `sampling_margin_of_error.md`;
- `observational_studies_experiments.md`.

### Transfer Question

Set A and Set B have equal medians. A has IQR 4; B has IQR 15.

What can you conclude?

<details>
<summary><strong>Reasoning</strong></summary>

Their middle 50% centers may be similar, but Set B has substantially larger spread in its middle 50%.

You **cannot** conclude their means are equal.

</details>

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я описываю distribution через shape, center и spread.
- [ ] Я выбираю mean или median с учётом skew/outliers.
- [ ] Я понимаю range, IQR и standard deviation концептуально.
- [ ] Я знаю, какие statistics чувствительны к outliers.
- [ ] Я читаю dot plots, histograms, box plots и frequency tables.
- [ ] Я вычисляю mean из frequency table.
- [ ] Я понимаю effect of adding/multiplying every observation.
- [ ] Я могу сравнить два data sets без лишних вычислений.

> **Mastery test:** вы должны уметь объяснить distribution словами ещё до того, как посчитали хоть одну формулу.