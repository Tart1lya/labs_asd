# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
from lab5.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

# Определяем пути к файлам
current_dir = os.path.dirname(os.path.abspath(__file__))  # Текущая директория task1/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
input_path = os.path.join(txtf_dir, "input.txt")


def build_min_heap(data):
    """Преобразует массив в min-heap и возвращает список свопов"""
    n = len(data)
    swaps = []

    def sift_down(i):
        """Функция просеивания вниз"""
        min_index = i
        left = 2 * i + 1  # индекс левого ребенка
        right = 2 * i + 2  # индекс правого ребенка

        # Если левый ребенок существует и меньше текущего узла
        if left < n and data[left] < data[min_index]:
            min_index = left

        # Если правый ребенок существует и меньше текущего минимального узла
        if right < n and data[right] < data[min_index]:
            min_index = right

        # Если текущий узел не минимальный, обмениваем местами и продолжаем
        if i != min_index:
            swaps.append((i, min_index))  # Запоминаем перестановку
            data[i], data[min_index] = data[min_index], data[i]  # Перестановка
            sift_down(min_index)  # Рекурсивно просеиваем вниз

    # Начинаем обработку с последнего родителя
    for i in range((n - 2) // 2, -1, -1):
        sift_down(i)

    return swaps


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    lines = open_file(input_path)
    n_str = lines[0].strip()  # Убираем пробелы и символы новой строки из первой строки
    m = lines[1].strip().split()  # Разделяем вторую строку на элементы

    n = int(n_str)  # Преобразуем первую строку в число n
    m = list(map(int, m))  # Преобразуем элементы массива в числа

    # Проверка корректности входных данных
    if (1 <= n <= 10 ** 5) and (all(0 <= i <= 10 ** 9 for i in m)):
        print(f"\nTask: 4\nInput:\n{n}\n{m}")
        delete_prev_values(4)

        # Строим min-heap и получаем список перестановок
        swaps = build_min_heap(m)

        output_path = get_output_path(4)
        # Формируем содержимое выходного файла
        output_data = [f"{len(swaps)}"] + [f"{i} {j}" for i, j in swaps]
        write_file("\n".join(output_data), output_path)
        print_output_file(4)
    else:
        # Выводим сообщение об ошибке, если данные некорректны
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
