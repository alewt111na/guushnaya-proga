n = int(input())
m = int(input())
for i in range(n):
    parts = input().split()
    total = 0
    for p in parts:
        total += int(p)
    print(total)