# Lines, Angles, and Triangles — Pedagogy V2

## 1. Зачем эта тема нужна на SAT

Задачи на линии, углы и треугольники часто выглядят визуально сложнее, чем они есть. На SAT почти никогда не нужно «угадывать по рисунку». Нужно распознать несколько повторяющихся отношений и превратить геометрию в короткую цепочку равенств или пропорций.

> **Главная идея:** рисунок даёт контекст, но доказательство дают только отметки, числа и теоремы.

### Mental model

```text
LOOK
 ↓
MARK RELATIONSHIPS
 ↓
CHOOSE THEOREM
 ↓
WRITE EQUATION / PROPORTION
 ↓
SOLVE
 ↓
CHECK GEOMETRIC MEANING
```

---

## 2. Pattern Map — что нужно узнать с первого взгляда

| Что видно | Какой pattern | Что делать |
|---|---|---|
| пересекающиеся линии | vertical angles | opposite angles equal |
| прямая линия и соседние углы | linear pair | сумма 180° |
| две parallel lines + transversal | corresponding / alternate interior | использовать равенства углов |
| треугольник и три угла | triangle sum | сумма 180° |
| exterior angle | exterior-angle theorem | сумма двух remote interior |
| два одинаковых по форме треугольника | similarity | corresponding sides proportional |
| одинаковые side/angle marks | congruence | SSS/SAS/ASA/AAS |
| размеры увеличились в одном ratio | scale factor | один `k` для всех corresponding lengths |

### Первый вопрос к себе

> Какие отношения **гарантированы**, а какие я только «вижу» на картинке?

SAT diagram может быть **not drawn to scale**.

---

## 3. Базовые visual anchors

### Vertical angles

```text
\ /
 X      opposite = equal
/ \
```

Если один угол 112°, противоположный тоже 112°.

### Linear pair

```text
------•------
      / 
```

Смежные углы на прямой:

```math
a+b=180^\circ
```

### Triangle sum

```math
A+B+C=180^\circ
```

### Parallel lines + transversal

Запоминайте не как набор случайных правил, а как форму:

```text
parallel lines preserve angle pattern
```

Если две линии parallel:

- corresponding angles equal;
- alternate interior angles equal;
- same-side interior angles sum to 180°.

---

## 4. Pattern A — найти неизвестный угол

### Worked Example 1

A triangle has angles `2x`, `3x`, and `4x`. Find the largest angle.

### Recognize

Три угла одного triangle → используем triangle sum.

### Choose

```math
2x+3x+4x=180
```

### Solve

```math
9x=180
```

```math
x=20
```

Largest angle:

```math
4x=80^\circ
```

### Check

```math
40+60+80=180
```

### Transfer

Если angles равны `x`, `2x+10`, `3x-10`, pattern тот же: сначала сумма 180°.

---

## 5. Pattern B — vertical / supplementary / transversal angles

### Worked Example 2

Two lines intersect. One angle is `3x+10` and its vertical angle is `5x-30`. Find `x`.

### Recognize

Vertical angles → equal.

### Equation

```math
3x+10=5x-30
```

```math
40=2x
```

```math
x=20
```

### Почему не 180°?

Потому что vertical angles находятся **напротив**, а не рядом.

### Pattern cue

```text
opposite → equal
next to each other on a line → add to 180
```

---

## 6. Pattern C — exterior angle

### Rule

Exterior angle of a triangle equals the sum of the two remote interior angles.

```math
E=A+B
```

### Worked Example 3

An exterior angle is `125°`. One remote interior angle is `55°`. Find the other.

```math
125=55+x
```

```math
x=70^\circ
```

### Shortcut insight

Не обязательно сначала искать adjacent interior angle через 180°. Exterior-angle theorem обычно быстрее.

---

## 7. Pattern D — Similar Triangles

### Mental model

```text
SAME SHAPE
DIFFERENT SIZE POSSIBLE
```

У similar triangles:

- corresponding angles equal;
- corresponding side lengths proportional.

Если scale factor from small → large равен `k`, то:

```math
large\ side=k\cdot small\ side
```

### Worked Example 4

Two similar triangles have corresponding sides 4 and 10. Another side of the smaller triangle is 6. Find the corresponding larger side.

### Step 1. Scale factor

```math
k=\frac{10}{4}=2.5
```

### Step 2. Apply same factor

```math
6(2.5)=15
```

### Check

Один и тот же scale factor должен работать для всех corresponding sides.

### Common recognition error

Нельзя сравнивать произвольные стороны. Сначала установите **correspondence**.

---

## 8. Pattern E — Congruent Triangles

### Mental model

```text
SIMILAR = same shape
CONGRUENT = same shape + same size
```

### Main criteria

| Criterion | Что известно |
|---|---|
| SSS | 3 corresponding sides |
| SAS | 2 sides + included angle |
| ASA | 2 angles + included side |
| AAS | 2 angles + nonincluded side |

### Worked Example 5

In triangles ABC and DEF:

```text
AB = DE
BC = EF
∠B = ∠E
```

Какой criterion?

Угол `B/E` находится **между** двумя данными sides.

Ответ:

```text
SAS
```

### Trap

SSA в общем случае **не гарантирует congruence**.

---

## 9. Decision Tree — какую идею применять

```text
Unknown angle?
├─ triangle only → sum 180
├─ straight line → sum 180
├─ opposite at intersection → vertical = equal
├─ parallel + transversal → angle relationships
└─ exterior angle → remote interiors add

Unknown side?
├─ similar triangles → scale factor / proportion
└─ congruent triangles → corresponding sides equal

Need proof of congruence?
→ SSS / SAS / ASA / AAS
```

---

## 10. SAT Language Decoder

| SAT phrase | Что это означает |
|---|---|
| `parallel lines` | можно применять transversal angle rules |
| `corresponding sides` | стороны в одинаковой позиции |
| `similar triangles` | same shape, proportional sides |
| `congruent triangles` | same shape and size |
| `included angle` | угол между двумя указанными sides |
| `exterior angle` | внешний угол у вершины triangle |
| `not drawn to scale` | нельзя измерять глазами |

---

## 11. Faded Examples — подсказки исчезают

### Example A

Two supplementary angles measure `4x+10` and `2x+20`.

**Pattern:** ____________________

**Equation:** ___________________

<details><summary>Проверка</summary>

```math
(4x+10)+(2x+20)=180
```

```math
6x+30=180
```

```math
x=25
```
</details>

### Example B

Two similar triangles have scale factor 3 from small to large. A corresponding small side is 7.

**Operation:** __________________

<details><summary>Проверка</summary>

```math
7\cdot3=21
```
</details>

### Example C

Two triangles have two equal sides and the included angle equal.

**Criterion:** __________________

<details><summary>Проверка</summary>
SAS
</details>

---

## 12. Error Clinic

### Error 1 — доверять рисунку

**Wrong:** «Этот угол выглядит acute, значит <90°.»

**Почему плохо:** diagram может быть not to scale.

**Fix:** используйте только numerical/marked information.

### Error 2 — перепутать vertical и supplementary

**Wrong pattern:** opposite angles add to 180°.

**Correct:** opposite vertical angles are equal.

### Error 3 — перепутать corresponding sides

Если scale factor нашли по одной паре, применять его нужно только к matching side pair.

### Error 4 — считать similar triangles congruent

Similarity не означает одинаковый size.

---

## 13. Digital SAT Strategy

Geometry часто решается быстрее маркировкой рисунка, чем вычислениями.

Перед началом:

1. подпишите known angles;
2. отметьте parallel lines;
3. обведите equal side marks;
4. укажите correspondence;
5. только потом пишите equation/proportion.

Desmos обычно здесь не нужен.

---

## 14. Independent SAT-Style Practice

### Problem 1 — Easy — Grid-in

Two supplementary angles are 65° and `x°`. Find `x`.

### Problem 2 — Easy — Multiple Choice

If one vertical angle measures 112°, its opposite angle is:

**A)** 68°  
**B)** 90°  
**C)** 112°  
**D)** 248°

### Problem 3 — Medium — Multiple Choice

Two similar triangles have corresponding sides 3 and 12. If another side of the smaller triangle is 5, the corresponding side of the larger triangle is:

**A)** 8  
**B)** 15  
**C)** 20  
**D)** 60

### Problem 4 — Medium — Grid-in

A triangle has angles `x`, `2x`, and `3x`. Find the largest angle.

### Problem 5 — Hard — Multiple Choice

Triangles ABC and DEF have `AB=DE`, `BC=EF`, and `∠B=∠E`. Which criterion proves congruence?

**A)** SSS  
**B)** SAS  
**C)** ASA  
**D)** SSA

<details>
<summary><strong>Ответы</strong></summary>

1. `115`  
2. **C**  
3. **C**, scale factor 4  
4. `90`  
5. **B**

</details>

---

## 15. Transfer Questions

1. Почему equal angles alone обычно доказывают similarity, но не congruence?
2. Если scale factor lengths равен 4, изменятся ли angles?
3. Почему same-side interior angles при parallel lines supplementary?
4. Как отличить SAS от SSA по положению angle?

---

## 16. Мини-чек-лист

- [ ] Я не доверяю масштабу рисунка без данных.
- [ ] Я распознаю vertical, supplementary и transversal angle patterns.
- [ ] Я использую triangle sum и exterior-angle theorem.
- [ ] Я различаю similarity и congruence.
- [ ] Я нахожу scale factor только по corresponding sides.
- [ ] Я выбираю SSS/SAS/ASA/AAS по реальным данным.
