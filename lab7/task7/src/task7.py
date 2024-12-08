import tracemalloc
import time
from lab7.utils import *

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(7)

def matches_pattern(pattern: str, string: str) -> str:
    """
    Проверяет, соответствует ли строка string шаблону pattern.

    :param pattern: Шаблон строки с использованием символов алфавита, '?' и '*'.
    :param string: Проверяемая строка.
    :return: 'YES', если строка соответствует шаблону, иначе 'NO'.
    """
    n, m = len(pattern), len(string)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Пустой шаблон соответствует только пустой строке
    dp[0][0] = True

    # Инициализация строки, если шаблон начинается с '*'
    for i in range(1, n + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
        else:
            break

    # Заполняем таблицу
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[i - 1] == string[j - 1] or pattern[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1] == '*':
                # '*' может соответствовать пустой строке или одному или нескольким символам
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    # Результат в последней ячейке
    return "YES" if dp[n][m] else "NO"

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    pattern = lines[0] if len(lines) > 0 else ""
    string = lines[1] if len(lines) > 1 else ""

    # Проверяем данные и записываем результат
    if len(pattern) <= 10_000 and len(string) <= 10_000:
        print(f"\nTask 7:\nPattern: {pattern}\nString: {string}")
        delete_prev_values(7)
        result = matches_pattern(pattern, string)
        write_file(result, OUTPUT_PATH)
        print_output_file(7)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
