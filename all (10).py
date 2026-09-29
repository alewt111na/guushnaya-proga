import math

s = int(input())

print("Часов: ", s // 3600)
print("Минут: ", (s % 3600) // 60)
print("Секунд: ", s % 60)