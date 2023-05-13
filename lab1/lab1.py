import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

disct = b * b - 4 * a * c

if disct > 0:
    x1 = (-b + math.sqrt(disct)) / (2 * a)
    x2 = (-b - math.sqrt(disct)) / (2 * a)
    print("x1=%.2f \nx2=%.2f" % (x1, x2))
elif disct == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
