# List comprehension

# выбрать из списка все числа, которые больше 0
# Обычный способ:

numbers = [-3, -2, -1, 0, 1, 2, 3]
positive_numbers = []
for n in numbers:
    if n > 0:
        positive_numbers.append(n)
 
print(positive_numbers)     # [1, 2, 3]

print("\n")

# Применим list comprehension:
    
numbers = [-3, -2, -1, 0, 1, 2, 3]
positive_numbers = [n for n in numbers if n > 0]
  
print(positive_numbers)     # [1, 2, 3]

print("\n")

# Источник данных iterable
# Функция range() возвращает все числя нуля до указанного порога не включая:
    
numbers = [n for n in range(10)]
print(numbers)      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\n")

# Создаём из словаря список:
    
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
words = [word for word in dictionary]
print(words)    # ['red', 'blue', 'green']

print("\n")

# Возвращение результата

numbers = [-3, -2, -1, 0, 1, 2, 3]
new_numbers = [n for n in numbers]
print(new_numbers)      # [-3, -2, -1, 0, 1, 2, 3]

print("\n")

# Возвращение удвоенных чисел

numbers = [-3, -2, -1, 0, 1, 2, 3]
new_numbers = [n * 2 for n in numbers]
print(new_numbers)      # [-6, -4, -2, 0, 2, 4, 6]

print("\n")

# Удваиваем только положительные числа:
    
numbers = [-3, -2, -1, 0, 1, 2, 3]
new_numbers = [n * 2 if n > 0 else n for n in numbers]
print(new_numbers)      # [-3, -2, -1, 0, 2, 4, 6]

print("\n")

# возвратим также из словаря значение по ключу:
    
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
words = [f"{key}: {dictionary[key]}" for key in dictionary]
print(words)    # ['red: красный', 'blue: синий', 'green: зеленый']

print("\n")

# Условие

# Выберем только четные числа:
    
numbers = [n for n in range(10) if n % 2 == 0]
print(numbers)      # [0, 2, 4, 6, 8]

print("\n")

# Выберем только те ключи из словаря, длина которых больше 3:
    
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
words = [f"{key}: {dictionary[key]}" for key in dictionary if len(key) > 3]
print(words)    # ['blue: синий', 'green: зеленый']

print("\n")

# Вопрос 1
# Каким будет результат работы следующей программы:
    
numbers = [1, 2, 3, 4, 5]
new_numbers = [i * i for i in numbers if i % 2 == 0]
print(new_numbers)

print("\n")