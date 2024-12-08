import tracemalloc
import time
import os
from lab6.utils import open_file, write_file, get_output_path, delete_prev_values, print_output_file

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(2)


def is_valid_name(name):
    """
    Проверяет валидность имени.
    Имя должно содержать только латинские буквы и иметь длину не более 15 символов.
    """
    return name.isalpha() and len(name) <= 15


def is_valid_number(number):
    """
    Проверяет валидность номера телефона.
    Номер должен состоять из цифр, иметь длину от 1 до 7 символов и не начинаться с нуля.
    """
    return number.isdigit() and 1 <= len(number) <= 7 and number[0] != '0'


def process_phone_book(queries):
    """
    Обрабатывает запросы для телефонной книги.

    :param queries: Список запросов
    :return: Список результатов для запросов типа "find"
    """
    phone_book = {}  # Словарь для хранения телефонной книги
    results = []  # Список результатов для команд "find"

    for query in queries:
        command = query.split()
        if command[0] == "add":
            number, name = command[1], command[2]
            if is_valid_number(number) and is_valid_name(name):
                phone_book[number] = name
            else:
                results.append("invalid")
        elif command[0] == "del":
            number = command[1]
            if is_valid_number(number):
                phone_book.pop(number, None)
        elif command[0] == "find":
            number = command[1]
            if is_valid_number(number):
                results.append(phone_book.get(number, "not found"))
            else:
                results.append("not found")

    return results

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = int(lines[0].strip())
    queries = lines[1:]

    if 1 <= n <= 10 ** 5:
        print(f"\nTask 2\nInput:\n{n}\n{queries}")
        delete_prev_values(2)

        results = process_phone_book(queries)

        write_file("\n".join(results), OUTPUT_PATH)
        print_output_file(2)

    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
