import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()
f_input = open('../txtf/input.txt', 'r')
n = int(f_input.readline())
m = [int(x) for x in f_input.readline().split()]
if (3 <= n <= 5000) and (all(abs(i) <= 10**9 for i in m)):
    f_output = open('../txtf/output.txt', 'w')
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            if m[j] < m[j - 1]:
                m[j], m[j - 1] = m[j - 1], m[j]
                f_output.write(f'Swap elements at indices {j} and {j + 1}.\n')
        if m == sorted(m):
            break
    f_output.write('No more swaps needed.')
else:
    print('Введите корректные данные')
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
tracemalloc.stop()