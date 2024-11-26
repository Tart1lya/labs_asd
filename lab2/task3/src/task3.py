# Импортируем библиотеки для отслеживания использования памяти и времени выполнения программы
import tracemalloc
import time
from lab2.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
input_path = os.path.join(txtf_dir, "input.txt")
output_path = get_output_path(3)
# Функция merge_and_count выполняет слияние двух отсортированных подмассивов в исходный массив arr,
# одновременно считая количество инверсий
def merge_and_count(arr, temp_arr, left, mid, right):
    i = left  # Начальный индекс для левого подмассива
    j = mid + 1  # Начальный индекс для правого подмассива
    k = left  # Начальный индекс для результирующего подмассива temp_arr
    inv_count = 0  # Счетчик инверсий

    # Сливаем подмассивы L и R, сохраняя упорядоченность и считая инверсии
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            # Количество инверсий равно числу оставшихся элементов в левом подмассиве
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    # Копируем оставшиеся элементы из левого подмассива, если они остались
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы из правого подмассива, если они остались
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Копируем отсортированные элементы из temp_arr обратно в arr
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count  # Возвращаем количество инверсий


# Рекурсивная функция merge_sort_and_count выполняет сортировку массива методом слияния
# и считает общее количество инверсий
def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0  # Счетчик инверсий
    if left < right:
        mid = (left + right) // 2

        # Считаем инверсии в левой половине массива
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        # Считаем инверсии в правой половине массива
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        # Считаем инверсии при слиянии двух половин
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count  # Возвращаем общее количество инверсий


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    n_str, m = open_file(input_path)
    n = int(n_str[0])  # Преобразуем первое значение в число n

    # Проверка корректности входных данных
    if (1 <= n <= 10 ** 5) and (all(abs(i) <= 10 ** 9 for i in m)):
        print(f"\nTask 3\nInput:\n{n}\n{m}")
        delete_prev_values(3)
        # Инициализируем временный массив для хранения отсортированных значений
        temp_arr = [0] * n
        # Выполняем сортировку с подсчетом инверсий и сохраняем результат
        result = merge_sort_and_count(m, temp_arr, 0, n - 1)
        # Записываем количество инверсий в файл output.txt
        write_file(result, output_path)
        print_output_file(3)
    else:
        # Сообщение об ошибке, если данные некорректны
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()  # Останавливаем отслеживание памяти
