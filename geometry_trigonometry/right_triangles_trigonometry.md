# Right Triangles and Trigonometry — прямоугольные треугольники и тригонометрия

## 1. Заголовок и краткое описание

**Right triangles and trigonometry** — официальный SAT skill. Нужно применять Pythagorean theorem, special right triangles, similarity, `sin`, `cos`, `tan` и связь тригонометрических функций complementary angles.

> **Главная идея:** сначала определите стороны относительно выбранного угла — opposite, adjacent, hypotenuse — и только потом выбирайте trig ratio.

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
| complementary identity | `sin θ = cos(90°-θ)` |
| complementary identity | `cos θ = sin(90°-θ)` |

### SOH–CAH–TOA

- **SOH**: Sine = Opposite / Hypotenuse
- **CAH**: Cosine = Adjacent / Hypotenuse
- **TOA**: Tangent = Opposite / Adjacent

### Почему complementary identity работает?

В right triangle два острых угла в сумме дают `90°`. Сторона, которая opposite для одного угла, является adjacent для другого. Hypotenuse остаётся той же.

Поэтому:

```math
\sin\theta=\cos(90^\circ-\theta).
```

### Визуальный якорь

Hypotenuse всегда:

- напротив `90°`;
- самая длинная сторона right triangle.

---

## 3. Пошаговый разбор — Guided Example

A right triangle has legs 6 and 8. Find the hypotenuse and `sin θ` if `θ` is opposite the side of length 6.

### Шаг 1. Pythagorean theorem

```math
6^2+8^2=c^2
```

```math
36+64=100
```

```math
c=10.
```

### Шаг 2. Определяем стороны относительно `θ`

- opposite = 6;
- adjacent = 8;
- hypotenuse = 10.

### Шаг 3. Используем sine

```math
\sin\theta=\frac6{10}=\frac35.
```

### Шаг 4. Проверяем complementary relation

Пусть второй острый угол равен `φ=90°-θ`. Для него adjacent side равна 6, поэтому:

```math
\cos\phi=\frac6{10}=\frac35.
```

Следовательно:

```math
\sin\theta=\cos\phi.
```

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Grid-in

A right triangle has legs 3 and 4. Find the hypotenuse.

### Problem 2 — Easy — Multiple Choice

Relative to angle `θ`, opposite=5 and hypotenuse=13. What is `sin θ`?

**A)** `5/12`  **B)** `5/13`  **C)** `12/13`  **D)** `13/5`

### Problem 3 — Medium — Multiple Choice

In a 45-45-90 triangle, each leg has length 7. What is the hypotenuse?

**A)** `7`  **B)** `7√2`  **C)** `14`  **D)** `14√2`

### Problem 4 — Medium — Grid-in

In a 30-60-90 triangle, the shortest side is 4. Find the hypotenuse.

### Problem 5 — Hard — Multiple Choice

If `sin 32° = k`, which expression also equals `k`?

**A)** `cos 32°`  
**B)** `cos 58°`  
**C)** `sin 58°`  
**D)** `tan 58°`

<details>
<summary><strong>Ответы и краткие решения</strong></summary>

1. **5**.  
2. **B**, opposite/hypotenuse.  
3. **B**, hypotenuse=`x√2`.  
4. **8**, hypotenuse=`2x`.  
5. **B**, `58°=90°-32°`, поэтому `sin32°=cos58°`.

</details>

---

## 5. Common Traps — типичные ловушки

### Ловушка 1. Неправильно определить adjacent

Adjacent — сторона рядом с выбранным acute angle, **кроме hypotenuse**.

### Ловушка 2. Использовать Pythagorean theorem в non-right triangle

Теорема применима только при угле `90°`.

### Ловушка 3. Учить sin/cos как отдельные несвязанные формулы

Для complementary angles они меняются местами:

```math
sin θ = cos(90°-θ).
```

---

## 6. Стратегия для Digital SAT

Если даны sides и нужен trig ratio, угол часто вычислять **не нужно**. Просто используйте SOH–CAH–TOA.

Desmos полезен для численных `sin`, `cos`, `tan` и inverse trig, но проверьте, что угол интерпретируется в нужных единицах.

Узнавание triples `3-4-5`, `5-12-13`, `8-15-17` и special triangles часто быстрее калькулятора.

---

## 7. Связи с другими темами

**Опирается на:** radicals, similar triangles, equations.  
**Связано с:**
- `circles.md` и unit-circle ideas;
- coordinate distance;
- slope;
- geometry modeling.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я применяю Pythagorean theorem.
- [ ] Я знаю ratios 45-45-90 и 30-60-90.
- [ ] Я выбираю sin/cos/tan по известным сторонам.
- [ ] Я использую `sin θ = cos(90°−θ)` и обратную связь.
