import tracemalloc
import time
from collections import OrderedDict
from lab6.utils import *

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # Директория task/src
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")  # Директория task/txtf
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(4)


def process_commands(commands):
    """
    Обрабатывает команды работы с ассоциативным массивом.
    """
    assoc_array = OrderedDict()
    results = []

    for line in commands:
        parts = line.strip().split()
        command = parts[0]

        if command == "put":
            # Добавление или обновление ключа
            x, y = parts[1], parts[2]
            if x in assoc_array:
                assoc_array[x] = y
            else:
                assoc_array[x] = y

        elif command == "get":
            # Получение значения по ключу
            x = parts[1]
            results.append(assoc_array.get(x, "<none>"))

        elif command == "prev":
            # Поиск предыдущего ключа
            x = parts[1]
            if x in assoc_array:
                keys = list(assoc_array.keys())
                idx = keys.index(x)
                if idx > 0:
                    results.append(assoc_array[keys[idx - 1]])
                else:
                    results.append("<none>")
            else:
                results.append("<none>")

        elif command == "next":
            # Поиск следующего ключа
            x = parts[1]
            if x in assoc_array:
                keys = list(assoc_array.keys())
                idx = keys.index(x)
                if idx < len(keys) - 1:
                    results.append(assoc_array[keys[idx + 1]])
                else:
                    results.append("<none>")
            else:
                results.append("<none>")

        elif command == "delete":
            # Удаление ключа
            x = parts[1]
            assoc_array.pop(x, None)

    return results


if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = int(lines[0])
    commands = lines[1:]

    if 1 <= n <= 5 * 10 ** 5 and all(len(cmd.split()) in (2, 3) for cmd in commands):
        print(f"\nTask 4\nInput:\n{lines}")
        delete_prev_values(4)

        results = process_commands(commands)

        write_file("\n".join(results), OUTPUT_PATH)
        print_output_file(4)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
