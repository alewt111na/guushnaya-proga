parts = input().split()
numbers = []
for p in parts:
    numbers.append(int(p))
best = 0
for i in range(len(numbers)):
    if numbers[i] > numbers[best]:
        best = i
print(best)