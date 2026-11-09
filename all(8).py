parts = input().split()
a = []
for p in parts:
    a.append(int(p))
print(round(sum(a) / len(a), 2))