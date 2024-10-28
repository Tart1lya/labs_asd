# Задача 2: Число Фибоначчи

## Описание

В данной задачи мы выводим n-ое число Фибоначчи

### Формат входных данных
- Входные данные находятся в файле inputfib.txt.
- Первая строка содержит одно число n (0 <= n <= 45)

### Формат выходных данных
- В выходном файле outputfib.txt должно содераться n-ое число Фибоначчи.


## Структура проекта
```
lab0/
|-- fib/
|   |-- src/
|   |   |-- fib.py
|   |-- txtf/
|   |   |-- inputfib.txt      # Входные данные
|   |   |-- outputfib.txt     # Выходные данные
```
## Код задачи
```
import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()
f = open('../txtf/inputfib.txt')
n = int(f.readline())
f1 = open('../txtf/outputfib.txt', 'w')
if 0 <= n <= 45:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    f1.write(str(b))
else:
    print('Не подходит диапазону, попробуйте ещё раз')
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
tracemalloc.stop()
```
## Запуск проекта

1. Перейдите в директорию fib.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл inputfib.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию fib.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python fib.py
   
7. Результат выполнения будет записан в файл outputfib.txt в директории txtf.

## Пример

### Входные данные (inputfib.txt)
10

### Выходные данные (outputfib.txt)
55
