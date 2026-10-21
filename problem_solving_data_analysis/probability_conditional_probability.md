# Probability and Conditional Probability — вероятность и условная вероятность

## 1. Заголовок и краткое описание

Probability and conditional probability — официальный skill Problem-Solving and Data Analysis. На SAT нужно читать таблицы, считать доли, понимать independent/dependent events и правильно определять denominator в условной вероятности.

> **Главная идея:** в conditional probability пространство возможных исходов сужается условием.

---

## 2. Ключевые понятия и формулы

| Понятие | Формула / смысл |
|---|---|
| probability | `favorable / total` |
| complement | `P(not A)=1-P(A)` |
| conditional probability | `P(A|B)=P(A and B)/P(B)` |
| independent events | `P(A and B)=P(A)P(B)` |
| mutually exclusive | события не могут произойти одновременно |

### Таблица — главный SAT-формат

Если вопрос звучит:

> Given that a selected student is in grade 11, what is the probability that the student plays soccer?

Denominator — **только все ученики grade 11**, а не вся таблица.

### Визуальный якорь

Слова **given that** означают: «сузь denominator».

---

## 3. Пошаговый разбор — Guided Example

В группе 40 учеников:

- 24 изучают Spanish;
- среди них 15 играют в школьной команде.

What is the probability that a randomly selected student plays on a school team **given that** the student studies Spanish?

### Шаг 1. Замечаем условие

Нас интересуют только ученики, которые study Spanish.

Значит denominator = `24`.

### Шаг 2. Находим favorable outcomes

Из этих 24 учеников 15 играют в команде.

### Шаг 3. Считаем

```math
P(team|Spanish)=\frac{15}{24}=\frac58.
```

Почему denominator не 40? Потому что условие уже ограничило выборку учениками Spanish.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

A fair die is rolled. What is the probability of rolling a 5?

**A)** `1/2`  **B)** `1/5`  **C)** `1/6`  **D)** `5/6`

### Problem 2 — Easy — Grid-in

A bag contains 3 red and 7 blue balls. What is the probability of selecting a red ball? Enter the decimal.

### Problem 3 — Medium — Multiple Choice

If `P(A)=0.35`, what is `P(not A)`?

**A)** 0.35  **B)** 0.50  **C)** 0.65  **D)** 1.35

### Problem 4 — Medium — Multiple Choice

In a class, 20 students are juniors. Of those juniors, 8 take physics. If a student is selected from the juniors, what is the probability that the student takes physics?

**A)** `8/30`  **B)** `8/20`  **C)** `20/8`  **D)** `12/20`

### Problem 5 — Hard — Grid-in

Two independent events have probabilities `P(A)=0.4` and `P(B)=0.5`. What is `P(A and B)`?

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **C**, one favorable face out of 6.  
2. **0.3**, `3/10`.  
3. **C**, `1-0.35=0.65`.  
4. **B**, condition limits denominator to 20 juniors.  
5. **0.2**, independence gives `0.4·0.5`.

</details>

---

## 5. Common Traps — типичные ловушки

- Использовать общий total вместо conditional denominator.
- Путать independent и mutually exclusive events.
- Забывать, что probability всегда между 0 и 1.

---

## 6. Стратегия для Digital SAT

Для two-way tables сначала буквально обведите мысленно строку/столбец, заданный словами **given that**. Это почти всегда мгновенно показывает denominator. Desmos здесь обычно не нужен.

---

## 7. Связи с другими темами

**Опирается на:** fractions, ratios, percentages.  
**Связано с:** sampling, statistics, two-way tables, inference.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я считаю basic probability.
- [ ] Я использую complement rule.
- [ ] Я правильно выбираю denominator для conditional probability.
- [ ] Я понимаю условие independence.
