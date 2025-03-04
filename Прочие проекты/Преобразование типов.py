# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:04:36 2024

@author: Администратор
"""

# Преобразование типов

a = 2       # число int
b = 2.5     # число float
c = a + b
print(c)    # 4.5


print("\n")

# int

a = "2"
b = 3
c = int(a) + b
print(c)    # 5

print("\n")


# Примеры преобразований с помощью int():

a = int(15)     # a = 15
b = int(3.7)    # b = 3
c = int("4")    # c = 4
e = int(False)    # e = 0
f = int(True)     # f = 1

print("\n")

'''
b = int("a1c")    # Ошибка
c = int("4.7")    # Ошибка

'''


# float

a = "2.7"
b = 3
c = float(a) + b
print(c) # 5.7

print("\n")

# Примеры преобразований с помощью float():

a = float(15)       # a = 15.0
b = float(3.7)      # b = 3.7
c = float("4.7")    # c = 4.7
d = float("5")      # d = 5.0
e = float(False)    # e = 0.0
f = float(True)     # f = 1.0

print("\n")


'''
d = float("abc")  # Ошибка
'''

# str

a = str(False)      # a = "False"
b = str(True)       # b = "True"
c = str(5)         # c = "5"
d = str(5.7)       # d = "5.7"

print("\n")

'''
age = 22
message = "Age: " + age     # Ошибка
print(message)
'''

age = 22
message = "Age: " + str(age)   # Age: 22
print(message)

print("\n")
