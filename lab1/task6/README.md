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
|-- task6/
|   |-- src/
|   |   |-- task6.py       # Реализация алгоритма сортировка вставками
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
if (1 <= n <= 10 ** 3) and (all(abs(i) <= 10 ** 9 for i in m)):

    #algorithm itself
    for i in range(len(m)):
        for j in range(len(m) - 1, i, -1):
            if m[j] < m[j - 1]:
                m[j], m[j - 1] = m[j - 1], m[j]
    m_sorted = ' '.join(map(str, m))
    f_output = open('../txtf/output.txt', 'w')
    f_output.write(m_sorted)
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()

    #The proof that m'[1] <= m'[2] <= ... <= m'[n], where m' is the output of the bubble sort procedure
    # and n is the length of the array m
    condition = 0
    for i in range(len(m) - 1):
        if m[i] < m[i + 1]:
            condition += 1
    if condition == len(m) - 1:
        print("m'[1] <= m'[2] <= ... <= m'[n]")
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
