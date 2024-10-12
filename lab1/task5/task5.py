import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()
f_input = open('input.txt', 'r')
n = int(f_input.readline())
m = [int(x) for x in f_input.readline().split()]
if (1 <= n <= 10**3) and (all(abs(i) <= 10**9 for i in m)):
    for i in range(len(m)):
        min_elem = i
        for j in range(i + 1, len(m)):
            if m[j] < m[min_elem]:
                min_elem = j
        m[i], m[min_elem] = m[min_elem], m[i]
    m_sorted = ' '.join(map(str, m))
    f_output = open('output.txt', 'w')
    f_output.write(m_sorted)
else:
    print('Введите корректные данные')
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
tracemalloc.stop()