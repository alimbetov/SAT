# SAT Math Practice — Question Bank и timed practice

Этот раздел превращает теорию репозитория в системную практику.

## Формат

Каждая задача имеет метаданные:

- **Domain** — официальный Math content domain College Board;
- **Skill** — конкретный навык;
- **Difficulty** — `Foundation`, `Easy`, `Medium`, `Hard`, `750–800`;
- **Type** — `Multiple Choice` или `Student-Produced Response (SPR / Grid-in)`;
- **Tool** — `Manual`, `Desmos useful`, `Desmos recommended`.

Все задачи в репозитории — **оригинальные учебные задачи**, написанные в стиле Digital SAT. Они не являются копиями вопросов College Board.

## Структура

```text
practice/
├── README.md
├── question_bank/
│   ├── algebra_set_01.md
│   ├── advanced_math_set_01.md
│   ├── psda_set_01.md
│   └── geometry_trigonometry_set_01.md
└── timed_modules/
    ├── math_module_01.md
    └── math_module_01_answers.md
```

## Как работать с Question Bank

1. Сначала пройти соответствующий урок из теоретической части.
2. Решить тематический set **без ответов**.
3. Отметить каждый вопрос как:
   - ✅ уверен;
   - ⚠️ решил, но не уверен;
   - ❌ не решил / ошибся.
4. Разобрать только ⚠️ и ❌.
5. Через 2–3 дня повторить ошибочные типы задач.

## Шкала сложности

| Уровень | Что проверяется |
|---|---|
| Foundation | определение, формула, один прямой шаг |
| Easy | стандартная SAT-модель, 1–2 шага |
| Medium | несколько действий или перевод текста в модель |
| Hard | скрытая структура, параметр, несколько представлений |
| 750–800 | оптимизация метода, параметр, ловушка, нетривиальная интерпретация |

## Timed Modules

Digital SAT Math содержит два модуля по **22 вопроса / 35 минут**. Поэтому тренировочный модуль в этом репозитории также состоит из 22 задач.

Режим:

```text
35:00 — старт
20:00 — контроль: примерно половина вопросов завершена
05:00 — оставить время на marked questions
00:00 — остановиться
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

## Цель следующего расширения

Довести банк до минимум **20–30 задач на каждую отдельную тему**, а затем собирать из них:

- topic drills;
- mixed domain sets;
- 22-question adaptive-style modules;
- 44-question full Math simulations;
- отдельные `750–800` challenge sets.
