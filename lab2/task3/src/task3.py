import tracemalloc
import time
from lab2.utils import open_file, write_file
t_start = time.perf_counter()
tracemalloc.start()

def merge_and_count(arr, temp_arr, left, mid, right):
    i = left  # Начальный индекс левой половины
    j = mid + 1  # Начальный индекс правой половины
    k = left  # Индекс для временного массива
    inv_count = 0

    # Пока есть элементы в левой и правой половинах
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # Есть инверсия, так как arr[i] > arr[j] и i < j
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    # Копируем оставшиеся элементы левой половины (если есть)
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы правой половины (если есть)
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Копируем отсортированные элементы из temp_arr обратно в arr
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count


if __name__ == "__main__":
    n_str, m = open_file("../txtf/input.txt")
    n = int(n_str)
    if (1 <= n <= 10**5) and (all(abs(i) <= 10**9 for i in m)):
        temp_arr = [0] * n
        result = merge_sort_and_count(m, temp_arr, 0, n - 1)
        write_file(result, "../txtf/output.txt")
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()