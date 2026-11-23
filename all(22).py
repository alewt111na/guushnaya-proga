def task_23(text):
    clean = ""
    for ch in text.lower():
        if ch.isalnum():
            clean += ch
    return clean == clean[::-1]