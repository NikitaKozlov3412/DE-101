# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:41:46 2025

@author: Администратор
"""

# Определим словарь:
    
users = {1: "Tom", 2: "Bob", 3: "Bill"}

# Ещё пример:
    
emails = {"tom@gmail.com": "Tom", "bob@gmai.com": "Bob", "sam@gmail.com": "Sam"}

# необязательно ключи и строки должны быть однотипными

objects = {1: "Tom", "2": True, 3: 100.6}

# пустой словарь

objects = {}

# можно пустой словарь задать так:

objects = dict()

# Преобразование списков и кортежей в словарь
#Список

users_list = [
    ["+111123455", "Tom"],
    ["+384767557", "Bob"],
    ["+958758767", "Alice"]
]
users_dict = dict(users_list)
print(users_dict)      # {"+111123455": "Tom", "+384767557": "Bob", "+958758767": "Alice"}

print("\n")

#Кортеж

users_tuple = (
    ("+111123455", "Tom"),
    ("+384767557", "Bob"),
    ("+958758767", "Alice")
)
users_dict = dict(users_tuple)
print(users_dict)

print("\n")

# Получение и изменение элементов

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
# получаем элемент с ключом "+11111111"
print(users["+11111111"])      # Tom
 
# установка значения элемента с ключом "+33333333"
users["+33333333"] = "Bob Smith"
print(users["+33333333"])   # Bob Smith

print("\n")

#Элемента с таким ключом нет в словаре, он добавится

users["+4444444"] = "Sam"

print(users)

#Если бы этого ключа не было в словаре,
#и мы бы хотели получить его значение, была бы ошибка KeyError

user = users["+4444444"]


print("\n")

#Проверка наличия ключа в словаре

key = "+555555"
if key in users:
    user = users[key]
    print(user)
else:
    print("Элемент не найден")
    
print("\n")

#Метод get для получения элементов словаря:

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
user1 = users.get("+55555555")
print(user1)    # Alice
user2 = users.get("+33333333", "Unknown user")
print(user2)    # Bob
user3 = users.get("+44444444", "Unknown user")
print(user3)    # Unknown user    

print("\n")


# Удаление

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
del users["+55555555"]
print(users)    # { "+11111111": "Tom", "+33333333": "Bob"}

print("\n")

# Проверка перед удалением элемента с данным ключом,
# чтобы не было ошибки KeyError

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
key = "+55555555"
if key in users:
    del users[key]
    print(f"Элемент с ключом {key} удален")
else:
    print("Элемент не найден")
    
print("\n")

# Метод pop() для удаления

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
key = "+55555555"
user = users.pop(key)
print(user)     # Alice
print(users)
 
user = users.pop("+4444444", "Unknown user")
print(user)     # Unknown user

print("\n")

# Удаление всех элементов методом clear():

users.clear()
print(users)

print("\n")