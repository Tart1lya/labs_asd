import tracemalloc
import time
from lab3.utils import *

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task1/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(7)


def radix_sort_phase(strings, phase):
    """Сортировка по заданной фазе (символу)."""
    return sorted(strings, key=lambda x: x[1][phase])


if __name__ == "__main__":
    (n, m, k), columns = open_file(INPUT_PATH)

    if (1 <= n <= 10**6) and (1 <= k <= m <= 10**6) and (n * m <= 5 * 10**7):
        print(f"\nTask 7\nInput:\n{n} {m} {k}\n{columns}")
        delete_prev_values(7)
        # Формируем список строк из колонок
        strings = [(i + 1, ''.join(columns[j][i] for j in range(m))) for i in range(n)]

        # Применяем сортировку по фазам
        for phase in range(min(m, k) - 1, -1, -1):
            strings = radix_sort_phase(strings, phase)

        # Подготовка результатов (выводим индексы строк в новом порядке)
        result = [str(item[0]) for item in strings]
        write_file(result, OUTPUT_PATH)
        print_output_file(7)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
