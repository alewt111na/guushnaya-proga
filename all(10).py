parts = input().split()
a = []
for p in parts:
    a.append(int(p))
a = sorted(a)
n = len(a)
if n % 2 == 1:
    print(a[n // 2])
else:
    print(round((a[n // 2 - 1] + a[n // 2]) / 2, 2))