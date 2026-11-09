n = int(input())
squares = []
for i in range(n):
    x = int(input())
    squares.append(str(x * x))
print(" ".join(squares))