parts = input().split()
result = []
for p in parts:
    if int(p) not in result:
        result.append(int(p))
print(" ".join(str(x) for x in result))