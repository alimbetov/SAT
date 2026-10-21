# SAT Math Practice — Question Bank и timed practice

Этот раздел превращает теорию репозитория в системную практику.

## Формат

Каждая задача использует единый набор метаданных:

- **Domain** — официальный Math content domain College Board;
- **Skill** — конкретный навык;
- **Difficulty** — `Foundation`, `Easy`, `Medium`, `Hard`, `750–800`;
- **Type** — `Multiple Choice` или `Student-Produced Response (SPR / Grid-in)`;
- **Tool** — `Manual`, `Desmos useful`, `Desmos recommended`.

Все задачи — **оригинальные учебные задачи**, написанные в стиле Digital SAT. Они не являются копиями вопросов College Board.

## Текущий объём практики

| Layer | Questions |
|---|---:|
| Topic Drills Set 01 | 250 |
| Domain Question Bank Set 01 | 80 |
| Timed Module 01 | 22 |
| Timed Module 02 — Hard Route | 22 |
| **Итого** | **374** |

Это не включает Practice Problems, уже встроенные в 25 теоретических уроков.

## Структура

```text
practice/
├── README.md
├── topic_drills/
│   ├── README.md
│   ├── algebra/
│   ├── advanced_math/
│   ├── problem_solving_data_analysis/
│   └── geometry_trigonometry/
├── question_bank/
│   ├── algebra_set_01.md
│   ├── advanced_math_set_01.md
│   ├── psda_set_01.md
│   └── geometry_trigonometry_set_01.md
└── timed_modules/
    ├── math_module_01.md
    ├── math_module_01_answers.md
    ├── math_module_02_hard.md
    └── math_module_02_hard_answers.md
```

## 1. Topic Drills

[`topic_drills/README.md`](topic_drills/README.md) содержит полный индекс.

Первый targeted batch:

- 25 тем;
- по 10 задач на каждую тему;
- **250 topic-specific questions**.

Рекомендуемый gate:

- **9–10/10** → переходить к mixed practice;
- **7–8/10** → targeted error review;
- **≤6/10** → вернуться к lesson и Guided Example.

## 2. Domain Question Bank

После точечной отработки темы переходите к смешанным вопросам внутри домена:

- [`question_bank/algebra_set_01.md`](question_bank/algebra_set_01.md)
- [`question_bank/advanced_math_set_01.md`](question_bank/advanced_math_set_01.md)
- [`question_bank/psda_set_01.md`](question_bank/psda_set_01.md)
- [`question_bank/geometry_trigonometry_set_01.md`](question_bank/geometry_trigonometry_set_01.md)

Каждый set содержит 20 вопросов.

## 3. Timed Modules

Digital SAT Math содержит два модуля по **22 вопроса / 35 минут**. Поэтому тренировочные модули используют тот же размер.

- [`Math Module 01`](timed_modules/math_module_01.md) — mixed baseline;
- [`Module 01 Answers`](timed_modules/math_module_01_answers.md);
- [`Math Module 02 — Hard Route`](timed_modules/math_module_02_hard.md) — усложнённый adaptive-style route;
- [`Module 02 Answers`](timed_modules/math_module_02_hard_answers.md).

Режим:

```text
35:00 — старт
20:00 — контроль: примерно половина вопросов завершена
05:00 — оставить время на marked questions
00:00 — остановиться
```

## Полный учебный цикл

```text
Lesson
  ↓
Practice Problems внутри lesson
  ↓
Topic Drill
  ↓
Domain Mixed Set
  ↓
Timed Module
  ↓
Error Log
  ↓
Targeted Review
  ↓
Hard Route / повторный модуль
```

После модуля анализируйте не только score, но и причину каждой ошибки:

```text
Concept gap
Algebra/arithmetic error
Misread question
Wrong model
Desmos misuse
Time pressure
Careless error
```

## Шкала сложности

| Уровень | Что проверяется |
|---|---|
| Foundation | определение, формула, один прямой шаг |
| Easy | стандартная SAT-модель, 1–2 шага |
| Medium | несколько действий или перевод текста в модель |
| Hard | скрытая структура, параметр, несколько представлений |
| 750–800 | оптимизация метода, параметр, ловушка, нетривиальная интерпретация |

## Следующий quality gate

Targeted coverage сейчас составляет **10 задач на тему**. Следующая планка — `Drill 02`, чтобы довести каждую тему до **20 задач**, причём второй набор должен быть смещён в сторону:

- Medium;
- Hard;
- 750–800;
- word problems;
- parameter questions;
- Desmos-efficient questions;
- common SAT traps.

После этого можно собирать полноценные **44-question Math simulations** из независимого банка задач.
