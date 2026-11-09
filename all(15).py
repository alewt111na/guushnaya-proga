n = int(input())
m = int(input())
matrix = []
for i in range(n):
    parts = input().split()
    row = []
    for p in parts:
        row.append(p)
    matrix.append(row)
for j in range(m):
    line = []
    for i in range(n):
        line.append(matrix[i][j])
    print(" ".join(line))