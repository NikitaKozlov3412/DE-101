# Математические функции и модуль math

# Пример применения некоторых функций:
    
import math
 
# возведение числа 2 в степень 3
n1 = math.pow(2, 3)
print(n1)  # 8
 
# ту же самую операцию можно выполнить так
n2 = 2**3
print(n2)
 
# квадратный корень числа
print(math.sqrt(9))  # 3
 
# ближайшее наибольшее целое число
print(math.ceil(4.56))  # 5
 
# ближайшее наименьшее целое число
print(math.floor(4.56))  # 4
 
# перевод из радиан в градусы
print(math.degrees(3.1415926))  # 180
 
# перевод из градусов в радианы
print(math.radians(180))   # 3.1415.....
# косинус
print(math.cos(math.radians(60)))  # 0.5
# cинус
print(math.sin(math.radians(90)))   # 1.0
# тангенс
print(math.tan(math.radians(0)))    # 0.0
 
print(math.log(8,2))    # 3.0
print(math.log10(100))    # 2.0

print("\n")

# Также модуль math предоставляет ряд встроенных констант, такие как PI и E:
    
import math
radius = 30
# площадь круга с радиусом 30
area = math.pi * math.pow(radius, 2)
print(area)
 
# натуральный логарифм числа 10
number = math.log(10, math.e)
print(number)

print("\n")

# Дополнительные математические функции
# Они не входжят в модуль math
# найдем "расстояние" между двумя числами 
# (абсолютную разность без учета знака):

num1 = 3
num2 = 8
diff = abs(num1-num2)  # 5
print(diff)   # 5

print("\n")

# Или найдем минимальное и максимальное число в списке:
    
numbers = [54, 23, 1, 4, 657, 2, -3, 56, 24]
 
min_number = min(numbers)  # -3
max_number = max(numbers)  # 657
print("min:", min_number) 
print("max:", max_number) 

print("\n")

