# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
import os
from lab2.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task/txtf
input_path = os.path.join(txtf_dir, "input.txt")


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


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    input_data = open_file(input_path)

    # Преобразуем входные данные
    n = int(input_data[0][0])  # Длина первой последовательности
    A = list(map(int, input_data[1]))  # Первая последовательность
    m = int(input_data[2][0])  # Длина второй последовательности
    B = list(map(int, input_data[3]))  # Вторая последовательность

    # Проверка корректности входных данных
    if (1 <= n <= 100) and (1 <= m <= 100) and (all(-10**9 < x < 10**9 for x in A + B)):
        print(f"Task 4\nInput:\n{n} {A}\n{m} {B}")
        delete_prev_values(4)

        # Вычисляем длину самой длинной общей подпоследовательности
        result = longest_common_subsequence(n, A, m, B)

        output_path = get_output_path(4)
        # Записываем результат в файл output.txt
        write_file(str(result), output_path)
        print_output_file(4)
    else:
        # Выводим сообщение об ошибке, если данные некорректны
        print("Введите корректные данные")

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
