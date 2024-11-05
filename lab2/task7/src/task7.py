import tracemalloc
import time
from lab2.utils import open_file, write_file
t_start = time.perf_counter()
tracemalloc.start()

def max_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(arr)):

        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]


        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i


    return arr[start:end + 1]


if __name__ == "__main__":
    n_list, arr = open_file("../txtf/input.txt")

    n = int(n_list[0])


    if 1 <= n <= 2 * 10**4 and (all(abs(i) <= 10**9 for i in arr)):
        write_file("", "../txtf/output.txt", mode="w")
        sub_arr = max_subarray(arr)
        write_file(sub_arr, "../txtf/output.txt")
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
