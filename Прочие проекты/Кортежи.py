# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:40:03 2025

@author: Администратор
"""
#Простой кортеж

tom = ("Tom", 23)
print(tom)     # ("Tom", 23)

print("\n")

#Кортеж без скобок

tom = "Tom", 23
print(tom)     # ("Tom", 23)

print("\n")

#Кортеж с одним элементом (нужна запятая)

tom = ("Tom",)

print("\n")

#Кортеж из другого типа (списка)

data = ["Tom", 37, "Google"]
tom = tuple(data)
print(tom)      # ("Tom", 37, "Google")

print("\n")

#Длина кортежа

tom = ("Tom", 37, "Google")
print(len(tom))     # 3

print("\n")

#Обращение к элементам кортежа

tom = ("Tom", 37, "Google", "software developer")
print(tom[0])       # Tom
print(tom[1])       # 37
print(tom[-1])      # software developer

print("\n")

#Эта запись не работает, т.к. в кортеже нельзя изменить элементы

'''
tom[1] = "Tim"
'''

# При необходимости мы можем разложить кортеж на отдельные переменные:
    
name, age, company, position = ("Tom", 37, "Google", "software developer")
print(name)         # Tom
print(age)          # 37
print(position)     # software developer
print(company)     # Google

print("\n")

# Когда функция возвращает несколько значений, фактически она возвращает кортеж:
    
def get_user():
    name = "Tom"
    age = 22
    company = "Google"
    return name, age, company
 
 
user = get_user()
print(user)     # ("Tom", 22, "Google")

print("\n")

'''
При передаче кортежа в функцию с помощью оператора * его можно 
разложить на отдельные значения, которые передаются параметрам функции:
'''

def print_person(name, age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")
 
tom = ("Tom", 22)
print_person(*tom, "Microsoft")     # Name: Tom  Age: 22  Company: Microsoft
 
bob = ("Bob", 41, "Apple")
print_person(*bob)      # Name: Bob  Age: 41  Company: Apple

print("\n")


#Перебор кортежей циклом for:
    
tom = ("Tom", 22, "Google")
for item in tom:
    print(item)
    
print("\n")

#Перебор кортежей циклом while:
    
tom = ("Tom", 25, "Google")
 
i = 0
while i < len(tom):
    print(tom[i])
    i += 1
    
print("\n")

#Проверка наличия элемента в кортеже

user = ("Tom", 22, "Google")
name = "Tom"
if name in user:
    print("Пользователя зовут Tom")
else:
    print("Пользователь имеет другое имя")
    
print("\n")

