# Задача 7: Шаблоны

## Описание

Этот код проверяет, соответствует ли заданная строка определённому шаблону (с символами `?` и `*`), считанному из файла, записывает результат проверки в файл, а также выводит информацию о времени выполнения и памяти.
### Формат входных данных
- Входные данные находятся в файле input.txt.
Первая строка входного файла определяет шаблон. Вторая строка S состоит только из символов алфавита.
Ее необходимо проверить на соответствие шаблону. Длины обеих строк не
превосходят 10 000. Строки могут быть пустыми.
### Формат выходных данных
- Если данная строка подходит под шаблон, выводится YES. Иначе выводится NO.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab7/
|--   task7/
|     |-- src/
|     |     |-- task7.py      # Реализация алгоритма
|     |-- tests/
|     |     |-- test_task7.py       # Тесты
|     |-- txtf/
|     |     |-- input.txt     # Входные данные
|     |     |-- output.txt    # Выходные данные
```
## Код задачи
```
# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
import os
from lab7.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

# Определяем пути к файлам
current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task/txtf
input_path = os.path.join(txtf_dir, "input.txt")

def matches_pattern(pattern: str, string: str) -> str:
    """
    Проверяет, соответствует ли строка string шаблону pattern.

    :param pattern: Шаблон строки с использованием символов алфавита, '?' и '*'.
    :param string: Проверяемая строка.
    :return: 'YES', если строка соответствует шаблону, иначе 'NO'.
    """
    n, m = len(pattern), len(string)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Пустой шаблон соответствует только пустой строке
    dp[0][0] = True

    # Инициализация строки, если шаблон начинается с '*'
    for i in range(1, n + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
        else:
            break

    # Заполняем таблицу
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[i - 1] == string[j - 1] or pattern[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1] == '*':
                # '*' может соответствовать пустой строке или одному или нескольким символам
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    # Результат в последней ячейке
    return "YES" if dp[n][m] else "NO"



# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    lines = open_file(input_path)
    pattern = lines[0] if len(lines) > 0 else ""
    string = lines[1] if len(lines) > 1 else ""

    # Проверяем данные и записываем результат
    if len(pattern) <= 10_000 and len(string) <= 10_000:
        print(f"\nTask 7:\nPattern: {pattern}\nString: {string}")
        delete_prev_values(7)
        result = matches_pattern(pattern, string)
        output_path = get_output_path(7)
        write_file(result, output_path)
        print_output_file(7)
    else:
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()

```
## Запуск проекта

1. Перейдите в директорию task7.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию task7.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python task7.py
   
7. Результат выполнения будет записан в файл output.txt в директории txtf.

## Пример

### Входные данные (input.txt)
```
k?t?n
kitten
```


### Выходные данные (output.txt)
```
NO
```
