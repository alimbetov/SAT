# Right Triangles and Trigonometry — прямоугольные треугольники и тригонометрия

## 1. Заголовок и краткое описание

**Right triangles and trigonometry** — официальный SAT skill. Нужно применять Pythagorean theorem, special right triangles, similarity и базовые `sin`, `cos`, `tan` для поиска сторон и углов.

> **Главная идея:** сначала определите, какие стороны известны относительно выбранного угла: opposite, adjacent, hypotenuse.

---

## 2. Ключевые понятия и формулы

| Понятие | Формула |
|---|---|
| Pythagorean theorem | `a²+b²=c²` |
| sine | `sin θ = opposite/hypotenuse` |
| cosine | `cos θ = adjacent/hypotenuse` |
| tangent | `tan θ = opposite/adjacent` |
| 45-45-90 | `x, x, x√2` |
| 30-60-90 | `x, x√3, 2x` |

### SOH–CAH–TOA

- **SOH**: Sine = Opposite / Hypotenuse
- **CAH**: Cosine = Adjacent / Hypotenuse
- **TOA**: Tangent = Opposite / Adjacent

### Визуальный якорь

Hypotenuse всегда:

- напротив угла `90°`;
- самая длинная сторона right triangle.

---

## 3. Пошаговый разбор — Guided Example

A right triangle has legs 6 and 8. Find the hypotenuse and `sin θ` if `θ` is opposite the side of length 6.

### Шаг 1. Pythagorean theorem

```math
6^2+8^2=c^2
```

```math
36+64=100=c^2
```

```math
c=10.
```

### Шаг 2. Определяем стороны относительно `θ`

- opposite = 6;
- hypotenuse = 10.

### Шаг 3. Используем sine

```math
\sin\theta=\frac6{10}=\frac35.
```

Почему не tangent? Потому что нам уже известны opposite и hypotenuse, а sine использует именно эту пару.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Grid-in

A right triangle has legs 3 and 4. Find the hypotenuse.

### Problem 2 — Easy — Multiple Choice

In a right triangle, relative to angle `θ`, opposite=5 and hypotenuse=13. What is `sin θ`?

**A)** `5/12`  **B)** `5/13`  **C)** `12/13`  **D)** `13/5`

### Problem 3 — Medium — Multiple Choice

In a 45-45-90 triangle, each leg has length 7. What is the hypotenuse?

**A)** `7`  **B)** `7√2`  **C)** `14`  **D)** `14√2`

### Problem 4 — Medium — Grid-in

In a 30-60-90 triangle, the shortest side is 4. Find the hypotenuse.

### Problem 5 — Hard — Multiple Choice

A right triangle has `tan θ=3/4` and hypotenuse 10. What is the side opposite `θ`?

**A)** 3  **B)** 4  **C)** 6  **D)** 8

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **5**.  
2. **B**, opposite/hypotenuse.  
3. **B**, `x√2`.  
4. **8**, hypotenuse=`2x`.  
5. **C**: ratio 3:4:5, scaled by 2 → opposite 6, adjacent 8, hypotenuse 10.

</details>

---

## 5. Common Traps — типичные ловушки

- Называть adjacent стороной, которая на самом деле hypotenuse.
- Использовать Pythagorean theorem в non-right triangle.
- Путать отношения special right triangles.

---

## 6. Стратегия для Digital SAT

Если даны sides и нужно trig ratio, часто угол вычислять **не нужно**. Просто используйте нужное отношение. В Desmos можно вычислить `sin`, `cos`, `tan` и inverse trig, но проверьте режим углов и контекст задачи.

При тройках `3-4-5`, `5-12-13`, `8-15-17` узнавание шаблона экономит время.

---

## 7. Связи с другими темами

**Опирается на:** radicals, equations, similar triangles.  
**Связано с:** circles/unit-circle ideas, distance, slope, geometry modeling.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я использую Pythagorean theorem.
- [ ] Я знаю 45-45-90 и 30-60-90 ratios.
- [ ] Я выбираю sin/cos/tan по известным сторонам.
- [ ] Я различаю opposite, adjacent и hypotenuse.
