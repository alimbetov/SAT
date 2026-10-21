# Lines, Angles, and Triangles — прямые, углы и треугольники

## 1. Заголовок и краткое описание

**Lines, angles, and triangles** — официальный skill Geometry and Trigonometry. На SAT проверяются vertical angles, parallel lines with transversals, triangle angle sums, **similarity**, **congruence**, scale factor и достаточность условий для геометрических выводов.

> **Главная идея:** большинство SAT-задач на геометрию решаются не рисунком «на глаз», а цепочкой строгих отношений: равенство углов, сумма углов, пропорциональность сторон.

---

## 2. Ключевые понятия и формулы

| Понятие | Правило |
|---|---|
| straight angle | `180°` |
| full turn | `360°` |
| complementary angles | сумма `90°` |
| supplementary angles | сумма `180°` |
| vertical angles | равны |
| triangle angle sum | `180°` |
| exterior angle | сумма двух remote interior angles |
| similar triangles | равные corresponding angles, proportional corresponding sides |
| congruent triangles | одинаковые размер и форма |

### Parallel lines + transversal

При параллельных прямых:

- corresponding angles равны;
- alternate interior angles равны;
- same-side interior angles supplementary.

### Similarity

Для similar triangles один scale factor `k` связывает все соответствующие sides:

```math
\frac{a_2}{a_1}=\frac{b_2}{b_1}=\frac{c_2}{c_1}=k.
```

Angles при масштабировании **не меняются**.

### Congruence criteria

Часто полезно знать:

- **SSS** — three corresponding sides equal;
- **SAS** — two sides and included angle;
- **ASA/AAS** — two angles and a side.

Для right triangles может применяться hypotenuse-leg reasoning.

### Визуальный якорь

**Similar = same shape, possibly different size.**  
**Congruent = same shape and same size.**

---

## 3. Пошаговый разбор — Guided Example

A triangle has angles `2x`, `3x`, and `4x`. Find the largest angle.

### Шаг 1. Используем triangle angle sum

```math
2x+3x+4x=180.
```

### Шаг 2. Объединяем

```math
9x=180.
```

### Шаг 3. Находим `x`

```math
x=20.
```

### Шаг 4. Находим largest angle

```math
4x=80^\circ.
```

Почему этот подход надёжен? Геометрическое правило превращает задачу в linear equation, а не требует оценивать рисунок визуально.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Grid-in

Two supplementary angles are 65° and `x°`. Find `x`.

### Problem 2 — Easy — Multiple Choice

If one vertical angle measures 112°, the opposite vertical angle measures:

**A)** 68°  **B)** 90°  **C)** 112°  **D)** 248°

### Problem 3 — Medium — Grid-in

A triangle has angles 45°, 55°, and `x°`. Find `x`.

### Problem 4 — Medium — Multiple Choice

Two similar triangles have corresponding side lengths 3 and 9. If another side of the smaller triangle is 5, the corresponding side of the larger triangle is:

**A)** 7  **B)** 11  **C)** 15  **D)** 45

### Problem 5 — Hard — Multiple Choice

Triangles ABC and DEF satisfy `AB=DE`, `BC=EF`, and angle `B` equals angle `E`. Which criterion proves the triangles congruent?

**A)** SSS  **B)** SAS  **C)** ASA  **D)** similarity only

<details>
<summary><strong>Ответы и краткие решения</strong></summary>

1. **115**.  
2. **C**, vertical angles are equal.  
3. **80**, triangle sum is 180°.  
4. **C**, scale factor `9/3=3`, so `5·3=15`.  
5. **B**, two sides and the included angle → SAS.

</details>

---

## 5. Common Traps — типичные ловушки

### Ловушка 1. Доверять масштабу рисунка

SAT diagrams могут быть **not drawn to scale**. Используйте только данные и теоремы.

### Ловушка 2. Путать similarity и congruence

У similar triangles стороны могут быть разной длины; у congruent — соответствующие sides равны.

### Ловушка 3. Нарушать correspondence

Если одна пара corresponding sides даёт scale factor 3, тот же factor применяется ко всем соответствующим sides.

---

## 6. Стратегия для Digital SAT

Помечайте на рисунке:

- равные angles;
- parallel marks;
- known side lengths;
- scale factor.

Для proof/sufficiency-style вопросов не спрашивайте «похоже ли это на равные треугольники?». Спросите: **какой конкретный theorem/criterion выполняется?**

Desmos здесь обычно вторичен.

---

## 7. Связи с другими темами

**Опирается на:** linear equations, ratios.  
**Связано с:**
- `right_triangles_trigonometry.md`;
- `area_volume.md`;
- `circles.md`;
- slope and similarity.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я работаю с complementary/supplementary/vertical angles.
- [ ] Я применяю triangle angle sum и transversal rules.
- [ ] Я различаю similarity и congruence.
- [ ] Я использую SSS/SAS/ASA/AAS и scale factor.
