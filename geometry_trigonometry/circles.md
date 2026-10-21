# Circles — окружности

## 1. Заголовок и краткое описание

**Circles** — официальный skill Geometry and Trigonometry. На SAT нужно работать с radius, diameter, circumference, area, arcs, sectors, central angles, tangent lines и equation of a circle.

> **Главная идея:** почти все circle questions сводятся к доле полного круга `360°` или к расстоянию от center до точки.

---

## 2. Ключевые понятия и формулы

| Понятие | Формула / правило |
|---|---|
| diameter | `d=2r` |
| circumference | `C=2πr=πd` |
| area | `A=πr²` |
| full circle | `360°` |
| arc length | `(θ/360)·2πr` |
| sector area | `(θ/360)·πr²` |
| circle equation | `(x-h)²+(y-k)²=r²` |
| tangent | perpendicular to radius at point of tangency |

### Визуальный якорь

Arc и sector — это **доля круга**:

```math
\frac{\theta}{360}.
```

Эту долю умножаем либо на circumference, либо на area.

---

## 3. Пошаговый разбор — Guided Example

A circle has radius 6. A sector has central angle 120°. Find the sector area.

### Шаг 1. Находим долю полного круга

```math
\frac{120}{360}=\frac13.
```

### Шаг 2. Находим full circle area

```math
A=\pi(6)^2=36\pi.
```

### Шаг 3. Берём одну треть

```math
\frac13\cdot36\pi=12\pi.
```

Почему используем area, а не circumference? Потому что спрашивается **sector area**, то есть часть поверхности круга.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Grid-in

A circle has radius 7. What is its diameter?

### Problem 2 — Easy — Multiple Choice

A circle has radius 4. What is its circumference?

**A)** `4π`  **B)** `8π`  **C)** `16π`  **D)** `32π`

### Problem 3 — Medium — Multiple Choice

What is the center of

```math
(x-3)^2+(y+2)^2=25?
```

**A)** `(3,2)`  **B)** `(-3,2)`  **C)** `(3,-2)`  **D)** `(-3,-2)`

### Problem 4 — Medium — Grid-in

A 90° arc is what fraction of a full circle? Enter the decimal.

### Problem 5 — Hard — Multiple Choice

A circle has radius 10. What is the length of an arc subtended by a 72° central angle?

**A)** `2π`  **B)** `4π`  **C)** `10π`  **D)** `20π`

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **14**.  
2. **B**, `2πr=8π`.  
3. **C**, center `(h,k)=(3,-2)`.  
4. **0.25**, `90/360=1/4`.  
5. **B**, `(72/360)·20π=4π`.

</details>

---

## 5. Common Traps — типичные ловушки

- Подставить diameter вместо radius в `πr²`.
- Перепутать arc length и sector area.
- Ошибиться со знаком center: `(x-h)²+(y-k)²`, поэтому `(y+2)²` означает `k=-2`.

---

## 6. Стратегия для Digital SAT

Desmos отлично строит circle equations, например:

```text
(x-3)^2+(y+2)^2=25
```

Это помогает увидеть center и radius и проверить intersections. Для arc/sector задач быстрее сначала найти fraction `θ/360`, затем умножить на full circumference/area.

---

## 7. Связи с другими темами

**Опирается на:** area, radicals, coordinate geometry, right triangles.  
**Связано с:** tangent-radius right angles, distance formula, trigonometry.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я различаю radius и diameter.
- [ ] Я считаю circumference и area.
- [ ] Я нахожу arc length и sector area.
- [ ] Я читаю center и radius из equation of a circle.
