# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
from lab2.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

# Пути к входному и выходному файлам
current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
input_path = os.path.join(txtf_dir, "input.txt")
output_path = os.path.join(txtf_dir, "output.txt")


def process_stack(commands):
    """
    Обрабатывает команды работы со стеком.
    :param commands: Список строк, содержащих команды (+ N или -)
    :return: Список чисел, удаленных из стека
    """
    stack = []
    results = []

    for command in commands:
        if command.startswith("+"):
            _, number = command.split()
            stack.append(int(number))
        elif command == "-":
            results.append(stack.pop())

    return results


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    lines = open_file(input_path)
    m = int(lines[0])  # Преобразуем первую строку в число m (количество команд)
    commands = lines[1:]  # Список команд

    # Проверка корректности входных данных
    if 1 <= m <= 10 ** 6 and all(
            cmd.startswith("+") and abs(int(cmd.split()[1])) <= 10 ** 9 or cmd == "-" for cmd in commands
    ):
        print(f"\nTask 1\nInput:\n{m}\n{commands}")
        delete_prev_values(1)

        # Обрабатываем команды и записываем результат
        results = process_stack(commands)
        write_file("\n".join(map(str, results)), output_path)
        print_output_file(1)
    else:
        # Выводим сообщение об ошибке, если данные некорректны
        print("Введите корректные данные")

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
