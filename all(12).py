parts = input().split()
a = []
for p in parts:
    a.append(int(p))
found = False
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        found = True
print(found)