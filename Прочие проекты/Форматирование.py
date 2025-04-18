# Форматирование

# В прошлых темах было рассмотрено, как можно вставлять в строку 
# некоторые значения, предваряя строку символом f:
    
first_name="Tom"
text = f"Hello, {first_name}."
print(text)     # Hello, Tom.
 
name="Bob"
age=23
info = f"Name: {name}\t Age: {age}"
print(info)     # Name: Bob  Age: 23

print("\n")

# Именованные параметры

text = "Hello, {first_name}.".format(first_name="Tom")
print(text)     # Hello, Tom.
 
info = "Name: {name}\t Age: {age}".format(name="Bob", age=23)
print(info)     # Name: Bob  Age: 23

print("\n")

# Параметры по позиции

info = "Name: {0}\t Age: {1}".format("Bob", 23)
print(info)     # Name: Bob  Age: 23

# При этом аргументы можно вставлять в строку множество раз:
    
text = "Hello, {0} {0} {0}.".format("Tom")
print(text)

print("\n")

# Подстановки

# При вызове метода format в него в качестве аргументов передаются 
# значения, которые вставляются на место плейсхолдеров:
    
welcome = "Hello {:s}"
name = "Tom"
formatted_welcome = welcome.format(name)
print(formatted_welcome)        # Hello Tom

print("\n")

# Форматирование целых чисел:
    
source = "{:d} символов"
number = 5
target = source.format(number)
print(target)   # 5 символов

print("\n")

'''
Если форматируемое число больше 999, то мы можем указать в определении 
плейсхолдера, что мы хотим использовать запятую в качестве 
разделителя разрядов:
'''

source = "{:,d} символов"
print(source.format(5000))   # 5,000 символов

print("\n")

# Плейсхолдеры можно использовать и в f-строках:
    
n = 5000
source = f"{n:,d} символов"
print(source)   # 5,000 символов

print("\n")

'''
Для дробных чисел, то есть таких, которые представляют тип float, 
перед кодом плейсхолдера после точки можно указать, сколько знаков 
в дробной части мы хотим вывести:
'''

number = 23.8589578
print("{:.2f}".format(number))   # 23.86
print("{:.3f}".format(number))   # 23.859
print("{:.4f}".format(number))   # 23.8590
print("{:,.2f}".format(10001.23554))    # 10,001.24

print("\n")

# Минимальная ширину форматируемого значения в символах (10 и 8):

print("{:10.2f}".format(23.8589578))    #     23.86
print("{:8d}".format(25))               #      25

print("\n")

# Аналогичный пример с f-строками

n1 = 23.8589578
print(f"{n1:10.2f}")    #     23.86
n2 = 25
print(f"{n2:8d}")       #      25

print("\n")

# Для вывода процентов лучше воспользоваться кодом "%":
    
number = .12345
print("{:%}".format(number))        # 12.345000%
print("{:.0%}".format(number))      # 12%
print("{:.1%}".format(number))      # 12.3%
 
print(f"{number:%}")        # 12.345000%
print(f"{number:.0%}")      # 12%
print(f"{number:.1%}")      # 12.3%

print("\n")

# Для вывода числа в экспоненциальной записи применяется плейсхолдер "e":
    
number = 12345.6789
print("{:e}".format(number))        # 1.234568e+04
print("{:.0e}".format(number))      # 1e+04
print("{:.1e}".format(number))      # 1.2e+04
 
print(f"{number:e}")        # 1.234568e+04
print(f"{number:.0e}")      # 1e+04
print(f"{number:.1e}")      # 1.2e+04

print("\n")

# Форматирование без метода format
# Рядом с плейсхолдером указывается знак процента и в отличие 
# от функции format здесь не требуются фигурные скобки.

info = "Имя: %s \t Возраст: %d" % ("Tom", 35)
print(info)   # Имя: Tom     Возраст: 35

# Причем способы форматирования чисел здесь также применяются:
    
number = 23.8589578
print("%0.2f  - %e" % (number, number))   # 23.86  - 2.385896e+01

print("\n")

# Установка длины строки

str = "Hello World"
print(f"{str:>16}!")     
print(f"{str:<16}!")   
print(f"{str:^16}!")
print(f"{str:.16}!") 
print(f"{str:.5}!") 

print("\n")