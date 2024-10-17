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
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab1/
|-- task8/
|   |-- src/
|   |   |-- task8.py       # Реализация алгоритма сортировка вставками
|   |-- txtf/
|   |   |-- input.txt      # Входные данные
|   |   |-- output.txt     # Выходные данные
```
## Код задачи
```
import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()
f_input = open('../txtf/input.txt', 'r')
n = int(f_input.readline())
m = [int(x) for x in f_input.readline().split()]
if (3 <= n <= 5000) and (all(abs(i) <= 10**9 for i in m)):
    f_output = open('../txtf/output.txt', 'w')
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            if m[j] < m[j - 1]:
                m[j], m[j - 1] = m[j - 1], m[j]
                f_output.write(f'Swap elements at indices {j} and {j + 1}.\n')
        if m == sorted(m):
            break
    f_output.write('No more swaps needed.')
else:
    print('Введите корректные данные')
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
