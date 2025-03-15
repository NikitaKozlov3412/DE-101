# Абстрактные классы и методы

import abc
class Shape(abc.ABC):
    @abc.abstractmethod 
    def area (self): pass       # площадь фигуры
    

print("\n")


'''
Стоит отметить, что мы не можем напрямую создать объект абстрактного класса
 с абстрактными методами, используя его конструктор:
'''

'''
import abc
class Shape(abc.ABC):
    @abc.abstractmethod 
    def area (self): pass       # площадь фигуры
 
shape = Shape()     # ! Ошибка - так нельзя
print(shape)

print("\n")

'''

'''
Классы-наследники должны реализовать все абстрактные методы 
абстрактного класса. Например, определим класс прямоугольника:
'''

import abc
class Shape(abc.ABC):
    @abc.abstractmethod 
    def area (self): pass       # площадь фигуры
 
# класс прямоугольника 
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area (self): return self.width * self.height
     
rect = Rectangle(30, 50)
print("Rectangle area:", rect.area())   # Rectangle area: 1500 

print("\n")

# Подобным образом можно определить и другие типы фигур. Например, 
# добавим класс круга:
    
import abc
class Shape(abc.ABC):
    @abc.abstractmethod 
    def area (self): pass       # площадь фигуры
 
# класс прямоугольника 
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area (self): return self.width * self.height
     
# класс круга 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area (self): return self.radius * self.radius * 3.14
     
 
def print_area(shape):
    print("Area:", shape.area())
     
 
rect = Rectangle(30, 50)
circle = Circle(30)
print_area(rect)        # Area: 1500
print_area(circle)      # Area: 2826.0

print("\n")
  
'''
При этом абстрактные классы также могут определять конструктор, 
атрибуты, неабстрактные методы, которые также могут применяться 
в классах-наследниках:
'''

import abc
class Shape(abc.ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y 
         
    @abc.abstractmethod     
    def area (self): pass       # абстрактны метод
     
    def print_point(self):          # неабстрактный метод
        print("X:", self.x, "\tY:", self.y)
 
# класс прямоугольника 
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
    def area (self): return self.width * self.height
     
def print_area(shape):                   #Это я дописал
    print("Area:", shape.area())         #Это я дописал


rect = Rectangle(10, 20, 100, 100)
rect.print_point()      # X: 10   Y: 20
print_area(rect)  #Это я дописал

print("\n")