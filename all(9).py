s = input()
found = False
for ch in s:
    if ch.isdigit():
        found = True
        break
print(found)