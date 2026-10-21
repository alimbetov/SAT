# Absolute Value — модуль числа и функции с модулем

## 1. Заголовок и краткое описание

Absolute value на SAT встречается внутри Advanced Math как один из типов nonlinear equations/functions. Нужно понимать модуль как расстояние, решать equations/inequalities и читать V-shaped graphs.

> **Главная идея:** `|x-a|` — это расстояние от `x` до `a` на числовой прямой.

---

## 2. Ключевые понятия и формулы

| Выражение | Смысл |
|---|---|
| `|x|` | расстояние от `x` до 0 |
| `|x-a|=d` | расстояние от `x` до `a` равно `d` |
| `|x-a|<d` | `x` внутри интервала вокруг `a` |
| `|x-a|>d` | `x` вне интервала вокруг `a` |
| `y=a|x-h|+k` | vertex `(h,k)` |

Если `d≥0`:

```math
|x-a|=d
```

даёт

```math
x=a+d\quad\text{или}\quad x=a-d.
```

### Визуальный якорь

Absolute value = **distance**, поэтому результат модуля не бывает отрицательным.

---

## 3. Пошаговый разбор — Guided Example

Solve:

```math
|2x-5|=9.
```

### Шаг 1. Создаём два случая

Расстояние 9 означает, что выражение внутри модуля может быть `9` или `-9`:

```math
2x-5=9
```

или

```math
2x-5=-9.
```

### Шаг 2. Решаем первый случай

```math
2x=14\Rightarrow x=7.
```

### Шаг 3. Решаем второй случай

```math
2x=-4\Rightarrow x=-2.
```

### Шаг 4. Проверяем

Оба значения дают модуль 9.

**Ответы: `-2` и `7`.**

---

## 4. Practice Problems — задачи для закрепления

### Problem 1 — Easy — Multiple Choice

What is `|-8|`?

**A)** -8  **B)** 0  **C)** 8  **D)** 16

### Problem 2 — Easy — Grid-in

Solve `|x-3|=5`. Enter the positive solution.

### Problem 3 — Medium — Multiple Choice

What is the vertex of `y=|x-4|+2`?

**A)** `(-4,2)`  **B)** `(4,2)`  **C)** `(2,4)`  **D)** `(4,-2)`

### Problem 4 — Medium — Multiple Choice

Which inequality is equivalent to `|x|<6`?

**A)** `x<6`  **B)** `x>-6`  **C)** `-6<x<6`  **D)** `x<-6 or x>6`

### Problem 5 — Hard — Grid-in

The equation `|3x+1|=10` has two solutions. What is the larger solution?

<details><summary><strong>Ответы и краткие решения</strong></summary>

1. **C**.  
2. **8**, потому что `x=3±5`.  
3. **B**.  
4. **C**.  
5. **3**, из `3x+1=10` получаем `x=3`; второй root `-11/3`.

</details>

---

## 5. Common Traps — типичные ловушки

- Считать, что `|x|` просто «меняет знак». Это distance, а не операция смены знака.
- Забывать второй случай в equation `|A|=d`.
- Пытаться решить `|A|=-3`: решений нет, потому что absolute value неотрицателен.

---

## 6. Стратегия для Digital SAT

В Desmos `y=abs(x-4)+2` строит V-shaped graph. Для equations удобно построить `y=abs(...)` и горизонтальную линию. Количество intersections показывает количество решений.

---

## 7. Связи с другими темами

**Опирается на:** linear equations, inequalities, functions.  
**Связано с:** nonlinear functions, distance models, piecewise reasoning.

---

## 8. Мини-чек-лист для самопроверки

- [ ] Я понимаю absolute value как расстояние.
- [ ] Я решаю equations с двумя случаями.
- [ ] Я решаю базовые absolute-value inequalities.
- [ ] Я читаю vertex V-shaped graph.
