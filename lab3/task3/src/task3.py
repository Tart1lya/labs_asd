import tracemalloc
import time
from lab2.utils import *


t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task1/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(3)


# Основная функция, которая проверяет, возможно ли отсортировать массив по описанным правилам
def can_sort(n, k, arr):
    # Разделяем элементы массива на k групп по остатку от деления на k
    groups = [[] for _ in range(k)]  # Создаем список групп, в каждой будет храниться часть элементов массива

    for i in range(n):  # Проходим по всем элементам массива
        groups[i % k].append(arr[i])  # Распределяем элементы по группам с учетом индекса и остатка от деления на k

    # Сортируем каждую группу по отдельности
    for i in range(k):  # Для каждой группы
        groups[i].sort()  # Сортируем элементы внутри группы

    # Воссоздаем отсортированный массив из отсортированных групп
    sorted_arr = []  # Список для хранения результирующего отсортированного массива
    for i in range(n):  # Проходим по всем индексам массива
        sorted_arr.append(groups[i % k].pop(0))  # Берем элементы из отсортированных групп в соответствующем порядке

    # Проверяем, совпадает ли получившийся массив с полностью отсортированным массивом
    if sorted_arr == sorted(arr):  # Если отсортированный массив совпадает с результатом
        return "ДА"  # Возвращаем "ДА", если сортировка возможна
    else:
        return "НЕТ"  # Возвращаем "НЕТ", если сортировка невозможна


if __name__ == "__main__":
    (n_and_k_str, m) = open_file(INPUT_PATH)
    n, k = n_and_k_str

    if (1 <= n <= 10 ** 5) and (all(abs(i) <= 10 ** 9 for i in m)) and (1 <= k <= 10 ** 5):
        print(f"\nTask 3\nInput:\n{n_and_k_str}\n{m}")
        delete_prev_values(3)
        result = can_sort(n, k, m)  # Проверяем, можем ли отсортировать массив по правилам
        write_file(result, OUTPUT_PATH)
        print_output_file(3)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
