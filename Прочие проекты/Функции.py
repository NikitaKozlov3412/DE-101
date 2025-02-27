#Функции

def say_hello():    # определение функции say_hello
    print("Hello")
 
 
say_hello()         # вызов функции say_hello
say_hello()
say_hello()


print("\n")

'''
Если функция имеет одну инструкцию, то ее можно разместить на одной строке 
с остальным определением функции:
'''

def say_hello(): print("Hello")


say_hello()


print("\n")

#Определим и выполним несколько функций:

def say_hello():
    print("Hello")
 
 
def say_goodbye():
    print("Good Bye")
 
 
say_hello()
say_goodbye()


print("\n")


# Локальные функции

def print_messages():
    # определение локальных функций
    def say_hello_1(): print("Hello")
    def say_goodbye(): print("Good Bye")
    # вызов локальных функций
    say_hello_1()
    say_goodbye()
 
# Вызов функции print_messages
print_messages()

print("\n")
 
#say_hello_1() # вне функции print_messages функция say_hello_1 не доступна

#Организация программы и функция main

def main():
    say_hello_2()
    say_goodbye_2()
 
def say_hello_2():
    print("Hello!")
 
def say_goodbye_2():
    print("Good Bye!")
 
# Вызов функции main
main()

