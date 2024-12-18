import tracemalloc
import time
from lab7.utils import *

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Текущая директория
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(5)

def longest_common_subsequence_3(a, b, c):
    """
    Вычисляет длину самой длинной общей подпоследовательности для трёх последовательностей.
    """
    n, m, l = len(a), len(b), len(c)

    # Инициализируем 3D массив dp размером (n+1) x (m+1) x (l+1)
    dp = [[[0] * (l + 1) for _ in range(m + 1)] for __ in range(n + 1)]

    # Заполнение dp массива
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[n][m][l]


if __name__ == "__main__":
    input_data = open_file(INPUT_PATH)

    n = int(input_data[0][0])
    m = int(input_data[2][0])
    l = int(input_data[4][0])
    a = list(map(int, input_data[1].split()))
    b = list(map(int, input_data[3].split()))
    c = list(map(int, input_data[5].split()))

    if all(1 <= val <= 100 for val in (n, m, l)) and \
            all(-10**9 < x < 10**9 for x in a + b + c):
        print(f"Task 5\nInput:\nA: {a}\nB: {b}\nC: {c}")
        delete_prev_values(5)

        # Вычисляем результат
        result = longest_common_subsequence_3(a, b, c)

        write_file(str(result), OUTPUT_PATH)
        print_output_file(5)

    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
