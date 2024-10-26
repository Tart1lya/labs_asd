import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()
f = open('../txtf/input.txt')
a, b = map(int, f.readline().split())
f1 = open('../txtf/output.txt', 'w')
if (-10**9 <= a <= 10**9) and (-10**9 <= b <= 10**9):
    f1.write(str(a + b))
else:
    print('Не подходит по диапазону, попробуйте ещё раз')
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
tracemalloc.stop()