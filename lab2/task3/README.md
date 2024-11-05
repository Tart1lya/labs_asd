# Задача 3: Число инверсий

## Описание

Код подсчитывает число инверсий в массиве, используя модификацию сортировки слиянием.
### Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит одно число n (1 ≤ n ≤ 10^5) — количество элементов в массиве.
- Вторая строка содержит n целых чисел, по модулю не превосходящих 10^9.

### Формат выходных данных
- В выходном файле output.txt должно быть количество инверсий.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab2/
|--   task3/
|     |-- src/
|     |     |-- task3.py      # Реализация алгоритма
|     |-- tests/
|     |     |-- test_task3.py       # Тесты
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

def merge_and_count(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0


    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:

            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1


    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1


    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1


    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count


if __name__ == "__main__":
    n_str, m = open_file("../txtf/input.txt")
    n = int(n_str[0])
    if (1 <= n <= 10**5) and (all(abs(i) <= 10**9 for i in m)):
        temp_arr = [0] * n
        result = merge_sort_and_count(m, temp_arr, 0, n - 1)
        write_file(result, "../txtf/output.txt")
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()






```
## Запуск проекта

1. Перейдите в директорию task3.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию task3.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python task3.py
   
7. Результат выполнения будет записан в файл output.txt в директории txtf.

## Пример

### Входные данные (input.txt)
10
1 8 2 1 4 7 3 2 3 6

### Выходные данные (output.txt)
17
