def task_18(op, a, b):
    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    if op not in ops:
        return None
    if op == "/" and b == 0:
        return None
    return ops[op](a, b)