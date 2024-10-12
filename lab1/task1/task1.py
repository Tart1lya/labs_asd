import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()
f_input = open('input.txt', 'r')
n = int(f_input.readline())
m = [int(x) for x in f_input.readline().split()]
if (1 <= n <= 10**3) and (all(abs(i) <= 10**9 for i in m)):
    for i in range(1, len(m)):
        key = m[i]
        j = i - 1
        while j >= 0 and m[j] > key:
            m[j + 1] = m[j]
            j -= 1
        m[j + 1] = key
    m_sorted = ' '.join(map(str, m))
    f_output = open('output.txt', 'w')
    f_output.write(m_sorted)
else:
    print('Введите корректные данные')
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
tracemalloc.stop()