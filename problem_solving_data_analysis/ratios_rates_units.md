# Ratios, Rates, Proportions, and Units — отношения, скорости, пропорции и единицы

## 1. Зачем эта тема нужна на SAT

Это один из базовых skills домена **Problem-Solving and Data Analysis**. На SAT задачи редко говорят: «найдите unit rate». Вместо этого они описывают расход топлива, скорость, цену за единицу, рецепт, плотность, масштаб карты или conversion между единицами.

Поэтому цель урока — не запомнить `a/b=c/d`, а научиться быстро отвечать на три вопроса:

1. **Какие две величины сравниваются?**
2. **Что должно оказаться “на 1”?**
3. **Какие units должен иметь ответ?**

> **Главная идея:** units — это часть математики. Они часто сами подсказывают нужную операцию.

---

## 2. Pattern Map — как распознавать тип задачи

| Что вы видите в условии | Pattern | Что делать |
|---|---|---|
| `3 red for every 5 blue` | ratio | сохранить порядок величин |
| `$18 for 6 notebooks` | unit rate | разделить, чтобы получить цену за 1 |
| `180 miles on 6 gallons` | rate | определить miles/gallon или gallons/mile |
| `at the same rate` | proportion | использовать постоянный multiplicative relationship |
| `y is directly proportional to x` | direct variation | `y=kx` |
| `1 cm represents 8 km` | scale | умножить/разделить на scale factor |
| `hours → minutes`, `miles → km` | unit conversion | dimensional analysis |
| `distance and time` | speed/rate | `distance/time` |

### Pattern 1. Ratio — «сколько одного относительно другого»

Если в группе 6 девочек и 9 мальчиков:

- girls : boys = `6:9 = 2:3`;
- girls : total = `6:15 = 2:5`.

Это **разные ratios**.

> **Якорь:** сначала подпишите словами, потом числами.

```text
girls / boys = 6 / 9
```

а не просто `6/9` без смысла.

### Pattern 2. Unit rate — «сколько на 1»

5 notebooks стоят `$15`.

```math
\frac{15\ dollars}{5\ notebooks}=3\ \frac{dollars}{notebook}
```

Unit rate = `$3 per notebook`.

> Слово **per** почти всегда означает division.

### Pattern 3. Proportional relationship

Если 4 одинаковых билета стоят `$28`, то цена одного билета постоянна:

```math
k=\frac{28}{4}=7
```

Тогда:

```math
y=7x
```

где `x` — число билетов, `y` — стоимость.

#### Как проверить, proportional ли relationship?

Для proportional relationship отношение `y/x` постоянно.

| x | y | y/x |
|---:|---:|---:|
| 2 | 10 | 5 |
| 4 | 20 | 5 |
| 7 | 35 | 5 |

Значит:

```math
y=5x
```

Но если есть стартовая плата:

```math
y=5x+8
```

это уже linear, но **не directly proportional**, потому что график не проходит через `(0,0)`.

> **SAT trap:** linear ≠ обязательно proportional.

### Pattern 4. Unit conversion — «units должны сократиться»

Convert `2.5 hours` to minutes.

```math
2.5\ h\cdot\frac{60\ min}{1\ h}=150\ min
```

`h` сокращаются.

Это dimensional analysis.

> **Якорь:** ненужная unit должна оказаться сверху и снизу и исчезнуть.

### Pattern 5. Scale factor

Если map scale:

```text
1 cm : 8 km
```

и расстояние на карте `6.5 cm`, то:

```math
6.5\ cm\cdot\frac{8\ km}{1\ cm}=52\ km
```

### Pattern 6. Speed / density / derived rates

Многие формулы — это просто rates:

```math
speed=\frac{distance}{time}
```

```math
density=\frac{mass}{volume}
```

```math
unit\ price=\frac{cost}{quantity}
```

Не нужно запоминать их как несвязанные правила. Во всех случаях вопрос один:

> **«Сколько numerator приходится на одну unit denominator?»**

---

## 3. Guided Learning — как выбирать метод

### Decision Tree

```text
В условии сравнивают две величины?
        │
        ├─ Нужно "per 1"?
        │      → unit rate
        │
        ├─ Сказано "same rate" / proportional?
        │      → unit rate или proportion
        │
        ├─ Нужно сменить units?
        │      → dimensional analysis
        │
        ├─ Дана карта/model scale?
        │      → scale factor
        │
        └─ Distance/time, cost/item, mass/volume?
               → rate
```

### Worked Example 1 — выбираем правильный rate

A car travels `180 miles` using `6 gallons` of fuel. How many miles does it travel per gallon?

#### Recognize

Фраза **per gallon** означает:

```text
miles / gallon
```

#### Solve

```math
\frac{180\ miles}{6\ gallons}=30\ miles/gallon
```

#### Check

Units ответа — `miles/gallon`, именно это спросили.

**Ответ: `30`.**

---

### Worked Example 2 — тот же контекст, но другой denominator

Same car: `180 miles` using `6 gallons`. How many gallons are used per mile?

Теперь спрашивают:

```text
gallons / mile
```

Поэтому:

```math
\frac{6}{180}=\frac1{30}\ gallon/mile
```

> Один и тот же набор чисел может дать **два разных rates**. Направление задаёт слово `per`.

---

### Worked Example 3 — proportion через unit rate

At the same fuel efficiency, how many gallons are needed for `300 miles`?

Из первого примера:

```math
30\ miles/gallon
```

Нужно gallons:

```math
300\ miles\div30\frac{miles}{gallon}=10\ gallons
```

Почему division? Потому что:

```text
miles ÷ (miles/gallon) = gallons
```

**Ответ: `10`.**

---

### Worked Example 4 — direct proportion from table

| x | y |
|---:|---:|
| 3 | 18 |
| 5 | 30 |
| 8 | 48 |

Find the constant of proportionality.

Проверяем:

```math
\frac{18}{3}=6
```

```math
\frac{30}{5}=6
```

```math
\frac{48}{8}=6
```

Значит:

```math
k=6
```

и relationship:

```math
y=6x
```

---

### Worked Example 5 — когда proportion использовать нельзя

A taxi charges `$4` plus `$2.50 per mile`.

Некоторые ученики пишут:

```math
\frac{cost}{miles}=constant
```

Но при `0 miles` стоимость уже `$4`.

Правильная модель:

```math
C=4+2.5m
```

Это linear relationship, но **не direct proportion**.

#### Recognition clue

Если есть:

- starting fee;
- initial amount;
- fixed charge;

то обычно модель имеет `+b` и не является `y=kx`.

---

### Worked Example 6 — multi-step unit conversion

A car moves at `72 km/h`. What is its speed in meters per second?

```math
72\frac{km}{h}
\cdot\frac{1000\ m}{1\ km}
\cdot\frac{1\ h}{3600\ s}
```

Units:

```text
km cancels
h cancels
→ m/s
```

Числа:

```math
72\cdot\frac{1000}{3600}=20
```

**Ответ: `20 m/s`.**

Это надёжнее, чем пытаться вспомнить отдельное правило «делить на 3.6».

---

## 4. Practice Ladder — от подсказки к самостоятельному решению

### A. Recognition Drill

Для каждого задания сначала назовите pattern, **не решая**.

1. `8 apples cost $12. Find cost per apple.`  
   Pattern: `__________`

2. `1 inch represents 25 miles.`  
   Pattern: `__________`

3. `y/x is constant for all data points.`  
   Pattern: `__________`

4. `Convert 3.2 kg to grams.`  
   Pattern: `__________`

<details>
<summary><strong>Recognition answers</strong></summary>

1. unit rate  
2. scale factor  
3. direct proportion  
4. unit conversion

</details>

---

### B. Faded Example

A printer produces `420 pages` in `7 minutes` at a constant rate. How many pages in `12 minutes`?

#### Step 1 — find pages per minute

```math
\frac{420}{7}=\boxed{\phantom{60}}
```

#### Step 2 — multiply by 12

```math
\boxed{\phantom{60}}\cdot12=\boxed{\phantom{720}}
```

<details>
<summary><strong>Solution</strong></summary>

`60 pages/min`, so `60·12=720 pages`.

</details>

---

### C. SAT-style Independent Practice

#### Problem 1 — Easy — Multiple Choice

If 5 notebooks cost `$15`, what is the unit price?

**A)** `$2`  
**B)** `$3`  
**C)** `$5`  
**D)** `$10`

#### Problem 2 — Easy — Grid-in

A runner covers `24 km` in `3 hours`. What is the average rate in km/h?

#### Problem 3 — Medium — Multiple Choice

A recipe uses flour and sugar in ratio `3:2`. If `12 cups` of flour are used, how many cups of sugar are needed?

**A)** 6  
**B)** 8  
**C)** 10  
**D)** 18

#### Problem 4 — Medium — Grid-in

A machine produces `1,500 parts` in `6 hours`. At the same rate, how many parts does it produce in `2.4 hours`?

#### Problem 5 — Hard — Multiple Choice

A map scale is `1 cm : 8 km`. Two points are `6.5 cm` apart on the map. What is the actual distance?

**A)** 14.5 km  
**B)** 48 km  
**C)** 52 km  
**D)** 64 km

#### Problem 6 — Hard Transfer — Grid-in

A liquid has density `1.25 g/mL`. What is the mass, in grams, of `240 mL` of the liquid?

<details>
<summary><strong>Ответы и решения</strong></summary>

1. **B**. `$15/5=$3 per notebook`.  
2. **8**. `24/3=8 km/h`.  
3. **B**. Scale factor `12/3=4`; sugar `2·4=8`.  
4. **600**. Unit rate `1500/6=250 parts/hour`; `250·2.4=600`.  
5. **C**. `6.5·8=52 km`.  
6. **300**. `1.25 g/mL · 240 mL = 300 g`.

</details>

---

## 5. Error Clinic — типичные ошибки и почему они возникают

### Ошибка 1. Перевернуть rate

Дано `180 miles` и `6 gallons`.

Если спрашивают **miles per gallon**:

```math
180/6
```

Если спрашивают **gallons per mile**:

```math
6/180
```

#### Как избежать

Перед числами напишите units:

```text
miles / gallon
```

---

### Ошибка 2. Использовать proportion там, где есть fixed value

`$5 admission + $3 per ride` — не `y=kx`.

Почему?

При `x=0`:

```math
y=5
```

а direct proportion должен проходить через `(0,0)`.

---

### Ошибка 3. Неправильно конвертировать units

Convert `2 hours` to minutes.

Неверный ход:

```math
2/60
```

Правильная dimensional chain:

```math
2\ h\cdot\frac{60\ min}{h}=120\ min
```

---

### Ошибка 4. Масштабировать только одну часть ratio неосознанно

Ratio `3:2`.

Если `3 → 12`, factor = 4.

Значит обязательно:

```text
2 → 8
```

У ratio обе части масштабируются одним factor.

---

## 6. Digital SAT Strategy — Manual vs Desmos

### Обычно быстрее вручную

- simple unit rate;
- ratio scaling;
- basic conversions;
- direct proportions.

### Desmos полезен, когда

- дана таблица и нужно проверить `y/x`;
- proportional model сравнивается с другой linear model;
- числа неудобные;
- есть несколько constraints.

### Desmos example

Если задача говорит:

```math
y=kx
```

и точка `(7,31.5)` лежит на графике, можно ввести:

```text
31.5 = k*7
```

и получить:

```text
k = 4.5
```

Но вручную `31.5/7` обычно столь же быстро.

### Time rule

Если setup задачи уже очевиден, не стройте график только потому, что калькулятор доступен.

> **Сначала model, потом calculator.**

---

## 7. SAT Language Decoder и связи с другими темами

### Language Decoder

| SAT phrase | Что означает математически |
|---|---|
| `per` | division / rate |
| `for every` | ratio |
| `at the same rate` | constant rate / proportion |
| `directly proportional` | `y=kx` |
| `constant of proportionality` | `k=y/x` |
| `unit rate` | denominator = 1 |
| `scale` | multiplicative factor |
| `represents` | scale relationship |
| `convert` | dimensional analysis |

### Связи

**Опирается на:** fractions, decimals, multiplication, division.  
**Используется дальше в:**

- `percentages.md`;
- `linear_functions.md`;
- `probability_conditional_probability.md`;
- geometry scale-factor problems;
- speed, density and real-world modeling.

### Transfer Question

A cyclist travels `45 km` in `1.5 hours`. Another cyclist travels `70 km` in `2 hours`.

Не вычисляя сразу, сформулируйте:

1. какой rate нужно сравнить;
2. какие units должен иметь ответ;
3. кто быстрее после вычисления.

<details>
<summary><strong>Transfer solution</strong></summary>

Сравниваем `km/h`.

First cyclist:

```math
45/1.5=30\ km/h
```

Second:

```math
70/2=35\ km/h
```

Второй быстрее.

</details>

---

## 8. Мини-чек-лист для самопроверки

Перед переходом дальше я умею:

- [ ] подписывать ratio словами до подстановки чисел;
- [ ] определять, какая величина должна быть denominator в rate;
- [ ] находить и интерпретировать unit rate;
- [ ] отличать direct proportion `y=kx` от обычной linear model `y=mx+b`;
- [ ] использовать dimensional analysis для conversions;
- [ ] решать scale-factor задачи;
- [ ] проверять решение по units;
- [ ] объяснить, почему выбран именно этот метод.

> **Mastery test:** если units в условии изменились, но структура осталась той же, вы всё равно должны узнать pattern.