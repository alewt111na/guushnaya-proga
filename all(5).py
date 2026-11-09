parts = input().split()
evens = []
for p in parts:
    if int(p) % 2 == 0:
        evens.append(p)
print(" ".join(evens))