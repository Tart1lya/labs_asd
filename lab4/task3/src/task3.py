# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
from lab2.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task/txtf
input_path = os.path.join(txtf_dir, "input.txt")


def is_valid_bracket_sequence(sequence):
    """
    Проверяет, является ли скобочная последовательность правильной.
    :param sequence: строка со скобочной последовательностью
    :return: True, если последовательность правильная, иначе False
    """
    stack = []
    matching_brackets = {')': '(', ']': '['}

    for char in sequence:
        if char in "([":  # Если открывающая скобка
            stack.append(char)
        elif char in ")]":  # Если закрывающая скобка
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return False  # Если не соответствует, последовательность неправильная
    return not stack  # Если стек пуст, последовательность правильная


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    lines = open_file(input_path)
    n = int(lines[0])  # Количество строк
    sequences = lines[1:]  # Последовательности для проверки

    # Проверка корректности входных данных
    if 1 <= n <= 500 and all(1 <= len(seq) <= 10**4 for seq in sequences):
        print(f"\nTask\nInput:\n{n}\n{sequences}")
        delete_prev_values(1)

        # Проверяем каждую последовательность
        results = []
        for seq in sequences:
            results.append("YES" if is_valid_bracket_sequence(seq) else "NO")

        output_path = get_output_path(1)
        # Записываем результаты проверки в файл output.txt
        write_file("\n".join(results), output_path)
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
