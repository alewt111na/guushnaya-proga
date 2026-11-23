def task_30(numbers, stop_value):
    total = 0
    for x in numbers:
        if x == stop_value:
            break
        total += x
    return total