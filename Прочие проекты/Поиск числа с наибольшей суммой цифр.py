from array import *
my_list = []
i = 0
maximum = 0
print ("Введите целое число")
n = int(input())
summa = 0
while n != 0:
    k = abs(n)
    s = 0
    while k > 0:
        s = s + k%10
        k //= 10
    if s > summa:
        summa = s
        maximum = n
        my_list.clear()
    elif s == summa:
       drugoe = n
       my_list.append(drugoe)
    print ("Введите другое число")
    n = int(input())
print ("Вы ввели 0")
if maximum != 0:
   print ("Число", maximum, "с наибольшей суммой цифр:", summa)
if len(my_list) > 0:
    print ("Другие числа",   "с такой же наибольшей суммой цифр:")
    print(*my_list, sep=', ')