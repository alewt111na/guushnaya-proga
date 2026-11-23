def task_06(name):
    words = name.split()
    result = []
    for w in words:
        result.append(w.capitalize())
    return " ".join(result)