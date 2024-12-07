# Задача 7: Снова сортировка

## Описание

Этот код выполняет сортировку массива методом пирамидальной сортировки (heapsort) с преобразованием результата в убывающий порядок, записывает отсортированный массив в `output.txt`, а также измеряет время выполнения и объем используемой памяти.
### Формат входных данных
- Входные данные находятся в файле input.txt.
- В первой строке входного файла содержится число n (1 ≤ n ≤ 10^5) — число элементов в массиве. Во второй
строке находятся n различных целых чисел, по модулю не превосходящих 10^9.

### Формат выходных данных
- Одна строка выходного файла с отсортированным по невозрастанию массивом. Между любыми двумя числами
должен стоять ровно один пробел.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab5/
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
from lab5.utils import *
import os

# Запуск таймера для измерения времени выполнения
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task/txtf
input_path = os.path.join(txtf_dir, "input.txt")

def heapify(arr, n, i):
    """
    Вспомогательная функция для преобразования массива в max-heap.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    """
    Пирамидальная сортировка массива.
    """
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    lines = open_file(input_path)
    n_str, m_str = lines[0].strip(), lines[1].strip()
    n = int(n_str)
    m = list(map(int, m_str.split()))  # Преобразуем строки в список чисел

    # Проверка корректности входных данных
    if (1 <= n <= 10 ** 5) and (all(abs(i) <= 10 ** 9 for i in m)):
        print(f"\nTask 7\nInput:\n{n}\n{m}")
        delete_prev_values(7)

        # Сортируем массив m с помощью heapsort
        heapsort(m)
        m.reverse()  # Инвертируем массив для получения убывающего порядка

        output_path = get_output_path(7)
        # Записываем результат в файл output.txt
        write_file(" ".join(map(str, m)), output_path)
        print_output_file(7)
    else:
        # Выводим сообщение об ошибке, если входные данные некорректны
        print('Введите корректные данные')

    # Выводим время выполнения программы
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
5
1 2 3 4 5
```


### Выходные данные (output.txt)
```
5 4 3 2 1
```
