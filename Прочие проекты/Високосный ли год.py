# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 14:09:27 2024

@author: Администратор
"""

god = int(input("Введите год: " ))
print(god)
if (god % 4 == 0) and (god % 100 == 0) and (god % 400 != 0):
    print("Год не високосный")
elif (god % 4 == 0) and (god % 100 == 0) and (god % 400 == 0):
    print("Год високосный")
elif (god % 4 == 0):
    print("Год високосный")
else:
    print("Год не високосный")

# Исправленный вариант

god = int(input("Введите год: "))
if (god % 400 == 0) or (god % 4 == 0 and god % 100 != 0):
    print("Год високосный")
else:
    print("Год не високосный")
    
