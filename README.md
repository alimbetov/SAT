# SAT Math — русскоязычный курс с двумя уровнями входа

Этот репозиторий теперь разделяет две разные задачи:

1. **построить математический фундамент**;
2. **подготовиться к Digital SAT Math**.

Это важно: наличие SAT-темы в репозитории не означает, что каждый школьник должен изучать её прямо сейчас.

---

# Сначала выберите маршрут

## Foundation Track

Для ученика, который ещё строит школьную базу и которому важнее понимание, чем экзаменационная скорость.

**Начать здесь:** [`study_paths/grade_6_foundation.md`](study_paths/grade_6_foundation.md)

Подача:

```text
CONCRETE
реальная ситуация
    ↓
VISUAL
рисунок / таблица / весы / bar model
    ↓
VERBAL
объяснение своими словами
    ↓
SYMBOLIC
x, y, formula
    ↓
SAT ENGLISH
короткая экзаменационная формулировка
```

Foundation modules:

1. [`Equation Balance`](foundation/01_equation_balance.md)
2. [`Ratios, Rates, Percentages`](foundation/02_ratios_rates_percentages.md)
3. [`Geometry Visual Reasoning`](foundation/03_geometry_visual_reasoning.md)
4. [`Coordinates and Linear Patterns`](foundation/04_coordinates_and_linear_patterns.md)
5. [`Squares, Roots, Quadratic Bridge`](foundation/05_squares_roots_quadratic_bridge.md)

Для этого маршрута **не нужен ранний таймер**. Сначала понимание и accuracy.

---

## SAT Bridge Track

Для ученика, который уже владеет базовой школьной алгеброй и геометрией и готов связывать их с SAT patterns, English wording, Desmos и временем.

**Начать здесь:** [`study_paths/grade_9_sat_bridge.md`](study_paths/grade_9_sat_bridge.md)

Подача:

```text
Prerequisite Check
→ Pattern
→ Method Choice
→ Worked Example
→ Variation
→ SAT Wording
→ Transfer
→ Timed Practice
```

---

# Учебные стандарты

Теоретические SAT-уроки используют **Pedagogy V2**:

```text
Recognize → Pattern → Choose → Solve → Check → Transfer
```

Практика использует **Practice V2**:

```text
Recognition → Core Pattern → Guided Variation → Word Problem → Trap → Transfer → Hard/750–800
```

Возрастно-адаптивная подача добавляет:

```text
Prerequisite Gate
→ Concrete / Visual Bridge
→ Think-Aloud Example
→ Faded Example
→ Mastery Gate
```

Документы:

- [`docs/PEDAGOGY_V2.md`](docs/PEDAGOGY_V2.md)
- [`docs/PRACTICE_V2.md`](docs/PRACTICE_V2.md)
- [`docs/AGE_ADAPTIVE_PEDAGOGY.md`](docs/AGE_ADAPTIVE_PEDAGOGY.md)
- [`docs/PEDAGOGICAL_AUDIT_AGE_ADAPTIVE.md`](docs/PEDAGOGICAL_AUDIT_AGE_ADAPTIVE.md)

---

# SAT Math coverage

Курс покрывает четыре content domains Digital SAT Math.

| Domain | Lessons |
|---|---:|
| Algebra | 5 |
| Advanced Math | 9 |
| Problem-Solving and Data Analysis | 7 |
| Geometry and Trigonometry | 4 |
| **Total** | **25** |

---

# 1. Algebra

- [`linear_equations.md`](algebra/linear_equations.md)
- [`linear_equations_two_variables.md`](algebra/linear_equations_two_variables.md)
- [`linear_functions.md`](algebra/linear_functions.md)
- [`systems_of_equations.md`](algebra/systems_of_equations.md)
- [`linear_inequalities.md`](algebra/linear_inequalities.md)

### Если Algebra пока тяжёлая

Сначала:

```text
foundation/01_equation_balance
→ foundation/04_coordinates_and_linear_patterns
→ Algebra lessons
```

---

# 2. Advanced Math

- [`equivalent_expressions.md`](advanced_math/equivalent_expressions.md)
- [`quadratics.md`](advanced_math/quadratics.md)
- [`polynomial_functions.md`](advanced_math/polynomial_functions.md)
- [`exponential_functions.md`](advanced_math/exponential_functions.md)
- [`rational_expressions_equations.md`](advanced_math/rational_expressions_equations.md)
- [`radicals_and_radical_equations.md`](advanced_math/radicals_and_radical_equations.md)
- [`absolute_value.md`](advanced_math/absolute_value.md)
- [`nonlinear_functions.md`](advanced_math/nonlinear_functions.md)
- [`nonlinear_equations_systems.md`](advanced_math/nonlinear_equations_systems.md)

### Readiness warning

Advanced Math не должен быть первым входом для младшего ученика.

Перед Quadratics желательно пройти:

[`foundation/05_squares_roots_quadratic_bridge.md`](foundation/05_squares_roots_quadratic_bridge.md)

Rational equations, nonlinear systems и другие поздние темы изучаются только после уверенной Algebra foundation.

---

# 3. Problem-Solving and Data Analysis

- [`ratios_rates_units.md`](problem_solving_data_analysis/ratios_rates_units.md)
- [`percentages.md`](problem_solving_data_analysis/percentages.md)
- [`one_variable_statistics.md`](problem_solving_data_analysis/one_variable_statistics.md)
- [`two_variable_data_scatterplots.md`](problem_solving_data_analysis/two_variable_data_scatterplots.md)
- [`probability_conditional_probability.md`](problem_solving_data_analysis/probability_conditional_probability.md)
- [`sampling_margin_of_error.md`](problem_solving_data_analysis/sampling_margin_of_error.md)
- [`observational_studies_experiments.md`](problem_solving_data_analysis/observational_studies_experiments.md)

### Foundation entry

Для ratios/percentages сначала:

[`foundation/02_ratios_rates_percentages.md`](foundation/02_ratios_rates_percentages.md)

---

# 4. Geometry and Trigonometry

- [`lines_angles_triangles.md`](geometry_trigonometry/lines_angles_triangles.md)
- [`area_volume.md`](geometry_trigonometry/area_volume.md)
- [`right_triangles_trigonometry.md`](geometry_trigonometry/right_triangles_trigonometry.md)
- [`circles.md`](geometry_trigonometry/circles.md)

### Foundation entry

Сначала:

[`foundation/03_geometry_visual_reasoning.md`](foundation/03_geometry_visual_reasoning.md)

Trig, radians и unit circle можно изучать позднее, когда базовая geometry и algebra уже устойчивы.

---

# Practice V2 — 624 questions

| Layer | Questions | Purpose |
|---|---:|---|
| Topic Drills | **500** | pattern learning + method choice |
| Domain Mixed Sets | **80** | independent transfer |
| Timed Modules | **44** | exam-like performance |
| **Total** | **624** | |

Start: [`practice/README.md`](practice/README.md)

## Topic Drills

```text
Drill 01
Recognition → Core → Variation → Word → Trap → Transfer

Drill 02
Method Selection → Hard Variations → Trap Clinic → Transfer → 750–800
```

Для Foundation learner Topic Drill 01 начинается **после соответствующего foundation bridge и mastery gate**.

## Mixed Sets

Mixed sets intentionally hide pattern hints. Они проверяют, узнаёт ли ученик метод самостоятельно.

После попытки используются diagnostic maps.

## Timed Modules

- Module 01 — 22 questions / 35 minutes
- Module 02 Hard Route — 22 questions / 35 minutes

Таймер подключается только после устойчивой accuracy.

---

# Error taxonomy

```text
R — Recognition
M — Method choice
A — Algebra / Arithmetic
L — Language
C — Constraint / Domain
G — Graph / Data
T — Trap
K — Check / Interpretation
```

Ошибка используется как диагноз:

```text
wrong answer
→ why?
→ repair exact gap
→ solve variation
→ retrieval check later
```

---

# Recommended learning loops

## Foundation

```text
Foundation Bridge
→ worked example together
→ 3–5 untimed problems
→ explain one solution aloud
→ mastery gate
→ SAT lesson when ready
```

## SAT Bridge

```text
Lesson V2
→ Topic Drill 01
→ Error Clinic
→ Topic Drill 02
→ Domain Mixed Set
→ Diagnostic Map
→ Timed Module
→ Targeted Repair
```

---

# Главная метрика

Не количество прочитанных тем и не количество решённых вопросов.

Ученик должен уметь:

1. понять, что дано;
2. объяснить математический смысл;
3. распознать pattern;
4. выбрать method;
5. решить контролируемыми шагами;
6. проверить ответ;
7. перенести идею на новую формулировку.

Только после этого скорость становится полезной метрикой.