# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
from lab2.utils import write_file, open_file, get_output_path, delete_prev_values
import os

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()


# Функция merge выполняет слияние двух отсортированных подмассивов
def merge(arr, left, mid, right):
    # Создаем временные подмассивы из элементов исходного массива
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    # Инициализируем индексы для подмассивов L, R и основного массива arr
    i = j = 0
    k = left

    # Сливаем элементы из L и R обратно в arr, выбирая меньший элемент
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Копируем оставшиеся элементы из L, если они есть
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы из R, если они есть
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


# Рекурсивная функция merge_sort выполняет сортировку массива методом слияния
def merge_sort(arr, left, right):
    if left < right:
        # Находим середину массива
        mid = (left + right) // 2
        # Рекурсивно сортируем левую и правую половины
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        # Сливаем отсортированные половины
        merge(arr, left, mid, right)


# Основной блок программы
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
    txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
    input_path = os.path.join(txtf_dir, "input.txt")
    # Читаем данные из файла input.txt с помощью функции open_file
    n_str, m = open_file(input_path)
    n = int(n_str[0])  # Преобразуем первую строку в число n

    # Проверка корректности входных данных
    if (1 <= n <= 2 * 10 ** 4) and (all(abs(i) <= 10 ** 9 for i in m)):
        # Сортируем массив m
        delete_prev_values(1)
        merge_sort(m, 0, n - 1)
        # Записываем отсортированный массив в файл output.txt
        output_path = get_output_path(1)  # Получаем путь к output.txt
        write_file(" ".join(str(a) for a in m), output_path)
    else:
        # Выводим сообщение об ошибке, если данные некорректны
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()  # Останавливаем отслеживание памяти
