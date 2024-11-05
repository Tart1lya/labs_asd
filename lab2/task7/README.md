# Задача 7: Поиск максимального подмассива за линейное время

## Описание

Код находит максимальный подмассив.
### Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит число n (1 ≤ n ≤ 2 * 10^4) — количество элементов в массиве.
- Вторая строка содержит n целых чисел, по модулю не превосходящих 10^9.


### Формат выходных данных
- В выходном файле output.txt должен содержаться подмассив с максимальной суммой элементов.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab2/
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
import tracemalloc
import time
from lab2.utils import open_file, write_file
t_start = time.perf_counter()
tracemalloc.start()

def max_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(arr)):

        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]


        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i


    return arr[start:end + 1]


if __name__ == "__main__":
    n_list, arr = open_file("../txtf/input.txt")

    n = int(n_list[0])


    if 1 <= n <= 2 * 10**4 and (all(abs(i) <= 10**9 for i in arr)):
        write_file("", "../txtf/output.txt", mode="w")
        sub_arr = max_subarray(arr)
        write_file(sub_arr, "../txtf/output.txt")
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
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
10
1 8 2 1 4 7 3 2 3 -1

### Выходные данные (output.txt)
1 8 2 1 4 7 3 2 3
