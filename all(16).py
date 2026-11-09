parts = input().split()
total = 0
result = []
for p in parts:
    total += int(p)
    result.append(str(total))
print(" ".join(result))