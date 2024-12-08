import tracemalloc
import time
import os
from lab6.utils import open_file, write_file, delete_prev_values, get_output_path, print_output_file

t_start = time.perf_counter()
tracemalloc.start()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = get_output_path(1)

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

if __name__ == "__main__":
    data = open_file(INPUT_PATH)
    n = int(data[0])
    operations = data[1:]

    if 1 <= n <= 5 * 10**5 and all(op[0] in "AD?" and abs(int(op[2:])) <= 10**18 for op in operations):
        print(f"\nTask: 1\nInput:\n{n}\n{operations}")
        delete_prev_values(1)

        results = process_operations(n, operations)

        write_file("\n".join(results), OUTPUT_PATH)
        print_output_file(1)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
