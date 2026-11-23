def task_22(text):
    counts = {}
    for w in text.split():
        if w not in counts:
            counts[w] = 0
        counts[w] += 1
    return counts