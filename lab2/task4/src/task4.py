import tracemalloc
import time
from lab2.utils import open_file, write_file
t_start = time.perf_counter()
tracemalloc.start()

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    data_n, data_k = open_file("../txtf/input.txt")

    n = int(data_n[0])
    a = data_n[1:]  # Здесь уже предполагаем, что данные очищены в open_file()
    k = int(data_k[0])
    b = data_k[1:]


    if 1 <= n <= 10**5 and 1 <= k <= 10**5 and min(a) >= 1 and \
        min(b) >= 1 and max(a) <= 10**9 and max(b) <= 10**9:
        write_file("", "../txtf/output.txt", mode="w")
        for i in b:
            result = binary_search(a, i)
            write_file(f"{result} ", "../txtf/output.txt", mode='a')
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
