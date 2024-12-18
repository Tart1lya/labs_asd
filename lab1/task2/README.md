# Задача 2: Сортировка вставкой+

## Описание

В данной задаче реализуется алгоритм сортировки вставками, который не только сортирует массив, но и отслеживает перемещения элементов. Алгоритм сортировки вставками проходит по элементам массива и вставляет каждый элемент в его правильную позицию среди уже отсортированных элементов. При этом алгоритм также возвращает список индексов, показывающий, как менялись позиции элементов в процессе сортировки.

### Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит одно число n (1 ≤ n ≤ 1000) — количество элементов в массиве.
- Вторая строка содержит n целых чисел, по модулю не превосходящих 10^9.

### Формат выходных данных
- В выходном файле output.txt должны содержаться две строки:
  1. Первая строка — индексы конечных позиций элементов после сортировки.
  2. Вторая строка — отсортированный массив. Все числа должны быть разделены ровно одним пробелом.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab1/
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
from labs.utils import open_file, write_file
t_start = time.perf_counter()
tracemalloc.start()

def insertion_sort_plus(n, m, indices):
    for i in range(1, n):
        key = m[i]
        j = i - 1
        while j >= 0 and m[j] > key:
            m[j + 1] = m[j]
            j -= 1
        m[j + 1] = key
        indices.append(j + 2)

if __name__ == "__main__":
    n_str, m = open_file("../txtf/input.txt")
    n = int(n_str)
    indices = [1]
    if (1 <= n <= 10 ** 3) and (all(abs(i) <= 10 ** 9 for i in m)):
        insertion_sort_plus(n, m, indices)
        write_file(" ".join(map(str, indices)), "../txtf/output.txt", mode='a')
        write_file(" ".join(str(a) for a in m), "../txtf/output.txt", mode='a')

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
4
4 3 2 1

### Выходные данные (output.txt)
0 1 2 3
1 2 3 4
