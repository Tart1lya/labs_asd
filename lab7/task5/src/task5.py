# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
import os
from lab2.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Текущая директория
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория txtf
input_path = os.path.join(txtf_dir, "input.txt")


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


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    input_data = open_file(input_path)

    # Разбираем данные
    n = int(input_data[0][0])
    a = list(map(int, input_data[1]))
    m = int(input_data[2][0])
    b = list(map(int, input_data[3]))
    l = int(input_data[4][0])
    c = list(map(int, input_data[5]))

    # Проверяем корректность данных
    if all(1 <= val <= 100 for val in (n, m, l)) and \
            all(-10**9 < x < 10**9 for x in a + b + c):
        print(f"Task 5\nInput:\nA: {a}\nB: {b}\nC: {c}")
        delete_prev_values(5)

        # Вычисляем результат
        result = longest_common_subsequence_3(a, b, c)

        # Записываем результат в файл output.txt
        output_path = get_output_path(5)
        write_file(str(result), output_path)
        print_output_file(5)

    else:
        # Выводим сообщение об ошибке, если данные некорректны
        print("Введите корректные данные")

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
