from array import *
my_list = []
m = 0
a = 0
k = 0
ch = 0

print('Введите число. От 1 до этого числа будет считаться \n'
      'сумма делителей чисел, не включая сами числа')
m = int(input())
for j in range (1, m+1):
    a = j
    ch = 0
    print("Делители числа", a, ": ")
    for i in range(2, a+1):
      if a%i == 0:
          k =  a//i
          ch  = ch + k
      if ch == 1:
         my_list.append(a)
    print("Сумма делителей числа",  a, ": " ,ch);
    if ch == a:
      print (a, " - совершенное число!");
print("Простые числа: ")  
print(*my_list, sep=', ')
