import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()
f = open('../txtf/inputfib.txt')
n = int(f.readline())
f1 = open('../txtf/outputfib.txt', 'w')
if 0 <= n <= 45:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    f1.write(str(b))
else:
    print('Не подходит диапазону, попробуйте ещё раз')
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
tracemalloc.stop()