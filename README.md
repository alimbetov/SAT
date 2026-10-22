# SAT Math — русскоязычный курс подготовки к Digital SAT

Этот репозиторий построен как учебная система, а не как набор формул и случайных задач.

## Учебная модель

Теоретические уроки используют **Pedagogy V2**:

```text
Recognize → Pattern → Choose → Solve → Check → Transfer
```

Практика использует **Practice V2**:

```text
Recognition → Core Pattern → Guided Variation → Word Problem → Trap → Transfer → Hard/750–800
```

Полные стандарты:

- [`docs/PEDAGOGY_V2.md`](docs/PEDAGOGY_V2.md)
- [`docs/PRACTICE_V2.md`](docs/PRACTICE_V2.md)

## SAT Math coverage

Курс покрывает все четыре content domains Digital SAT Math:

| Domain | Lessons |
|---|---:|
| Algebra | 5 |
| Advanced Math | 9 |
| Problem-Solving and Data Analysis | 7 |
| Geometry and Trigonometry | 4 |
| **Total** | **25** |

## Теория — 25 V2 lessons

### Algebra

- [`linear_equations.md`](algebra/linear_equations.md)
- [`linear_equations_two_variables.md`](algebra/linear_equations_two_variables.md)
- [`linear_functions.md`](algebra/linear_functions.md)
- [`systems_of_equations.md`](algebra/systems_of_equations.md)
- [`linear_inequalities.md`](algebra/linear_inequalities.md)

### Advanced Math

- [`equivalent_expressions.md`](advanced_math/equivalent_expressions.md)
- [`quadratics.md`](advanced_math/quadratics.md)
- [`polynomial_functions.md`](advanced_math/polynomial_functions.md)
- [`exponential_functions.md`](advanced_math/exponential_functions.md)
- [`rational_expressions_equations.md`](advanced_math/rational_expressions_equations.md)
- [`radicals_and_radical_equations.md`](advanced_math/radicals_and_radical_equations.md)
- [`absolute_value.md`](advanced_math/absolute_value.md)
- [`nonlinear_functions.md`](advanced_math/nonlinear_functions.md)
- [`nonlinear_equations_systems.md`](advanced_math/nonlinear_equations_systems.md)

### Problem-Solving and Data Analysis

- [`ratios_rates_units.md`](problem_solving_data_analysis/ratios_rates_units.md)
- [`percentages.md`](problem_solving_data_analysis/percentages.md)
- [`one_variable_statistics.md`](problem_solving_data_analysis/one_variable_statistics.md)
- [`two_variable_data_scatterplots.md`](problem_solving_data_analysis/two_variable_data_scatterplots.md)
- [`probability_conditional_probability.md`](problem_solving_data_analysis/probability_conditional_probability.md)
- [`sampling_margin_of_error.md`](problem_solving_data_analysis/sampling_margin_of_error.md)
- [`observational_studies_experiments.md`](problem_solving_data_analysis/observational_studies_experiments.md)

### Geometry and Trigonometry

- [`lines_angles_triangles.md`](geometry_trigonometry/lines_angles_triangles.md)
- [`area_volume.md`](geometry_trigonometry/area_volume.md)
- [`right_triangles_trigonometry.md`](geometry_trigonometry/right_triangles_trigonometry.md)
- [`circles.md`](geometry_trigonometry/circles.md)

## Practice V2 — 624 questions

| Layer | Questions | Purpose |
|---|---:|---|
| Topic Drills | **500** | pattern learning + method choice |
| Domain Mixed Sets | **80** | independent transfer |
| Timed Modules | **44** | exam-like performance |
| **Total** | **624** | |

Start here: [`practice/README.md`](practice/README.md).

### Topic Drills

Каждая из 25 тем имеет 20 targeted questions:

```text
Drill 01
Recognition → Core → Variation → Word → Trap → Transfer

Drill 02
Method Selection → Hard Variations → Trap Clinic → Transfer → 750–800
```

Index: [`practice/topic_drills/README.md`](practice/topic_drills/README.md).

### Mixed Domain Sets

Pattern hints скрыты во время попытки. После выполнения используются отдельные diagnostic maps:

- Algebra — 20
- Advanced Math — 20
- PSDA — 20
- Geometry & Trigonometry — 20

Index: [`practice/question_bank/README.md`](practice/question_bank/README.md).

### Timed Modules

- Module 01 — 22 questions / 35 minutes
- Module 02 Hard Route — 22 questions / 35 minutes

Timed questions intentionally contain no scaffolding. Practice V2 learning happens in the post-test diagnostics.

## Error taxonomy

Курс отслеживает не только «правильно/неправильно», но и причину ошибки:

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

## Recommended learning loop

```text
Lesson V2
   ↓
Topic Drill 01
   ↓
Error Clinic
   ↓
Topic Drill 02
   ↓
Domain Mixed Set
   ↓
Diagnostic Map
   ↓
Timed Module 01
   ↓
Targeted Repair
   ↓
Hard Route Module 02
```

Главная метрика курса — не количество решённых задач, а способность ученика:

1. распознать pattern;
2. выбрать короткий метод;
3. решить без технической ошибки;
4. проверить результат;
5. перенести метод на новую формулировку.

После устойчивого освоения этого слоя следующий уровень курса — **Desmos Speed Drills → 750–800 Challenge Sets → full 44-question simulations**.
