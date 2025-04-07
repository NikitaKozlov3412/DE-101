# Упаковка и распаковка в параметрах функций

# *args

# Оператор * позволяет передать в функцию несколько значений, 
# и все они будут упакованы в кортеж:
    
def fun(*args):
    # обращаемся к первому элементу кортежа
    print(args[0])
  
    # выводим весь кортеж
    print(args)
  
fun("Python", "C++", "Java", "C#")

print("\n")

# мы можем передавать в функцию переменное количество значений:
    
def sum(*args):
    result = 0
    for arg in args: 
        result += arg
    return result
  
print(sum(1, 2, 3))         # 6
print(sum(1, 2, 3, 4))      # 10
print(sum(1, 2, 3, 4, 5))   # 15

print("\n")

# Оператор **

# Оператор ** упаковывает аргументы, переданные по имени, в словарь. 
# Имена параметров служат ключами.

def fun(**kwargs):
    print(kwargs)   # выводим словарь на консоль
  
fun(name="Tom", age="38", company="Google")
fun(language="Python", version="3.11")

print("\n")

'''
Поскольку аргументы передаются в функцию в виде словаря, 
то внутри функции через ключи мы можем получить их значения:
'''

def fun(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
  
fun(name="Tom", age="38", company="Google")

print("\n")

# Распаковка аргументов

# Оператор * и распаковка

'''
def sum(*args):
  result = 0
  for arg in args:
    result += arg
  return result
  
numbers = (1, 2, 3, 4, 5)
print(sum(numbers))

В данном случае кортеж numbers передается как элемент кортежа *args.
Поэтому ошибка TypeError. 

'''

# чтобы элементы кортежа были переданы в кортеж *args как отдельные 
# значения, необходимо выполнить их распаковку:
    
def sum(*args):
  result = 0
  for arg in args:
    result += arg
  return result
  
numbers = (1, 2, 3, 4, 5)
# применяем распаковку - *numbers
print(sum(*numbers))     # 15

print("\n")

# функция принимает несколько параметров, а мы передаем один кортеж 
# или список:

def print_person(name, age, company):
  print(f"Name:{name}, Age: {age}, Company: {company}")
  
person =("Tom", 38, "Google")
# выполняем распаковку кортежа person
print_person(*person)   # Name:Tom, Age: 38, Company: Google

print("\n")

# Оператор ** и распаковка

# Оператор ** применяется для распаковки словарей:
    
def print_person(name, age, company):
  print(f"Name:{name}, Age: {age}, Company: {company}")
  
tom ={"name":"Tom", "age":38, "company":"Google"}
# выполняем распаковку словаря tom
print_person(**tom) # Name:Tom, Age: 38, Company: Google

print("\n")

# Сочетание параметров
# Параметры *args и *kwargs могут использоваться в функции 
# вместе с другими параметрами. Например:

def sum(num1, num2, *nums):
    result=num1+num2
    for n in nums:
        result += n
    return result
 
print(sum(1,2,3))       # 6
print(sum(1,2,3,4,7))     # 17

print("\n")