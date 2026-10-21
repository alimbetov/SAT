# Linear Equations — линейные уравнения с одной переменной

> **Цель урока:** не просто научиться «переносить числа через знак равно», а научиться **узнавать тип линейной задачи**, быстро выбирать метод и объяснять, почему он работает.

Линейные уравнения — фундамент SAT Math. Они встречаются напрямую, внутри word problems, systems, functions, percentages, geometry и даже Advanced Math.

Главная мысль этого урока:

> **Не начинайте считать, пока не поняли паттерн задачи.**

---

# 1. Карта темы — Pattern Map

Перед решением спросите себя: **«Что именно я вижу?»**

| Что вижу в задаче | Паттерн | Первая мысль |
|---|---|---|
| `3x+7=25` | **Isolate the variable** | отменяю операции в обратном порядке |
| `5x+2=2x+17` | **Variable on both sides** | собираю все `x` на одной стороне |
| `3(x+4)=21` | **Parentheses** | ищу короткий путь; если нет — раскрываю скобки |
| `x/4+5=11` | **Fractions / division** | сначала убираю внешние операции |
| `4x+5=4x+9` | **Variable disappears** | проверяю `no solution` или `infinitely many solutions` |
| `$18 + $7 per month = $81` | **Fixed + rate × quantity** | строю модель `total = fixed + rate·quantity` |
| `k(x+3)=6x+18` | **Parameter / same equation** | сравниваю coefficients и constants |

Эта таблица важнее любой отдельной формулы.

Если вы научились узнавать паттерн, половина задачи уже решена.

---

# 2. Главная идея: уравнение — это весы

Рассмотрим:

```math
3x+7=25
```

Представьте весы:

```text
ЛЕВАЯ ЧАСТЬ              ПРАВАЯ ЧАСТЬ

   3x + 7          ⚖          25
```

Равенство означает баланс.

Если убрать `7` только слева, баланс нарушится.

Поэтому любое допустимое действие делаем **с обеими сторонами**.

```math
3x+7-7=25-7
```

получаем

```math
3x=18
```

Теперь делим **обе стороны** на `3`:

```math
x=6
```

## Визуальный якорь

```text
Equation = balance

что сделал слева
        ↓
делай и справа
```

Не учите правило «переносим через равно и меняем знак» как магию.

Реальная логика такая:

```text
+7 мешает x
→ применяем обратную операцию
→ -7 с обеих сторон
```

Это особенно важно, когда задачи становятся сложнее.

---

# 3. PATTERN 1 — Isolate the variable

## Как узнать

Переменная находится только с одной стороны.

Примеры:

```math
3x+7=25
```

```math
5x-9=31
```

```math
\frac{x}{4}+3=8
```

## Главный принцип

Чтобы оставить `x` один, **отменяйте операции в обратном порядке**.

Например:

```math
3x+7=25
```

Что произошло с `x`?

```text
x
↓ ×3
3x
↓ +7
3x+7
```

Значит при решении идём назад:

```text
3x+7
↓ -7
3x
↓ ÷3
x
```

Это очень полезный паттерн:

> **Solve = undo operations backward.**

---

## Worked Example 1 — полный разбор

### Задача

```math
4x+11=35
```

### Notice — что замечаем

`x` только слева. Это обычный **isolate-the-variable** pattern.

### Decision — что делаем первым

`x` сначала умножили на `4`, затем прибавили `11`.

При решении отменяем операции в обратном порядке.

Сначала отменяем `+11`.

### Action

```math
4x+11-11=35-11
```

```math
4x=24
```

Теперь отменяем `×4` делением на `4`:

```math
x=6
```

### Check

Подставляем:

```math
4(6)+11=24+11=35
```

Работает.

**Ответ: `6`.**

---

## Worked Example 2 — отрицательная constant

```math
5x-8=27
```

### Сначала назовите паттерн

Обычное isolate-the-variable equation.

### Что мешает `5x`?

`-8`.

Чтобы отменить `-8`, **прибавляем 8**:

```math
5x=35
```

```math
x=7
```

### Важная мысль

Не говорите себе:

> «-8 переходит вправо и становится +8».

Лучше:

> «Я прибавляю 8 с обеих сторон».

Так вы меньше ошибётесь в сложной задаче.

---

## Worked Example 3 — division pattern

```math
\frac{x}{6}+4=9
```

Что произошло с `x`?

```text
x
↓ ÷6
x/6
↓ +4
x/6+4
```

Отменяем назад:

```math
\frac{x}{6}=5
```

Теперь умножаем обе стороны на `6`:

```math
x=30
```

---

## Mini Transfer

Не решая полностью, скажите **первое действие**:

1. `7x+9=44`
2. `3x-5=22`
3. `x/8+6=10`

<details>
<summary>Проверка</summary>

1. вычесть `9`;
2. прибавить `5`;
3. вычесть `6`.

Почему? Мы отменяем последнюю операцию вокруг `x`.

</details>

---

# 4. PATTERN 2 — Variable on both sides

## Как узнать

`x` находится и слева, и справа.

```math
5x+2=2x+17
```

Главная фраза:

> **Сначала собери все x, потом числа.**

---

## Worked Example 1

```math
5x+2=2x+17
```

### Notice

`x` по обе стороны.

### Decision

Удобно оставить `x` слева, потому что `5x` больше `2x` и тогда коэффициент получится положительным.

Вычитаем `2x` с обеих сторон:

```math
3x+2=17
```

Теперь убираем `+2`:

```math
3x=15
```

```math
x=5
```

### Check

Левая часть:

```math
5(5)+2=27
```

Правая часть:

```math
2(5)+17=27
```

Баланс есть.

---

## Worked Example 2 — можно выбрать более удобную сторону

```math
3x+14=7x-6
```

Есть два пути.

### Неудачный, но допустимый путь

Вычесть `7x`:

```math
-4x+14=-6
```

Работает, но появляется отрицательный coefficient.

### Более удобный путь

Вычесть `3x`:

```math
14=4x-6
```

Прибавить `6`:

```math
20=4x
```

```math
x=5
```

### SAT-паттерн

Если можете выбрать, часто выгодно оставить `x` там, где коэффициент будет положительным.

Это не обязательное правило, а стратегия уменьшения ошибок.

---

## Faded Example — теперь часть решения ваша

```math
8x-3=5x+18
```

### Шаг 1

Какой паттерн?

```text
____________________________
```

### Шаг 2

Какое действие удобно сделать первым?

```text
____________________________
```

### Шаг 3

После первого действия должно получиться:

```math
3x-3=18
```

Продолжите самостоятельно.

<details>
<summary>Ответ</summary>

Pattern: variable on both sides.

Вычитаем `5x`:

```math
3x-3=18
```

Прибавляем `3`:

```math
3x=21
```

```math
x=7
```

</details>

---

# 5. PATTERN 3 — Parentheses

## Как узнать

Есть выражение вида:

```math
a(bx+c)
```

Например:

```math
3(x+4)=21
```

Здесь есть **два возможных метода**.

---

## Method Selector

### Вопрос 1

Можно ли сначала удобно разделить обе стороны на число перед скобкой?

Если да — часто это короче.

### Вопрос 2

Если разделить неудобно — раскрывайте скобки.

---

## Worked Example 1 — короткий путь

```math
3(x+4)=21
```

Вместо раскрытия скобок сразу делим на `3`:

```math
x+4=7
```

```math
x=3
```

Три коротких шага.

---

## Worked Example 2 — distributive property

```math
4(2x-3)=20
```

Можно сначала поделить на `4`:

```math
2x-3=5
```

```math
2x=8
```

```math
x=4
```

Это проще, чем раскрывать скобки.

---

## Worked Example 3 — когда раскрытие полезно

```math
3(x+2)=2x+11
```

Справа нет общего множителя `3`, поэтому раскрываем:

```math
3x+6=2x+11
```

Теперь видим знакомый Pattern 2: `x` по обе стороны.

Вычитаем `2x`:

```math
x+6=11
```

```math
x=5
```

### Важная идея

Сложные задачи часто являются **цепочкой знакомых паттернов**:

```text
parentheses
   ↓
variable on both sides
   ↓
isolate x
```

Не нужно запоминать отдельное решение для каждого вида.

---

# 6. Error Clinic — distributive property

Посмотрите на ошибку:

```math
3(x+4)=3x+4
```

Это неверно.

Почему ученик ошибается? Он умножил `3` только на первый член.

Используйте визуальный якорь:

```text
       ┌──→ x
3  ────┤
       └──→ 4
```

Правильно:

```math
3(x+4)=3x+12
```

## Быстрая тренировка

Раскройте:

```math
-2(3x-5)
```

<details>
<summary>Ответ</summary>

```math
-6x+10
```

Обратите внимание: `-2×-5=+10`.

</details>

---

# 7. PATTERN 4 — Variable disappears

Это один из самых важных SAT-паттернов.

Иногда после упрощения `x` полностью исчезает.

Тогда не нужно паниковать и искать, «куда делся x».

Смотрите, **что осталось**.

---

## Case A — No solution

```math
4x+5=4x+9
```

Вычитаем `4x`:

```math
5=9
```

Это ложь.

Значит ни одно `x` не может сделать исходное равенство верным.

```text
FALSE statement
→ NO SOLUTION
```

---

## Case B — Infinitely many solutions

```math
3(x+2)=3x+6
```

Раскрываем:

```math
3x+6=3x+6
```

Вычитаем `3x`:

```math
6=6
```

Это всегда правда.

```text
TRUE statement
→ INFINITELY MANY SOLUTIONS
```

---

## Якорь для памяти

```text
x исчез
   ↓
смотрю на оставшееся равенство

5 = 9  → FALSE → no solution
5 = 5  → TRUE  → infinitely many solutions
```

---

## Recognition Drill

Не решайте подробно. Определите только тип ответа.

### A

```math
2(x+5)=2x+10
```

### B

```math
7x-4=7x+8
```

<details>
<summary>Ответы</summary>

A → infinitely many solutions.

B → no solution.

</details>

---

# 8. PATTERN 5 — Word Problems: fixed + rate × quantity

Это один из самых повторяемых SAT word-problem patterns.

## Как узнать

В тексте есть:

- фиксированная начальная стоимость;
- стоимость **за каждую** единицу;
- общая стоимость.

Формула:

```math
\text{total}=\text{fixed}+\text{rate}\times\text{quantity}
```

---

# SAT Language Decoder

| Фраза | Что означает |
|---|---|
| `one-time fee` | fixed amount |
| `initial fee` | fixed amount |
| `per month` | rate × months |
| `for each` | multiplication |
| `in total` | total |
| `costs $7 per...` | coefficient = 7 |
| `how many months/items/...` | обычно это variable |

---

## Worked Example 1 — subscription

> A streaming service charges a one-time activation fee of `$18` and `$7` per month. A customer paid `$81` in total. How many months did the customer use the service?

### Step 1 — не считаем, а раскладываем текст

```text
fixed       = 18
rate        = 7 per month
quantity    = m months
total       = 81
```

### Step 2 — вставляем в паттерн

```math
\text{total}=\text{fixed}+\text{rate}\times\text{quantity}
```

```math
81=18+7m
```

или

```math
18+7m=81
```

### Step 3 — решаем знакомое equation

```math
7m=63
```

```math
m=9
```

### Step 4 — проверяем смысл

9 месяцев должны дать:

```math
18+7(9)=81
```

Да.

---

## Worked Example 2 — taxi

> A taxi charges `$4` to start the ride and `$2.50` per mile. The total fare is `$24`. How many miles were traveled?

Перед уравнением заполните таблицу:

```text
fixed    = 4
rate     = 2.50
quantity = m
total    = 24
```

Модель:

```math
4+2.5m=24
```

```math
2.5m=20
```

```math
m=8
```

### Transfer

Хотя история другая — streaming service vs taxi — математический паттерн один и тот же.

Именно это нужно научиться видеть на SAT.

---

# 9. PATTERN 6 — Parameter questions

Hard SAT часто спрашивает не `x`, а coefficient или parameter.

Пример:

```math
k(x+3)=6x+18
```

Equation has infinitely many solutions. Find `k`.

## Что означает infinitely many solutions?

Обе стороны должны быть **одним и тем же выражением**.

Раскрываем левую:

```math
kx+3k=6x+18
```

Чтобы выражения совпадали для любого `x`:

```text
coefficient of x must match
constant must match
```

Сравниваем coefficient:

```math
k=6
```

Проверяем constant:

```math
3k=18
```

```math
k=6
```

Совпадает.

**Ответ: `6`.**

---

## Паттерн для параметров

Если спрашивают, при каком `k` уравнение имеет infinitely many solutions:

```text
упрости обе стороны
        ↓
сравни coefficient при x
        ↓
сравни constants
        ↓
оба должны совпасть
```

Если нужен **no solution**:

```text
coefficient при x совпадает
НО constants различаются
```

Пример структуры:

```math
5x+2=5x+k
```

Для no solution нужно:

```math
k\ne2
```

---

# 10. Method Selector — что делать первым?

Используйте этот decision tree.

```text
Есть x только с одной стороны?
│
├─ Да → isolate x, отменяя операции назад
│
└─ Нет
   ↓
Есть x с обеих сторон?
│
├─ Да → собрать x на одной стороне
│
└─ Нет

Есть скобки?
│
├─ Можно легко поделить обе стороны? → делим
│
└─ Иначе → distributive property

После упрощения x исчез?
│
├─ осталось FALSE → no solution
│
└─ осталось TRUE  → infinitely many solutions

Это word problem?
│
└─ сначала назвать quantities и построить модель

Спрашивают parameter?
│
└─ сравни structure / coefficients / constants
```

---

# 11. Desmos: когда полезен, а когда мешает

Простые linear equations обычно быстрее решать вручную.

Например:

```math
7x+4=39
```

Ручное решение занимает несколько секунд:

```math
7x=35
```

```math
x=5
```

Но Desmos полезен для **проверки** или когда уравнение неудобное.

## Способ через графики

Для

```math
5x+2=2x+17
```

введите:

```text
y=5x+2
y=2x+17
```

Точка пересечения имеет `x=5`.

### Что это означает геометрически?

Solution equation = x-coordinate точки, где две функции имеют одинаковое значение.

Так algebra и graph становятся одной идеей.

---

# 12. Error Clinic — 5 ошибок, которые нужно научиться ловить

## Ошибка 1 — изменить знак «потому что перенесли»

Лучше всегда называть реальную операцию.

```text
+7 мешает
→ вычитаю 7 с обеих сторон
```

---

## Ошибка 2 — distributive property только на первый член

Неверно:

```math
4(x+3)=4x+3
```

Правильно:

```math
4x+12
```

---

## Ошибка 3 — получить `5=9` и написать `x=0`

Если `x` исчез, это не означает `x=0`.

```math
5=9
```

означает **no solution**.

---

## Ошибка 4 — начать вычисления до построения word-problem model

Сначала подпишите:

```text
fixed
rate
quantity
total
```

Только потом пишите equation.

---

## Ошибка 5 — найти число, но ответить не на тот вопрос

SAT может спросить не `x`, а:

```math
2x+1
```

Если нашли `x=4`, ответ не `4`, а:

```math
2(4)+1=9
```

Всегда перечитывайте последнюю строку вопроса.

---

# 13. Guided Practice — подсказки постепенно исчезают

## Level A — pattern указан

### Problem A1

**Pattern: isolate the variable**

```math
6x+5=41
```

1. Что отменяем первым? `_____`
2. После этого получаем `_____`.
3. Ответ `x=_____`.

<details>
<summary>Решение</summary>

Вычитаем 5:

```math
6x=36
```

```math
x=6
```

</details>

---

## Level B — паттерн нужно назвать

### Problem B1

```math
7x-8=3x+20
```

Перед решением заполните:

```text
Pattern: ____________________
Первое действие: ____________
```

<details>
<summary>Решение</summary>

Pattern: variable on both sides.

Вычитаем `3x`:

```math
4x-8=20
```

```math
4x=28
```

```math
x=7
```

</details>

---

## Level C — word problem

### Problem C1

A gym charges a `$25` registration fee plus `$15` per month. A member paid `$130` total. For how many months was the membership active?

Перед решением заполните:

```text
fixed    = ____
rate     = ____
quantity = ____
total    = ____
```

<details>
<summary>Решение</summary>

```text
fixed    = 25
rate     = 15
quantity = m
total    = 130
```

```math
25+15m=130
```

```math
15m=105
```

```math
m=7
```

</details>

---

## Level D — SAT Hard transfer

### Problem D1

For what value of `k` does the equation

```math
4(x+5)=kx+20
```

have infinitely many solutions?

Не начинайте с вычислений. Сначала ответьте:

> Что должно быть правдой об обеих сторонах для **любого** `x`?

<details>
<summary>Решение</summary>

Раскрываем левую:

```math
4x+20=kx+20
```

Для infinitely many solutions коэффициенты должны совпадать:

```math
k=4
```

</details>

---

# 14. SAT-style Independent Practice

Теперь подсказки убраны.

## Problem 1 — Easy — Multiple Choice

What value of `x` satisfies

```math
4x+9=29?
```

**A)** `4`  
**B)** `5`  
**C)** `7`  
**D)** `8`

---

## Problem 2 — Easy — SPR

```math
5(x-2)=35
```

Find `x`.

---

## Problem 3 — Medium — Multiple Choice

Which equation has **no solution**?

**A)** `2x+6=18`  
**B)** `3(x+4)=3x+12`  
**C)** `4x+5=4x+9`  
**D)** `7x-3=4x+12`

---

## Problem 4 — Medium — SPR

A rental service charges a fixed fee of `$12` plus `$6` per hour. The total cost is `$54`. How many hours was the item rented?

---

## Problem 5 — Medium/Hard — Multiple Choice

If

```math
3x+7=25,
```

what is the value of

```math
6x+14?
```

**A)** `12`  
**B)** `25`  
**C)** `36`  
**D)** `50`

> **Pattern clue after solving:** иногда SAT не требует находить `x`; выражение `6x+14` — это ровно `2(3x+7)`.

---

## Problem 6 — Hard — Multiple Choice

The equation

```math
k(x-4)=5x-20
```

has infinitely many solutions. What is `k`?

**A)** `4`  
**B)** `5`  
**C)** `20`  
**D)** `25`

---

## Problem 7 — Hard — SPR

For what value of `a` does

```math
6x+9=6x+a
```

have infinitely many solutions?

---

## Problem 8 — 750–800 Pattern Recognition

The equation

```math
3(2x+p)=6x+21
```

has infinitely many solutions. Find `p`.

<details>
<summary><strong>Ответы и разбор паттернов</strong></summary>

### 1

**B, `5`.**

Pattern: isolate the variable.

```math
4x+9=29
```

```math
4x=20
```

```math
x=5
```

### 2

**`9`.**

Самый короткий путь: сначала разделить на 5.

```math
x-2=7
```

```math
x=9
```

### 3

**C.**

```math
4x+5=4x+9
```

после вычитания `4x`:

```math
5=9
```

FALSE → no solution.

Вариант B даёт TRUE identity → infinitely many solutions.

### 4

**`7`.**

Pattern: fixed + rate × quantity.

```math
12+6h=54
```

```math
6h=42
```

```math
h=7
```

### 5

**D, `50`.**

Можно найти `x=6`, но есть более быстрый pattern.

Дано:

```math
3x+7=25
```

Искомое:

```math
6x+14=2(3x+7)
```

Поэтому:

```math
6x+14=2(25)=50
```

Это пример SAT efficiency: иногда лучше преобразовать искомое выражение, чем решать всё уравнение.

### 6

**B, `5`.**

Раскрываем:

```math
kx-4k=5x-20
```

Для infinitely many solutions коэффициенты и constants должны совпасть.

```math
k=5
```

Проверка:

```math
-4k=-20
```

тоже даёт `k=5`.

### 7

**`9`.**

Для infinitely many solutions обе стороны должны быть одинаковыми:

```math
6x+9=6x+a
```

поэтому `a=9`.

### 8

**`7`.**

Раскрываем:

```math
6x+3p=6x+21
```

Для infinitely many solutions:

```math
3p=21
```

```math
p=7
```

</details>

---

# 15. Transfer Questions — можете объяснить без вычислений?

Ответьте словами.

1. Почему из `3x+7=25` нельзя просто убрать `7` только слева?
2. Почему в `5x+2=2x+17` полезно сначала собрать все `x` на одной стороне?
3. Как понять разницу между no solution и infinitely many solutions, если `x` исчез?
4. Почему `3(x+4)=21` быстрее начать с деления на `3`, а не обязательно раскрывать скобки?
5. Какие четыре величины ищем в word problem типа subscription/taxi?
6. Если equation has infinitely many solutions, что должно совпасть после упрощения?
7. Когда Desmos для linear equation помогает, а когда только замедляет?

Если можете ответить на эти вопросы без подсказки, вы понимаете тему глубже, чем просто умеете повторить алгоритм.

---

# 16. Мини-чек-лист

Перед переходом к следующей теме убедитесь:

- [ ] Я сначала определяю **паттерн задачи**, а потом считаю.
- [ ] Я понимаю equation как balance, а не как набор правил «переноса».
- [ ] Я умею отменять операции в обратном порядке.
- [ ] Я умею собирать variable terms на одной стороне.
- [ ] Я правильно раскрываю parentheses.
- [ ] Я различаю one solution / no solution / infinitely many solutions.
- [ ] Я узнаю `fixed + rate × quantity` в word problems.
- [ ] Я умею решать parameter questions на совпадение coefficients/constants.
- [ ] Я проверяю, что отвечаю именно на то, что спросили.
- [ ] Я могу объяснить, **почему** выбрал этот метод.

---

# 17. Что дальше

Следующие темы используют те же идеи:

```text
Linear Equations
      ↓
Linear Equations in Two Variables
      ↓
Linear Functions
      ↓
Systems of Equations
      ↓
Linear Inequalities
```

Если этот урок освоен хорошо, следующие разделы становятся намного проще: меняется форма задачи, но базовый навык построения и преобразования уравнений остаётся тем же.
