parts = input().split()
numbers = []
for p in parts:
    numbers.append(int(p))
biggest = numbers[0]
smallest = numbers[0]
for x in numbers:
    if x > biggest:
        biggest = x
    if x < smallest:
        smallest = x
print("Максимум:", biggest)
print("Минимум:", smallest)