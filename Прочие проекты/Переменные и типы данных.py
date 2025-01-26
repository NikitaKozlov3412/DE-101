# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:59:10 2024

@author: Администратор
"""

# Переменные и типы данных

a = 0o7
b = 0o11
c = 0o17
print(a)    # 7 в десятичной системе
print(b)    # 9 в десятичной системе
print(c)    # 15 в десятичной системе


a = 0b11
b = 0b1011
c = 0b100001
print(a)    # 3 в десятичной системе
print(b)    # 11 в десятичной системе
print(c)    # 33 в десятичной системе


a = 0x0A
b = 0xFF
c = 0xA1
print(a)    # 10 в десятичной системе
print(b)    # 255 в десятичной системе
print(c)    # 161 в десятичной системе


x = 3.9e3
print(x)  # 3900.0
 
x = 3.9e-3
print(x)  # 0.0039

complexNumber = 1+2j
print(complexNumber)   # (1+2j)

text = ("Laudate omnes gentes laudate "
        "Magnificat in secula ")
print(text)

userName = "Tom"
userAge = 37
user = f"name: {userName}  age: {userAge}"
print(user)   # name: Tom  age: 37


userId = "abc"      # тип str
print(type(userId)) # <class 'str'>
 
userId = 234        # тип int
print(type(userId)) # <class 'int'>