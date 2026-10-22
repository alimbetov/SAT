# Right Triangles and Trigonometry — Pedagogy V2

## 1. Зачем эта тема нужна на SAT

Большинство задач на right triangles решаются одним из нескольких повторяющихся паттернов. Главная ошибка ученика — выбирать формулу до того, как он понял, **какие стороны известны относительно угла**.

> **Главная идея:** сначала назовите sides относительно выбранного angle, потом выбирайте theorem или trig ratio.

### Mental model

```text
RIGHT TRIANGLE?
      ↓
WHAT IS KNOWN?
      ↓
SIDES ONLY? → PYTHAGOREAN / SPECIAL TRIANGLE
ANGLE + SIDES? → SOH-CAH-TOA
      ↓
SOLVE
      ↓
CHECK SIZE / TRIANGLE MEANING
```

---

## 2. Pattern Map

| Что видно | Pattern | Метод |
|---|---|---|
| two sides of right triangle | missing side | Pythagorean theorem |
| 45°-45°-90° | special triangle | `x,x,x√2` |
| 30°-60°-90° | special triangle | `x,x√3,2x` |
| opposite + hypotenuse | sine | SOH |
| adjacent + hypotenuse | cosine | CAH |
| opposite + adjacent | tangent | TOA |
| `sin θ` and complementary angle | cofunction | `sin θ=cos(90°-θ)` |
| angle unknown, sides known | inverse trig / Desmos | `sin⁻¹`, `cos⁻¹`, `tan⁻¹` |

---

## 3. First recognition: find the hypotenuse

Hypotenuse is always:

- opposite the `90°` angle;
- longest side of a right triangle.

### Visual anchor

```text
      /|
     / |
 hyp/  | leg
   /   |
  /____|
    leg
```

Never define adjacent before identifying the hypotenuse.

---

## 4. Pattern A — Pythagorean theorem

```math
a^2+b^2=c^2
```

where `c` is hypotenuse.

### Worked Example 1

Legs are 6 and 8.

```math
6^2+8^2=c^2
```

```math
36+64=100
```

```math
c=10
```

### Check

Hypotenuse 10 is longer than 6 and 8.

### Useful triples

```text
3-4-5
5-12-13
8-15-17
```

Scaled versions also work:

```text
6-8-10
10-24-26
```

---

## 5. Pattern B — Special triangle 45-45-90

Sides:

```text
x : x : x√2
```

### Recognition cue

Two acute angles are both 45° → legs equal.

### Worked Example 2

Each leg is 7.

Hypotenuse:

```math
7\sqrt2
```

### Reverse direction

If hypotenuse is `10√2`, each leg is 10.

---

## 6. Pattern C — Special triangle 30-60-90

Sides opposite:

```text
30° → x
60° → x√3
90° → 2x
```

### Worked Example 3

Shortest side is 4.

```text
short = 4
long  = 4√3
hyp   = 8
```

### Recognition anchor

```text
30 → smallest
90 → largest = double smallest
```

---

## 7. Pattern D — SOH-CAH-TOA

Before choosing a ratio, label relative to **θ**:

- Opposite
- Adjacent
- Hypotenuse

### Worked Example 4

Relative to `θ`:

```text
opposite = 6
adjacent = 8
hypotenuse = 10
```

Then:

```math
\sin\theta=\frac6{10}=\frac35
```

```math
\cos\theta=\frac8{10}=\frac45
```

```math
\tan\theta=\frac6{8}=\frac34
```

### Decision cue

```text
Need O and H → sine
Need A and H → cosine
Need O and A → tangent
```

---

## 8. Pattern E — complementary angles

In a right triangle, acute angles add to 90°.

If one is `θ`, the other is:

```math
90^\circ-\theta
```

Because opposite and adjacent swap roles:

```math
\sin\theta=\cos(90^\circ-\theta)
```

```math
\cos\theta=\sin(90^\circ-\theta)
```

### Worked Example 5

If:

```math
\sin32^\circ=k
```

then:

```math
\cos58^\circ=k
```

because:

```math
58=90-32
```

---

## 9. Pattern F — find an angle from sides

Suppose:

```math
\sin\theta=\frac35
```

Then:

```math
\theta=\sin^{-1}\left(\frac35\right)
```

Use Desmos/calculator when numerical angle is requested.

### Trap

`sin⁻¹` here means inverse sine, not `1/sin`.

---

## 10. Decision Tree

```text
Is triangle right?
│
├─ No → don't use Pythagorean/SOHCAHTOA automatically
│
└─ Yes
   │
   ├─ Two sides known, one missing?
   │   └─ Pythagorean
   │
   ├─ 45-45-90?
   │   └─ x,x,x√2
   │
   ├─ 30-60-90?
   │   └─ x,x√3,2x
   │
   ├─ Need side ratio relative to angle?
   │   └─ SOH-CAH-TOA
   │
   └─ Need angle from side ratio?
       └─ inverse trig
```

---

## 11. SAT Language Decoder

| Phrase | Meaning |
|---|---|
| `right triangle` | one 90° angle |
| `leg` | non-hypotenuse side |
| `hypotenuse` | side opposite 90° |
| `opposite to θ` | side across from θ |
| `adjacent to θ` | touching θ, but not hypotenuse |
| `angle of elevation` | angle measured upward from horizontal |
| `complementary angles` | sum 90° |

---

## 12. Word-problem pattern — angle of elevation

### Worked Example 6

A person stands 20 m from a building. The angle of elevation to the top is 35°. Find the building height `h`.

Relative to 35°:

```text
opposite = h
adjacent = 20
```

So use tangent:

```math
\tan35^\circ=\frac{h}{20}
```

```math
h=20\tan35^\circ
```

### Why tangent?

Because the two involved sides are opposite and adjacent.

---

## 13. Faded Examples

### Example A

Right triangle legs 9 and 12. Find hypotenuse.

**Pattern:** __________

<details><summary>Проверка</summary>

```math
9^2+12^2=225
```

```math
c=15
```
</details>

### Example B

45-45-90 triangle with hypotenuse `8√2`.

Each leg = ______.

<details><summary>Проверка</summary>
8
</details>

### Example C

Relative to θ, opposite=5, adjacent=12.

Which trig ratio directly uses both?

<details><summary>Проверка</summary>

```text
tangent
```
</details>

---

## 14. Error Clinic

### Error 1 — wrong adjacent

Adjacent is not “any side next to the angle.” Hypotenuse may touch the angle too, but it is never called adjacent in SOH-CAH-TOA.

### Error 2 — wrong `c` in Pythagorean theorem

`c` must be hypotenuse.

### Error 3 — use theorem in non-right triangle

Pythagorean theorem and SOH-CAH-TOA require right-triangle context.

### Error 4 — compute angle when ratio is enough

If question asks `sin θ`, do not waste time finding θ first.

---

## 15. Digital SAT Strategy

Fastest sequence:

```text
1. mark 90°
2. identify hypotenuse
3. mark θ
4. label O/A/H
5. choose method
```

Desmos is useful for:

- trig evaluation;
- inverse trig;
- checking numerical answers.

But special triangles and common triples are usually faster manually.

---

## 16. Independent SAT-Style Practice

### Problem 1 — Easy — Grid-in

A right triangle has legs 3 and 4. Find hypotenuse.

### Problem 2 — Easy — Multiple Choice

Relative to `θ`, opposite=5 and hypotenuse=13. What is `sin θ`?

**A)** `5/12`  
**B)** `5/13`  
**C)** `12/13`  
**D)** `13/5`

### Problem 3 — Medium — Multiple Choice

In a 45-45-90 triangle, each leg is 7. Hypotenuse is:

**A)** `7`  
**B)** `7√2`  
**C)** `14`  
**D)** `14√2`

### Problem 4 — Medium — Grid-in

In a 30-60-90 triangle, shortest side is 4. Find hypotenuse.

### Problem 5 — Hard — Multiple Choice

If `sin32°=k`, which expression equals `k`?

**A)** `cos32°`  
**B)** `cos58°`  
**C)** `sin58°`  
**D)** `tan58°`

<details>
<summary><strong>Ответы</strong></summary>

1. `5`  
2. **B**  
3. **B**  
4. `8`  
5. **B**

</details>

---

## 17. Transfer Questions

1. Why can the same side be opposite for one angle and adjacent for another?
2. Why does `sin θ = cos(90°-θ)` follow from triangle geometry?
3. When is recognizing `3-4-5` faster than Pythagorean calculation?
4. If only `sin θ` is requested, why might finding θ be unnecessary?

---

## 18. Мини-чек-лист

- [ ] Я сначала нахожу hypotenuse.
- [ ] Я использую Pythagorean theorem только для right triangles.
- [ ] Я узнаю 45-45-90 и 30-60-90.
- [ ] Я правильно маркирую O/A/H относительно выбранного angle.
- [ ] Я выбираю sine/cosine/tangent по нужным sides.
- [ ] Я понимаю complementary trig identity.
