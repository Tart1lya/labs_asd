# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
from lab6.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

# Задаём пути к файлам
current_dir = os.path.dirname(os.path.abspath(__file__))  # Текущая директория
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Папка с файлами
input_path = os.path.join(txtf_dir, "input.txt")


def count_beautiful_pairs(n, k, S, beautiful_pairs):
    """Вычисление количества красивых пар."""
    count = {}
    result = 0

    # Проходим по строке S
    for char in S:
        # Проверяем, образует ли текущий символ красивую пару с ранее встреченными
        for a, b in beautiful_pairs:
            if char == b:
                result += count.get(a, 0)

        # Увеличиваем счётчик для текущего символа
        count[char] = count.get(char, 0) + 1

    return result


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt
    input_data = open_file(input_path)
    n, k = map(int, input_data[0].split())
    S = input_data[1].strip()
    pairs = input_data[2:]  # Читаем пары

    # Формируем множество красивых пар
    beautiful_pairs = set()
    for pair in pairs:
        beautiful_pairs.add((pair[0], pair[1]))

    print(beautiful_pairs)

    # Проверяем корректность входных данных
    if (1 <= n <= 100000) and (1 <= k <= 676) and len(S) == n:
        print(f"\nTask 7\nInput:\n{n} {k}\n{S}\n{beautiful_pairs}")
        delete_prev_values(7)

        # Считаем количество красивых пар
        result = count_beautiful_pairs(n, k, S, beautiful_pairs)

        output_path = get_output_path(7)
        # Записываем результат в файл output.txt
        write_file(str(result), output_path)
        print_output_file(7)
    else:
        # Сообщаем об ошибке, если данные некорректны
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
