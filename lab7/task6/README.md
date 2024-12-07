# Задача 6: Наибольшая возрастающая подпоследовательность

## Описание

Этот код вычисляет длину наибольшей возрастающей подпоследовательности.
### Формат входных данных
- Входные данные находятся в файле input.txt.
- В первой строке входных данных задано целое число n – длина последовательности (1 ≤ n ≤ 300000).
- Во второй строке задается сама последовательность. Числа разделяются пробелом.
Элементы последовательности – целые числа, не превосходящие по модулю 10^9.
### Формат выходных данных
- В первой строке выводится длина наибольшей возрастающей подпоследовательности, а во второй
строке выводится через пробел сама наибольшая возрастающая подпоследовательность данной последовательности. Если ответов несколько - выводится
любой.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab7/
|--   task6/
|     |-- src/
|     |     |-- task6.py      # Реализация алгоритма
|     |-- tests/
|     |     |-- test_task6.py       # Тесты
|     |-- txtf/
|     |     |-- input.txt     # Входные данные
|     |     |-- output.txt    # Выходные данные
```
## Код задачи
```
import tracemalloc
import time
from lab7.utils import *
import os
from bisect import bisect_left

# Запуск таймера для измерения времени выполнения программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

# Определяем пути к файлам
current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
input_path = os.path.join(txtf_dir, "input.txt")

def find_lis(n, sequence):
    """Функция для нахождения LIS и её длины."""
    # Массивы для вычисления LIS
    lis = []  # Концы подпоследовательностей
    parent = [-1] * n  # Индексы предыдущих элементов
    indices = []  # Индексы элементов LIS

    # Поиск LIS с использованием бинарного поиска
    for i in range(n):
        pos = bisect_left(lis, sequence[i])
        if pos == len(lis):
            lis.append(sequence[i])
            indices.append(i)
        else:
            lis[pos] = sequence[i]
            indices[pos] = i

        if pos > 0:
            parent[i] = indices[pos - 1]

    # Восстановление LIS
    lis_length = len(lis)
    lis_sequence = []
    current_index = indices[-1]

    for _ in range(lis_length):
        lis_sequence.append(sequence[current_index])
        current_index = parent[current_index]

    lis_sequence.reverse()  # Переворачиваем последовательность
    return lis_length, lis_sequence

# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    input_data = open_file(input_path)
    n = int(input_data[0][0])  # Количество элементов
    sequence = list(map(int, input_data[1].strip().split()))  # Последовательность

    # Проверка корректности входных данных
    if (1 <= n <= 10**5) and (all(abs(x) <= 10**9 for x in sequence)):
        print(f"\nTask 6\nInput:\n{n}\n{sequence}")
        delete_prev_values(6)
        # Нахождение LIS
        lis_length, lis_sequence = find_lis(n, sequence)
        output_path = get_output_path(6)
        # Записываем длину LIS и саму последовательность в файл
        write_file(f"{lis_length}\n" + " ".join(map(str, lis_sequence)), output_path)
        print_output_file(6)
    else:
        print("Введите корректные данные")

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()


```
## Запуск проекта

1. Перейдите в директорию task6.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию task6.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python task6.py
   
7. Результат выполнения будет записан в файл output.txt в директории txtf.

## Пример

### Входные данные (input.txt)
```
6
3 29 5 5 28 6
```


### Выходные данные (output.txt)
```
3
3 5 6
```
