# Задача 1: Куча ли?

## Описание

Данный код проверяет, является ли массив из файла `input.txt` неубывающей пирамидой, записывает результат в `output.txt`, а также измеряет время выполнения и затраты памяти программы.
### Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка входного файла содержит целое число n (1 ≤ n ≤ 10^6). Вторая строка содержит n целых чисел,
по модулю не превосходящих 2 * 10^9.

### Формат выходных данных
- В выходном файле output.txt должен выводиться «YES», если массив яв-
ляется неубывающей пирамидой, и «NO» в противном случае.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab5/
|--   task1/
|     |-- src/
|     |     |-- task1.py      # Реализация алгоритма
|     |-- tests/
|     |     |-- test_task1.py       # Тесты
|     |-- txtf/
|     |     |-- input.txt     # Входные данные
|     |     |-- output.txt    # Выходные данные
```
## Код задачи
```
# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
import os
from lab5.utils import open_file, write_file, delete_prev_values, get_output_path, print_output_file

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Текущая директория
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория для input.txt и output.txt
input_path = os.path.join(txtf_dir, "input.txt")

def is_heap(array, n):
    """
    Проверяет, является ли массив неубывающей пирамидой.

    :param array: массив целых чисел
    :param n: размер массива
    :return: True, если массив - пирамида, иначе False
    """
    for i in range(n):
        left_child_index = 2 * (i + 1) - 1  # Индекс левого потомка
        right_child_index = 2 * (i + 1)  # Индекс правого потомка

        # Проверяем условие для левого потомка
        if left_child_index < n and array[i] > array[left_child_index]:
            return False

        # Проверяем условие для правого потомка
        if right_child_index < n and array[i] > array[right_child_index]:
            return False

    return True

# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    n_str, array_str = open_file(input_path)
    n = int(n_str.strip())  # Преобразуем первую строку в число n
    array = list(map(int, array_str.strip().split()))  # Преобразуем элементы массива в числа
    # Проверка корректности входных данных
    if (1 <= n <= 10 ** 6) and (all(abs(i) <= 2 * 10 ** 9 for i in array)):
        print(f"\nTask: 1\nInput:\n{n}\n{array}")
        delete_prev_values(1)

        # Проверяем массив на условие пирамиды
        result = "YES" if is_heap(array, n) else "NO"

        # Записываем результат в файл output.txt
        output_path = get_output_path(1)
        write_file(result, output_path)
        print_output_file(1)
    else:
        # Выводим сообщение об ошибке, если данные некорректны
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()


```
## Запуск проекта

1. Перейдите в директорию task1.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию task1.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python task1.py
   
7. Результат выполнения будет записан в файл output.txt в директории txtf.

## Пример

### Входные данные (input.txt)
```
5
1 3 2 5 4
```


### Выходные данные (output.txt)
```
YES
```
