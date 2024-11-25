# Импортируем библиотеки для измерения памяти и времени работы программы
import tracemalloc
import time
from lab2.utils import *

# Запускаем таймер для отслеживания времени выполнения программы
t_start = time.perf_counter()
# Включаем отслеживание использования памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
input_path = os.path.join(txtf_dir, "input.txt")
output_path = get_output_path(5)
# Функция count_occurrences подсчитывает количество вхождений числа num в подмассиве arr[left:right]
def count_occurrences(arr, num, left, right):
    count = 0  # Инициализируем счетчик
    for i in range(left, right):
        if arr[i] == num:
            count += 1  # Увеличиваем счетчик при совпадении
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

# Основной блок программы
if __name__ == "__main__":
    # Считываем данные из файла input.txt с помощью функции open_file
    n_list, arr = open_file(input_path)

    # Извлекаем количество элементов в массиве
    n = int(n_list[0])

    # Проверка корректности входных данных
    if 1 <= n <= 10**5 and (all(abs(i) <= 10**9 for i in arr)):
        # Очищаем файл output.txt перед записью результатов
        delete_prev_values(5)

        # Запускаем рекурсивную функцию для поиска мажоритарного элемента
        majority_element = majority_element_rec(arr, 0, n)
        # Проверяем, встречается ли найденный элемент более чем в половине массива
        if majority_element is not None:
            if count_occurrences(arr, majority_element, 0, n) > n // 2:
                write_file('1\n', output_path, mode="a")  # Записываем '1', если мажоритарный элемент найден
            else:
                write_file('0\n', output_path, mode="a")  # Записываем '0', если нет мажоритарного элемента
        else:
            write_file('0\n', output_path, mode="a")  # Записываем '0', если мажоритарного элемента нет
    else:
        # Сообщение об ошибке, если данные некорректны
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество затраченной памяти
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    # Останавливаем отслеживание памяти
    tracemalloc.stop()
