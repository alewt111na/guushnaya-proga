
price = float(input())
count = int(input())
sale = int(input())

if sale > 100 or sale < 0: print("нормально скидку введи, гений")

print("Стоимость: ", price * count)
print("Скидка: ", count * sale / 100)
print("К оплате: ", (price * count) - (count * sale / 100))