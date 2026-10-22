# Foundation Bridge 05 — Squares, Square Roots, and the Road to Quadratics

**Learner label:** `FOUNDATION / BRIDGE`

Этот модуль не заменяет полный урок Quadratics. Он объясняет идеи, без которых quadratic formulas превращаются в зубрёжку.

---

# 1. Что означает x²

```math
x^2=x·x
```

Не:

```text
x × 2
```

а:

```text
x multiplied by itself
```

Examples:

```math
3^2=3·3=9
```

```math
5^2=5·5=25
```

```math
10^2=100
```

---

# 2. Area model

Square with side 4:

```text
4 by 4
```

Area:

```math
4·4=4^2=16
```

Поэтому слово **square** связано и с фигурой, и с operation `²`.

Если area square = 49, side length:

```math
\sqrt{49}=7
```

Square root отвечает:

> Какое nonnegative число, умноженное само на себя, даёт это число?

---

# 3. Square numbers worth recognizing

| n | n² |
|---:|---:|
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |
| 4 | 16 |
| 5 | 25 |
| 6 | 36 |
| 7 | 49 |
| 8 | 64 |
| 9 | 81 |
| 10 | 100 |
| 11 | 121 |
| 12 | 144 |

These reduce cognitive load later.

---

# 4. Square root vs equation x²=49

Important distinction:

```math
\sqrt{49}=7
```

The radical symbol means the principal nonnegative square root.

But equation:

```math
x^2=49
```

asks:

> Which signed values of x produce 49 when squared?

Both:

```math
7^2=49
```

and

```math
(-7)^2=49
```

So:

```math
x=\pm7
```

This is why `±` appears.

---

# 5. Why negative squared becomes positive

```math
(-3)^2=(-3)(-3)=9
```

Two negative factors make a positive product.

But notice:

```math
-3^2=-(3^2)=-9
```

Parentheses matter.

This is a common future SAT trap.

---

# 6. From rectangle area to factoring

A rectangle has sides:

```text
x+2
x+3
```

Area:

```math
(x+2)(x+3)
```

Expand by splitting the rectangle:

```text
        x      3
     +------+---+
 x   | x²   |3x |
     +------+---+
 2   | 2x   | 6 |
     +------+---+
```

Total area:

```math
x^2+3x+2x+6
```

```math
x^2+5x+6
```

So:

```math
(x+2)(x+3)=x^2+5x+6
```

Factoring later means reversing this process.

---

# 7. Factoring as «find the rectangle sides»

Given:

```math
x^2+5x+6
```

We want:

```math
(x+p)(x+q)
```

Need:

```text
p + q = 5
p × q = 6
```

Numbers 2 and 3 work.

Therefore:

```math
x^2+5x+6=(x+2)(x+3)
```

Instead of memorizing two conditions, connect them to expansion.

---

# 8. Zero-product idea

Suppose:

```math
(x-2)(x-5)=0
```

A product equals zero only if at least one factor is zero.

So:

```math
x-2=0
```

or

```math
x-5=0
```

Therefore:

```math
x=2\ or\ x=5
```

### Why?

Try ordinary numbers:

```text
3 × 0 = 0
0 × 8 = 0
```

But two nonzero numbers cannot multiply to zero.

This is the reason factoring solves many quadratics.

---

# 9. Worked Example — x²-7x+12=0

We want two numbers that:

```text
multiply to +12
add to -7
```

Candidates with product +12:

```text
1 and 12
2 and 6
3 and 4
```

To get negative sum, both must be negative.

```text
-3 + -4 = -7
(-3)(-4)=12
```

So:

```math
x^2-7x+12=(x-3)(x-4)
```

Set each factor to zero:

```math
x=3\ or\ 4
```

### Check

For x=3:

```math
9-21+12=0
```

For x=4:

```math
16-28+12=0
```

Both work.

---

# 10. Parabola as a picture of outputs

Consider:

```math
y=x^2
```

Table:

| x | y |
|---:|---:|
| -3 | 9 |
| -2 | 4 |
| -1 | 1 |
| 0 | 0 |
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |

Notice symmetry:

```text
x=2 and x=-2 give same y=4
```

That is another reason quadratic equations can have two solutions.

---

# 11. Roots as x-intercepts

If:

```math
y=(x-2)(x-5)
```

then y becomes zero when:

```math
x=2
```

or

```math
x=5
```

On a graph, those are places where the parabola crosses the x-axis.

So three phrases connect:

```text
solutions
roots / zeros
x-intercepts
```

They are related views of the same idea.

---

# 12. Faded Example

Factor and solve:

```math
x^2+7x+12=0
```

Fill in:

```text
Need p×q = ______
Need p+q = ______
Numbers: ______ and ______
Factored form: ______
Solutions: ______
```

<details><summary>Проверка</summary>

```text
p×q = 12
p+q = 7
3 and 4
(x+3)(x+4)=0
x=-3 or x=-4
```

</details>

---

# 13. When NOT to start full Quadratics yet

Pause and review prerequisites if the learner struggles with:

- negative-number multiplication;
- distributive property;
- simple factoring;
- square numbers;
- square roots;
- coordinate graph basics.

A quadratic lesson should not simultaneously teach all of those from scratch.

---

# 14. SAT English Bridge

| English | Meaning |
|---|---|
| squared | возведено в квадрат |
| square root | квадратный корень |
| factor | множитель |
| roots / zeros | значения x, где expression/function = 0 |
| x-intercept | точка пересечения с x-axis |
| quadratic | выражение/функция со степенью 2 как highest power |

---

# 15. Foundation Practice

1. `7² = ?`
2. `√81 = ?`
3. Solve `x²=36`.
4. Expand `(x+2)(x+4)`.
5. Factor `x²+5x+6`.
6. Solve `(x-3)(x+1)=0`.

<details><summary>Ответы</summary>

1. `49`
2. `9`
3. `x=±6`
4. `x²+6x+8`
5. `(x+2)(x+3)`
6. `x=3` or `x=-1`

</details>

---

# Mastery Gate

Full Quadratics is appropriate when the learner can:

- [ ] evaluate squares;
- [ ] recognize common square roots;
- [ ] handle negative signs with squares;
- [ ] expand two simple binomials;
- [ ] factor simple monic quadratics;
- [ ] use zero-product idea;
- [ ] understand roots as x-intercepts at a basic level.
