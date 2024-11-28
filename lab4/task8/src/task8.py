# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
from lab4.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

# Устанавливаем пути для файлов
current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
input_path = os.path.join(txtf_dir, "input.txt")


# Функция для вычисления значения выражения в постфиксной записи
def evaluate_postfix(expression):
    """
    Вычисляет значение выражения в постфиксной записи.

    :param expression: Список строк, представляющих постфиксное выражение.
    :return: Результат вычисления.
    """
    stack = []  # Инициализируем стек для промежуточных значений

    for token in expression:
        if token.isdigit():
            # Если токен - число, помещаем его в стек
            num = int(token)
            if abs(num) >= 2 ** 31:
                raise ValueError("Найдено число, выходящее за пределы |2^31|")
            stack.append(num)
        else:
            # Если токен - оператор, выполняем соответствующую операцию
            b = stack.pop()  # Второй операнд
            a = stack.pop()  # Первый операнд

            # Гарантируем, что промежуточные результаты также находятся в пределах |2^31|
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:
                raise ValueError(f"Неизвестный оператор: {token}")

            if abs(result) >= 2 ** 31:
                raise ValueError("Промежуточный результат превышает предел |2^31|")
            stack.append(result)

    # Результат вычислений остаётся единственным элементом в стеке
    return stack.pop()


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    lines = open_file(input_path)
    n = int(lines[0].strip())  # Количество элементов в выражении
    expr = lines[1].strip().split()  # Постфиксное выражение как список строк

    # Проверка корректности входных данных
    if 1 <= n <= 10 ** 6 and len(expr) == n:
        print(f"\nTask 8\nInput:\n{n}\n{' '.join(expr)}")
        delete_prev_values(8)

        # Вычисляем значение выражения
        try:
            result = evaluate_postfix(expr)
        except ValueError as e:
            print(f"Ошибка: {e}")
            result = None

        if result is not None:
            # Записываем результат в файл output.txt
            output_path = get_output_path(8)
            write_file(str(result), output_path)
            print_output_file(8)
    else:
        # Выводим сообщение об ошибке, если данные некорректны
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
