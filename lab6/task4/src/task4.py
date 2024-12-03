import tracemalloc
import time
from collections import OrderedDict
from lab6.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task/txtf
input_path = os.path.join(txtf_dir, "input.txt")


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


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    lines = open_file(input_path)
    n = int(lines[0])  # Преобразуем первую строку в число операций
    commands = lines[1:]  # Команды операций

    # Проверяем корректность входных данных
    if 1 <= n <= 5 * 10 ** 5 and all(len(cmd.split()) in (2, 3) for cmd in commands):
        print(f"\nTask 4\nInput:\n{lines}")
        delete_prev_values(4)

        # Обрабатываем команды
        results = process_commands(commands)

        # Записываем результаты в файл output.txt
        output_path = get_output_path(4)
        write_file("\n".join(results), output_path)
        print_output_file(4)
    else:
        # Выводим сообщение об ошибке, если данные некорректны
        print("Введите корректные данные")

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
