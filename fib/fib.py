f = open('inputfib.txt')
n = int(f.readline())
f1 = open('outputfib.txt', 'w')
if 0 <= n <= 45:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    f1.write(str(b))
