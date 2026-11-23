def task_35(items, index):
    try:
        return items[index]
    except IndexError:
        return "индекс вне диапазона"