import tracemalloc
import time

t_start = time.perf_counter()
tracemalloc.start()
f_input = open('../txtf/input.txt', 'r')
n = int(f_input.readline())
m = [int(x) for x in f_input.readline().split()]
if (1 <= n <= 10 ** 3) and (all(abs(i) <= 10 ** 9 for i in m)):

    #algorithm itself
    for i in range(len(m)):
        for j in range(len(m) - 1, i, -1):
            if m[j] < m[j - 1]:
                m[j], m[j - 1] = m[j - 1], m[j]
    m_sorted = ' '.join(map(str, m))
    f_output = open('../txtf/output.txt', 'w')
    f_output.write(m_sorted)
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
else:
    print('Введите корректные данные')
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
