# Множества

#Во множестве все элементы уникальны

users = {"Tom", "Bob", "Alice", "Tom"}
print(users)    # {'Bob', 'Tom', 'Alice'}

print("\n")

'''
Также для определения множества может применяться функция set(), в 
которую передается список или кортеж элементов:
'''

people = ["Mike", "Bill", "Ted"]
users = set(people)
print(users)    # {"Mike", "Bill", "Ted"}

print("\n")

# Пустое множество:
    
users = set()


# Длина множества 

users = {"Tom", "Bob", "Alice"}
print(len(users))       # 3

print("\n")

# Добавление элементов

# Метод add() (добавляет одиночный элемент):

users = set()
users.add("Sam")
print(users)

print("\n")

# Удаление элементов

# remove() удаляет один элемент.
# Нужна проверка на наличие элемента:
    
users = {"Tom", "Bob", "Alice"}
 
user = "Tom"
if user in users: 
    users.remove(user)
print(users)    # {"Bob", "Alice"}

print("\n")

# метод discard() не генерирует исключения
# при отсутствии элемента:
    
users = {"Tom", "Bob", "Alice"}
 
users.discard("Tim")    # элемент "Tim" отсутствует, и метод ничего не делает
print(users)    #  {"Tom", "Bob", "Alice"}
 
users.discard("Tom")    # элемент "Tom" есть, и метод удаляет элемент
print(users)    #  {"Bob", "Alice"}

print("\n")

# метод clear() удаляет все элементы:
    
users.clear()


# Перебор множества (удобен цикл for):
    
users = {"Alice", "Bob", "Tom"}
 
for user in users:
    print(user)
    
print("\n")

# Дополнительно:
# Если порядок важен, но нужно всё же множество,
# то нужно сделать вот так:
from collections import OrderedDict

users = OrderedDict.fromkeys(["Alice", "Bob", "Tom"])

for user in users:
    print(user)
    
print("\n")

