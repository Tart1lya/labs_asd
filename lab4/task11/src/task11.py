# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
from collections import deque
from lab4.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

# Устанавливаем пути к входному и выходному файлам
current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task/txtf
input_path = os.path.join(txtf_dir, "input.txt")


def process_queue(n, m, a):
    """
    Функция вычисляет состояние очереди после завершения выдачи m справок.

    :param n: Количество посетителей в очереди.
    :param m: Общее количество справок, которое министерство может выдать.
    :param a: Список чисел, где a[i] — количество справок, которые нужны i-му посетителю.
    :return: Количество оставшихся в очереди посетителей и их оставшиеся справки.
    """
    queue = deque((i, a[i]) for i in range(n))
    remaining_docs = m  # Сколько справок осталось выдать

    while queue and remaining_docs > 0:
        idx, docs_needed = queue.popleft()
        if docs_needed > 1:
            queue.append((idx, docs_needed - 1))  # Возвращаем в конец очереди с уменьшенным числом справок
        remaining_docs -= 1

    if not queue:
        return -1, []
    remaining_people = len(queue)
    remaining_a = [docs for _, docs in queue]

    return remaining_people, remaining_a


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    first_line, second_line = open_file(input_path)
    first_line = first_line.strip()
    n = int(first_line[0])
    m = int(first_line[2])
    a = []
    i = 0
    while len(a) != n:
        a.append(int(second_line[i]))
        i += 2

    # Проверка корректности входных данных
    if (1 <= n <= 10 ** 5) and (0 <= m <= 10 ** 9) and all(1 <= ai <= 10 ** 6 for ai in a):
        print(f"\nTask 11\nInput:\n{n} {m}\n{a}")
        delete_prev_values(11)

        # Обрабатываем очередь
        remaining_people, remaining_a = process_queue(n, m, a)

        output_path = get_output_path(11)
        # Записываем результат в файл output.txt
        if remaining_people == -1:
            write_file("-1", output_path)
        else:
            write_file(f"{remaining_people}\n" + " ".join(map(str, remaining_a)), output_path)

        print_output_file(11)
    else:
        print("Введите корректные данные")

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
