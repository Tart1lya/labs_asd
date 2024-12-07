# Задача 2: Телефонная книга

## Описание

Этот код обрабатывает запросы для телефонной книги (добавление, удаление, поиск номеров), проверяет корректность данных, записывает результаты в файл и выводит информацию о времени работы и потреблённой памяти.
### Формат входных данных
- Входные данные находятся в файле input.txt.
- В первой строке входного файла содержится число N (1 ≤ N ≤ 10^5) - количество запросов. Далее следуют N строк, каждая из которых содержит один запрос в формате,
описанном выше.
Все номера телефонов состоят из десятичных цифр, в них нет нулей в начале
номера, и каждый состоит не более чем из 7 цифр. Все имена представляют
собой непустые строки из латинских букв, каждая из которых имеет длину
не более 15. Гарантируется при проверке, что не будет человека с именем
«not found».

### Формат выходных данных
- Выводится результат каждого поискового запроса find – имя, соответствующее номеру телефона,
или «not found» (без кавычек), если в телефонной книге нет человека с таким номером телефона. Выводится по одному результату в каждой строке в
том же порядке, как были заданы запросы типа find во входных данных.

### Ограничения
- Время выполнения: 6 секунд.
- Память: 512 МБ.

## Структура проекта
```
lab6/
|--   task2/
|     |-- src/
|     |     |-- task2.py      # Реализация алгоритма
|     |-- tests/
|     |     |-- test_task2.py       # Тесты
|     |-- txtf/
|     |     |-- input.txt     # Входные данные
|     |     |-- output.txt    # Выходные данные
```
## Код задачи
```
import tracemalloc
import time
import os
from lab6.utils import open_file, write_file, get_output_path, delete_prev_values, print_output_file

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
    lines = open_file(input_path)
    n = int(lines[0].strip())  # Количество запросов
    queries = lines[1:]  # Список запросов

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


```
## Запуск проекта

1. Перейдите в директорию task2.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию task2.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python task2.py
   
7. Результат выполнения будет записан в файл output.txt в директории txtf.

## Пример

### Входные данные (input.txt)
```
12
add 911 police
add 76213 Mom
add 17239 Bob
find 76213
find 910
find 911
del 910
del 911
find 911
find 76213
add 76213 daddy
find 76213
```


### Выходные данные (output.txt)
```
Mom
not found
police
not found
Mom
daddy
```
