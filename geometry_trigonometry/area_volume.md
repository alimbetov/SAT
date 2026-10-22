# Area, Perimeter, Surface Area, and Volume — Pedagogy V2

## 1. Зачем эта тема нужна на SAT

В задачах на площадь и объём основная сложность обычно не в формуле, а в том, чтобы понять **что именно измеряют**, какие размеры относятся к нужной фигуре и как меняется результат при масштабировании.

> **Главная идея:** сначала определите dimension of the answer — length, square units или cubic units. Это почти всегда подсказывает нужный тип формулы.

### Mental model

```text
WHAT IS ASKED?
      ↓
1D / 2D / 3D?
      ↓
WHICH SHAPE?
      ↓
WHICH DIMENSIONS MATTER?
      ↓
FORMULA / SCALE RULE
      ↓
CHECK UNITS
```

---

## 2. Pattern Map

| Что спрашивают | Dimension | Pattern |
|---|---:|---|
| perimeter / circumference | 1D | boundary length |
| area | 2D | square units |
| surface area | 2D surfaces of 3D object | sum of face areas |
| volume | 3D | cubic units |
| scale factor | depends | `k`, `k²`, `k³` |
| missing dimension | algebra + geometry | solve formula backward |
| composite figure | split/add/subtract | decompose into known shapes |

### Visual anchor

```text
LENGTH  → k
AREA    → k²
VOLUME  → k³
```

---

## 3. Formula families — не учим как случайный список

### Rectangles

```math
P=2l+2w
```

```math
A=lw
```

### Triangles

```math
A=\frac12bh
```

Важно: `h` — **perpendicular height**, а не любая сторона.

### Circles

```math
C=2\pi r
```

```math
A=\pi r^2
```

### Prisms

```math
V=(\text{base area})\cdot h
```

Это универсальный pattern.

Rectangular prism:

```math
V=lwh
```

Cylinder:

```math
V=\pi r^2h
```

### Surface area

Surface area = сумма площадей всех внешних surfaces.

Для closed cylinder:

```math
SA=2\pi r^2+2\pi rh
```

---

## 4. Pattern A — perimeter vs area

### Worked Example 1

A rectangle has length 9 and width 4. Find both perimeter and area.

### Recognize

- perimeter = boundary length;
- area = region inside.

### Solve

```math
P=2(9)+2(4)=26
```

```math
A=9\cdot4=36
```

### Unit check

If dimensions are in cm:

```text
perimeter → 26 cm
area      → 36 cm²
```

### Pattern cue

Если answer unit должен быть squared, perimeter formula точно не подходит.

---

## 5. Pattern B — area from hidden height/base

### Worked Example 2

A triangle has base 12 and perpendicular height 7. Find its area.

```math
A=\frac12(12)(7)=42
```

### Trap

Если дана slanted side 7, но она не perpendicular to base, её нельзя автоматически использовать как height.

---

## 6. Pattern C — volume as base area × height

### Worked Example 3

A cylinder has radius 3 and height 8.

Base area:

```math
\pi(3)^2=9\pi
```

Then:

```math
V=(9\pi)(8)=72\pi
```

### Mental anchor

```text
VOLUME OF PRISM/CYLINDER
=
AREA OF ONE BASE × DISTANCE THROUGH THE SOLID
```

Это помогает не запоминать `πr²h` как отдельную магическую формулу.

---

## 7. Pattern D — surface area as “unwrap the object”

### Worked Example 4

Closed cylinder, `r=3`, `h=8`.

Есть:

- 2 circles;
- 1 curved rectangle-like lateral surface.

So:

```math
SA=2\pi r^2+2\pi rh
```

```math
=2\pi(9)+2\pi(3)(8)
```

```math
=18\pi+48\pi=66\pi
```

### Recognition cue

Если container **open at top**, одной circular base может не быть в surface area.

Context matters.

---

## 8. Pattern E — scale factors

Это один из самых частых SAT geometry patterns.

Если linear dimensions change by factor `k`:

```math
length\to k
```

```math
area\to k^2
```

```math
volume\to k^3
```

### Worked Example 5

Every dimension of a solid doubles.

```math
k=2
```

Volume factor:

```math
2^3=8
```

Не нужно вычислять старый или новый volume.

### Transfer

Если side lengths decrease by 20%, linear factor is:

```math
0.8
```

Area factor:

```math
0.8^2=0.64
```

So area decreases by 36%, not 20%.

---

## 9. Pattern F — solve formula backward

### Worked Example 6

A rectangular prism has volume 240, length 10, width 6. Find height.

```math
240=10\cdot6\cdot h
```

```math
240=60h
```

```math
h=4
```

### Recognition cue

Geometry formula can become an ordinary algebra equation.

---

## 10. Pattern G — composite figures

### Mental model

```text
COMPLICATED FIGURE
=
SIMPLE SHAPE ± SIMPLE SHAPE
```

### Example

A 10×8 rectangle has a 3×2 rectangular corner removed.

Original area:

```math
80
```

Removed area:

```math
6
```

Remaining:

```math
74
```

### Trap

Не пытайтесь искать «новую специальную формулу» для irregular shape, если её можно разложить.

---

## 11. Decision Tree

```text
What does the question ask?
│
├─ boundary length → perimeter/circumference
├─ inside 2D region → area
├─ outside of 3D object → surface area
├─ space inside 3D object → volume
├─ resized similar figure → k / k² / k³
├─ missing dimension → formula + algebra
└─ weird composite shape → split/add/subtract
```

---

## 12. SAT Language Decoder

| Phrase | Meaning |
|---|---|
| `perimeter` | total outer boundary length |
| `circumference` | perimeter of circle |
| `area` | 2D region |
| `surface area` | sum of outside surfaces |
| `volume` | 3D space inside |
| `closed cylinder` | both circular ends included |
| `open-top container` | top surface excluded |
| `similar solids` | corresponding lengths use one scale factor |
| `all dimensions are doubled` | volume ×8, area ×4 |

---

## 13. Units as a built-in error detector

| Quantity | Typical units |
|---|---|
| length | cm |
| area | cm² |
| volume | cm³ |

If you get:

```text
volume = 72 cm²
```

something is wrong.

### Dimensional reasoning

```math
(length)(length)=area
```

```math
(area)(length)=volume
```

---

## 14. Faded Examples

### Example A

A square has side 6. What is its area?

**Quantity type:** __________

**Formula:** __________

<details><summary>Проверка</summary>

```math
A=6^2=36
```
</details>

### Example B

All dimensions of a cube triple.

**Linear factor:** ______

**Area factor:** ______

**Volume factor:** ______

<details><summary>Проверка</summary>

`3`, `9`, `27`
</details>

### Example C

A cylinder has volume `100π` and radius 5. Find height.

<details><summary>Проверка</summary>

```math
100\pi=\pi(25)h
```

```math
h=4
```
</details>

---

## 15. Error Clinic

### Error 1 — diameter used as radius

If diameter = 10:

```math
r=5
```

Not 10.

### Error 2 — area scales linearly

Wrong:

```text
side ×3 → area ×3
```

Correct:

```text
side ×3 → area ×9
```

### Error 3 — wrong units

Area is never measured in cubic units.

### Error 4 — surface area vs volume

Painting the outside → surface area.

Filling the inside → volume.

---

## 16. Digital SAT Strategy

Before calculating, write mentally:

```text
ASKED:
GIVEN:
UNITS:
SHAPE:
```

This prevents most formula-selection errors.

Desmos is useful for arithmetic with `π`, powers, roots, but not for choosing geometry structure.

For scale-factor questions, avoid unnecessary full calculations.

---

## 17. Independent SAT-Style Practice

### Problem 1 — Easy — Grid-in

A rectangle has length 9 and width 4. Find its area.

### Problem 2 — Easy — Multiple Choice

What is the perimeter of a rectangle with sides 7 and 5?

**A)** 12  
**B)** 24  
**C)** 35  
**D)** 70

### Problem 3 — Medium — Multiple Choice

A circle has radius 5. What is its area?

**A)** `10π`  
**B)** `20π`  
**C)** `25π`  
**D)** `50π`

### Problem 4 — Medium — Grid-in

A rectangular prism measures `3×4×10`. Find its volume.

### Problem 5 — Hard — Multiple Choice

Every linear dimension of a solid is multiplied by 1.5. By what factor does its volume change?

**A)** 1.5  
**B)** 2.25  
**C)** 3.375  
**D)** 4.5

<details>
<summary><strong>Ответы</strong></summary>

1. `36`  
2. **B**  
3. **C**  
4. `120`  
5. **C**, `1.5³=3.375`

</details>

---

## 18. Transfer Questions

1. Why does doubling all lengths multiply area by 4?
2. Why is cylinder volume naturally `base area × height`?
3. How can units reveal that you used a perimeter formula instead of area?
4. If a figure's area increases by factor 9, what length scale factor is consistent with similar figures?

---

## 19. Мини-чек-лист

- [ ] Я сначала определяю dimension of the answer.
- [ ] Я различаю perimeter, area, surface area и volume.
- [ ] Я вижу volume as base area × height.
- [ ] Я использую `k`, `k²`, `k³` без лишних вычислений.
- [ ] Я решаю missing-dimension задачи через algebra.
- [ ] Я проверяю answer units.
