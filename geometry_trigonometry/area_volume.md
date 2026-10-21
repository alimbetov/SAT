# Area, Perimeter, Surface Area, and Volume — площадь, периметр, поверхность и объём

## 1. Заголовок и краткое описание

**Area and volume** — официальный skill Geometry and Trigonometry. На SAT сюда входят не только площади и объёмы, но и **perimeter**, **surface area**, реальные модели фигур и scale factors. Нужно выбрать правильную формулу и понять, как изменение линейного размера влияет на площадь и объём.

> **Главная идея:** длины масштабируются как `k`, площади как `k²`, объёмы как `k³`.

---

## 2. Ключевые понятия и формулы

| Фигура / величина | Формула |
|---|---|
| rectangle perimeter | `P=2l+2w` |
| rectangle area | `A=lw` |
| triangle area | `A=1/2 bh` |
| circle area | `A=πr²` |
| circle circumference | `C=2πr` |
| rectangular prism volume | `V=lwh` |
| rectangular prism surface area | `SA=2lw+2lh+2wh` |
| cylinder volume | `V=πr²h` |
| cylinder surface area | `SA=2πr²+2πrh` |
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

Например, если side length увеличилась в 3 раза:

- perimeter / length → ×3;
- area → ×9;
- volume → ×27.

### Вопрос к читателю

Если radius цилиндра удвоить, а height оставить прежней, во сколько раз изменится volume?

---

## 3. Пошаговый разбор — Guided Example

A closed cylinder has radius `3` and height `8`. Find its volume and surface area.

### Шаг 1. Volume

```math
V=\pi r^2h
```

```math
V=\pi(3)^2(8)=72\pi.
```

### Шаг 2. Surface area

У закрытого цилиндра есть две circular bases и боковая поверхность:

```math
SA=2\pi r^2+2\pi rh.
```

Подставляем:

```math
SA=2\pi(3)^2+2\pi(3)(8)
```

```math
SA=18\pi+48\pi=66\pi.
```

### Шаг 3. Проверяем units

- Volume → cubic units.
- Surface area → square units.

Почему это важная проверка? Неверная размерность часто сразу показывает, что выбрана неправильная формула.

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Grid-in

A rectangle has length 9 and width 4. Find its area.

### Problem 2 — Easy — Multiple Choice

What is the perimeter of a rectangle with sides 7 and 5?

**A)** 12  **B)** 24  **C)** 35  **D)** 70

### Problem 3 — Medium — Multiple Choice

A circle has radius 5. What is its area?

**A)** `10π`  **B)** `20π`  **C)** `25π`  **D)** `50π`

### Problem 4 — Medium — Grid-in

A rectangular prism measures `3×4×10`. What is its volume?

### Problem 5 — Hard — Multiple Choice

All dimensions of a solid are doubled. By what factor does its volume change?

**A)** 2  **B)** 4  **C)** 6  **D)** 8

<details>
<summary><strong>Ответы и краткие решения</strong></summary>

1. **36**, `9·4`.  
2. **B**, `2(7)+2(5)=24`.  
3. **C**, `π·5²=25π`.  
4. **120**, `3·4·10`.  
5. **D**, volume factor `2³=8`.

</details>

---

## 5. Common Traps — типичные ловушки

### Ловушка 1. Путать perimeter, area и surface area

- perimeter — длина границы 2D-фигуры;
- area — площадь 2D-фигуры;
- surface area — суммарная площадь внешних поверхностей 3D-фигуры.

### Ловушка 2. Использовать diameter как radius

Если `d=10`, то `r=5`.

### Ловушка 3. Неверно масштабировать

Scale factor `k=2` не означает, что area тоже увеличивается в 2 раза. Area изменяется в `2²=4` раза.

---

## 6. Стратегия для Digital SAT

Desmos полезен как вычислитель для `π`, powers и roots, но не заменяет выбор формулы.

Перед вычислением задайте три вопроса:

1. Что спрашивают: length, perimeter, area, surface area или volume?
2. Какие dimensions даны?
3. Какие units должен иметь ответ?

Если задача про scale factor, часто вообще не нужно вычислять исходные площадь или объём — используйте `k`, `k²`, `k³` напрямую.

---

## 7. Связи с другими темами

**Опирается на:** algebra, exponents, unit conversions.  
**Связано с:**
- `circles.md`;
- similarity and scale factor;
- right triangles;
- ratios, rates, and units.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я различаю perimeter, area, surface area и volume.
- [ ] Я выбираю правильную формулу для standard figures.
- [ ] Я проверяю square/cubic units.
- [ ] Я применяю `k`, `k²`, `k³` при масштабировании.
