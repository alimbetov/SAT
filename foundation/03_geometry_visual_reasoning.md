# Foundation Bridge 03 — Geometry Visual Reasoning

**Learner label:** `FOUNDATION`

Цель — научиться видеть геометрические отношения до алгебраических выражений вида `3x+10`.

Главная мысль:

> Сначала распознай отношение на рисунке. Потом считай.

---

# 1. Периметр и площадь — не одно и то же

Представьте прямоугольный двор.

- **Perimeter** — длина забора вокруг.
- **Area** — сколько места внутри.

```text
+----------+
|          |
|  AREA    |
|          |
+----------+
  PERIMETER вокруг
```

## Example

Rectangle: length 6, width 4.

### Perimeter

Идём по границе:

```math
6+4+6+4=20
```

### Area

Считаем квадратные клетки внутри:

```math
6·4=24
```

Ответы имеют разные units:

```text
perimeter → cm
area      → cm²
```

---

# 2. Почему area измеряется square units

Rectangle 3 by 4 можно представить как клетки:

```text
□ □ □ □
□ □ □ □
□ □ □ □
```

Всего 12 квадратов.

Поэтому:

```math
A=3·4=12\ square\ units
```

Формула `A=lw` — короткая запись счёта клеток.

---

# 3. Triangle area — половина rectangle

Возьмём rectangle 6 by 4.

Диагональ делит его на два одинаковых triangles.

```text
+------+
|\     |
|  \   |
|    \ |
+------+
```

Rectangle area:

```math
6·4=24
```

Каждый triangle — половина:

```math
24÷2=12
```

Отсюда:

```math
A=\frac12 bh
```

Формула теперь имеет смысл, а не выглядит случайной.

---

# 4. Angles on a straight line

Прямая линия образует 180°.

```text
----------•----------
           \
            \
```

Если один угол 65°, соседний:

```math
180-65=115^°
```

Mental anchor:

```text
straight line → 180°
```

---

# 5. Vertical angles

Когда две линии пересекаются:

```text
\  /
 \/
 /\
/  \
```

Противоположные углы равны.

```text
opposite → equal
```

Если один 70°, противоположный тоже 70°.

Соседний:

```math
180-70=110^°
```

---

# 6. Triangle sum

У треугольника сумма внутренних углов:

```math
180^°
```

### Worked Example 1

Angles: 50°, 60°, and `?`.

```math
50+60+?=180
```

Сначала известная сумма:

```math
50+60=110
```

Осталось:

```math
180-110=70
```

Third angle = 70°.

---

# 7. Geometry before algebra

Сначала научимся решать так:

```text
one angle = 110°
vertical angle = ?
```

Ответ 110°.

Только потом добавляем algebra:

```text
one angle = 3x+10
vertical angle = 5x-30
```

Поскольку vertical angles equal:

```math
3x+10=5x-30
```

Теперь geometry дала нам equation.

Это важная идея:

> Geometry сначала говорит, **какое отношение верно**. Algebra помогает найти число.

---

# 8. Similar shapes — same shape, different size

Два прямоугольника:

```text
small:  2 × 3
large:  4 × 6
```

Каждая сторона large в 2 раза больше.

Scale factor:

```math
k=2
```

Если у small side = 5, corresponding large side:

```math
5·2=10
```

Главное:

```text
same scale factor for all corresponding lengths
```

---

# 9. Scale factor and area intuition

Square side 2:

```math
A=2·2=4
```

Увеличим side в 3 раза:

```text
2 → 6
```

Новая area:

```math
6·6=36
```

Area выросла:

```math
36÷4=9
```

То есть:

```text
length ×3
area ×9 = ×3²
```

Это подготовка к SAT scale questions.

---

# 10. Faded Example

Triangle has angles 35°, 85°, and `x`.

Заполните:

```text
Rule: triangle angles sum to ______
Known angles total: ______
Equation: ______
Answer: ______
```

<details><summary>Проверка</summary>

```text
Rule: 180°
Known total: 120°
Equation: x+120=180
Answer: 60°
```

</details>

---

# 11. SAT English Bridge

| English | Meaning |
|---|---|
| angle | угол |
| vertical angles | противоположные углы при пересечении |
| supplementary | сумма 180° |
| triangle | треугольник |
| perimeter | длина границы |
| area | площадь внутри |
| similar | одинаковая форма, размер может отличаться |
| scale factor | во сколько раз изменили длины |

---

# 12. Check for Understanding

1. Чем perimeter отличается от area?
2. Почему `cm²` используется для area?
3. Что можно сказать про opposite angles при пересечении линий?
4. Почему triangle angles дают 180°?
5. Если side scale factor = 2, что произойдёт с corresponding side?

---

# 13. Foundation Practice

1. Rectangle 8 by 3: perimeter?
2. Rectangle 8 by 3: area?
3. Triangle base 10, height 6: area?
4. Supplementary angle to 72°?
5. Triangle angles 40°, 65°, `x`: find `x`.
6. Similar figures scale factor 3; small side 7: large side?

<details><summary>Ответы</summary>

1. `22`
2. `24`
3. `30`
4. `108°`
5. `75°`
6. `21`

</details>

---

# Mastery Gate

Готовность к SAT geometry lesson:

- [ ] perimeter и area не путаются;
- [ ] square units понятны;
- [ ] straight line → 180°;
- [ ] vertical → equal;
- [ ] triangle sum → 180°;
- [ ] простой scale factor применяется уверенно;
- [ ] ученик сначала называет geometric rule, потом пишет equation.
