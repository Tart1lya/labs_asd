# Импортируем модули для отслеживания использования памяти и времени выполнения
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
output_path = get_output_path(7)
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
        # Если текущий элемент arr[i] больше суммы текущего подмассива с добавленным элементом arr[i],
        # начинаем новый подмассив с индекса i
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

# Основной блок программы
if __name__ == "__main__":
    # Считываем данные из файла input.txt с помощью функции open_file
    n_list, arr = open_file(input_path)

    # Извлекаем количество элементов в массиве
    n = int(n_list[0])

    # Проверяем корректность входных данных
    if 1 <= n <= 2 * 10**4 and (all(abs(i) <= 10**9 for i in arr)):
        # Очищаем файл output.txt перед записью результата
        delete_prev_values(7)
        # Находим подмассив с максимальной суммой
        sub_arr = max_subarray(arr)
        # Записываем результат в файл output.txt
        write_file(sub_arr, output_path)
    else:
        # Выводим сообщение об ошибке, если данные некорректны
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим объем затраченной памяти
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    # Останавливаем отслеживание памяти
    tracemalloc.stop()
