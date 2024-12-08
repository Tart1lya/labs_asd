import tracemalloc
import time
from lab2.utils import *

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task5/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task5/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(5)


# Функция count_occurrences подсчитывает количество вхождений числа num в подмассиве arr[left:right]
def count_occurrences(arr, num, left, right):
    count = 0
    for i in range(left, right):
        if arr[i] == num:
            count += 1
    return count


# Рекурсивная функция majority_element_rec для поиска элемента, встречающегося более половины раз в массиве arr
def majority_element_rec(arr, left, right):
    # Базовый случай рекурсии: если подмассив состоит из одного элемента
    if left == right - 1:
        return arr[left]

    # Определяем середину подмассива
    mid = (left + right) // 2
    # Рекурсивно находим мажоритарный элемент в левой и правой половинах подмассива
    left_majority = majority_element_rec(arr, left, mid)
    right_majority = majority_element_rec(arr, mid, right)

    # Если мажоритарные элементы совпадают, возвращаем этот элемент
    if left_majority == right_majority:
        return left_majority

    # Подсчитываем количество вхождений мажоритарных элементов обеих половин в полном подмассиве
    left_count = count_occurrences(arr, left_majority, left, right)
    right_count = count_occurrences(arr, right_majority, left, right)

    # Возвращаем мажоритарный элемент, если его количество превышает половину подмассива, иначе None
    if left_count > (right - left) // 2:
        return left_majority
    elif right_count > (right - left) // 2:
        return right_majority
    else:
        return None


if __name__ == "__main__":
    # Считываем данные из файла input.txt с помощью функции open_file
    n_list, arr = open_file(INPUT_PATH)

    # Извлекаем количество элементов в массиве
    n = int(n_list[0])

    if 1 <= n <= 10**5 and (all(abs(i) <= 10**9 for i in arr)):
        print(f"\nTask 5\nInput:\n{n}\n{arr}")
        delete_prev_values(5)

        # Запускаем рекурсивную функцию для поиска мажоритарного элемента
        majority_element = majority_element_rec(arr, 0, n)
        # Проверяем, встречается ли найденный элемент более чем в половине массива
        if majority_element is not None:
            if count_occurrences(arr, majority_element, 0, n) > n // 2:
                write_file('1', OUTPUT_PATH, mode="a")  # Записываем '1', если мажоритарный элемент найден
            else:
                write_file('0', OUTPUT_PATH, mode="a")  # Записываем '0', если нет мажоритарного элемента
        else:
            write_file('0', OUTPUT_PATH, mode="a")  # Записываем '0', если мажоритарного элемента нет
        print_output_file(5)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
