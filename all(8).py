n = int(input())

is_prime = True              # сначала считаем, что простое
for d in range(2, n):
    if n % d == 0:           # нашёлся делитель
        is_prime = False
        break                # дальше искать незачем

print(is_prime)