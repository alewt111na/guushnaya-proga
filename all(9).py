parts = input().split()
x = int(input())
result = []
for p in parts:
    if int(p) != x:
        result.append(p)
print(" ".join(result))