parts = input().split()
k = int(input())
result = parts[len(parts) - k:] + parts[:len(parts) - k]
print(" ".join(result))