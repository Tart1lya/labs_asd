import tracemalloc
import time
from lab4.utils import *

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task1/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(5)


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


if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = int(lines[0].strip())
    commands = [line.strip() for line in lines[1:]]

    max_stack = MaxStack()
    output = []

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

        write_file("\n".join(output), OUTPUT_PATH)
        print_output_file(5)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
