# Упаковка и распаковка

# Распаковка

x, y = 1, 2
print(x)    # 1
print(y)    # 2

print("\n")

x, y = (1, 2)
print(x)    # 1
print(y)    # 2

print("\n")

# Можно распаковывать разные кортежи:

name, age, company = ("Tom", 38, "Google")
print(name)         # Tom
print(age)          # 38
print(company)      # Google

print("\n")

# Можно также распаковывать списки:
    
people = ["Tom", "Bob", "Sam"]
first, second, third = people
print(first)      # Tom
print(second)     # Bob
print(third)      # Sam

print("\n")

# При разложении словаря переменные получают ключи словаря:
    
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
r, b, g = dictionary
print(r)    # red
print(b)    # blue
print(g)    # green
# получаем значение по ключу
print(dictionary[g])    # зеленый

print("\n")

# Деструктуризация в циклах

# Циклы в Python позволяют разложить коллекции на отдельные составляющие:
    
people = [
    ("Tom", 38, "Google"),
    ("Bob", 42, "Microsoft"),
    ("Sam", 29, "JetBrains")
]
 
for name, age, company in people:
    print(f"Name: {name}, Age: {age}, Company: {company}")
    
print("\n")

# функция enumerate() создает для каждого элемента кортеж 
# и возвращает набор из подобных кортежей

people = ["Tom", "Bob", "Sam"]
for index, name in enumerate(people):
    print(f"{index}.{name}")

print("\n")

# результат
# 0.Tom
# 1.Bob
# 2.Sam

# Игнорирование значений

person =("Tom", 38, "Google")
name, _, company = person
print(name)     # Tom
print(company)  # Google

print("\n")


'''
Здесь нам не важен второй элемент кортежа, поэтому для него 
определяем переменную _. Хотя в реальности _ - такое же действительное имя, 
как name и company:
'''

name, _, company = person
print(_)     # 38

print("\n")

# Упаковка значений и оператор *

num1=1
num2=2
num3=3
*numbers,=num1,num2,num3
print(numbers)  #[1, 2, 3]

print("\n")

# Первый элемент - в head, остальные - в tail:

head, *tail = [1, 2, 3, 4, 5]
 
print(head)  # 1
print(tail)  # [2, 3, 4, 5]

# Теперь наоборот:

*head, tail = [1, 2, 3, 4, 5]
 
print(head)  # [1, 2, 3, 4]
print(tail)  # 5

print("\n")

# Полчуим элементы по середине, кроме первого и последнего:
    
head, *middle, tail = [1, 2, 3, 4, 5]
 
print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5

print("\n")

# Или все кроме первого и второго:
    
first, second, *other = [1, 2, 3, 4, 5]
 
print(first)    # 1
print(second)   # 2
print(other)    # [3, 4, 5]

print("\n")

# Надо получить только первый, третий и последний элемент

first, _, third, *_, last = [1, 2, 3, 4, 5, 6, 7, 8]
 
print(first)   # 1
print(third)   # 3
print(last)    # 8

print("\n")

# Также можно получить ключи словаря:
    
red, *other, green = {"red":"красный", "blue":"синий", "yellow":"желтый", "green":"зеленый"}
 
print(red)          # red
print(green)        # green
print(other)        # ['blue', 'yellow']

print("\n")

# Распаковка и операторы * и **

# Оператор * используется для распаковки кортежей, списков, строк, множеств, 
# а оператор ** - для распаковки словарей.

nums1 = [1, 2, 3]
nums2 = (4, 5, 6)
 
# распаковываем список nums1 и кортеж nums2
nums3 = [*nums1, *nums2] 
print(nums3)        # [1, 2, 3, 4, 5, 6]

print("\n")

# Подобным образом раскладываются словари, только применяется оператор **:
    
dictionary1 = {"red":"красный", "blue":"синий"}
dictionary2 = {"green":"зеленый", "yellow":"желтый"}
 
# распаковываем словари
dictionary3 = {**dictionary1, **dictionary2}
print(dictionary3)  
# {'red': 'красный', 'blue': 'синий', 'green': 'зеленый', 'yellow': 'желтый'}

print("\n")