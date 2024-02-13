print ("Введите целое число")
n = int(input())
summa = 0
maximum = 0
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
    print ("Введите другое число")
    n = int(input())
print ("Вы ввели 0")
print("Число", maximum, "с наибольшей суммой цифр:", summa)
