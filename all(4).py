n = int(input())

result = 0
while n > 0:
    digit = n % 10               # последняя цифра
    result = result * 10 + digit # приписываем её справа к результату
    n = n // 10                  # отрезаем последнюю цифру

print(result)