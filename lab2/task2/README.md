# Задача 2: Сортировка слиянием+

## Описание

Код реализует алгоритм сортировки слиянием и включает в себя функциональность для чтения входных данных из файла и записи отсортированных данных в выходной файл, а также отслеживание времени выполнения и использования памяти, а также вывод индексов граничных элементов и их значения.
### Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит одно число n (1 ≤ n ≤ 10^5) — количество элементов в массиве.
- Вторая строка содержит n целых чисел, по модулю не превосходящих 10^9.

### Формат выходных данных
- В выходном файле output.txt должен содержаться индексы пограничных элементов и их значения, а также отсортированный массив. Все числа должны быть разделены ровно одним пробелом.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab2/
|--   task2/
|     |-- src/
|     |     |-- task2.py      # Реализация алгоритма
|     |-- tests/
|     |     |-- test_task2.py       # Тесты
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

def merge(arr, left, mid, right):

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]


    i = j = 0
    k = left


    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1


    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1


    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    write_file(f"{left + 1} {right + 1} {arr[left]} {arr[right]}\n", "../txtf/output.txt", mode='a')

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

if __name__ == "__main__":
    n_str, m = open_file("../txtf/input.txt")
    n = int(n_str[0])
    if (1 <= n <= 10**5) and (all(abs(i) <= 10**9 for i in m)):
        merge_sort(m, 0, n - 1)
        write_file(" ".join(str(a) for a in m), "../txtf/output.txt", mode='a')
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()






```
## Запуск проекта

1. Перейдите в директорию task2.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию task2.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python task2.py
   
7. Результат выполнения будет записан в файл output.txt в директории txtf.

## Пример

### Входные данные (input.txt)
10
1 8 2 1 4 7 3 2 3 6

### Выходные данные (output.txt)
1 2 1 8
1 3 1 8
4 5 1 4
1 5 1 8
6 7 3 7
6 8 2 7
9 10 3 6
6 10 2 7
1 10 1 8
1 1 2 2 3 3 4 6 7 8
