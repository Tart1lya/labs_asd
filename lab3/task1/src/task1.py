# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
import random
from lab2.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
input_path = os.path.join(txtf_dir, "input.txt")
def randomized_partition(arr, low, high):
    # Случайный выбор опорного элемента для разделения массива
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]

    pivot = arr[high]
    i = low - 1
    # Разбиение массива на элементы, меньшие и большие опорного
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Обмен опорного элемента с элементом на позиции i + 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def partition3(arr, low, high):
    # Разбиение массива на три части относительно опорного элемента
    pivot = arr[high]
    lt = low  # Определяет конец области < pivot
    gt = high  # Начало области > pivot
    i = low

    while i <= gt:
        # Если текущий элемент меньше опорного
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        # Если текущий элемент больше опорного
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        # Если текущий элемент равен опорному
        else:
            i += 1
    return lt, gt


def randomized_quick_sort_3way(arr, low, high):
    # Рекурсивная сортировка массива с трёхсторонним разбиением
    if low < high:
        # Случайный выбор опорного элемента для разбиения на три части
        pivot_index = random.randint(low, high)
        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]

        # Трёхстороннее разбиение массива
        lt, gt = partition3(arr, low, high)

        # Рекурсивная сортировка частей массива
        randomized_quick_sort_3way(arr, low, lt - 1)
        randomized_quick_sort_3way(arr, gt + 1, high)


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    n_str, m = open_file(input_path)
    n = int(n_str[0])  # Преобразуем первую строку в число n

    # Проверка корректности входных данных: размер массива и элементы
    if (1 <= n <= 10 ** 4) and (all(abs(i) <= 10 ** 9 for i in m)):
        print(f"\nTask 1\nInput:\n{n}\n{m}")
        delete_prev_values(1)
        # Сортируем массив m с помощью функции randomized_quick_sort_3way
        randomized_quick_sort_3way(m, 0, n - 1)
        output_path = get_output_path(1)
        # Записываем отсортированный массив в файл output.txt
        write_file(" ".join(str(a) for a in m), output_path)
        print_output_file(1)
    else:
        # Выводим сообщение об ошибке, если данные некорректны
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
