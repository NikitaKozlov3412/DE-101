# Копирование и объединение словарей

# Метод copy() копирует содержимое словаря, возвращая новый словарь:

users = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
students = users.copy()
print(students)     # {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}

print("\n")

# Метод update() объединяет два словаря:
    
users = {"+1111111": "Tom", "+3333333": "Bob"}
 
users2 = {"+2222222": "Sam", "+6666666": "Kate"}
users.update(users2)
 
print(users)    # {"+1111111": "Tom", "+3333333": "Bob", "+2222222": "Sam", "+6666666": "Kate"}
print(users2)   # {"+2222222": "Sam", "+6666666": "Kate"}

print("\n")

# Объединение двух словарей в какой-то третий:
    
users3 = users.copy()
users3.update(users2)

print(users3)

print("\n")


# Перебор словаря

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users:
    print(f"Phone: {key}  User: {users[key]} ")
    
print("\n")

# Метод items() для перебора элементов словаря:
    
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key, value in users.items():
    print(f"Phone: {key}  User: {value} ")
    
print("\n")

# Для перебора ключей мы можем вызвать у словаря метод keys():
    
for key in users.keys():
    print(key)

print("\n")

# Для перебора только значений мы можем вызвать у словаря метод values():
    
for value in users.values():
    print(value)
    
print("\n")


# Комплексные словари

# Кроме простейших объектов типа чисел и строк словари также могут 
# хранить и более сложные объекты - те же списки, кортежи или другие словари:
    
users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}

# Для обращения к элементам вложенного словаря соответственно необходимо 
# использовать два ключа:
    
old_email = users["Tom"]["email"]
users["Tom"]["email"] = "supertom@gmail.com"
print(users["Tom"])     # { phone": "+971478745", "email": "supertom@gmail.com }

print("\n")

'''
# если мы попробуем получить значение по ключу, который отсутствует 
# в словаре, Python сгенерирует исключение KeyError:
    
tom_skype = users["Tom"]["skype"]   # KeyError

'''

# Чтобы избежать ошибки, можно проверять наличие ключа в словаре:
    
key = "skype"
if key in users["Tom"]:
    print(users["Tom"]["skype"])
else:
    print("skype is not found")
    
print("\n")

# Либо в качестве альтернативы можно использовать метод get():
    
users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    }
}
 
tom_skype = users["Tom"].get("skype", "Undefined")
print(tom_skype)    # Undefined

print("\n")

