# Area and Volume — площади, объёмы и масштабирование

## 1. Заголовок и краткое описание

**Area and volume** — официальный skill Geometry and Trigonometry. На SAT нужно применять формулы к прямоугольникам, треугольникам, кругам, призмам, цилиндрам и задачам со scale factor.

> **Главная идея:** длины масштабируются как `k`, площади как `k²`, объёмы как `k³`.

---

## 2. Ключевые понятия и формулы

| Фигура | Формула |
|---|---|
| rectangle area | `A=lw` |
| triangle area | `A=1/2 bh` |
| circle area | `A=πr²` |
| rectangular prism volume | `V=lwh` |
| cylinder volume | `V=πr²h` |
| prism volume | `V=(base area)·h` |

### Scale factors

Если все линейные размеры умножить на `k`:

```math
length\ factor=k
```

```math
area\ factor=k^2
```

```math
volume\ factor=k^3.
```

### Визуальный якорь

**Length → k, Area → k², Volume → k³.**

---

## 3. Пошаговый разбор — Guided Example

A cylinder has radius 3 and height 8. What is its volume?

### Шаг 1. Выбираем правильную формулу

Cylinder:

```math
V=\pi r^2h.
```

Почему не `2πr`? Это circumference, а задача спрашивает volume.

### Шаг 2. Подставляем

```math
V=\pi(3)^2(8).
```

### Шаг 3. Вычисляем

```math
V=72\pi.
```

### Шаг 4. Проверяем units

Volume измеряется в **cubic units**, не square units.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Grid-in

A rectangle has length 9 and width 4. Find its area.

### Problem 2 — Easy — Multiple Choice

What is the area of a triangle with base 10 and height 6?

**A)** 16  **B)** 30  **C)** 60  **D)** 120

### Problem 3 — Medium — Multiple Choice

A circle has radius 5. What is its area?

**A)** `10π`  **B)** `20π`  **C)** `25π`  **D)** `50π`

### Problem 4 — Medium — Grid-in

A rectangular prism measures `3×4×10`. What is its volume?

### Problem 5 — Hard — Multiple Choice

All dimensions of a solid are doubled. By what factor does its volume change?

**A)** 2  **B)** 4  **C)** 6  **D)** 8

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **36**.  
2. **B**, `1/2·10·6=30`.  
3. **C**, `π·5²=25π`.  
4. **120**.  
5. **D**, volume factor `2³=8`.

</details>

---

## 5. Common Traps — типичные ловушки

- Использовать diameter вместо radius без деления на 2.
- Путать square units и cubic units.
- При scale factor применять `k` к area/volume вместо `k²`/`k³`.

---

## 6. Стратегия для Digital SAT

Desmos полезен как калькулятор для `π`, roots и сложных чисел, но ключевой шаг — выбрать правильную формулу. Перед вычислением выпишите, какая величина дана: radius, diameter, base area, height.

---

## 7. Связи с другими темами

**Опирается на:** algebra, exponents, circles.  
**Связано с:** similarity, scale factors, right triangles, unit conversions.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я выбираю правильную формулу area/volume.
- [ ] Я различаю radius и diameter.
- [ ] Я правильно работаю с units.
- [ ] Я применяю `k²` и `k³` при масштабировании.
