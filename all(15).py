def task_16(password):
    has_upper = False
    has_digit = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.isdigit():
            has_digit = True
    return len(password) >= 8 and has_upper and has_digit