parts = input().split()
k = int(input())
count = 0
for p in parts:
    if int(p) > k:
        count += 1
print(count)