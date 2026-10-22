# Circles — Pedagogy V2

## 1. Зачем эта тема нужна на SAT

Circles на SAT — это не одна тема, а несколько повторяющихся паттернов: radius/diameter, arc/sector как доля круга, tangent geometry, degrees/radians, unit circle и coordinate-circle equations.

Главная цель — быстро распознать, **к какой семье относится вопрос**.

> **Главная идея:** circle = все точки на одном расстоянии `r` от center.

### Mental model

```text
WHAT KIND OF CIRCLE QUESTION?
        ↓
measure? arc? angle? tangent? coordinates? radians?
        ↓
choose one pattern
        ↓
solve
        ↓
check geometric meaning
```

---

## 2. Pattern Map

| Что спрашивают | Pattern | Главная идея |
|---|---|---|
| radius / diameter | size | `d=2r` |
| circumference | boundary | `2πr` |
| area | inside region | `πr²` |
| arc length | fraction of circumference | angle fraction × `2πr` |
| sector area | fraction of area | angle fraction × `πr²` |
| tangent | right angle | radius ⟂ tangent |
| inscribed angle | half central angle | same arc |
| degrees ↔ radians | unit conversion | `180°=π` |
| point on unit circle | trig coordinates | `(cosθ,sinθ)` |
| circle equation | center-distance model | `(x-h)²+(y-k)²=r²` |
| expanded equation | completing square | reveal center/radius |

---

## 3. Pattern A — radius, diameter, circumference, area

### Anchor

```math
d=2r
```

```math
C=2\pi r=\pi d
```

```math
A=\pi r^2
```

### Worked Example 1

A circle has diameter 14.

Radius:

```math
r=7
```

Circumference:

```math
C=14\pi
```

Area:

```math
A=49\pi
```

### Error pattern

If SAT gives diameter, convert to radius before using `πr²`.

---

## 4. Pattern B — arc length and sector area

Both are just **fractions of a full circle**.

### Degree form

```math
\text{fraction}=\frac{\theta}{360}
```

Arc:

```math
L=\frac{\theta}{360}(2\pi r)
```

Sector:

```math
A_{sector}=\frac{\theta}{360}(\pi r^2)
```

### Worked Example 2

Radius 10, central angle 72°.

Fraction of circle:

```math
\frac{72}{360}=\frac15
```

Arc length:

```math
\frac15(20\pi)=4\pi
```

Sector area:

```math
\frac15(100\pi)=20\pi
```

### Mental anchor

```text
ARC = slice of circumference
SECTOR = slice of area
```

---

## 5. Pattern C — radians

The conversion anchor:

```math
180^\circ=\pi\text{ radians}
```

### Degrees → radians

```math
\theta_{rad}=\theta_{deg}\cdot\frac{\pi}{180}
```

### Radians → degrees

```math
\theta_{deg}=\theta_{rad}\cdot\frac{180}{\pi}
```

### Worked Example 3

Convert 60°:

```math
60\cdot\frac\pi{180}=\frac\pi3
```

### High-value values

```text
30° = π/6
45° = π/4
60° = π/3
90° = π/2
180° = π
360° = 2π
```

---

## 6. Pattern D — arc length in radians

If angle is already in radians:

```math
s=r\theta
```

### Worked Example 4

Radius 6, angle `π/3`.

```math
s=6\cdot\frac\pi3=2\pi
```

### Trap

Do **not** use `s=rθ` with degrees unless you convert first.

---

## 7. Pattern E — central vs inscribed angle

For the **same intercepted arc**:

```math
\text{inscribed angle}=\frac12(\text{central angle})
```

### Worked Example 5

Central angle = 100°.

Inscribed angle intercepting same arc:

```math
50^\circ
```

### Recognition cue

Ask:

> Do both angles intercept the same arc?

If not, the simple half-rule may not apply directly.

---

## 8. Pattern F — tangent geometry

At point of tangency:

```text
radius ⟂ tangent
```

So angle = 90°.

### Worked Example 6

A radius to tangent point has length 9. An external point is 12 units from tangent point. Find distance from center to external point.

The radius and tangent segment form a right triangle:

```math
9^2+12^2=d^2
```

```math
d=15
```

### Transfer

Circle tangent questions often secretly become right-triangle questions.

---

## 9. Pattern G — standard equation of a circle

```math
(x-h)^2+(y-k)^2=r^2
```

### Read it directly

```math
(x-3)^2+(y+2)^2=25
```

means:

```text
center = (3,-2)
radius = 5
```

### Mental anchor

Signs inside parentheses are opposite the center coordinates.

```text
(x - h) → center x = h
(y + 2) → center y = -2
```

---

## 10. Why the equation makes sense

For any point `(x,y)` on the circle, distance from `(h,k)` to `(x,y)` equals `r`:

```math
\sqrt{(x-h)^2+(y-k)^2}=r
```

Square both sides:

```math
(x-h)^2+(y-k)^2=r^2
```

So the circle equation is just the **distance formula with fixed distance**.

This connection is more useful than rote memorization.

---

## 11. Pattern H — completing the square

### Worked Example 7

```math
x^2+y^2-6x+4y-12=0
```

Move constant:

```math
x^2-6x+y^2+4y=12
```

Complete x-square:

```math
x^2-6x+9=(x-3)^2
```

Complete y-square:

```math
y^2+4y+4=(y+2)^2
```

Add both values to both sides:

```math
(x-3)^2+(y+2)^2=25
```

Therefore:

```text
center = (3,-2)
radius = 5
```

### Recognition cue

If you see:

```text
x² + y² + linear x + linear y + constant = 0
```

think:

```text
COMPLETE TWO SQUARES
```

---

## 12. Pattern I — unit circle

Unit circle:

```math
x^2+y^2=1
```

At angle `θ`:

```math
(x,y)=(\cos\theta,\sin\theta)
```

### Anchor

```text
x-coordinate = cos
 y-coordinate = sin
```

### Core points

| Angle | Point |
|---|---|
| `0` | `(1,0)` |
| `π/6` | `(√3/2,1/2)` |
| `π/4` | `(√2/2,√2/2)` |
| `π/3` | `(1/2,√3/2)` |
| `π/2` | `(0,1)` |

### Worked Example 8

At `θ=π/3`:

```math
(\cos\theta,\sin\theta)=\left(\frac12,\frac{\sqrt3}{2}\right)
```

---

## 13. Decision Tree

```text
Circle question
│
├─ radius/diameter/circumference/area?
│   └─ basic circle formulas
│
├─ arc or sector?
│   └─ fraction of full circle
│
├─ radians?
│   ├─ convert using 180°=π
│   └─ arc with radians → s=rθ
│
├─ tangent?
│   └─ radius ⟂ tangent → right triangle
│
├─ inscribed angle?
│   └─ half central angle on same arc
│
├─ standard coordinate equation?
│   └─ read center/radius
│
├─ expanded coordinate equation?
│   └─ complete square twice
│
└─ unit circle?
    └─ (cosθ,sinθ)
```

---

## 14. SAT Language Decoder

| Phrase | Meaning |
|---|---|
| `subtends an arc` | angle intercepts that arc |
| `central angle` | vertex at center |
| `inscribed angle` | vertex on circle |
| `point of tangency` | tangent touches circle there |
| `unit circle` | radius 1 |
| `centered at (h,k)` | use `(x-h)²+(y-k)²` |
| `arc length` | part of circumference |
| `sector` | wedge-shaped part of area |

---

## 15. Faded Examples

### Example A

Radius 8, central angle 90°. Find arc length.

**Fraction of circle:** ______

**Arc:** ______

<details><summary>Проверка</summary>

```math
\frac{90}{360}=\frac14
```

```math
\frac14(16\pi)=4\pi
```
</details>

### Example B

Circle:

```math
(x+4)^2+(y-1)^2=36
```

Center = ______

Radius = ______

<details><summary>Проверка</summary>

```text
center = (-4,1)
radius = 6
```
</details>

### Example C

At angle `π/6` on unit circle, y-coordinate = ______.

<details><summary>Проверка</summary>

```math
\sin\frac\pi6=\frac12
```
</details>

---

## 16. Error Clinic

### Error 1 — use diameter as radius

Wrong:

```math
A=\pi d^2
```

Correct:

```math
r=d/2
```

then `A=πr²`.

### Error 2 — confuse arc and sector

Arc is length → linear units.

Sector is area → square units.

### Error 3 — wrong sign of center

```math
(x+3)^2
```

means center x-coordinate `-3`.

### Error 4 — `s=rθ` with degrees

`θ` must be radians.

### Error 5 — unit-circle order reversed

Always:

```text
(cos, sin)
```

---

## 17. Digital SAT / Desmos Strategy

Desmos is useful for coordinate circles:

```text
(x-3)^2+(y+2)^2=25
```

You can inspect center and intersections visually.

But use manual recognition for:

- radius/diameter;
- fractions of circle;
- standard radian conversions;
- unit-circle special angles.

For expanded equations, completing the square is often faster than graphing if center/radius are specifically requested.

---

## 18. Independent SAT-Style Practice

### Problem 1 — Easy — Grid-in

A circle has radius 7. Find diameter.

### Problem 2 — Easy — Multiple Choice

Convert `60°` to radians.

**A)** `π/6`  
**B)** `π/3`  
**C)** `2π/3`  
**D)** `3π`

### Problem 3 — Medium — Multiple Choice

What is the center of

```math
(x-3)^2+(y+2)^2=25?
```

**A)** `(3,2)`  
**B)** `(-3,2)`  
**C)** `(3,-2)`  
**D)** `(-3,-2)`

### Problem 4 — Medium — Grid-in

Radius 10, central angle 72°. What is arc length divided by `π`?

### Problem 5 — Hard — Multiple Choice

On unit circle, `θ=π/3` corresponds to:

**A)** `(√3/2,1/2)`  
**B)** `(1/2,√3/2)`  
**C)** `(-1/2,√3/2)`  
**D)** `(1,0)`

<details>
<summary><strong>Ответы</strong></summary>

1. `14`  
2. **B**  
3. **C**  
4. `4`  
5. **B**

</details>

---

## 19. Transfer Questions

1. Why does the circle equation come directly from distance formula?
2. Why is an inscribed angle half a central angle on the same arc?
3. Why does tangent geometry often create a right triangle?
4. How can you tell whether to use degree-fraction formula or `s=rθ`?
5. Why are unit-circle coordinates `(cos,sin)` rather than `(sin,cos)`?

---

## 20. Мини-чек-лист

- [ ] Я отличаю radius и diameter.
- [ ] Я вижу arc/sector как fraction of full circle.
- [ ] Я перевожу degrees ↔ radians.
- [ ] Я использую `s=rθ` только с radians.
- [ ] Я применяю radius ⟂ tangent.
- [ ] Я связываю central/inscribed angles.
- [ ] Я читаю center/radius из standard equation.
- [ ] Я выполняю completing the square для circle equation.
- [ ] Я использую `(cosθ,sinθ)` на unit circle.
