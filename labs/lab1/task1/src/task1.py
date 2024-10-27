import tracemalloc
import time
from labs.utils import open_file, write_file
t_start = time.perf_counter()
tracemalloc.start()

def insertion_sort(n, m):
    for i in range(1, len(m)):
        key = m[i]
        j = i - 1
        while j >= 0 and m[j] > key:
            m[j + 1] = m[j]
            j -= 1
        m[j + 1] = key


if __name__ == "__main__":
    n_str, m = open_file("../txtf/input.txt")
    print(m)
    n = int(n_str)
    if (1 <= n <= 10**3) and (all(abs(i) <= 10**9 for i in m)):
        insertion_sort(n, m)
        write_file(" ".join(str(a) for a in m), "../txtf/output.txt")
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()

