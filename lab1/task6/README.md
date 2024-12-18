# Задача 6: Пузырьковая сортировка

## Описание

В данной задаче реализуется алгоритм пузырьковой сортировки. Алгоритм многократно проходит по массиву, сравнивая соседние элементы и меняя их местами, если они стоят в неправильном порядке. Этот процесс повторяется до тех пор, пока массив не будет полностью отсортирован по возрастанию.

### Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит одно число n (1 ≤ n ≤ 1000) — количество элементов в массиве.
- Вторая строка содержит n целых чисел, по модулю не превосходящих 10^9.

### Формат выходных данных
- В выходном файле output.txt должен содержаться отсортированный массив. Все числа должны быть разделены ровно одним пробелом.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab1/
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
from labs.utils import open_file, write_file
t_start = time.perf_counter()
tracemalloc.start()

def bubble_sort(n, m):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if m[j] < m[j - 1]:
                m[j], m[j - 1] = m[j - 1], m[j]


if __name__ == "__main__":
    n_str, m = open_file("../txtf/input.txt")
    n = int(n_str)
    if (1 <= n <= 10**3) and (all(abs(i) <= 10**9 for i in m)):
        bubble_sort(n, m)
        write_file(" ".join(str(a) for a in m), "../txtf/output.txt")
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
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
6
31 41 59 26 41 58

### Выходные данные (output.txt)
26 31 41 41 58 59
