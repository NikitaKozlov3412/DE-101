# Основные методы строк

#Проверка, введено ли число:

'''
string = input("Введите число: ")
if string.isnumeric():
    number = int(string)
    print(number)
'''

# Проверка, начинается или оканчивается строка на определенную подстроку:

file_name = "hello.py"
 
starts_with_hello = file_name.startswith("hello")   # True
ends_with_exe = file_name.endswith("exe")           # False

print(starts_with_hello)
print(ends_with_exe)

print("\n")

# Удаление пробелов в начале и в конце строки:
    
string = "   hello  world!  "
string = string.strip()
print(string)           # hello  world!

print("\n")

# Дополнение строки пробелами и выравнивание:
    
print("iPhone 7:", "52000".rjust(10))
print("Huawei P10:", "36000".rjust(10))

print("\n")

# Поиск в строке

# метод find(), который возвращает индекс первого вхождения 
# подстроки в строку и имеет три формы:
    
welcome = "Hello world! Goodbye world!"
index = welcome.find("wor")
print(index)       # 6
 
# поиск с 10-го индекса
index = welcome.find("wor",10)
print(index)       # 21
 
# поиск с 10 по 15 индекс
index = welcome.find("wor",10,15)
print(index)       # -1

print("\n")

# Замена в строке

# Для замены в строке одной подстроки на другую применяется метод replace():
    
phone = "+1-234-567-89-10"
 
# замена дефисов на пробел
edited_phone = phone.replace("-", " ")
print(edited_phone)     # +1 234 567 89 10
 
# удаление дефисов
edited_phone = phone.replace("-", "")
print(edited_phone)     # +12345678910
 
# замена только первого дефиса
edited_phone = phone.replace("-", "", 2)
print(edited_phone)     # +1234-567-89-10

print("\n")

# Разделение на подстроки

text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# разделение по пробелам
splitted_text = text.split()
print(splitted_text)
print(splitted_text[6])     # дуб,
 
# разбиение по запятым
splitted_text = text.split(",")
print(splitted_text)
print(splitted_text[1])     # в два обхвата дуб
 
# разбиение по первым пяти пробелам
splitted_text = text.split(" ", 5)
print(splitted_text)        
print(splitted_text[5])     # обхвата дуб, с обломанными ветвями и с обломанной корой

print("\n")

# метод - partition() разбивает строку по разделителю на три подстроки 
# и возвращает кортеж из трех элементов - подстрока до разделителя, 
# разделитель и подстрока после разделителя:

text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
text_parts = text.partition("дуб")
print(text_parts)
# ('Это был огромный, в два обхвата ', 'дуб', ', с обломанными ветвями и с обломанной корой')

print("\n")

# Соединение строк

words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]
 
# разделитель - пробел
sentence = " ".join(words)
print(sentence)  # Let me speak from my heart in English
 
# разделитель - вертикальная черта
sentence = " | ".join(words)
print(sentence)  # Let | me | speak | from | my | heart | in | English

print("\n")

# Можно применить соединение для простой строки
# В этом случае разделитель будет между всеми символам, кроме крайних:
    
word = "hello"
joined_word = "|".join(word)
print(joined_word)      # h|e|l|l|o

print("\n")


 