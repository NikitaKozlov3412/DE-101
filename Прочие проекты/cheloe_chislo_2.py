from array import *
print ("Введите целое число")
n = int(input())
summa = 0
while n != 0:
    k = abs(n)
    m = n
    s = 0
    while k > 0:
        s = s + k%10
        k //= 10
    if s > summa:
        summa = s
        maximum = m
        print ("Новое число", maximum, "с наибольшей суммой цифр:", summa)
    elif s == summa:
       drugoe = m
       print ("другое число", drugoe,  "с такой же наибольшей суммой цифр:", summa)
    print ("Введите другое число")
    n = int(input())
print ("Вы ввели 0")

