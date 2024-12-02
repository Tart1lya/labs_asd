import tracemalloc
import time
import os
from lab2.utils import open_file, write_file, get_output_path, delete_prev_values, print_output_file

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

# Пути к входному и выходному файлам
current_dir = os.path.dirname(os.path.abspath(__file__))  # Текущая директория
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория txtf
input_path = os.path.join(txtf_dir, "input.txt")


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
                results.append("invalid")  # Для отладки можно использовать вывод ошибки
        elif command[0] == "del":
            number = command[1]
            if is_valid_number(number):
                phone_book.pop(number, None)
        elif command[0] == "find":
            number = command[1]
            if is_valid_number(number):
                results.append(phone_book.get(number, "not found"))
            else:
                results.append("not found")  # Некорректный номер считается ненайденным

    return results


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt
    data = open_file(input_path)
    n = int(data[0][0])  # Количество запросов
    queries = data[1]  # Список запросов

    # Проверка корректности входных данных
    if 1 <= n <= 10 ** 5:
        print(f"\nTask 2\nInput:\n{n}\n{queries}")
        delete_prev_values(1)

        # Обрабатываем запросы
        results = process_phone_book(queries)

        # Формируем путь к выходному файлу
        output_path = get_output_path(1)

        # Записываем результаты в файл output.txt
        write_file("\n".join(results), output_path)
        print_output_file(1)

    else:
        print("Введите корректные данные")

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
