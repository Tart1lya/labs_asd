# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
import os
from lab2.utils import open_file, write_file, delete_prev_values, get_output_path, print_output_file

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Текущая директория
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория для input.txt и output.txt
input_path = os.path.join(txtf_dir, "input.txt")

def is_heap(array, n):
    """
    Проверяет, является ли массив неубывающей пирамидой.

    :param array: массив целых чисел
    :param n: размер массива
    :return: True, если массив - пирамида, иначе False
    """
    for i in range(n):
        left_child_index = 2 * (i + 1) - 1  # Индекс левого потомка
        right_child_index = 2 * (i + 1)  # Индекс правого потомка

        # Проверяем условие для левого потомка
        if left_child_index < n and array[i] > array[left_child_index]:
            return False

        # Проверяем условие для правого потомка
        if right_child_index < n and array[i] > array[right_child_index]:
            return False

    return True

# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    n_str, array = open_file(input_path)
    n = int(n_str[0])  # Преобразуем первую строку в число n

    # Проверка корректности входных данных
    if (1 <= n <= 10 ** 6) and (all(abs(i) <= 2 * 10 ** 9 for i in array)):
        print(f"\nTask: 1\nInput:\n{n}\n{array}")
        delete_prev_values(1)

        # Проверяем массив на условие пирамиды
        result = "YES" if is_heap(array, n) else "NO"

        # Записываем результат в файл output.txt
        output_path = get_output_path(1)
        write_file(result, output_path)
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
