# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:43:31 2025

@author: Администратор
"""

# Вопрос 1

# Что выведет на консоль следующая программа:
print({key: value for key, value in enumerate("abcd")})

print("\n")

# Вопрос 2

# Что выведет на консоль следующая программа:
    
data = {1:"one", 2:"two", 3:"three"}
for key in data:
    print(key, data[key], end=",")

print("\n")

# Вопрос 3

# Что выведет на консоль следующая программа:
    
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict.keys())

print("\n")

# Упражнение 1

'''
Создайте словарь, который хранит информацию о человеке. Допустим, 
человека зовут "Том", ему 39 лет, он работает в компание SuperCorp и 
в работе использует языки программирования Python и JavaScript. 
Сохраните всю эту информацию в словаре. Затем выведите эту информацию 
из словаря на консоль
'''

person = {
    "name": "Tom",
    "age": 39,
    "company": "SuperCorp",
    "languages": ["Python", "JavaScript"]
    }

print(person)

print("Name: ", person["name"])
print("Age: ", person.get("age"))
print("Company: ", person["company"])
print("Languages: ", person["languages"])


print("\n")


# Упражнение 2

'''
Пусть дан следующий список, которые хранит несколько словарей (будет ниже):
    
Каждый словарь в списке представляет программиста, где поле "name" 
представляет имя, а поле "languages" - список используемых языков 
программирования. Выведите на консоль из каждого словаря имя и 
последний язык программирования, чтобы получился следуюший консольный вывод:
    
Name:  Tom
Last language:  JavaScript
Name:  Bob
Last language:  C#
Name:  Sam
Last language:  Java
'''

people = [
    {"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]},
    {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
    {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "Java"]}
]

for vocs in people:
    print("Name: ", vocs["name"])
    print("Last language: ", vocs["languages"][-1])
    
print("\n")

