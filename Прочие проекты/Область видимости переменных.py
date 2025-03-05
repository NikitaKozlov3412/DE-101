# Область видимости переменных

# Глобальный контекст

name = "Tom"
 
 
def say_hi():
    print("Hello", name)
 
 
def say_bye():
    print("Good bye", name)
 
say_hi()
say_bye()

print("\n")


# Локальный контекст

def say_hi():
    name = "Sam"
    surname = "Johnson"
    print("Hello", name, surname)
 
 
def say_bye():
    name = "Tom"
    print("Good bye", name)
 
say_hi()
say_bye()

print("\n")


# Скрытие переменных

name = "Tom"
 
 
def say_hi():
    name = "Bob"        # скрываем значение глобальной переменной
    print("Hello", name)
 
 
def say_bye():
    print("Good bye", name)
 
 
say_hi()    # Hello Bob
say_bye()   # Good bye Tom

print("\n")


'''
Если же мы хотим изменить в локальной функции глобальную переменную, а не определить локальную, то необходимо использовать ключевое слово global:
'''

name = "Tom"
 
 
def say_hi():
    global  name
    name = "Bob"        # изменяем значение глобальной переменной
    print("Hello", name)
 
 
def say_bye():
    print("Good bye", name)
 
 
say_hi()    # Hello Bob
say_bye()   # Good bye Bob

print("\n")


# nonlocal

def outer():  # внешняя функция
    n = 5
 
    def inner():    # вложенная функция
        nonlocal n  # указываем, что n - это переменная из окружающей функции
        n = 25
        print(n)
 
    inner()     # 25
    print(n)
 
 
outer()          # 25

print("\n")


# Без nonlocal будет два вывода: 25 и 5

def outer():  # внешняя функция
    n = 5
 
    def inner():    # вложенная функция
        n = 25
        print(n)
 
    inner()     # 25
    print(n)
 
 
outer()     # 5 
# 25    - inner
# 5     - outer

print("\n")
