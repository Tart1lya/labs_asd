import tracemalloc
import time
from lab5.utils import *


t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(4)


def build_min_heap(data):
    """Преобразует массив в min-heap и возвращает список свопов"""
    n = len(data)
    swaps = []

    def sift_down(i):
        """Функция просеивания вниз"""
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] < data[min_index]:
            min_index = left

        if right < n and data[right] < data[min_index]:
            min_index = right

        if i != min_index:
            swaps.append((i, min_index))  # Запоминаем перестановку
            data[i], data[min_index] = data[min_index], data[i]  # Перестановка
            sift_down(min_index)  # Рекурсивно просеиваем вниз

    for i in range((n - 2) // 2, -1, -1):
        sift_down(i)

    return swaps


if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n_str = lines[0].strip()
    m = lines[1].strip().split()

    n = int(n_str)
    m = list(map(int, m))

    if (1 <= n <= 10 ** 5) and (all(0 <= i <= 10 ** 9 for i in m)):
        print(f"\nTask: 4\nInput:\n{n}\n{m}")
        delete_prev_values(4)

        # Строим min-heap и получаем список перестановок
        swaps = build_min_heap(m)

        output_data = [f"{len(swaps)}"] + [f"{i} {j}" for i, j in swaps]
        write_file("\n".join(output_data), OUTPUT_PATH)
        print_output_file(4)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
