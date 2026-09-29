weight = float(input())
height = float(input())

height = height / 100
bmi = (weight / height ** 2)

if bmi < 18.5: print ("недостаточный")
elif bmi >= 18.5 and bmi <= 25: print ("норма")
elif bmi >= 25 and bmi <= 30: print ("избыточный")
else: print("ожирение")