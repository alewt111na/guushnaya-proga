n = int(input())

original = n                 # запоминаем, потому что n будет разрушаться
reversed_n = 0
while n > 0:
    reversed_n = reversed_n * 10 + n % 10
    n = n // 10

print(original == reversed_n)