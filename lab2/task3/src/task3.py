import tracemalloc
import time
from lab2.utils import open_file, write_file
t_start = time.perf_counter()
tracemalloc.start()

def merge_and_count(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0


    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:

            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1


    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1


    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1


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
    n = int(n_str[0])
    if (1 <= n <= 10**5) and (all(abs(i) <= 10**9 for i in m)):
        temp_arr = [0] * n
        result = merge_sort_and_count(m, temp_arr, 0, n - 1)
        write_file(result, "../txtf/output.txt")
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()