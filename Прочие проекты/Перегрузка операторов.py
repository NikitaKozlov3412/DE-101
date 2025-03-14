# Перегрузка операторов

class Counter:
    def __init__(self, value):
        self.value = value
    # переопределение оператора сложения
    def __add__(self, other):
        return Counter(self.value + other.value)
     
counter1 = Counter(5)
counter2 = Counter(15)
counter3 = counter1 + counter2
print(counter3.value)       # 20

'''
Что, если мы хотим складывать Counter не с другим объектом Counter, 
а с числом. Тогда мы могли определить следующий оператор:
'''

print("\n")

class Counter:
    def __init__(self, value):
        self.value = value
         
    def __add__(self, other):
        return Counter(self.value + other)
     
counter1 = Counter(5)
counter3 = counter1 + 6
print(counter3.value)       # 11

print("\n")

'''
Возвращаемый тип ряда операторов также жестко не определен. 
Например, мы могли бы возвращить также обычное число:
'''

class Counter:
    def __init__(self, value):
        self.value = value
         
    def __add__(self, other):
        return self.value + other
     
counter1 = Counter(5)
result = counter1 + 7
print(result)       # 12

print("\n")


# Истинность объекта

class Counter:
    def __init__(self, value):
        self.value = value
    def __bool__(self):
        return self.value > 0
     
def test(counter):
    if counter: print("Counter = True")
    else: print("Counter = False")
     
counter1 = Counter(3)
test(counter1)              # Counter = True
 
counter2 = Counter(-3)
test(counter2)              # Counter = False

print("\n")

'''
Мы могли бы использовать объект Counter в цикле while в качестве условия:
'''

class Counter:
    def __init__(self, value):
        self.value = value
    def __bool__(self):
        return self.value > 0
     
counter1 = Counter(3)
 
while(counter1):
    print("Counter1: ", counter1.value)
    counter1.value -=1
    
print("\n")

# Операторы, которые возвращают значение bool

class Counter:
    def __init__(self, value):
        self.value = value
         
    def __gt__(self, other):
        return self.value > other.value
    def __lt__(self, other):
        return self.value < other.value
 
     
counter1 = Counter(1)
counter2 = Counter(2)
     
if counter1 > counter2: 
    print("counter1 больше чем counter2")
elif counter1 < counter2:
    print("counter1 меньше чем counter2")
else: 
    print("counter1 и counter2 равны")
    
print("\n")

# Операции обращения по индексу

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
         
    def __getitem__(self, prop):
        if prop == "name": return self.__name
        elif prop == "age": return self.__age
        return None
     
tom = Person("Tom", 39)
 
print("Name:", tom["name"])     # Name: Tom
print("Age:", tom["age"])       # Age: 39
print("Id:", tom["id"])         # Id: None

print("\n")

# Проверка наличия свойства

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
         
    def __contains__(self, prop):
        if prop == "name" or prop == "age": return True
        return False
     
tom = Person("Tom", 39)
print("name" in tom)        # True
print("id" in tom)          # False

print("\n")

# Реализация операторов парами

class Counter:
    def __init__(self, value):
        self.value = value
     
    def __eq__(self, other): return self.value == other.value
    def __ne__(self, other): return not (self == other)
     
    def __gt__(self, other): return self.value > other.value
    def __le__(self, other): return not (self > other)
     
    def __lt__(self, other): return self.value < other.value
    def __ge__(self, other): return not (self < other)
         
c1 = Counter(1)
c2 = Counter(2)
 
print(c1 == c2)     # False
print(c1 != c2)     # True
 
print(c1 < c2)      # True
print(c1 >= c2)     # False

print("\n")

#Задача на сложение векторов

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, b):
        return Vector(self.x+b.x, self.y+b.y)
    
    def __sub__(self, b):
        return Vector(self.x-b.x, self.y-b.y)
    
a = Vector(5,3)
b = Vector(8,4)
c = a+b
d = a-b
print(f"x={c.x}, y={c.y}")
print(f"x={d.x}, y={d.y}")
