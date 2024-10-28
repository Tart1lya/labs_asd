import tracemalloc
import time
from lab1.utils import open_file, write_file
t_start = time.perf_counter()
tracemalloc.start()

def swap_secretary(n, m):
    for i in range(n):
        for j in range(i + 1, n):
            if m[j] < m[j - 1]:
                m[j], m[j - 1] = m[j - 1], m[j]
                write_file(f'Swap elements at indices {j} and {j + 1}.', "../txtf/output.txt", mode='a')
        if m == sorted(m):
            break


if __name__ == "__main__":
    n_str, m = open_file("../txtf/input.txt")
    n = int(n_str)
    if (3 <= n <= 5000) and (all(abs(i) <= 10 ** 9 for i in m)):
        swap_secretary(n, m)
        write_file('No more swaps needed.', "../txtf/output.txt", mode='a')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()