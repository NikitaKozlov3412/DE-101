# Цикл while

number = 1
 
while number < 5:
    print(f"number = {number}")
    number += 1
print("Работа программы завершена")

print("\n")

number = 1
 
while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

print("\n")

number = 10
 
while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

print("\n")

# Цикл for

message = "Hello"
 
for c in message:
    print(c)

print("\n")
    
for n in range(10):
    print(n, end=" ")
    
print("\n")

for n in range(4, 10):
    print(n, end=" ")
    
print("\n")

for n in range(0, 10, 2):
    print(n, end=" ")
    
print("\n")

message = "Hello"
for c in message:
    print(c)
else:
    print(f"Последний символ: {c}. Цикл завершен");
print("Работа программы завершена")  # инструкция не имеет отступа, поэтому не относится к else


print("\n")


# Вложенные циклы

# Таблица умножения
i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1
    
print("\n")

#ещё один пример вложенных циклов

for c1 in  "ab":
    for c2 in "ba":
        print(f"{c1}{c2}")
        
print("\n")


#Выход из цикла. break и continue


number = 0
while number < 5:
    number += 1
    if number == 3 :    # если number = 3, выходим из цикла
        break
    print(f"number = {number}")
    
print("\n")


number = 0
while number < 5:
    number += 1
    if number == 3 :    # если number = 3, переходим к новой итерации цикла
        continue
    print(f"number = {number}")
    

#Упражнение
#Мой ответ:

lit = 'l'
while (lit != 'y' or lit != 'y'):

    a1 = int(input("Введите первое число: "))
    a2 = int(input("Введите второе число: "))
    a3 = a1 + a2
    print(f"Сумма чисел = {a3}")
    lit = str(input("Нажмите Y или y для завершения программы: "))
    if (lit == 'Y' or lit == 'y'):
        break

'''
#Верный ответ:

# бесконечный цикл
while True:
    # вводим первое число
    num1 = int(input("Введите первое число: "))
    # вводим второе число
    num2 = int(input("Введите второе число: "))
    # вычисление суммы чисел
    print("Сумма чисел: ", num1+num2 )
    # запрос на выход из цикла
    str = input ("Нажмите Y или y для завершения программы: ")
    # выходим из цикла
    if (str =="Y" or str =="y"):  break

'''

