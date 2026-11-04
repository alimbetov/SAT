# Scoring, time capture and learner report — V1

## 1. Что фиксировать

**Учитывать время начала/окончания каждой темы — да.** В Foundation время записывается без обратного отсчёта и без ограничения. Для SAT Bridge можно включить отдельный timed mode только после прохождения mastery gate.

| Field | Тип / смысл | Требование |
|---|---|---|
| `student_code` | Псевдоним (не имя и не дата рождения) | Required |
| `attempt_id` | Идентификатор попытки | Required |
| `session_id` | Сессия M1–M5, E1–E4 и т.п. | Required |
| `topic_id` | Например ALG-01, EN-A1-01 | Required |
| `question_set_revision` | Версия банка, напр. v1.0 | Required |
| `topic_started_at` | ISO 8601 с offset, например 2026-11-04T10:00:00+05:00 | Required |
| `topic_finished_at` | То же, после выбора/сдачи ответа 5 | Required |
| `paused_seconds` | Паузы/перерывы | Required; default 0 |
| `elapsed_seconds` | finish - start | Derived |
| `active_seconds` | elapsed - paused | Derived; nonnegative |
| `answers` | 5 записей: `question_id, selected, correct, answered_at, seconds_spent(optional), changed_answer(optional)` | Required |
| `hint_used` | Подсказка / помощь родителей | Required boolean |
| `error_codes` | Классы ошибок, первичная + вторичные | For each mistake |
| `self_confidence` | 1/2/3: не уверен / частично / уверен | Optional |
| `teacher_note` | Пояснение причин ошибок | Optional |
| `status` | submitted / paused / incomplete / not_assessed | Required |
| `timing_mode` | observational / timed | Required |

### Формула времени

- `elapsed_seconds = topic_finished_at - topic_started_at`
- `active_seconds = max(0, elapsed_seconds - paused_seconds)`
- `seconds_per_question = active_seconds / answered_questions` (только для описания, не для оценки mastery).
- Пауза должна фиксироваться явно; закрытие браузера/потеря сети — **incomplete**, а не «очень медленно».
- Сохраняйте время каждого вопроса при наличии приложения; время темы остаётся обязательным.
- Не считать чтение объяснений после сдачи темы частью диагностического времени.

## 2. Точность и интерпретация малой выборки

`accuracy = correct / 5` только когда предъявлены и завершены все 5 заданий, без подсказок. В рамках диагностики пропущенный после предъявления вопрос помечать как unanswered и учитывать отдельно; не путать с not_assessed.

| Результат | Временная категория | Следующее действие |
|---|---|---|
| 0–2/5 | `GAP` | Вернуться к prerequisite и объяснению; затем новые задания |
| 3/5 | `VERIFY` | 2–3 новых задания, проверить тип ошибки |
| 4–5/5 | `PROVISIONAL_SECURE` | 1–2 новых transfer/prerequisite задач для подтверждения |
| Тема не проводилась | `NOT_ASSESSED` | Планировать диагностику или отложить по prerequisites |
| Попытка прервана | `INCOMPLETE` | Возобновить с новой попыткой по правилам сессии |

Нельзя утверждать «тема освоена навсегда» на основании 5 вопросов. Рекомендуемое подтверждение: **2/2 новых transfer задач без помощи** и повтор **5 новых вопросов через 7–14 дней** после обучения; критерий 4+/5 без критических ошибок. Это педагогические эвристики, не психометрически валидированные пороги.

**Точность — главный показатель стартовой диагностики.** Время, уверенность, ошибки при чтении и помощь могут изменить рекомендацию, но не подменять число правильных ответов.

## 3. Критические случаи

- `5/5` + явно запрошенная подсказка → `ASSISTED`, не confirmed.
- `5/5` + transfer failed → `VERIFY`.
- `2/5` + системные ошибки чтения английского → возможен языковой барьер, провести RU Math equivalence check.
- `0/5` + topic not taught yet → `NOT_READY`, а не вывод о способностях.
- `3/5` + ответ изменён после объяснения → оценивать сохранённый **первый закрытый ответ**.
- Слишком быстрое решение и одновременно ошибка → пометить `RUSH` как гипотезу; не считать причиной без подтверждения.

## 4. Шаблон результатов одной темы

| Question | Selected | Correct | Outcome | Error reason |
|---|---|---|---|---|
| ALG-01-Q1 | B | B | correct | — |
| ALG-01-Q2 | A | B | wrong | A: арифметика |
| ALG-01-Q3 | C | C | correct | — |
| ALG-01-Q4 | C | D | wrong | T: противоречие коэффициентов |
| ALG-01-Q5 | A | C | wrong | L: понимание word problem |

**Итог:** `ALG-01 2/5 → GAP`; сначала Foundation equation balance, затем ALG-01 practice drill и новый transfer check.

## 5. Шаблон итогового отчёта для родителя и ученика

### STUDENT GAP REPORT — example (синтетические данные)

- Student code: `STUDENT-DEMO`
- Цель: SAT readiness; track: SAT Bridge; exam date: unknown
- Math assessed: 3 из 25 тем; English grammar assessed: 15 из 20 тем.
- Time mode: observational only; оценка не зависит от скорости.

| Предмет | Тема/блок | Результат | Вывод | Действие |
|---|---|---|---|---|
| Math | ALG-01 linear equations | 2/5 | GAP | Пройти `foundation/01_equation_balance.md` → `algebra/linear_equations.md` |
| Math | PSD-02 percentages | 4/5 | PROVISIONAL_SECURE | Новая задача на reverse percentage |
| Math | GEO-01 angles | 5/5 | PROVISIONAL_SECURE | Transfer check |
| English | A1 (5 topics) | 23/25 | Mostly secure, gaps still possible | Проверить слабую тему |
| English | A2 (5 topics) | 20/25 | Verify | Уточнить конкретные 1–2 темы |
| English | B1 (5 topics) | 11/25 | Gaps | Учить слабые B1 rules; B2 не открывать без готовности |
| English | B2 | not assessed | No result | Не писать «B2 не знает», тест ещё не проводился |

**Вывод по английскому:** grammar screening ориентировочно A2 с неустойчивыми темами B1. Это **не итоговый CEFR уровень**. Reading, vocabulary, writing, listening, speaking не оценивались.

### Индивидуальная стратегия — 2 недели (пример)

| Период | Работа | Проверка |
|---|---|---|
| Дни 1–3 | Баланс уравнения, простые двухшаговые равенства | 5 новых без подсказок |
| Дни 4–5 | Линейные уравнения: обе стороны, отсутствие решения, контекст | 2 transfer + устное объяснение |
| Дни 6–7 | English A2 weak grammar topics | 5 вопросов на каждую слабую тему |
| Дни 8–10 | B1 Present Perfect vs Past Simple + short reading | 5 грамматических + 1 текст |
| Дни 11–14 | Смешанная проверка по прошлым ошибкам | Новые вопросы, сравнение accuracy and time |

**Принцип приоритета:** prerequisite gap > high-impact SAT topic > minor trap > performance tuning. Повтор через 7–14 дней фиксируется новой попыткой.

## 6. Хранение результатов детей

- Не хранить реальное имя, адрес, дату рождения, телефон или фото ученика в GitHub.
- Для бумажного/Markdown-пилота использовать `student_code` и хранить персональные результаты локально у родителя.
- Если появится приложение: минимизация данных, согласие родителя при необходимости, разграничение доступа, политика удаления, ограничение срока хранения.
- В репозитории сохранять **только пустой шаблон или синтетический пример**, никогда реальные результаты.

## 7. Тестирование качества

- Reject: отрицательное `active_seconds`, конец раньше начала, дубли `question_id`, несовпадение `revision`.
- `NOT_ASSESSED` исключить из знаменателей.
- Не менять оценку после раскрытия ключа; повторную попытку хранить отдельно.
- Вывод о быстроте/медлительности делать после достаточной выборки одинаково сложных задач, не по одной теме.
- Промежуточные результаты неизменяемые; редактура вопроса создаёт новую ревизию.
