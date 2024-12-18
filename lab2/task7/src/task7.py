import tracemalloc
import time
from lab2.utils import *

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task7/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task7/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(7)


# Функция max_subarray находит подмассив с максимальной суммой в массиве arr
def max_subarray(arr):
    # Инициализируем переменные для хранения максимальной суммы и текущей суммы подмассива
    max_sum = arr[0]
    current_sum = arr[0]
    # Инициализируем индексы для отслеживания начальной и конечной позиций подмассива с максимальной суммой
    start = end = 0
    temp_start = 0  # Временная начальная позиция подмассива для текущей суммы

    # Проходим по массиву начиная со второго элемента
    for i in range(1, len(arr)):
        # Если текущий элемент arr[i] больше суммы текущего подмассива с добавленным элементом arr[i], начинаем новый подмассив с индекса i
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i  # Обновляем временное начало подмассива
        else:
            # В противном случае добавляем arr[i] к текущей сумме
            current_sum += arr[i]

        # Обновляем максимальную сумму и индексы подмассива, если текущая сумма больше max_sum
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start  # Обновляем начальный индекс подмассива с максимальной суммой
            end = i  # Обновляем конечный индекс подмассива с максимальной суммой

    # Возвращаем подмассив с максимальной суммой
    return arr[start:end + 1]

if __name__ == "__main__":
    n_list, arr = open_file(INPUT_PATH)
    n = int(n_list[0])

    if 1 <= n <= 2 * 10**4 and (all(abs(i) <= 10**9 for i in arr)):
        print(f"\nTask 7\nInput:\n{n}\n{arr}")
        delete_prev_values(7)
        # Находим подмассив с максимальной суммой
        sub_arr = max_subarray(arr)
        write_file(sub_arr, OUTPUT_PATH)
        print_output_file(7)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
