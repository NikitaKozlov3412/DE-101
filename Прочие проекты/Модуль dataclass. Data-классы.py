# Модуль dataclass. Data-классы
# Они позволяют сократить шаблонный код классов


# Рассмотрим простейший пример:
    
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
tom = Person("Tom", 38)
print(f"Name: {tom.name}  Age: {tom.age}")      # Name: Tom  Age: 38

print("\n")

# Теперь изменим эту программу, сделав класс Person data-классом:
    
from dataclasses import dataclass
 
@dataclass
class Person:
    name: str
    age: int
 
tom = Person("Tom", 38)
print(f"Name: {tom.name}  Age: {tom.age}")      # Name: Tom  Age: 38

print("\n")

# Здесь задействован не весь функционал
# В реальности data-класс будет аналогичен следующему:

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r}"
     
    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.name, self.age) == (other.name, other.age)
        return NotImplemented
'''    

# Применение функций __repr__ и __eq__:
    
from dataclasses import dataclass
 
@dataclass
class Person:
    name: str
    age: int
 
 
tom = Person("Tom", 38)
bob = Person("Bob", 42)
tomas = Person("Tom", 38) 
print(tom == tomas)     # True
print(tom == bob)       # False
print(tom)              # Person(name="Tom", age=38)

print("\n")

# Параметры декоратора dataclass

# unsafe_hash: если равно True, то генерируется функция __hash__(), 
# которая возвращает хеш объекта. По умолчанию равно False 
# order: если равно True, то генерируются функции __lt__ (операция <), 
#__le__ (<=), __gt__ (>), __ge__ (>=), которые применяются для упорядочивания 
# объектов. По умолчанию равно False

from dataclasses import dataclass
 
@dataclass(unsafe_hash=True, order=True)
class Person:
    name: str
    age: int
    def __repr__(self):
        return f"Person. Name: {self.name}  Age: {self.age}"
 
 
tom = Person("Tom", 38)
print(tom.__hash__())   # -421667297069596717
print(tom)              # Person. Name: Tom  Age: 38

print("\n")

# При необходимости атрибутам можно присвоить значения по умолчанию, 
# если в конструкторе им не передаются значения:
    
from dataclasses import dataclass
 
@dataclass
class Person:
    name: str
    age: int = 18
 
 
tom = Person("Tom", 38)
print(tom)              # Person(name="Tom", age=38)
 
bob = Person("Bob")
print(bob)              # Person(name="Bob", age=18)

print("\n")

'''
Хотя data-классы предназначены прежде всего для хранения различных данных, 
но также в них можно определять поведение с помощью дополнительных функций:
'''

from dataclasses import dataclass
 
@dataclass
class Person:
    name: str
    age: int
 
    def say_hello(self):
        print(f"{self.name} says hello")
 
 
tom = Person("Tom", 38)
tom.say_hello()     # Tom says hello

print("\n")