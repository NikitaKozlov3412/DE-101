# Строки

message = "Hello World!"
print(message)  # Hello World!
 
name = 'Tom'
print(name)  # Tom

print("\n")

'''
Если строка длинная, ее можно разбить на части и разместить их на разных 
строках кода. В этом случае вся строка заключается в круглые скобки, а ее 
отдельные части - в кавычки:
'''

text = ("Laudate omnes gentes laudate "
        "Magnificat in secula ")
print(text)

print("\n")

'''
Если же мы хотим определить многострочный текст, то такой текст заключается 
в тройные двойные или одинарные кавычки.
Но строку тогда нужно присвоить переменной:
'''

'''
Это комментарий
'''
text = '''Laudate omnes gentes laudate
Magnificat in secula
Et anima mea laudate
Magnificat in secula 
'''
print(text)

print("\n")

# Управляющие последовательности в строке

text = "Message:\n\"Hello World\""
print(text)

print("\n")

#Чтобы избежать невреного прочтения \n, нужно использовать символ r

path = r"C:\python\name.txt"
print(path)

print("\n")

# Вставка значений в строку
# внутри строки переменные размещаются в фигурных скобках {}, 
# а перед всей строкой ставится символ f:

userName = "Tom"
userAge = 37
user = f"name: {userName}  age: {userAge}"
print(user)   # name: Tom  age: 37

print("\n")

# Обращение к символам строки

string = "hello world"
c0 = string[0]  # h
print(c0)
c6 = string[6]  # w
print(c6)
 
'''
c11 = string[11]  # ошибка IndexError: string index out of range
print(c11)
'''

print("\n")

# Отрицательные индексы

string = "hello world"
c1 = string[-1]  # d
print(c1)
c5 = string[-5]  # w
print(c5)

print("\n")

'''
string = "hello world"
string[1] = "R"
Будет ошибка, потому что строка - это неизменяемый (immutable) тип
'''

