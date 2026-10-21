# Circles — окружности, radians и unit circle

## 1. Заголовок и краткое описание

**Circles** — официальный skill Geometry and Trigonometry. На SAT сюда входят radius/diameter, circumference, area, tangents, central/inscribed angles, arcs, sectors, **degrees ↔ radians**, **unit circle**, equation of a circle, distance formula и completing the square.

> **Главная идея:** круг связывает геометрию и координаты: расстояние от center до любой точки окружности всегда равно radius.

---

## 2. Ключевые понятия и формулы

| Понятие | Формула / правило |
|---|---|
| diameter | `d=2r` |
| circumference | `C=2πr=πd` |
| area | `A=πr²` |
| full circle | `360° = 2π radians` |
| arc length | `(θ/360)·2πr` или `s=rθ` при θ в radians |
| sector area | `(θ/360)·πr²` |
| circle equation | `(x-h)²+(y-k)²=r²` |
| distance | `d=√((x₂-x₁)²+(y₂-y₁)²)` |
| tangent-radius | tangent ⟂ radius at point of tangency |

### Degrees and radians

```math
180^\circ=\pi\text{ radians}
```

Поэтому:

```math
\text{radians}=\text{degrees}\cdot\frac{\pi}{180}
```

```math
\text{degrees}=\text{radians}\cdot\frac{180}{\pi}.
```

Примеры:

```math
90^\circ=\frac\pi2,\quad60^\circ=\frac\pi3,\quad45^\circ=\frac\pi4.
```

### Unit circle

Unit circle имеет radius `1` и equation:

```math
x^2+y^2=1.
```

Точка, соответствующая углу `θ`, имеет coordinates:

```math
(\cos\theta,\sin\theta).
```

Полезные значения:

| θ | `(cos θ, sin θ)` |
|---|---|
| `0` | `(1,0)` |
| `π/6` | `(√3/2, 1/2)` |
| `π/4` | `(√2/2, √2/2)` |
| `π/3` | `(1/2, √3/2)` |
| `π/2` | `(0,1)` |

### Central and inscribed angles

Для одной и той же arc:

```math
inscribed\ angle=\frac12(central\ angle).
```

### Completing the square для equation of a circle

Например:

```math
x^2+y^2-6x+4y-12=0.
```

Группируем:

```math
(x^2-6x)+(y^2+4y)=12.
```

Дополняем квадраты:

```math
(x-3)^2+(y+2)^2=25.
```

Center `(3,-2)`, radius `5`.

### Визуальный якорь

- Arc/sector = доля полного круга.
- Circle equation = **distance from center = r**.
- Unit circle point = `(cos, sin)`.

---

## 3. Пошаговый разбор — Guided Example

A circle is represented by

```math
x^2+y^2-6x+4y-12=0.
```

Find its center and radius.

### Шаг 1. Переносим constant

```math
x^2-6x+y^2+4y=12.
```

### Шаг 2. Complete the square для x

Половина `-6` равна `-3`; квадрат — `9`:

```math
x^2-6x+9=(x-3)^2.
```

### Шаг 3. Complete the square для y

Половина `4` равна `2`; квадрат — `4`:

```math
y^2+4y+4=(y+2)^2.
```

Добавляем `9+4` к обеим сторонам:

```math
(x-3)^2+(y+2)^2=25.
```

### Шаг 4. Читаем свойства

Center:

```math
(3,-2)
```

Radius:

```math
r=\sqrt{25}=5.
```

Почему completing the square полезен? Он преобразует equation в standard circle form, где center и radius видны напрямую.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Grid-in

A circle has radius 7. What is its diameter?

### Problem 2 — Easy — Multiple Choice

Convert `60°` to radians.

**A)** `π/6`  **B)** `π/3`  **C)** `2π/3`  **D)** `3π`

### Problem 3 — Medium — Multiple Choice

What is the center of

```math
(x-3)^2+(y+2)^2=25?
```

**A)** `(3,2)`  **B)** `(-3,2)`  **C)** `(3,-2)`  **D)** `(-3,-2)`

### Problem 4 — Medium — Grid-in

A circle has radius 10. A central angle is `72°`. What is the arc length divided by `π`?

### Problem 5 — Hard — Multiple Choice

On the unit circle, an angle `θ=π/3` corresponds to which point?

**A)** `(√3/2,1/2)`  
**B)** `(1/2,√3/2)`  
**C)** `(-1/2,√3/2)`  
**D)** `(1,0)`

<details>
<summary><strong>Ответы и краткие решения</strong></summary>

1. **14**.  
2. **B**, `60·π/180=π/3`.  
3. **C**, standard form gives center `(3,-2)`.  
4. **4**, arc=`(72/360)·20π=4π`.  
5. **B**, `(cos π/3, sin π/3)=(1/2,√3/2)`.

</details>

---

## 5. Common Traps — типичные ловушки

### Ловушка 1. Перепутать signs центра

В `(x-h)²+(y-k)²=r²` знаки внутри скобок противоположны coordinates center.

### Ловушка 2. Использовать formula `s=rθ` с degrees

В `s=rθ` угол `θ` должен быть в **radians**.

### Ловушка 3. Путать unit-circle coordinates

Порядок всегда:

```text
(cos θ, sin θ)
```

не наоборот.

### Ловушка 4. Tangent не параллелен radius

В точке касания tangent и radius **perpendicular**.

---

## 6. Стратегия для Digital SAT

Desmos особенно полезен для coordinate-circle questions:

```text
(x-3)^2+(y+2)^2=25
```

можно построить напрямую и проверить center/intersections.

Для equations не в standard form используйте completing the square или график. Для unit-circle/radian задач полезнее запомнить базовые `30°/45°/60°` значения и conversion `180°=π`.

---

## 7. Связи с другими темами

**Опирается на:**
- `right_triangles_trigonometry.md`;
- radicals;
- coordinate plane;
- completing the square из quadratics.

**Связано с:**
- distance formula;
- unit-circle trigonometry;
- equation transformations;
- tangent/right-angle geometry.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я считаю circumference, area, arc length и sector area.
- [ ] Я перевожу degrees ↔ radians.
- [ ] Я использую `(cos θ, sin θ)` на unit circle.
- [ ] Я нахожу center/radius из equation, включая completing the square.
