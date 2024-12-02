# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
import os
from lab2.utils import open_file, write_file, delete_prev_values, get_output_path, print_output_file

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

# Устанавливаем пути к файлам
current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория текущего скрипта
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория с текстовыми файлами
input_path = os.path.join(txtf_dir, "input.txt")

# Функция обработки операций множества
def process_operations(n, operations):
    current_set = set()  # Создаём множество для хранения элементов
    results = []  # Для хранения результатов операций "?"

    for operation in operations:
        cmd, x = operation.split()
        x = int(x)

        if cmd == "A":
            # Добавляем элемент x в множество
            current_set.add(x)
        elif cmd == "D":
            # Удаляем элемент x из множества, если он существует
            current_set.discard(x)
        elif cmd == "?":
            # Проверяем наличие элемента x и записываем результат
            if x in current_set:
                results.append("Y")
            else:
                results.append("N")
    return results

# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    data = open_file(input_path)
    n = int(data[0])  # Первая строка содержит количество операций
    operations = data[1:]  # Последующие строки — это операции

    # Проверка корректности входных данных
    if 1 <= n <= 5 * 10**5 and all(op[0] in "AD?" and abs(int(op[2:])) <= 10**18 for op in operations):
        print(f"\nTask: 1\nInput:\n{n}\n{operations}")
        delete_prev_values(1)

        # Обрабатываем операции
        results = process_operations(n, operations)

        # Записываем результаты в файл output.txt
        output_path = get_output_path(1)
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
