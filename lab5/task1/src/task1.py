import tracemalloc
import time
import os
from lab5.utils import open_file, write_file, delete_prev_values, get_output_path, print_output_file

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Текущая директория
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория для input.txt и output.txt
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(1)


def is_heap(array, n):
    """
    Проверяет, является ли массив неубывающей пирамидой.

    :param array: массив целых чисел
    :param n: размер массива
    :return: True, если массив - пирамида, иначе False
    """
    for i in range(n):
        left_child_index = 2 * (i + 1) - 1  # Индекс левого потомка
        right_child_index = 2 * (i + 1)  # Индекс правого потомка

        # Проверяем условие для левого потомка
        if left_child_index < n and array[i] > array[left_child_index]:
            return False

        # Проверяем условие для правого потомка
        if right_child_index < n and array[i] > array[right_child_index]:
            return False

    return True

if __name__ == "__main__":
    n_str, array_str = open_file(INPUT_PATH)
    n = int(n_str.strip())
    array = list(map(int, array_str.strip().split()))

    if (1 <= n <= 10 ** 6) and (all(abs(i) <= 2 * 10 ** 9 for i in array)):
        print(f"\nTask: 1\nInput:\n{n}\n{array}")
        delete_prev_values(1)

        # Проверяем массив на условие пирамиды
        result = "YES" if is_heap(array, n) else "NO"

        write_file(result, OUTPUT_PATH)
        print_output_file(1)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
