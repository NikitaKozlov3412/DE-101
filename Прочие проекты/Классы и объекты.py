# Классы и объекты


class Person:
    # конструктор
    def __init__(self):
        print("Создание объекта Person")
 
tom = Person()      # Создание объекта Person

print("\n")

# Атрибуты объекта

class Person:
 
    def __init__(self, name, age):
        self.name = name    # имя человека
        self.age = age        # возраст человека
 
 
tom = Person("Tom", 22)
 
# обращение к атрибутам
# получение значений
print(tom.name)     # Tom
print(tom.age)      # 22
# изменение значения
tom.age = 37
print(tom.age)      # 37

print("\n")

'''
В принципе нам необязательно определять атрибуты внутри класса - Python 
позволяет сделать это динамически вне кода:

'''

class Person:
 
    def __init__(self, name, age):
        self.name = name        # имя человека
        self.age = age          # возраст человека
 
 
tom = Person("Tom", 22)
 
tom.company = "Microsoft"
print(tom.company)  # Microsoft


print("\n")

# Методы классов

class Person:       # определение класса Person
    def say(self, message):     # метод 
        print(message)
 
tom = Person()
tom.say("Hello METANIT.COM")    # Hello METANIT.COM


print("\n")


class Person:
 
    def __init__(self, name, age):
        self.name = name        # имя человека
        self.age = age          # возраст человека
     
    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")
 
 
tom = Person("Tom", 22)
tom.display_info()      # Name: Tom  Age: 22
 
bob = Person("Bob", 43)
bob.display_info()      # Name: Bob  Age: 43

print("\n")


# Деструкторы

class Person:
  
    def __init__(self, name):
        self.name = name
        print("Создан человек с именем", self.name)
     
    def __del__(self):
        print("Удален человек с именем", self.name)
  
tom = Person("Tom")
#Должно быть сообщение "Удален человек с именем Tom", но оно
#не выводится. Непонятно...

print("\n")


class Person:
  
    def __init__(self, name):
        self.name = name
        print("Создан человек с именем", self.name)
     
    def __del__(self):
        print("Удален человек с именем", self.name)
  
 
def create_person():
    tom = Person("Tom")
     
create_person()
print("Конец программы")
#Здесь всё правильно выводится

print("\n")


# Упражнение 1

class Rectangle:
    
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
             
        return self.width * self.length
    
    def perimeter(self):
        
        return 2*(self.width + self.length)
    
a = Rectangle(4, 9)
print(f"Площадь: {a.area()}")
print(f"Периметр: {a.perimeter()}")

b = Rectangle(12, 7)
print(f"Площадь: {b.area()}")
print(f"Периметр: {b.perimeter()}")

print("\n")
