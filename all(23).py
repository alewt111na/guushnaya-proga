def task_24(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total