# Percentages — проценты и процентные изменения

## 1. Заголовок и краткое описание

Percentages — официальный skill Problem-Solving and Data Analysis. На SAT встречаются percent of, percent increase/decrease, reverse percentage, markups, discounts, taxes и последовательные изменения.

> **Главная идея:** процент — это множитель относительно исходного значения.

---

## 2. Ключевые понятия и формулы

| Задача | Формула |
|---|---|
| `p%` от `A` | `A·p/100` |
| increase by `p%` | `new=old(1+p/100)` |
| decrease by `p%` | `new=old(1-p/100)` |
| percent change | `(new-old)/old ·100%` |
| reverse percent | `old=new/factor` |

### Визуальный якорь

- `+15%` → multiply by `1.15`;
- `−15%` → multiply by `0.85`.

Важно: увеличение на 20%, а затем уменьшение на 20% **не возвращает** исходное значение, потому что проценты берутся от разных bases.

---

## 3. Пошаговый разбор — Guided Example

A jacket originally costs `$80`. Its price is increased by 25% and then discounted by 20%. What is the final price?

### Шаг 1. Первый multiplier

Рост 25%:

```math
80(1.25)=100.
```

### Шаг 2. Второй multiplier

Скидка 20%:

```math
100(0.80)=80.
```

### Шаг 3. Интерпретируем

В этом конкретном случае цена вернулась к `$80`, но это произошло из-за выбранных процентов `25%` и `20%`, а не потому что любые противоположные проценты взаимно уничтожаются.

Почему? Потому что `25% of 80 = 20`, а `20% of 100 = 20`.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

What is 30% of 90?

**A)** 18  **B)** 27  **C)** 30  **D)** 60

### Problem 2 — Easy — Grid-in

A `$50` item is discounted by 10%. What is the sale price?

### Problem 3 — Medium — Multiple Choice

A population rises from 400 to 460. What is the percent increase?

**A)** 6%  **B)** 10%  **C)** 15%  **D)** 60%

### Problem 4 — Medium — Grid-in

After a 20% discount, a product costs `$96`. What was the original price?

### Problem 5 — Hard — Multiple Choice

A value is increased by 10% twice. Overall, by what percent has it increased?

**A)** 20%  **B)** 21%  **C)** 22%  **D)** 110%

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **B**, `90·0.30=27`.  
2. **45**, `50·0.90`.  
3. **C**, `60/400=0.15=15%`.  
4. **120**, `96/0.8`.  
5. **B**, `1.1²=1.21`, то есть +21%.

</details>

---

## 5. Common Traps — типичные ловушки

- Делить percent change на новое значение вместо исходного.
- Складывать последовательные percent changes вместо перемножения factors.
- В reverse percentage вычитать процент от final value вместо деления на factor.

---

## 6. Стратегия для Digital SAT

Для нескольких последовательных изменений сразу записывайте multipliers. Например, `+8%`, затем `−5%` → `1.08·0.95`. Desmos полезен как быстрый калькулятор, но модель важнее вычисления.

---

## 7. Связи с другими темами

**Опирается на:** ratios, decimals, multiplication.  
**Связано с:** exponential functions, finance-style word problems, statistics.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я нахожу процент от числа.
- [ ] Я считаю percent increase/decrease от правильной base.
- [ ] Я решаю reverse-percentage задачи.
- [ ] Я работаю с последовательными percentage changes через multipliers.
