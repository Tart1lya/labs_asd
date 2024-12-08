import tracemalloc
import time
from lab7.utils import *

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(4)

def longest_common_subsequence(n, A, m, B):
    """
    Вычисляет длину самой длинной общей подпоследовательности для последовательностей A и B.
    """
    # Инициализация DP-таблицы
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Заполнение таблицы
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:  # Элементы совпадают
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # Элементы не совпадают
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Результат — последняя ячейка таблицы
    return dp[n][m]


if __name__ == "__main__":
    input_data = open_file(INPUT_PATH)

    n = int(input_data[0].strip())
    A = list(map(int, input_data[1].strip().split()))
    m = int(input_data[2].strip())
    B = list(map(int, input_data[3].strip().split()))

    if (1 <= n <= 100) and (1 <= m <= 100) and (all(-10**9 < x < 10**9 for x in A + B)):
        print(f"Task 4\nInput:\n{n} {A}\n{m} {B}")
        delete_prev_values(4)

        # Вычисляем длину самой длинной общей подпоследовательности
        result = longest_common_subsequence(n, A, m, B)

        write_file(str(result), OUTPUT_PATH)
        print_output_file(4)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
