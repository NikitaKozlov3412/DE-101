# Класс object. Строковое представление объекта

class Person:
    def __init__(self, name, age):
        self.name = name  # устанавливаем имя
        self.age = age  # устанавливаем возраст
 
    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")
 
 
tom = Person("Tom", 23)
print(tom) #<__main__.Person object at 0x000000000B2503D0>

print("\n")

#  определим в классе Person метод __str__() 

class Person:
    def __init__(self, name, age):
        self.name = name  # устанавливаем имя
        self.age = age  # устанавливаем возраст
 
    def display_info(self):
        print(self)
        #print(self.__str__())     # или так
 
    def __str__(self):
        return f"Name: {self.name}  Age: {self.age}"
    
    def abc(self):
        print(self.__str__())
 
 
tom = Person("Tom", 23)
print(tom)      # Name: Tom  Age: 23
tom.display_info()  # Name: Tom  Age: 23
tom.abc()

print("\n")

