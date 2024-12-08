import tracemalloc
import time
from lab4.utils import *

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(3)


def is_valid_bracket_sequence(sequence):
    """
    Проверяет, является ли скобочная последовательность правильной.
    :param sequence: строка со скобочной последовательностью
    :return: True, если последовательность правильная, иначе False
    """
    stack = []
    matching_brackets = {')': '(', ']': '['}

    for char in sequence:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return False  # Если не соответствует, последовательность неправильная
    return not stack  # Если стек пуст, последовательность правильная


if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = int(lines[0])
    sequences = lines[1:]

    if 1 <= n <= 500 and all(1 <= len(seq) <= 10**4 for seq in sequences):
        print(f"\nTask 3\nInput:\n{n}\n{sequences}")
        delete_prev_values(3)

        # Проверяем каждую последовательность
        results = []
        for seq in sequences:
            results.append("YES" if is_valid_bracket_sequence(seq) else "NO")

        write_file("\n".join(results), OUTPUT_PATH)
        print_output_file(3)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
