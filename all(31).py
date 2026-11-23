def task_32(text):
    try:
        return int(text)
    except ValueError:
        return None