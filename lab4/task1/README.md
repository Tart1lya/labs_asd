# Задача 1: Стек

## Описание

Этот код обрабатывает команды для работы со стеком, читает входные данные из файла, выполняет операции добавления и удаления элементов из стека, записывает результаты в выходной файл и выводит информацию о времени работы и затраченной памяти программы.
### Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит одно число M (1 ≤ M ≤ 10^6) — число команд.
- Каждая последующая строка исходного файла содержит ровно одну команду.

### Формат выходных данных
- В выходном файле output.txt должны содержаться числа, которые удаляются из стека с помощью команды “–”, по одному в каждой строке.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab4/
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
from lab4.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

# Пути к входному и выходному файлам
current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
input_path = os.path.join(txtf_dir, "input.txt")
output_path = os.path.join(txtf_dir, "output.txt")


def process_stack(commands):
    """
    Обрабатывает команды работы со стеком.
    :param commands: Список строк, содержащих команды (+ N или -)
    :return: Список чисел, удаленных из стека
    """
    stack = []
    results = []

    for command in commands:
        if command.startswith("+"):
            _, number = command.split()
            stack.append(int(number))
        elif command == "-":
            results.append(stack.pop())

    return results


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt
    lines = open_file(input_path)

    # Удаляем символы новой строки у каждой команды
    commands = [cmd.strip() for cmd in lines[1:]]  # Убираем \n

    # Проверка корректности входных данных
    if 1 <= len(commands) <= 10 ** 6 and all(
            (cmd.startswith("+") and len(cmd.split()) == 2 and abs(int(cmd.split()[1])) <= 10 ** 9) or cmd == "-" for
            cmd in commands
    ):
        print(f"\nTask 1\nInput:\n{len(commands)}\n{commands}")
        delete_prev_values(1)

        # Обрабатываем команды и записываем результат
        results = process_stack(commands)
        write_file("\n".join(map(str, results)), output_path)
        print_output_file(1)
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
6
+ 1
+ 10
-
+ 2
+ 1234
-
```


### Выходные данные (output.txt)
```
10
1234
```
