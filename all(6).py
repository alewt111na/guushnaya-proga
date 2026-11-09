VOWELS = "аеёиоуыэюя"

s = input().lower()
count = 0
for ch in s:
    if ch in VOWELS:
        count += 1
print(count)