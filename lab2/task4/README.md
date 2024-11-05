# Задача 4: Бинарный поиск

## Описание

Код реализует алгоритм бинарного поиска.
### Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит число n (1 ≤ n ≤ 10^5) — количество элементов в массиве и последовательность a, где элементы от 1 до 10^9.
- Вторая строка содержит число n (1 ≤ n ≤ 10^5) — количество элементов в массиве и последовательность b, где элементы от 1 до 10^9.


### Формат выходных данных
- В выходном файле output.txt должен содержаться целевое значение или -1.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab2/
|--   task4/
|     |-- src/
|     |     |-- task4.py      # Реализация алгоритма
|     |-- tests/
|     |     |-- test_task4.py       # Тесты
|     |-- txtf/
|     |     |-- input.txt     # Входные данные
|     |     |-- output.txt    # Выходные данные
```
## Код задачи
```
import tracemalloc
import time
from lab2.utils import open_file, write_file
t_start = time.perf_counter()
tracemalloc.start()

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    data_n, data_k = open_file("../txtf/input.txt")

    n = int(data_n[0])
    a = data_n[1:]
    k = int(data_k[0])
    b = data_k[1:]


    if 1 <= n <= 10**5 and 1 <= k <= 10**5 and min(a) >= 1 and \
        min(b) >= 1 and max(a) <= 10**9 and max(b) <= 10**9:
        write_file("", "../txtf/output.txt", mode="w")
        for i in b:
            result = binary_search(a, i)
            write_file(f"{result} ", "../txtf/output.txt", mode='a')
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()







```
## Запуск проекта

1. Перейдите в директорию task4.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию task4.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python task4.py
   
7. Результат выполнения будет записан в файл output.txt в директории txtf.

## Пример

### Входные данные (input.txt)
5 1 5 8 12 13
5 8 1 23 1 11

### Выходные данные (output.txt)
2 0 -1 0 -1
