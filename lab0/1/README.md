# Задача 1: Ввод-вывод

## Описание

В данной задачи мы практикуемся с вводом и выводом данных

### Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит два числа a,b (-10^9 <= a,b <= 10^9) - числа, с которыми мы будем работать

### Формат выходных данных
- В выходном файле output.txt должен содержаться результат выражения в зависимости от условия задачи.


## Структура проекта
```
lab0/
|-- 1/
|   |-- src/
|   |   |-- 1.py
|   |   |-- 2.py
|   |   |-- 3.py
|   |   |-- 4.py
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
f = open('../txtf/input.txt')
a, b = map(int, f.readline().split())
f1 = open('../txtf/output.txt', 'w')
if (-10**9 <= a <= 10**9) and (-10**9 <= b <= 10**9):
    f1.write(str(a + b))
else:
    print('Не подходит по диапазону, попробуйте ещё раз')
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
tracemalloc.stop()
```
## Запуск проекта

1. Перейдите в директорию 1.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию 1.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python 2.py
   
7. Результат выполнения будет записан в файл output.txt в директории txtf.

## Пример

### Входные данные (input.txt)
12 25

### Выходные данные (output.txt)
37
