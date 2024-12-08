import tracemalloc
import time
from lab3.utils import *


t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task1/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(6)


# Генерация массива попарных произведений
def generate_pairwise_array(A, B):
    C = []
    for a in A:
        for b in B:
            C.append(a * b)
    return C


if __name__ == "__main__":
    n_and_m_str, A, B = open_file(INPUT_PATH)
    n = int(n_and_m_str[0])
    m = int(n_and_m_str[1])

    if (1 <= n, m <= 6000) and (all(0 <= i <= 40000 for i in A)) and all(0 <= i <= 40000 for i in B):
        print(f"\nTask 6\nInput:\n{n_and_m_str}\n{A}\n{B}")
        delete_prev_values(6)
        C = generate_pairwise_array(A, B)
        C.sort()
        result = sum(C[i] for i in range(0, len(C), 10))
        write_file(result, OUTPUT_PATH)
        print_output_file(6)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
