import tracemalloc
import time
from lab4.utils import *

t_start = time.perf_counter()
tracemalloc.start()


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")


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


if __name__ == "__main__":
    lines = open_file(INPUT_PATH)

    commands = [cmd.strip() for cmd in lines[1:]]

    if 1 <= len(commands) <= 10 ** 6 and all(
            (cmd.startswith("+") and len(cmd.split()) == 2 and abs(int(cmd.split()[1])) <= 10 ** 9) or cmd == "-" for
            cmd in commands
    ):
        print(f"\nTask 1\nInput:\n{len(commands)}\n{commands}")
        delete_prev_values(1)

        results = process_stack(commands)
        write_file("\n".join(map(str, results)), OUTPUT_PATH)
        print_output_file(1)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
