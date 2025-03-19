# Список

numbers = [5] * 6   # 6 раз повторяем 5
print(numbers)      # [5, 5, 5, 5, 5, 5]
 
people = ["Tom"] * 3    # 3 раза повторяем "Tom"
print(people)           # ["Tom", "Tom", "Tom"]
 
students = ["Bob", "Sam"] * 2   # 2 раза повторяем "Bob", "Sam"
print(students)                 # ["Bob", "Sam", "Bob", "Sam"]


print("\n")


# Обращение к элементам списка

people = ["Tom", "Sam", "Bob"]
 
people[1] = "Mike"  # изменение второго элемента
print(people[1])    # Mike
print(people)       # ["Tom", "Mike", "Bob"]


print("\n")


# Сравнение списков

numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4, 5])
if numbers1 == numbers2:
    print("numbers1 equal to numbers2")
else:
    print("numbers1 is not equal to numbers2")
    
print("\n")

# Получение части списка

people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
 
slice_people1 = people[:3]   # с 0 по 3
print(slice_people1)   # ["Tom", "Bob", "Alice"]
 
slice_people2 = people[1:3]   # с 1 по 3
print(slice_people2)   # ["Bob", "Alice"]
 
slice_people3 = people[1:6:2]   # с 1 по 6 с шагом 2
print(slice_people3)   # ["Bob", "Sam", "Bill"]

print("\n")

people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
 
slice_people1 = people[:-1]   # с предпоследнего по нулевой
print(slice_people1)   # ["Tom", "Bob", "Alice", "Sam", "Tim"]
 
slice_people2 = people[-3:-1]   # с третьего с конца по предпоследний
print(slice_people2)   # [ "Sam", "Tim"]

print("\n")


# Добавление и удаление элементов

people = ["Tom", "Bob"]
 
# добавляем в конец списка
people.append("Alice")  # ["Tom", "Bob", "Alice"]
# добавляем на вторую позицию
people.insert(1, "Bill")  # ["Tom", "Bill", "Bob", "Alice"]
# добавляем набор элементов ["Mike", "Sam"]
people.extend(["Mike", "Sam"])      # ["Tom", "Bill", "Bob", "Alice", "Mike", "Sam"]
# получаем индекс элемента
index_of_tom = people.index("Tom")
print(index_of_tom)
# удаляем по этому индексу
removed_item = people.pop(index_of_tom)     # ["Bill", "Bob", "Alice", "Mike", "Sam"]
# удаляем последний элемент
last_item = people.pop()     # ["Bill", "Bob", "Alice", "Mike"]
print(last_item)
# удаляем элемент "Alice"
people.remove("Alice")      # ["Bill", "Bob", "Mike"]
print(people)       # ["Bill", "Bob", "Mike"]
# удаляем все элементы
people.clear()
print(people)       # []

print("\n")

# Проекция списка

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
         
people = [ Person("Tom", 38), Person("Kate", 31), Person("Bob", 42), 
        Person("Alice", 34),  Person("Sam", 25) ]
 
# получаем из Person строку с именем
view = map(lambda p: p.name, people)
  
for person in view:
    print(person)
    
print("\n")

