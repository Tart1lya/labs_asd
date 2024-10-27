# Задача 8: Секретарь Своп

## Описание

В данной задаче реализуется алгоритм пузырьковой сортировки. Алгоритм многократно проходит по массиву, сравнивая соседние элементы и меняя их местами, если они стоят в неправильном порядке. Этот процесс повторяется до тех пор, пока массив не будет полностью отсортирован по возрастанию.

### Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит одно число n (3 ≤ n ≤ 5000) — количество элементов в массиве.
- Вторая строка содержит n целых чисел, по модулю не превосходящих 10^9.

### Формат выходных данных
- В выходном файле output.txt должна содержать информация о том, на каких местах элементы взаимно поменялись местами.

### Ограничения
- Время выполнения: 1 секунда.
- Память: 256 МБ.

## Структура проекта
```
labs/
|-- lab1/
|     |-- task8/
|     |     |-- src/
|     |     |     |-- task8.py      # Реализация алгоритма сортировка вставками
|     |     |-- tests/
|     |     |     |-- test_task8.py       # Тесты
|     |     |-- txtf/
|     |     |     |-- input.txt     # Входные данные
|     |     |     |-- output.txt    # Выходные данные
```
## Код задачи
```
import tracemalloc
import time
from labs.utils import open_file, write_file
t_start = time.perf_counter()
tracemalloc.start()

def swap_secretary(n, m):
    for i in range(n):
        for j in range(i + 1, n):
            if m[j] < m[j - 1]:
                m[j], m[j - 1] = m[j - 1], m[j]
                write_file(f'Swap elements at indices {j} and {j + 1}.', "../txtf/output.txt", mode='a')
        if m == sorted(m):
            break


if __name__ == "__main__":
    n_str, m = open_file("../txtf/input.txt")
    n = int(n_str)
    if (3 <= n <= 5000) and (all(abs(i) <= 10 ** 9 for i in m)):
        swap_secretary(n, m)
        write_file('No more swaps needed.', "../txtf/output.txt", mode='a')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
```
## Запуск проекта

1. Перейдите в директорию task8.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию task8.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python task8.py
   
7. Результат выполнения будет записан в файл output.txt в директории txtf.

## Пример

### Входные данные (input.txt)
5
3 1 4 2 2

### Выходные данные (output.txt)
Swap elements at indices 1 and 2.
Swap elements at indices 3 and 4.
Swap elements at indices 4 and 5.
Swap elements at indices 2 and 3.
Swap elements at indices 3 and 4.
No more swaps needed.
