import tracemalloc
import time
from lab4.utils import *


t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(8)


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


if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = int(lines[0].strip())
    expr = lines[1].strip().split()

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
            write_file(str(result), OUTPUT_PATH)
            print_output_file(8)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
