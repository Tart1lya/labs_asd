import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()
f = open('inputfib2.txt')
n = int(f.readline())
f1 = open('outputfib2.txt', 'w')
if 0 <= n <= 10**7:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b % 10, (a + b) % 10
    f1.write(str(b))
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
tracemalloc.stop()
