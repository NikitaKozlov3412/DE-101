# Функция random() возвращает случайное число с плавающей точкой 
# в промежутке от 0.0 до 1.0.

import random
 
number = random.random()  # значение от 0.0 до 1.0
print(number)
number = random.random() * 100  # значение от 0.0 до 100.0
print(number)

print("\n")

# Функция randint(min, max) возвращает случайное целое число 
# в промежутке между двумя значениями min и max.

import random
 
number = random.randint(20, 35)  # значение от 20 до 35
print(number)

print("\n")

# Функция randrange() возвращает случайное целое число из определенного 
# набора чисел. Она имеет три формы:
    
import random
 
number = random.randrange(10)  # значение от 0 до 10 не включая
print(number)
number = random.randrange(2, 10)  # значение в диапазоне 2, 3, 4, 5, 6, 7, 8, 9
print(number)
number = random.randrange(2, 10, 2)  # значение в диапазоне 2, 4, 6, 8
print(number)

print("\n")

# Работа со списком

# Для работы со списками в модуле random определены две функции: 
# функция shuffle() перемешивает список случайным образом, 
# а функция choice() возвращает один случайный элемент из списка:
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)  
random_number = random.choice(numbers)
print(random_number)

print("\n")