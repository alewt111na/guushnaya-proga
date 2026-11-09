parts = input().split()
total = 0
count = 0
for p in parts:
    total += int(p)
    count += 1
print("Сумма:", total)
print("Количество:", count)