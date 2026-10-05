n = int(input())

a = int(input())
b = int(input())
if a > b:
    first, second = a, b
else:
    first, second = b, a

for _ in range(n - 2):       # два числа уже прочитаны
    x = int(input())
    if x > first:
        second = first       # старый лидер становится вторым
        first = x
    elif x > second:
        second = x

print(second)