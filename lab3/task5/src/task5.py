import tracemalloc
import time
from lab3.utils import *


t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task1/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(5)


# Функция для вычисления индекса H (h-index) на основе списка цитирований
def h_index(citations):
    # Сортируем список цитирований по убыванию, чтобы проверить индекс H быстрее
    citations.sort(reverse=True)

    # Проходим по отсортированному списку и находим максимальное значение citations[i], которое выполняет условие citations[i] <= цитированию на позиции i
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i  # Возвращаем индекс citations[i], если условие нарушено

    # Если все элементы соответствуют условиям, возвращаем длину списка как индекс H
    return len(citations)



if __name__ == "__main__":
    citations_str = open_file(INPUT_PATH)
    citations = citations_str[0]

    if (1 <= len(citations) <= 5000) and (all(0 <= i <= 1000 for i in citations)):
        print(f"\nTask 5\nInput:\n{citations}")
        delete_prev_values(5)
        # Вычисляем индекс H для списка цитирований
        h_index_value = h_index(citations)
        write_file(h_index_value, OUTPUT_PATH)
        print_output_file(5)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
