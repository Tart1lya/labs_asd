# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import os
import time
import tracemalloc
from lab2.utils import open_file, write_file, get_output_path, delete_prev_values, print_output_file

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Текущая директория
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Путь к директории с файлами
input_path = os.path.join(txtf_dir, "input.txt")


# Основная функция обработки операций
def process_priority_queue(operations):
    import heapq

    heap = []  # Минимальная куча
    element_map = {}  # Словарь для отслеживания актуальных значений
    id_map = {}  # Словарь: идентификатор строки → элемент
    removed = set()  # Множество удаленных элементов
    result = []  # Для хранения выходных данных

    current_id = 0  # Уникальный идентификатор для операций A

    for i, operation in enumerate(operations):
        parts = operation.split()
        if parts[0] == "A":
            # Добавляем элемент в кучу
            x = int(parts[1])
            heapq.heappush(heap, (x, current_id))
            element_map[current_id] = x
            id_map[i + 1] = current_id  # i+1 соответствует строке x + 1
            current_id += 1

        elif parts[0] == "X":
            # Удаляем минимальный элемент
            while heap and heap[0][1] in removed:
                heapq.heappop(heap)  # Пропускаем удаленные элементы

            if heap:
                _, element_id = heapq.heappop(heap)
                result.append(str(element_map[element_id]))
                removed.add(element_id)
            else:
                result.append("*")

        elif parts[0] == "D":
            # Уменьшаем значение элемента
            x = int(parts[1]) + 1
            y = int(parts[2])
            element_id = id_map[x]  # Получаем идентификатор элемента

            # Уменьшаем значение в словаре
            element_map[element_id] = y

            # Добавляем в кучу новое значение
            heapq.heappush(heap, (y, element_id))

    return result


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    lines = open_file(input_path)
    n = int(lines[0])  # Число операций
    operations = lines[1:]  # Список операций

    # Проверка корректности входных данных
    if 1 <= n <= 10 ** 6 and all(len(op.split()) in (1, 2, 3) for op in operations):
        print(f"\nTask: 6\nInput Operations: {n}")
        delete_prev_values(6)  # Очищаем предыдущие результаты

        # Обрабатываем операции
        results = process_priority_queue(operations)

        output_path = get_output_path(6)
        # Записываем результаты операций X в файл output.txt
        write_file("\n".join(results), output_path)
        print_output_file(6)
    else:
        print("Введите корректные данные")

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
