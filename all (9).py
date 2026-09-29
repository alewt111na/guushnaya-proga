import math

a = int(input())
b = int(input())
c = int(input())

D = b**2 - 4*a*c

if D < 0: 
    print ("нет корней")
elif D == 0:
    print ("Один корень: ", round((-b + math.sqrt(D)) / (2 * a), 3)
else: 
    print ("Два корня: ", round((-b + math.sqrt(D)) / (2 * a), 3), round((-b - math.sqrt(D)) / (2 * a), 3)