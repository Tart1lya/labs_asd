import tracemalloc
import time
from lab1.utils import open_file, write_file, get_output_path, delete_prev_values

t_start = time.perf_counter()
tracemalloc.start()

def insertion_sort(n, m):
    for i in range(1, n):
        key = m[i]
        j = i - 1
        while j >= 0 and m[j] > key:
            m[j + 1] = m[j]
            j -= 1
        m[j + 1] = key


if __name__ == "__main__":
    # Формируем путь к input.txt
    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
    txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
    input_path = os.path.join(txtf_dir, "input.txt")
    n_str, m = open_file(input_path)
    n = int(n_str)
    if (1 <= n <= 10**3) and (all(abs(i) <= 10**9 for i in m)):
        delete_prev_values(1)
        insertion_sort(n, m)
        output_path = get_output_path(1)  # Получаем путь к output.txt
        write_file(" ".join(str(a) for a in m), output_path)
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()

