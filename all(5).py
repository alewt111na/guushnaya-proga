target = 42

while True:
    x = int(input())
    if x == target:
        print("угадал")
        break
    elif x < TARGET:
        print("больше")
    else:
        print("меньше")