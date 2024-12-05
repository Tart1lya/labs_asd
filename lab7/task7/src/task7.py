# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
import os
from lab7.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

# Определяем пути к файлам
current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task/txtf
input_path = os.path.join(txtf_dir, "input.txt")

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



# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    lines = open_file(input_path)
    pattern = lines[0] if len(lines) > 0 else ""
    string = lines[1] if len(lines) > 1 else ""

    # Проверяем данные и записываем результат
    if len(pattern) <= 10_000 and len(string) <= 10_000:
        print(f"\nTask 7:\nPattern: {pattern}\nString: {string}")
        delete_prev_values(7)
        result = matches_pattern(pattern, string)
        output_path = get_output_path(7)
        write_file(result, output_path)
        print_output_file(7)
    else:
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
