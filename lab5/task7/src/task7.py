import tracemalloc
import time
from lab5.utils import *
import os

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(7)

def heapify(arr, n, i):
    """
    Вспомогательная функция для преобразования массива в max-heap.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    """
    Пирамидальная сортировка массива.
    """
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n_str, m_str = lines[0].strip(), lines[1].strip()
    n = int(n_str)
    m = list(map(int, m_str.split()))  # Преобразуем строки в список чисел

    if (1 <= n <= 10 ** 5) and (all(abs(i) <= 10 ** 9 for i in m)):
        print(f"\nTask 7\nInput:\n{n}\n{m}")
        delete_prev_values(7)

        # Сортируем массив m с помощью heapsort
        heapsort(m)
        m.reverse()  # Инвертируем массив для получения убывающего порядка

        write_file(" ".join(map(str, m)), OUTPUT_PATH)
        print_output_file(7)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
