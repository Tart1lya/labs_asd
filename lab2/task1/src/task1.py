import tracemalloc
import time
from lab2.utils import open_file, write_file
t_start = time.perf_counter()
tracemalloc.start()

def merge(arr, left, mid, right):
    # Создаем копии двух половин
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    # Указатели для L, R и основного массива
    i = j = 0
    k = left

    # Объединяем две половины
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Копируем оставшиеся элементы L, если есть
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы R, если есть
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

if __name__ == "__main__":
    n_str, m = open_file("../txtf/input.txt")
    n = int(n_str[0])
    if (1 <= n <= 2 * 10**4) and (all(abs(i) <= 10**9 for i in m)):
        merge_sort(m, 0, n - 1)
        write_file(" ".join(str(a) for a in m), "../txtf/output.txt")
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()

