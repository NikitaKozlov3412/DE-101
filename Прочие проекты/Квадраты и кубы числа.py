# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:56:39 2025

@author: Администратор
"""

sp1 = []
sp2 = sp1.copy()
sp3 = sp2.copy()

for i in range(10):
    sp1.append(i+1)
    
print("numbers: ", sp1)



for i in range(10):
    sp2.append((i+1)**2)
    
print("squares: ", sp2)


for i in range(10):
    sp3.append((i+1)**3)
    
print("cubes: ", sp3)
