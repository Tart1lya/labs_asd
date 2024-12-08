import tracemalloc
import time
from lab6.utils import *

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Текущая директория
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Папка с файлами
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(7)


def count_beautiful_pairs(n, k, S, beautiful_pairs):
    """Вычисление количества красивых пар."""
    count = {}
    result = 0

    # Проходим по строке S
    for char in S:
        # Проверяем, образует ли текущий символ красивую пару с ранее встреченными
        for a, b in beautiful_pairs:
            if char == b:
                result += count.get(a, 0)

        # Увеличиваем счётчик для текущего символа
        count[char] = count.get(char, 0) + 1

    return result


if __name__ == "__main__":
    input_data = open_file(INPUT_PATH)
    n, k = map(int, input_data[0].split())
    S = input_data[1].strip()
    pairs = input_data[2:]

    beautiful_pairs = set()
    for pair in pairs:
        beautiful_pairs.add((pair[0], pair[1]))

    print(beautiful_pairs)

    if (1 <= n <= 100000) and (1 <= k <= 676) and len(S) == n:
        print(f"\nTask 7\nInput:\n{n} {k}\n{S}\n{beautiful_pairs}")
        delete_prev_values(7)

        # Считаем количество красивых пар
        result = count_beautiful_pairs(n, k, S, beautiful_pairs)

        write_file(str(result), OUTPUT_PATH)
        print_output_file(7)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
