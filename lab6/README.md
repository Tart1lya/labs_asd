# Лабораторная работа №6: Хеширование. Хеш-таблицы

Студент ИТМО, Артемов Илья Витальевич 465054
## Вариант 5
### Навигация

- [ ] [Задача 1 - Множество](task1)
- [ ] [Задача 2 - Телефонная книга](task2)
- [ ] [Задача 4 - Прошитый ассоциативный массив](task4)
- [ ] [Задача 7 - Драгоценные камни](task7)

## Описание
Лабораторная работа посвящена хешированию и хеш-таблицам.

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Tart1lya/labs_asd.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd labs_asd/lab5
   ```
3. **Запуск всех задач**
   ```bash
    for script in lab*/src/*.py; do PYTHONPATH=$(pwd) python "$script"; done
   ```

## Тестирование
Для запуска тестов выполните:
```bash
    for script in lab*/tests/*.py; do PYTHONPATH=$(pwd) python "$script"; done
```