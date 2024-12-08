import tracemalloc
import time
from lab2.utils import *
import os

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task1/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")

# Функция merge выполняет слияние двух отсортированных подмассивов
def merge(arr, left, mid, right):

    # Создаем временные подмассивы из элементов исходного массива
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    # Инициализируем индексы для подмассивов L, R и основного массива arr
    i = j = 0
    k = left

    # Сливаем элементы из L и R обратно в arr, выбирая меньший элемент
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Копируем оставшиеся элементы из L, если они есть
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы из R, если они есть
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


# Рекурсивная функция merge_sort выполняет сортировку массива методом слияния
def merge_sort(arr, left, right):
    if left < right:

        # Находим середину массива
        mid = (left + right) // 2

        # Рекурсивно сортируем левую и правую половины
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Сливаем отсортированные половины
        merge(arr, left, mid, right)



if __name__ == "__main__":
    n_str, m = open_file(INPUT_PATH)
    n = int(n_str[0])

    if (1 <= n <= 2 * 10 ** 4) and (all(abs(i) <= 10 ** 9 for i in m)):
        print(f'\nTask 1\nInput:\n{n}\n{m}')
        # Сортируем массив m
        delete_prev_values(1)
        merge_sort(m, 0, n - 1)
        output_path = get_output_path(1)
        write_file(" ".join(str(a) for a in m), output_path)
        print_output_file(1)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
