
# Копирование множества:
    
users = {"Tom", "Bob", "Alice"}
students = users.copy()
print(students)     # {"Tom", "Bob", "Alice"}

print("\n")

# Объединение множеств

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
users3 = users.union(users2)
print(users3)   # {"Bob", "Alice", "Sam", "Kate", "Tom"}

#Объединить можно ещё так:

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
print(users | users2)   # {"Bob", "Alice", "Sam", "Kate", "Tom"}

print("\n")

#Пересечение множеств

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
users3 = users.intersection(users2)
print(users3)   # {"Bob"}

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
print(users & users2)   # {"Bob"}

print("\n")

# intersection_update() заменяет пересечёнными элементами
# первое множество:
    
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
users.intersection_update(users2)
print(users)   # {"Bob"}

print("\n")

# Разность множеств

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
users3 = users.difference(users2)
print(users3)           # {"Tom", "Alice"}
print(users - users2)   # {"Tom", "Alice"}

print("\n")

# Симметрическая разность
# Возвращает все элементы обоих множеств за исключением общих:
    
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
users3 = users.symmetric_difference(users2)
print(users3)   # {"Tom", "Alice", "Sam", "Kate"}
 
users4 = users ^ users2
print(users4)   # {"Tom", "Alice", "Sam", "Kate"}

print("\n")

# Отношения между множествами

# Метод issubset позволяет выяснить, является ли текущее множество 
# подмножеством (то есть частью) другого множества:

users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
 
print(users.issubset(superusers))   # True
print(superusers.issubset(users))   # False


# Метод issuperset, наоборот, возвращает True, если текущее множество 
# является надмножеством (то есть содержит) для другого множества:
    
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
 
print(users.issuperset(superusers))   # False
print(superusers.issuperset(users))   # True

print("\n")

# frozen set
# В такое множество нельзя 
# ни добавить элементы, ни удалить уже имеющиеся
# frozen set поддерживает ограниченный набор операций

users = frozenset({"Tom", "Bob", "Alice"})

print(len(users))