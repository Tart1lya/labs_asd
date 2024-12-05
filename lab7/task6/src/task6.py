import tracemalloc
import time
from lab7.utils import *
import os
from bisect import bisect_left

# Запуск таймера для измерения времени выполнения программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

# Определяем пути к файлам
current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
input_path = os.path.join(txtf_dir, "input.txt")

def find_lis(n, sequence):
    """Функция для нахождения LIS и её длины."""
    # Массивы для вычисления LIS
    lis = []  # Концы подпоследовательностей
    parent = [-1] * n  # Индексы предыдущих элементов
    indices = []  # Индексы элементов LIS

    # Поиск LIS с использованием бинарного поиска
    for i in range(n):
        pos = bisect_left(lis, sequence[i])
        if pos == len(lis):
            lis.append(sequence[i])
            indices.append(i)
        else:
            lis[pos] = sequence[i]
            indices[pos] = i

        if pos > 0:
            parent[i] = indices[pos - 1]

    # Восстановление LIS
    lis_length = len(lis)
    lis_sequence = []
    current_index = indices[-1]

    for _ in range(lis_length):
        lis_sequence.append(sequence[current_index])
        current_index = parent[current_index]

    lis_sequence.reverse()  # Переворачиваем последовательность
    return lis_length, lis_sequence

# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    input_data = open_file(input_path)
    n = int(input_data[0][0])  # Количество элементов
    sequence = list(map(int, input_data[1].strip().split()))  # Последовательность

    # Проверка корректности входных данных
    if (1 <= n <= 10**5) and (all(abs(x) <= 10**9 for x in sequence)):
        print(f"\nTask 6\nInput:\n{n}\n{sequence}")
        delete_prev_values(6)
        # Нахождение LIS
        lis_length, lis_sequence = find_lis(n, sequence)
        output_path = get_output_path(6)
        # Записываем длину LIS и саму последовательность в файл
        write_file(f"{lis_length}\n" + " ".join(map(str, lis_sequence)), output_path)
        print_output_file(6)
    else:
        print("Введите корректные данные")

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
