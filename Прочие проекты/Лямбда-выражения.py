# Лямбда-выражения

message = lambda: print("hello")
 
message()   # hello

print("\n")


#Квадрат числа

square = lambda n: n * n
 
print(square(4))    # 16
print(square(5))    # 25

print("\n")

#Сумма двух чисел (функция принимает два параметра)

sum = lambda a, b: a + b
 
print(sum(4, 5))    # 9
print(sum(5, 6))    # 11

print("\n")


# передача лямбда-выражения в качестве параметра

def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
 
do_operation(5, 4, lambda a, b: a + b)  # result = 9
do_operation(5, 4, lambda a, b: a * b)  # result = 20
do_operation(5, 4, lambda a, b: a // b) # Это я сам дописал

print("\n")


# возвращение лямбда-выражений из функций

def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    elif choice == 4:
        return lambda a, b: a // b  # Это я дописал сам
    else:
        return lambda a, b: a * b
 
 
operation = select_operation(1)  # operation = sum
print(operation(10, 6))  # 16
 
operation = select_operation(2)  # operation = subtract
print(operation(10, 6))  # 4
 
operation = select_operation(3)  # operation = multiply
print(operation(10, 6))  # 60

operation = select_operation(4)  # Это я дописал сам (деление с остатком)
print(operation(10, 6))  # 4


print("\n")
