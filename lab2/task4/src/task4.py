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
output_path = get_output_path(4)
# Функция binary_search выполняет двоичный поиск элемента target в отсортированном массиве arr
def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Инициализация левого и правого указателей
    while left <= right:
        mid = (left + right) // 2  # Находим средний индекс
        if arr[mid] == target:
            return mid  # Возвращаем индекс, если элемент найден
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой половине массива
        else:
            right = mid - 1  # Ищем в левой половине массива
    return -1  # Возвращаем -1, если элемент не найден

# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    data_n, data_k = open_file(input_path)

    # Извлекаем количество элементов n и массив a из первого блока данных
    n = int(data_n[0])
    a = data_n[1:]

    # Извлекаем количество элементов k и массив b из второго блока данных
    k = int(data_k[0])
    b = data_k[1:]

    # Проверка корректности входных данных
    if 1 <= n <= 10**5 and 1 <= k <= 10**5 and min(a) >= 1 and \
        min(b) >= 1 and max(a) <= 10**9 and max(b) <= 10**9:
        print(f"\nTask 4\nInput:\n{data_n}\n{data_k}")
        # Очищаем файл output.txt перед записью результатов
        delete_prev_values(4)
        # Выполняем двоичный поиск для каждого элемента массива b в массиве a
        for i in b:
            result = binary_search(a, i)  # Ищем элемент i из b в a
            # Записываем результат поиска в output.txt
            write_file(f"{result} ", output_path, mode='a')
        print_output_file(4)
    else:
        # Сообщение об ошибке, если данные некорректны
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()  # Останавливаем отслеживание памяти
