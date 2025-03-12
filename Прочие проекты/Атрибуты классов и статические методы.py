# Атрибуты класса

class Person:
     type = "Person"
     description = "Describes a person"
 
 
print(Person.type)          # Person
print(Person.description)   # Describes a person
 
Person.type = "Class Person"
print(Person.type)          # Class Person

print("\n")

'''
Для обращения к атрибутам класса мы можем использовать имя класса, 
например: Person.type, и, как и атрибуты объекта, мы можем получать 
и изменять их значения.
Подобные атрибуты являются общими для всех объектов класса:
'''

class Person:
     type = "Person"
     def __init__(self, name):
         self.name = name
 
 
tom = Person("Tom")
bob = Person("Bob")
print(tom.type)     # Person
print(bob.type)     # Person
 
# изменим атрибут класса
Person.type = "Class Person"
print(tom.type)     # Class Person
print(bob.type)     # Class Person

print("\n")

'''
Атрибуты класса могут применяться для таких ситуаций, когда нам надо 
определить некоторые общие данные для всех объектов. Например:
'''

class Person:
    default_name = "Undefined"
 
    def __init__(self, name):
        if name:
            self.name = name
        else:
            self.name = Person.default_name
 
 
tom = Person("Tom")
bob = Person("")
print(tom.name)  # Tom
print(bob.name)  # Undefined

print("\n")

# Атрибут класса

'''
Возможна ситуация, когда атрибут класса и атрибут объекта совпадает по имени.
 Если в коде для атрибута объекта не задано значение, то для него может 
 применяться значение атрибута класса:
'''

class Person:
    name = "Undefined"
 
    def print_name(self):
        print(self.name)
 
 
tom = Person()
bob = Person()
tom.print_name()    # Undefined
bob.print_name()    # Undefined
 
bob.name = "Bob"
bob.print_name()    # Bob
tom.print_name()    # Undefined

print("\n")


# Статические методы

class Person:
    __type = "Person"
 
    @staticmethod
    def print_type():
        print(Person.__type)
 
 
Person.print_type()     # Person - обращение к статическому методу через имя класса
 
tom = Person()
tom.print_type()     # Person - обращение к статическому методу через имя объекта

print("\n")

    
    