import tracemalloc
import time
a, b = map(int, input().split())
t_start = time.perf_counter()
tracemalloc.start()
while True:
    if (-10**9 <= a <= 10**9) and (-10**9 <= b <= 10**9):
        print(a + b**2)
        break
    else:
        print('Не подходит по диапазону')
        a, b = map(int, input().split())
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
tracemalloc.stop()