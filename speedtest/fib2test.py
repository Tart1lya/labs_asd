import time
t_start = time.perf_counter()
f = open('inputfibtest.txt')
n = int(f.readline())
f1 = open('outputfibtest.txt', 'w')
if 0 <= n <= 10**7:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    f1.write(str(b % 10))
f1.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
