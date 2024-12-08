import tracemalloc
import time
from lab1.utils import open_file, write_file, get_output_path, delete_prev_values
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task1/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(1)

t_start = time.perf_counter()
tracemalloc.start()

def insertion_sort(n, m):
    for i in range(1, n):
        key = m[i]
        j = i - 1
        while j >= 0 and m[j] > key:
            m[j + 1] = m[j]
            j -= 1
        m[j + 1] = key


if __name__ == "__main__":
    n_str, m = open_file(INPUT_PATH)
    n = int(n_str)
    if (1 <= n <= 10**3) and (all(abs(i) <= 10**9 for i in m)):
        delete_prev_values(1)
        insertion_sort(n, m)

        write_file(" ".join(str(a) for a in m), OUTPUT_PATH)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()

