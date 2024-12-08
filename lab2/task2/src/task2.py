import tracemalloc
import time
from lab2.utils import *

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task2/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task2/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(2)

# Функция merge выполняет слияние двух отсортированных подмассивов в исходный массив arr
def merge(arr, left, mid, right):

    # Создаем временные подмассивы из элементов исходного массива
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    # Инициализируем индексы для подмассивов L и R, а также для arr
    i = j = 0
    k = left

    # Объединяем элементы L и R, выбирая наименьшие значения для сохранения упорядоченности
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Копируем оставшиеся элементы из L, если они остались
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы из R, если они остались
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    # Записываем текущие индексы и крайние элементы объединенного подмассива в файл
    write_file(f"{left + 1} {right + 1} {arr[left]} {arr[right]}\n", OUTPUT_PATH, mode='a')


# Рекурсивная функция merge_sort выполняет сортировку массива методом слияния
def merge_sort(arr, left, right):
    if left < right:

        # Находим середину массива
        mid = (left + right) // 2

        # Рекурсивно сортируем левую и правую половины массива
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Сливаем отсортированные половины
        merge(arr, left, mid, right)



if __name__ == "__main__":

    n_str, m = open_file(INPUT_PATH)
    n = int(n_str[0])

    if (1 <= n <= 10 ** 5) and (all(abs(i) <= 10 ** 9 for i in m)):
        print(f"\nTask 2\nInput:\n{n}\n{m}")
        # Сортируем массив m
        delete_prev_values(2)
        merge_sort(m, 0, n - 1)
        write_file(" ".join(str(a) for a in m), OUTPUT_PATH, mode='a')
        print_output_file(2)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
