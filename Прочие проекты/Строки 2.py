# Строки 2
# Перебор строки

string = "hello world"
for char in string:
    print(char)
    
print("\n")

# Получение подстроки

string = "hello world"
 
# с 0 до 5 индекса
sub_string1 = string[:5]
print(sub_string1)      # hello
 
# со 2 до 5 индекса
sub_string2 = string[2:5]
print(sub_string2)      # llo
 
# с 2 по 9 индекса через один символ
sub_string3 = string[2:9:2]
print(sub_string3)      # l

print("\n")

# Объединение строк

name = "Tom"
surname = "Smith"
fullname = name + " " + surname
print(fullname)  # Tom Smith

print("\n")

name = "Tom"
age = 33
info = "Name: " + name + " Age: " + str(age)
print(info)  # Name: Tom Age: 33

print("\n")

# Повторение строки

print("a" * 3)  # aaa
print("he" * 4)  # hehehehe

print("\n")

# Сравнение строк

str1 = "1a"
str2 = "aa"
str3 = "Aa"
print(str1 > str2)  # False, так как первый символ в str1 - цифра
print(str2 > str3)  # True, так как первый символ в str2 - в нижнем регистре

print("\n")

# Функция lower() приводит строку к нижнему регистру, 
# а функция upper() - к верхнему.

str1 = "Tom"
str2 = "tom"
print(str1 == str2)  # False - строки не равны
 
print(str1.lower() == str2.lower())  # True

print("\n")

# Функции ord и len

# с помощью функции ord() мы можем получить числовое значение для символа 
# в кодировке Unicode:
    
print(ord("A"))     # 65
    
string = "hello world"
length = len(string)
print(length)   # 11

print("\n")

# Поиск в строке (оператора in)

text = "hello world"
exist = "hello" in text
print(exist)    # True
 
exist = "sword" in text
print(exist)    # False

# C помощью операторов not in можно проверить отсутствие подстроки в строке:
    
text = "hello world"
print("hello" not in text)    # False
print("sword" not in text)    # True

print("\n")