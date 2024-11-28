# Задача 5: Стек с максимумом

## Описание

Этот код реализует стек с операцией нахождения максимального элемента за время O(1), обрабатывает команды для добавления, удаления элементов и получения максимума, записывает результаты в выходной файл и выводит информацию о времени работы и затраченной памяти программы.
### Формат входных данных
- Входные данные находятся в файле input.txt.
- В первой строке входного файла содержится n (1 ≤ n ≤ 400000) – число команд. Последующие n строк исходного файла содержит ровно одну команду: push V, pop или max. 0 ≤ V ≤ 10^5.

### Формат выходных данных
- Для каждого запроса max выводится (в отдельной строке) максимальное значение стека.

### Ограничения
- Время выполнения: 5 секунд.
- Память: 512 МБ.

## Структура проекта
```
lab4/
|--   task5/
|     |-- src/
|     |     |-- task5.py      # Реализация алгоритма
|     |-- tests/
|     |     |-- test_task5.py       # Тесты
|     |-- txtf/
|     |     |-- input.txt     # Входные данные
|     |     |-- output.txt    # Выходные данные
```
## Код задачи
```
import tracemalloc
import time
from lab4.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
input_path = os.path.join(txtf_dir, "input.txt")


class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.max_stack.pop()

    def max(self):
        return self.max_stack[-1] if self.max_stack else None


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    lines = open_file(input_path)
    n = int(lines[0].strip())  # Количество команд
    commands = [line.strip() for line in lines[1:]]  # Список команд

    max_stack = MaxStack()
    output = []

    # Проверка корректности входных данных
    if 1 <= n <= 400000 and all(
        command.startswith("push") and 0 <= int(command.split()[1]) <= 100000 if command.startswith("push") else True for command in commands):
        print(f"\nTask 5\nInput:\n{n}\n{commands}")
        delete_prev_values(5)

        for command in commands:
            if command.startswith("push"):
                _, value = command.split()
                value = int(value)
                max_stack.push(value)
            elif command == "pop":
                max_stack.pop()
            elif command == "max":
                output.append(str(max_stack.max()))

        # Записываем результаты в файл output.txt
        output_path = get_output_path(5)
        write_file("\n".join(output), output_path)
        print_output_file(5)
    else:
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()

```
## Запуск проекта

1. Перейдите в директорию task5.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию task5.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python task5.py
   
7. Результат выполнения будет записан в файл output.txt в директории txtf.

## Пример

### Входные данные (input.txt)
```
5
push 2
push 1
max
pop
max
```


### Выходные данные (output.txt)
```
2
2
```
