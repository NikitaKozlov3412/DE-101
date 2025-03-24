# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 16:53:12 2025

@author: Администратор
"""

sp = [10, 20, 10, 20, 30, 40, 60, 50]

sp2 = []

for i in sp:
    if i not in sp2:
        sp2.append(i)

sp2.sort()

print("Начальный список: ", sp)
print("После удаления дублей: ", sp2)