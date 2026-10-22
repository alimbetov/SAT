# Percentages — проценты и процентные изменения

## 1. Зачем эта тема нужна на SAT

Проценты на Digital SAT — это не один тип задач, а целое семейство: **percent of**, **percent change**, **discount/markup**, **reverse percent**, **successive changes**, taxes и growth/decay.

Основная причина ошибок — ученик знает формулу, но не понимает, **какое число является base**.

> **Главная идея:** процент всегда берётся **от чего-то**. Сначала найдите base, потом считайте.

Перед вычислениями задайте себе:

```text
100% = что именно?
```

Если вы не можете ответить — модель ещё не готова.

---

## 2. Pattern Map — шесть основных типов SAT-задач

| Что спрашивают | Pattern | Модель |
|---|---|---|
| `What is 30% of 90?` | percent of | `part = base·rate` |
| `increased by 15%` | forward increase | `new=old·1.15` |
| `decreased by 15%` | forward decrease | `new=old·0.85` |
| `from 80 to 100` | percent change | `(change/original)·100%` |
| `after 20% discount costs 96` | reverse percent | `old=new/0.80` |
| `+10%, then +10%` | successive changes | multiply factors |

### Universal triangle

Все basic percentage questions можно связать тремя величинами:

```text
PART = BASE × RATE
```

где rate записан decimal.

Пример:

```text
27 is 30% of 90
```

```math
27=90\cdot0.30
```

Здесь:

- part = 27;
- base = 90;
- rate = 0.30.

### Pattern 1. Percent of

`18% of 250`:

```math
250\cdot0.18=45
```

> **Language anchor:** `of` почти всегда превращается в multiplication.

### Pattern 2. Increase / decrease as multiplier

Increase by 12%:

```math
100\%+12\%=112\%=1.12
```

Decrease by 12%:

```math
100\%-12\%=88\%=0.88
```

Поэтому:

```text
+12% → ×1.12
-12% → ×0.88
```

### Pattern 3. Percent change

Если значение изменилось с `old` до `new`:

```math
percent\ change=\frac{new-old}{old}\cdot100\%
```

Критический вопрос:

> Почему denominator = old?

Потому что мы измеряем изменение **относительно исходного значения**.

### Pattern 4. Reverse percent

После скидки 20% осталось 80% original:

```math
new=0.80\cdot old
```

Если `new=96`:

```math
96=0.80\cdot old
```

```math
old=96/0.80=120
```

> Reverse problem → обычно division by multiplier.

### Pattern 5. Successive changes

`+10%`, затем `+10%`:

```math
1.10\cdot1.10=1.21
```

Overall change = `+21%`, не `+20%`.

Почему?

Вторые 10% берутся уже от нового числа.

### Pattern 6. Opposite percentages are usually not inverses

Начали со 100.

Increase 20%:

```math
100\cdot1.20=120
```

Decrease 20%:

```math
120\cdot0.80=96
```

Мы получили 96, а не 100.

> **Якорь:** equal percentages ≠ equal amounts, если bases разные.

---

## 3. Guided Learning — как распознавать base и выбирать действие

### Decision Tree

```text
Есть слово "of"?
   → multiply base by rate

Есть "increase/decrease by p%"?
   → multiplier 1±p

Даны old и new, спрашивают percent change?
   → change / old

Дано final после discount/markup, ищут original?
   → divide by multiplier

Несколько изменений подряд?
   → multiply multipliers
```

### Worked Example 1 — percent of

What is `35% of 240`?

#### Recognize

`of` → multiplication.

#### Convert

```math
35\%=0.35
```

#### Solve

```math
240\cdot0.35=84
```

**Ответ: `84`.**

---

### Worked Example 2 — percent increase

A price rises from `$80` to `$92`. What is the percent increase?

#### Step 1. Find change

```math
92-80=12
```

#### Step 2. Identify base

Original price = 80.

#### Step 3. Compare change to base

```math
\frac{12}{80}=0.15
```

```math
0.15=15\%
```

**Ответ: `15%`.**

#### Why not divide by 92?

Because 92 is the result, not the starting reference point.

---

### Worked Example 3 — reverse discount

After a 25% discount, a jacket costs `$90`. Find original price.

25% discount means 75% remains:

```math
90=0.75P
```

```math
P=\frac{90}{0.75}=120
```

**Ответ: `$120`.**

#### Recognition clue

Если в условии есть:

```text
after a discount
sale price
final value
original price?
```

это reverse percent.

---

### Worked Example 4 — tax + discount

A `$200` item is discounted by 15%, then 8% sales tax is applied. Find final price.

Discount factor:

```math
0.85
```

Tax factor:

```math
1.08
```

Итог:

```math
200\cdot0.85\cdot1.08=183.6
```

**Ответ: `$183.60`.**

> Не складывайте `-15%+8%=-7%`. Bases меняются.

---

### Worked Example 5 — find equivalent single percent

A quantity increases by 20% and then decreases by 10%.

Overall multiplier:

```math
1.20\cdot0.90=1.08
```

Значит итог = 108% original.

**Overall increase = 8%.**

---

### Worked Example 6 — percentage points vs percent change

A survey result rises from `40%` to `50%`.

Two different statements:

- increase of **10 percentage points**;
- relative percent increase:

```math
\frac{50-40}{40}=0.25=25\%
```

> SAT может проверять различие между абсолютным изменением percentage и relative percent change.

---

## 4. Practice Ladder — от распознавания к transfer

### A. Recognition Drill

Назовите pattern без вычислений.

1. `What is 18% of 350?` → `__________`  
2. `A value rises from 400 to 460.` → `__________`  
3. `After 20% discount, price is 96.` → `__________`  
4. `Value grows 5% each year for 3 years.` → `__________`

<details>
<summary><strong>Answers</strong></summary>

1. percent of  
2. percent change  
3. reverse percent  
4. successive/exponential multipliers

</details>

### B. Faded Example

A laptop costs `$800` and is discounted by `12%`.

Multiplier:

```math
1-0.12=\boxed{\phantom{0.88}}
```

Final price:

```math
800\cdot\boxed{\phantom{0.88}}=\boxed{\phantom{704}}
```

<details>
<summary><strong>Solution</strong></summary>

`0.88`; final price `$704`.

</details>

### C. SAT-style Independent Practice

#### Problem 1 — Easy — Multiple Choice

What is 30% of 90?

**A)** 18  
**B)** 27  
**C)** 30  
**D)** 60

#### Problem 2 — Easy — Grid-in

A `$50` item is discounted by 10%. What is the sale price?

#### Problem 3 — Medium — Multiple Choice

A population rises from 400 to 460. What is the percent increase?

**A)** 6%  
**B)** 10%  
**C)** 15%  
**D)** 60%

#### Problem 4 — Medium — Grid-in

After a 20% discount, a product costs `$96`. What was the original price?

#### Problem 5 — Hard — Multiple Choice

A value is increased by 10% twice. Overall, by what percent has it increased?

**A)** 20%  
**B)** 21%  
**C)** 22%  
**D)** 110%

#### Problem 6 — Hard Transfer — Grid-in

A quantity decreases by 20% and then increases by 25%. What is the overall percent change relative to the original value?

<details>
<summary><strong>Ответы и решения</strong></summary>

1. **B.** `90·0.30=27`.  
2. **45.** `50·0.90=45`.  
3. **C.** `(460-400)/400=60/400=15%`.  
4. **120.** `96/0.80=120`.  
5. **B.** `1.10²=1.21`, so +21%.  
6. **0%.** `0.80·1.25=1.00`; the value returns exactly to original.

</details>

---

## 5. Error Clinic — ошибки, которые SAT специально провоцирует

### Ошибка 1. Wrong base

From 80 to 100:

Неверно:

```math
20/100=20\%
```

Правильно:

```math
20/80=25\%
```

#### Diagnostic question

```text
100% = какое число?
```

Здесь 100% = original 80.

---

### Ошибка 2. Использовать `0.15` как final multiplier после increase 15%

Неверно:

```math
new=old\cdot0.15
```

Это оставляет только 15%.

Правильно:

```math
new=old\cdot1.15
```

---

### Ошибка 3. Складывать successive rates

`+10%`, затем `+20%`:

Неверно считать overall `+30%`.

Правильно:

```math
1.10\cdot1.20=1.32
```

Overall `+32%`.

---

### Ошибка 4. Reverse percent через subtraction

После 20% discount цена 80.

Нельзя:

```text
80 + 20% of 80
```

Потому что 20% discount считался от **original**, не от 80.

Правильно:

```math
80/0.80=100
```

---

## 6. Digital SAT Strategy — быстрые методы и Desmos

### Mental multiplier table

Полезно узнавать без паузы:

| Change | Multiplier |
|---|---:|
| +5% | 1.05 |
| +10% | 1.10 |
| +20% | 1.20 |
| -5% | 0.95 |
| -10% | 0.90 |
| -20% | 0.80 |
| -25% | 0.75 |
| -50% | 0.50 |

### Desmos полезен для

- нескольких multipliers;
- reverse percentage с неудобными decimals;
- growth over many periods;
- проверок percent change.

Пример:

```text
200*0.85*1.08
```

Но Desmos не решает главную проблему — **выбрать правильный base**.

### 30-second sanity check

Если цена после discount получилась **больше** original — почти наверняка model неверна.

Если increase 5% дал factor `0.05` — ошибка в переводе процента.

---

## 7. SAT Language Decoder и связи

### Language Decoder

| SAT phrase | Перевод в модель |
|---|---|
| `p percent of A` | `A·p/100` |
| `increased by p%` | `×(1+p)` |
| `decreased by p%` | `×(1-p)` |
| `p% greater than` | `×(1+p)` |
| `p% less than` | `×(1-p)` |
| `percent increase` | `(new-old)/old` |
| `original value` | reverse percent |
| `after discount` | final = original × remaining factor |
| `markup` | increase |
| `sales tax` | increase |

### Связи

**Опирается на:** ratios, decimals, multiplication.  
**Используется в:**

- exponential functions;
- financial word problems;
- probability;
- statistics;
- growth/decay modeling.

### Transfer Question

A city population falls 10% in year 1 and rises 10% in year 2.

Will it return to the original population?

<details>
<summary><strong>Reasoning</strong></summary>

No.

```math
0.90\cdot1.10=0.99
```

Final = 99% original, so it is 1% lower.

</details>

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я всегда могу назвать base = 100%.
- [ ] Я отличаю `percent of` от `percent change`.
- [ ] Я использую multiplier для increase/decrease.
- [ ] Я делю на multiplier в reverse-percent problems.
- [ ] Я перемножаю successive percentage factors.
- [ ] Я отличаю percentage points от relative percent change.
- [ ] Я могу объяснить, почему denominator в percent change — original value.
- [ ] Я проверяю ответ на здравый смысл до перехода дальше.

> **Mastery test:** если слова `discount`, `markup`, `growth` и `reverse percentage` исчезнут, вы всё равно должны узнать задачу по структуре `part/base/rate`.