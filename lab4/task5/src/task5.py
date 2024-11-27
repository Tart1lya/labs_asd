import tracemalloc
import time
from lab2.utils import *

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
    n_str, commands = open_file(input_path)
    n = int(n_str[0])  # Преобразуем первую строку в число n

    max_stack = MaxStack()
    output = []

    # Проверка корректности входных данных
    if 1 <= n <= 400000 and all(
        command.startswith("push") and 0 <= int(command.split()[1]) <= 100000 if command.startswith("push") else True for command in commands):
        print(f"\nTask\nInput:\n{n}\n{commands}")
        delete_prev_values(1)

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
        output_path = get_output_path(1)
        write_file("\n".join(output), output_path)
        print_output_file(1)
    else:
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
