# SAT Math — полный учебный курс на русском языке

Этот репозиторий — системный курс подготовки к **Digital SAT Math** для старшеклассников 15–18 лет. Материалы объясняют математику простым русским языком, но сохраняют экзаменационную английскую терминологию: *slope*, *intercept*, *vertex*, *discriminant*, *margin of error*, *student-produced response* и другие термины.

## Актуальный формат SAT Math

- **44 задания** за **70 минут**.
- **2 адаптивных модуля** по 35 минут.
- В каждом модуле представлены все четыре Math domains.
- Используются **Multiple Choice** и **Student-Produced Response (SPR / grid-in)**.
- Примерно 30% вопросов — contextual / word problems.
- Калькулятор доступен на всём Math section; в Bluebook встроен Desmos.

## Официальные Math content domains

| Domain | Доля | Официальные skills |
|---|---:|---|
| **Algebra** | ≈35% | Linear equations in 1 variable; linear equations in 2 variables; linear functions; systems; linear inequalities |
| **Advanced Math** | ≈35% | Equivalent expressions; nonlinear equations; systems in 2 variables; nonlinear functions |
| **Problem-Solving and Data Analysis** | ≈15% | Ratios/rates/units; percentages; one-variable data; two-variable data; probability; inference & margin of error; statistical claims |
| **Geometry and Trigonometry** | ≈15% | Area & volume; lines/angles/triangles; right triangles & trigonometry; circles |

## Как устроен каждый урок

Каждая тема — отдельный Markdown-файл с единым 8-секционным шаблоном:

1. **Заголовок и краткое описание** — зачем тема нужна на SAT.
2. **Ключевые понятия и формулы** — таблицы, определения, визуальные якоря.
3. **Guided Example** — пошаговое решение с объяснением, почему выполняется каждый шаг.
4. **Practice Problems** — Easy → Medium → Hard, Multiple Choice и Grid-in.
5. **Common Traps** — типичные ошибки и способы их избежать.
6. **Digital SAT Strategy** — когда решать вручную, когда использовать Desmos.
7. **Связи с другими темами** — зависимости внутри курса.
8. **Мини-чек-лист** — «Я умею…» для самопроверки.

Ответы к упражнениям скрыты в `<details>`, чтобы ученик сначала сделал собственную попытку.

---

# Полная карта курса

## 1. Algebra

Официальный домен закрыт по всем пяти skills.

| Тема | Файл | Статус |
|---|---|---|
| Linear equations in one variable | [`algebra/linear_equations.md`](algebra/linear_equations.md) | ✅ |
| Linear equations in two variables | [`algebra/linear_equations_two_variables.md`](algebra/linear_equations_two_variables.md) | ✅ |
| Linear functions | [`algebra/linear_functions.md`](algebra/linear_functions.md) | ✅ |
| Systems of two linear equations | [`algebra/systems_of_equations.md`](algebra/systems_of_equations.md) | ✅ |
| Linear inequalities in one or two variables | [`algebra/linear_inequalities.md`](algebra/linear_inequalities.md) | ✅ |

### Рекомендуемый порядок

```text
Linear equations (1 variable)
        ↓
Linear equations (2 variables)
        ↓
Linear functions
        ↓
Systems
        ↓
Linear inequalities
```

---

## 2. Advanced Math

Официальные skills раскрыты отдельными тематическими уроками, чтобы quadratic, exponential, polynomial, rational, radical и absolute-value задачи не смешивались в один перегруженный файл.

| Тема | Файл | Статус |
|---|---|---|
| Equivalent expressions | [`advanced_math/equivalent_expressions.md`](advanced_math/equivalent_expressions.md) | ✅ |
| Quadratics | [`advanced_math/quadratics.md`](advanced_math/quadratics.md) | ✅ |
| Polynomial functions | [`advanced_math/polynomial_functions.md`](advanced_math/polynomial_functions.md) | ✅ |
| Exponential functions | [`advanced_math/exponential_functions.md`](advanced_math/exponential_functions.md) | ✅ |
| Rational expressions and equations | [`advanced_math/rational_expressions_equations.md`](advanced_math/rational_expressions_equations.md) | ✅ |
| Radicals and radical equations | [`advanced_math/radicals_and_radical_equations.md`](advanced_math/radicals_and_radical_equations.md) | ✅ |
| Absolute value | [`advanced_math/absolute_value.md`](advanced_math/absolute_value.md) | ✅ |
| Nonlinear functions | [`advanced_math/nonlinear_functions.md`](advanced_math/nonlinear_functions.md) | ✅ |
| Nonlinear equations and systems | [`advanced_math/nonlinear_equations_systems.md`](advanced_math/nonlinear_equations_systems.md) | ✅ |

### Рекомендуемый порядок

```text
Equivalent expressions
        ↓
Quadratics → Polynomials
        ↓
Exponentials
        ↓
Rational + Radical + Absolute Value
        ↓
Nonlinear Functions
        ↓
Nonlinear Equations & Systems
```

---

## 3. Problem-Solving and Data Analysis

Все официальные SAT skills этого домена вынесены в отдельные уроки.

| Тема | Файл | Статус |
|---|---|---|
| Ratios, rates, proportional relationships, units | [`problem_solving_data_analysis/ratios_rates_units.md`](problem_solving_data_analysis/ratios_rates_units.md) | ✅ |
| Percentages | [`problem_solving_data_analysis/percentages.md`](problem_solving_data_analysis/percentages.md) | ✅ |
| One-variable data: center and spread | [`problem_solving_data_analysis/one_variable_statistics.md`](problem_solving_data_analysis/one_variable_statistics.md) | ✅ |
| Two-variable data: models and scatterplots | [`problem_solving_data_analysis/two_variable_data_scatterplots.md`](problem_solving_data_analysis/two_variable_data_scatterplots.md) | ✅ |
| Probability and conditional probability | [`problem_solving_data_analysis/probability_conditional_probability.md`](problem_solving_data_analysis/probability_conditional_probability.md) | ✅ |
| Inference and margin of error | [`problem_solving_data_analysis/sampling_margin_of_error.md`](problem_solving_data_analysis/sampling_margin_of_error.md) | ✅ |
| Observational studies and experiments | [`problem_solving_data_analysis/observational_studies_experiments.md`](problem_solving_data_analysis/observational_studies_experiments.md) | ✅ |

### Рекомендуемый порядок

```text
Ratios / Rates / Units
        ↓
Percentages
        ↓
One-variable Statistics
        ↓
Scatterplots & Models
        ↓
Probability
        ↓
Sampling & Margin of Error
        ↓
Studies / Experiments / Statistical Claims
```

---

## 4. Geometry and Trigonometry

Все четыре официальных skills покрыты.

| Тема | Файл | Статус |
|---|---|---|
| Area and volume | [`geometry_trigonometry/area_volume.md`](geometry_trigonometry/area_volume.md) | ✅ |
| Lines, angles, and triangles | [`geometry_trigonometry/lines_angles_triangles.md`](geometry_trigonometry/lines_angles_triangles.md) | ✅ |
| Right triangles and trigonometry | [`geometry_trigonometry/right_triangles_trigonometry.md`](geometry_trigonometry/right_triangles_trigonometry.md) | ✅ |
| Circles | [`geometry_trigonometry/circles.md`](geometry_trigonometry/circles.md) | ✅ |

### Рекомендуемый порядок

```text
Lines / Angles / Triangles
        ↓
Area / Volume / Scale
        ↓
Right Triangles
        ↓
Trigonometry
        ↓
Circles
```

---

# Practice System

Теория связана с отдельным практическим слоем в [`practice/`](practice/README.md).

## Domain Question Bank — Set 01

Первый пакет содержит **80 оригинальных задач** — по 20 на каждый официальный домен.

| Domain | Practice set | Questions |
|---|---|---:|
| Algebra | [`practice/question_bank/algebra_set_01.md`](practice/question_bank/algebra_set_01.md) | 20 |
| Advanced Math | [`practice/question_bank/advanced_math_set_01.md`](practice/question_bank/advanced_math_set_01.md) | 20 |
| Problem-Solving and Data Analysis | [`practice/question_bank/psda_set_01.md`](practice/question_bank/psda_set_01.md) | 20 |
| Geometry and Trigonometry | [`practice/question_bank/geometry_trigonometry_set_01.md`](practice/question_bank/geometry_trigonometry_set_01.md) | 20 |

Каждая задача помечается skill, difficulty, response type и рекомендацией по использованию Desmos.

## Timed Modules

Собраны два самостоятельных модуля по **22 вопроса / 35 минут**.

| Module | Роль | Questions |
|---|---|---:|
| [`Math Module 01`](practice/timed_modules/math_module_01.md) | базовый mixed module | 22 |
| [`Module 01 Answers`](practice/timed_modules/math_module_01_answers.md) | решения + error log | — |
| [`Math Module 02 — Hard Route`](practice/timed_modules/math_module_02_hard.md) | усложнённый adaptive-style route | 22 |
| [`Module 02 Answers`](practice/timed_modules/math_module_02_hard_answers.md) | решения + diagnostic interpretation | — |

На текущем этапе практический слой содержит **124 оригинальных задания** помимо Practice Problems внутри каждого теоретического урока.

## Учебный цикл

```text
Lesson
  ↓
Practice Problems внутри урока
  ↓
Domain Question Bank
  ↓
Mixed Timed Module
  ↓
Error Log
  ↓
Targeted Review
  ↓
Hard Route / повторный модуль
```

Для каждой ошибки фиксируется причина:

- Concept gap
- Wrong model
- Algebra/arithmetic error
- Misread question
- Desmos misuse
- Time pressure
- Careless error

---

# Рекомендуемый маршрут подготовки

## Stage 1 — Foundation

Закрыть Algebra до автоматизма:

```text
Linear Equations → Linear Functions → Systems → Inequalities
```

## Stage 2 — Advanced Math

```text
Equivalent Expressions → Quadratics → Polynomials → Exponentials
→ Rational/Radical/Absolute Value → Nonlinear Systems
```

## Stage 3 — Data Reasoning

```text
Ratios → Percentages → Statistics → Scatterplots → Probability
→ Sampling → Experimental Design
```

## Stage 4 — Geometry & Trigonometry

```text
Angles/Triangles → Area/Volume → Right Triangles/Trig → Circles
```

## Stage 5 — Mixed Digital SAT Practice

1. untimed accuracy;
2. domain question banks;
3. timed mixed modules;
4. hard-route modules;
5. full Bluebook tests;
6. error log → targeted review → повторный тест.

---

# Как работать с Desmos

Desmos — не замена математике, а инструмент ускорения.

**Особенно полезен для:**

- intersections of equations;
- systems;
- quadratic roots and vertex;
- nonlinear equations;
- regression;
- graph interpretation;
- checking equivalent functions.

**Часто быстрее вручную:**

- simple linear equations;
- basic factoring;
- ratios and percentages;
- angle relationships;
- straightforward probability.

Главный вопрос перед использованием калькулятора:

> Что быстрее и надёжнее именно для этой задачи: algebra, graph или numerical calculation?

---

# Официальные источники

Карта курса сверяется с текущей структурой College Board:

- [SAT Math Overview](https://satsuite.collegeboard.org/sat/whats-on-the-test/math/overview)
- [Math Content Domains and Skills](https://satsuite.collegeboard.org/practice/content-domains)
- [Math Specifications](https://satsuite.collegeboard.org/k12-educators/about/alignment/math)

---

> **Цель курса:** не заучить набор формул, а научиться распознавать математическую модель, выбирать самый эффективный способ решения, проверять результат и стабильно работать в условиях Digital SAT.
