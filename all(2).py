n = int(input())

best = int(input())          # первое число пока считаем лучшим
for _ in range(n - 1):       # остальные n - 1 чисел
    x = int(input())
    if x > best:
        best = x

print(best)