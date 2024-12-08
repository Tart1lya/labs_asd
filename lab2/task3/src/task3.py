import tracemalloc
import time
from lab2.utils import *


t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task3/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task3/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(3)


# Функция merge_and_count выполняет слияние двух отсортированных подмассивов в исходный массив arr, одновременно считая количество инверсий
def merge_and_count(arr, temp_arr, left, mid, right):
    i = left  # Начальный индекс для левого подмассива
    j = mid + 1  # Начальный индекс для правого подмассива
    k = left  # Начальный индекс для результирующего подмассива temp_arr
    inv_count = 0  # Счетчик инверсий

    # Сливаем подмассивы L и R, сохраняя упорядоченность и считая инверсии
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            # Количество инверсий равно числу оставшихся элементов в левом подмассиве
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    # Копируем оставшиеся элементы из левого подмассива, если они остались
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы из правого подмассива, если они остались
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Копируем отсортированные элементы из temp_arr обратно в arr
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count  # Возвращаем количество инверсий


# Рекурсивная функция merge_sort_and_count выполняет сортировку массива методом слияния и считает общее количество инверсий
def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0  # Счетчик инверсий
    if left < right:
        mid = (left + right) // 2

        # Считаем инверсии в левой половине массива
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        # Считаем инверсии в правой половине массива
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        # Считаем инверсии при слиянии двух половин
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count  # Возвращаем общее количество инверсий



if __name__ == "__main__":
    n_str, m = open_file(INPUT_PATH)
    n = int(n_str[0])

    if (1 <= n <= 10 ** 5) and (all(abs(i) <= 10 ** 9 for i in m)):
        print(f"\nTask 3\nInput:\n{n}\n{m}")
        delete_prev_values(3)
        # Инициализируем временный массив для хранения отсортированных значений
        temp_arr = [0] * n
        # Выполняем сортировку с подсчетом инверсий и сохраняем результат
        result = merge_sort_and_count(m, temp_arr, 0, n - 1)
        write_file(result, OUTPUT_PATH)
        print_output_file(3)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
