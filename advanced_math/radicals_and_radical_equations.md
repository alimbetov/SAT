# Radicals and Radical Equations — корни и уравнения с радикалами

## 1. Зачем эта тема нужна на SAT

Radicals проверяют три разных навыка, которые важно не смешивать:

1. упрощать radical expressions;
2. переводить между radical и fractional exponent forms;
3. решать radical equations и отсеивать extraneous solutions.

> **Главная идея:** squaring может убрать radical, но может создать лишний candidate.

---

## 2. Pattern Map — что вижу и что делать

| Что вы видите | Паттерн | Что делать |
|---|---|---|
| `√72` | simplify radical | extract largest perfect square |
| `x^(1/2)` | radical/exponent conversion | rewrite as `√x` |
| `x^(m/n)` | nth root power | `ⁿ√(x^m)` |
| `√(expression)=number` | simple radical equation | isolate, square, solve |
| radical on one side, expression on other | possible extraneous roots | square, then check |
| even root | domain restriction | radicand `≥0` |

### Mental model: squaring is not reversible for free

```text
original equation
   ↓ square both sides
new equation with more candidates
   ↓ check candidates
valid solutions only
```

Почему? Потому что squaring loses sign information.

---

## 3. Учимся решать по паттернам

### Pattern A — Simplify a radical

#### Worked Example

Simplify:

```math
\sqrt{72}.
```

Find largest perfect-square factor:

```math
72=36\cdot2.
```

So:

```math
\sqrt{72}=\sqrt{36}\sqrt2=6\sqrt2.
```

### Recognition trick

Look for:

```text
4, 9, 16, 25, 36, 49, 64, 81, 100
```

inside the radicand.

---

### Pattern B — Fractional exponents

```math
a^{1/2}=\sqrt a
```

```math
a^{1/3}=\sqrt[3]a
```

```math
a^{m/n}=\sqrt[n]{a^m}.
```

#### Worked Example

```math
x^{2/3}
```

means:

```math
\sqrt[3]{x^2}.
```

The denominator of exponent tells the root.

> **Memory anchor:** denominator = root, numerator = power.

---

### Pattern C — Simple radical equation

#### Worked Example

Solve:

```math
\sqrt{x+1}=5.
```

Square both sides:

```math
x+1=25.
```

```math
x=24.
```

Check:

```math
\sqrt{25}=5.
```

Valid.

---

### Pattern D — Radical equation with extraneous solution

#### Worked Example

Solve:

```math
\sqrt{x+5}=x-1.
```

### Step 1 — domain / sign reasoning

Left side is nonnegative, so right side must be nonnegative:

```math
x-1\ge0
```

```math
x\ge1.
```

### Step 2 — square

```math
x+5=(x-1)^2.
```

### Step 3 — solve quadratic

```math
x+5=x^2-2x+1
```

```math
x^2-3x-4=0
```

```math
(x-4)(x+1)=0.
```

Candidates:

```text
4, -1
```

### Step 4 — check original equation

`x=4` works.

`x=-1` fails and also violates `x≥1`.

Answer:

```math
x=4.
```

---

### Pattern E — Why extraneous roots appear

Suppose:

```math
A=B.
```

Then certainly:

```math
A^2=B^2.
```

But reverse is not always true.

Example:

```math
3^2=(-3)^2,
```

but:

```math
3\ne-3.
```

That is the logic behind extraneous solutions.

---

## 4. Method Selector + SAT Language Decoder

### Decision Tree

```text
Need to simplify √N?
  → extract perfect-square factors

Fractional exponent?
  → denominator = root, numerator = power

Equation with one radical?
  → isolate radical first
  → square
  → solve
  → CHECK original equation

Even root?
  → radicand must be ≥0
```

### SAT English Decoder

| Phrase | What it means |
|---|---|
| `simplify the expression` | extract factors / rewrite form |
| `equivalent expression` | radical ↔ fractional exponent |
| `valid solution` | reject extraneous candidates |
| `real solution` | respect radical domain |
| `principal square root` | nonnegative square root |

---

## 5. Guided Practice — fading support

### Example 1 — full support

Simplify:

```math
\sqrt{50}.
```

```math
50=25\cdot2
```

```math
\sqrt{50}=5\sqrt2.
```

### Example 2 — partial support

Rewrite:

```math
x^{3/2}
```

as a radical.

- denominator `2` → square root;
- numerator `3` → cube.

<details><summary>Answer</summary>

```math
\sqrt{x^3}
```

</details>

### Example 3 — solve with check

```math
\sqrt{2x+3}=x.
```

Square:

```math
2x+3=x^2.
```

```math
x^2-2x-3=0.
```

```math
(x-3)(x+1)=0.
```

Candidates: `3`, `-1`.

Check original:

- `3` works;
- `-1` does not because left side is nonnegative while right side is negative.

Answer: `3`.

### Example 4 — recognition only

Why must

```math
\sqrt{x-4}
```

satisfy `x≥4` for real values?

Because radicand of an even root cannot be negative in the real-number system.

---

## 6. Error Clinic + Desmos Strategy

### Error 1 — `√(a+b)=√a+√b`

Usually false.

Example:

```math
\sqrt{9+16}=5,
```

but:

```math
\sqrt9+\sqrt{16}=3+4=7.
```

### Error 2 — skipping the check

After squaring, candidates are not automatically solutions.

### Error 3 — squaring before isolating radical

Usually isolate the radical first; otherwise algebra becomes needlessly complicated.

### Desmos

For

```math
\sqrt{x+5}=x-1,
```

enter:

```text
y=sqrt(x+5)
y=x-1
```

The intersections show valid real solutions directly.

But still understand why an algebraic candidate may be extraneous.

---

## 7. SAT-Style Practice

### Problem 1 — Easy — Multiple Choice

Simplify:

```math
\sqrt{98}.
```

**A)** `7√2`  
**B)** `14√7`  
**C)** `49√2`  
**D)** `2√49`

### Problem 2 — Easy — Multiple Choice

Which is equivalent to

```math
x^{1/3}?
```

**A)** `x/3`  
**B)** `3x`  
**C)** `∛x`  
**D)** `x³`

### Problem 3 — Medium — Grid-in

Solve:

```math
\sqrt{x+4}=6.
```

### Problem 4 — Medium — Multiple Choice

Which is equivalent to

```math
x^{5/2}?
```

**A)** `√(x^5)`  
**B)** `x^(2/5)`  
**C)** `5√x`  
**D)** `x²/5`

### Problem 5 — Hard — Grid-in

Solve for the valid real solution:

```math
\sqrt{2x+8}=x.
```

<details><summary><strong>Answers</strong></summary>

1. **A**  
2. **C**  
3. `32`  
4. **A**  
5. `4`

</details>

---

## 8. Мини-чек-лист и Transfer

- [ ] Я упрощаю radicals через perfect-square factors.
- [ ] Я перевожу radical ↔ fractional exponent.
- [ ] Я понимаю domain even roots.
- [ ] Я изолирую radical перед squaring.
- [ ] Я всегда проверяю candidates в original equation.

### Transfer Question

Почему squaring both sides может увеличить число solutions, а taking a square root может уменьшить information about sign?

Потому что both `a` and `-a` produce the same square `a²`; squaring merges sign information.
