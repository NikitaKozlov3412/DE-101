# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 14:42:37 2024

@author: Администратор
"""

# Возвращение результата

def get_message():
    return "Hello METANIT.COM"
 
 
message = get_message()  # получаем результат функции get_message в переменную message
print(message)          # Hello METANIT.COM
 
# можно напрямую передать результат функции get_message
print(get_message())    # Hello METANIT.COM

print("\n")

# Удвоение

def double(number):
    return 2 * number
 
result1 = double(4)     # result1 = 8
result2 = double(5)     # result2 = 10
print(f"result1 = {result1}")   # result1 = 8
print(f"result2 = {result2}")   # result2 = 10

print("\n")

# Получение суммы чисел

def sum(a, b):
    return a + b
 
 
result = sum(4, 6)                  # result = 0
print(f"sum(4, 6) = {result}")      # sum(4, 6) = 10
print(f"sum(3, 5) = {sum(3, 5)}")   # sum(3, 5) = 8

print("\n")


# Выход из функции

'''
Оператор return не только возвращает значение, но и производит выход из 
функции. Поэтому он должен определяться после остальных инструкций. 
Например:
'''

def get_message():
    return "Hello METANIT.COM"
    print("End of the function")
 
print(get_message())

print("\n")

# Однако мы можем использовать оператор return и в таких функциях, 
# которые не возвращают никакого значения

def print_person(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return
    print(f"Name: {name}  Age: {age}")
 
 
print_person("Tom", 22)
print_person("Bob", -102)

print("\n")