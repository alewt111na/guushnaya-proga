k = int(input())
s = input()
result = ""
for ch in s:
    if ch == " ":
        result += " "
    else:
        result += chr((ord(ch) - ord("a") + k) % 26 + ord("a"))
print(result)