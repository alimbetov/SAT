# Exponential Functions — экспоненциальные функции

## 1. Заголовок и краткое описание

Экспоненциальные модели появляются в Advanced Math, когда величина изменяется на **одинаковый процент**, а не на одинаковую абсолютную величину. SAT проверяет рост, decay, процентные изменения, интерпретацию параметров и сравнение linear vs exponential models.

> **Главная идея:** linear добавляет одно и то же число; exponential умножает на один и тот же коэффициент.

---

## 2. Ключевые понятия и формулы

| Ситуация | Формула | Смысл |
|---|---|---|
| общий вид | `y=a(b)^x` | `a` initial value, `b` growth factor |
| рост на `r` | `y=a(1+r)^x` | `r` в десятичной форме |
| уменьшение на `r` | `y=a(1-r)^x` | decay factor |
| рост `p%` | multiply by `1+p/100` | `20% → 1.20` |
| уменьшение `p%` | multiply by `1-p/100` | `20% → 0.80` |

### Как читать коэффициент

```math
P(t)=500(1.08)^t
```

- `500` — initial value;
- `1.08` — growth factor;
- `0.08=8%` — growth rate per period.

### Визуальный якорь

`1.12` означает **+12%**, а не 112% роста.  
`0.88` означает **−12%**.

### Вопрос к читателю

Если количество ежегодно уменьшается на 30%, какой множитель используется каждый год: `0.30`, `0.70` или `1.30`?

---

## 3. Пошаговый разбор — Guided Example

### Задача

A population of bacteria starts at `800` and increases by `25%` every hour. Write a model for the population after `h` hours and find the population after 2 hours.

### Шаг 1. Находим initial value

В начале:

```math
P(0)=800.
```

Поэтому `a=800`.

### Шаг 2. Переводим процент в growth factor

Рост 25% означает, что после каждого периода остаётся 100% старого количества плюс 25% нового:

```math
1+0.25=1.25.
```

### Шаг 3. Строим модель

```math
P(h)=800(1.25)^h.
```

### Шаг 4. Подставляем `h=2`

```math
P(2)=800(1.25)^2=800(1.5625)=1250.
```

Почему мы не используем `800+0.25h`? Потому что 25% каждый раз берутся от **нового текущего значения**, а не от фиксированного первоначального значения.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

A quantity increases by 6% each year. Which factor represents one year of growth?

**A)** `0.06`  
**B)** `0.94`  
**C)** `1.06`  
**D)** `1.60`

### Problem 2 — Easy — Multiple Choice

For

```math
f(x)=300(0.8)^x,
```

what percent decrease occurs per unit increase in `x`?

**A)** `8%`  
**B)** `20%`  
**C)** `80%`  
**D)** `120%`

### Problem 3 — Medium — Grid-in

An account contains `$1000` and grows by `10%` for one year. What is the balance after one year?

### Problem 4 — Medium — Multiple Choice

Which situation is best modeled exponentially?

**A)** A tank loses exactly 5 liters every minute.  
**B)** A worker earns `$20` for each hour worked.  
**C)** A car loses 15% of its value each year.  
**D)** A taxi charges `$4` plus `$2` per mile.

### Problem 5 — Hard — Grid-in

A population is modeled by

```math
P(t)=1200(1.5)^{t/3}.
```

By what percent does the population increase every 3 time units?

<details>
<summary><strong>Ответы и краткие решения</strong></summary>

1. **C.** `1+0.06=1.06`.  
2. **B.** `0.8=1-0.2`, значит decay 20%.  
3. **1100.** `1000(1.10)=1100`.  
4. **C.** Один и тот же процент ежегодно → exponential.  
5. **50.** При увеличении `t` на 3 показатель степени увеличивается на 1, то есть величина умножается на `1.5`, рост 50%.

</details>

---

## 5. Common Traps — типичные ловушки

### Ловушка 1. Использовать процент вместо factor

Рост 7% → factor `1.07`, не `0.07`.

### Ловушка 2. Путать linear и exponential

`+50` каждый год — linear.  
`+5%` каждый год — exponential.

### Ловушка 3. Не заметить масштаб времени

В выражении `(1.2)^(t/4)` factor `1.2` относится к **4 единицам времени**, а не к одной.

---

## 6. Стратегия для Digital SAT

В Desmos можно сравнить модели:

```text
y=100(1.1)^x
y=100+10x
```

Это помогает увидеть различие exponential и linear growth.

Для задач с неизвестным временем часто удобно построить exponential model и горизонтальную линию `y=target`, затем найти intersection.

---

## 7. Связи с другими темами

**Опирается на:** percentages, exponent rules, functions.

**Связано с:**
- `nonlinear_functions.md`;
- `equivalent_expressions.md`;
- `percentages.md`;
- word problems on growth and decay.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я различаю linear и exponential change.
- [ ] Я перевожу процент роста/снижения в growth/decay factor.
- [ ] Я понимаю параметры `a` и `b` в `a(b)^x`.
- [ ] Я учитываю период времени в показателе степени.
