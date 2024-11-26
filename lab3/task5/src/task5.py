# Импортируем библиотеки для отслеживания времени работы программы и использования памяти
import tracemalloc
import time
from lab3.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти, чтобы отслеживать, сколько памяти использует программа
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
input_path = os.path.join(txtf_dir, "input.txt")
# Функция для вычисления индекса H (h-index) на основе списка цитирований
def h_index(citations):
    # Сортируем список цитирований по убыванию, чтобы проверить индекс H быстрее
    citations.sort(reverse=True)

    # Проходим по отсортированному списку и находим максимальное значение citations[i],
    # которое выполняет условие citations[i] <= цитированию на позиции i
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i  # Возвращаем индекс citations[i], если условие нарушено

    # Если все элементы соответствуют условиям, возвращаем длину списка как индекс H
    return len(citations)


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    citations_str = open_file(input_path)
    citations = citations_str[0]

    # Проверка корректности входных данных:
    # - размер массива должен быть в пределах от 1 до 5000
    # - все элементы массива должны быть в пределах от 0 до 1000
    if (1 <= len(citations) <= 5000) and (all(0 <= i <= 1000 for i in citations)):
        print(f"\nTask 5\nInput:\n{citations}")
        delete_prev_values(5)
        # Вычисляем индекс H для списка цитирований
        h_index_value = h_index(citations)
        output_path = get_output_path(5)
        # Записываем полученное значение индекса H в файл output.txt
        write_file(h_index_value, output_path)
        print_output_file(5)
    else:
        # Если данные некорректны, выводим сообщение об ошибке
        print('Введите корректные данные')

    # Выводим время выполнения программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))

    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
