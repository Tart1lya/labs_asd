# Задача 4: Прошитый ассоциативный массив

## Описание

Этот код обрабатывает команды для работы с ассоциативным массивом (добавление, удаление, получение значений по ключам, а также нахождение предыдущего и следующего ключа), записывает результаты в файл и выводит информацию о времени работы и потреблённой памяти.
- Входные данные находятся в файле input.txt.
- В первой строке входного файла находится строго положительное целое число операций N, не превышающее
5 * 10^5. В каждой из последующих N строк находится одна из приведенных
выше операций. Ключи и значения операций - строки из латинских букв
длиной не менее одного и не более 20 символов.

### Формат выходных данных
- Выводится последовательно результат выполнения всех операций get, prev, next

### Ограничения
- Время выполнения: 4 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab6/
|--   task4/
|     |-- src/
|     |     |-- task4.py      # Реализация алгоритма
|     |-- tests/
|     |     |-- test_task4.py       # Тесты
|     |-- txtf/
|     |     |-- input.txt     # Входные данные
|     |     |-- output.txt    # Выходные данные
```
## Код задачи
```
import tracemalloc
import time
from collections import OrderedDict
from lab6.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task/txtf
input_path = os.path.join(txtf_dir, "input.txt")


def process_commands(commands):
    """
    Обрабатывает команды работы с ассоциативным массивом.
    """
    assoc_array = OrderedDict()
    results = []

    for line in commands:
        parts = line.strip().split()
        command = parts[0]

        if command == "put":
            # Добавление или обновление ключа
            x, y = parts[1], parts[2]
            if x in assoc_array:
                assoc_array[x] = y
            else:
                assoc_array[x] = y

        elif command == "get":
            # Получение значения по ключу
            x = parts[1]
            results.append(assoc_array.get(x, "<none>"))

        elif command == "prev":
            # Поиск предыдущего ключа
            x = parts[1]
            if x in assoc_array:
                keys = list(assoc_array.keys())
                idx = keys.index(x)
                if idx > 0:
                    results.append(assoc_array[keys[idx - 1]])
                else:
                    results.append("<none>")
            else:
                results.append("<none>")

        elif command == "next":
            # Поиск следующего ключа
            x = parts[1]
            if x in assoc_array:
                keys = list(assoc_array.keys())
                idx = keys.index(x)
                if idx < len(keys) - 1:
                    results.append(assoc_array[keys[idx + 1]])
                else:
                    results.append("<none>")
            else:
                results.append("<none>")

        elif command == "delete":
            # Удаление ключа
            x = parts[1]
            assoc_array.pop(x, None)

    return results


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    lines = open_file(input_path)
    n = int(lines[0])  # Преобразуем первую строку в число операций
    commands = lines[1:]  # Команды операций

    # Проверяем корректность входных данных
    if 1 <= n <= 5 * 10 ** 5 and all(len(cmd.split()) in (2, 3) for cmd in commands):
        print(f"\nTask 4\nInput:\n{lines}")
        delete_prev_values(4)

        # Обрабатываем команды
        results = process_commands(commands)

        # Записываем результаты в файл output.txt
        output_path = get_output_path(4)
        write_file("\n".join(results), output_path)
        print_output_file(4)
    else:
        # Выводим сообщение об ошибке, если данные некорректны
        print("Введите корректные данные")

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()


```
## Запуск проекта

1. Перейдите в директорию task4.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию task4.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python task4.py
   
7. Результат выполнения будет записан в файл output.txt в директории txtf.

## Пример

### Входные данные (input.txt)
```
14
put zero a
put one b
put two c
put three d
put four e
get two
prev two
next two
delete one
delete three
get two
prev two
next two
next four
```


### Выходные данные (output.txt)
```
c
b
d
c
a
e
<none>
```
