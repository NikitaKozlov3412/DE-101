# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:00:41 2025

@author: Администратор
"""

mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# вывод всей матрицы
for i in mat:
    print(i)
    

for i in mat:
    for j in i:
        print(j, end=" ")
    print()