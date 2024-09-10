f = open('input.txt')
a, b = map(int, f.readline().split())
f1 = open('output.txt', 'w')
f1.write(str(a + b**2))