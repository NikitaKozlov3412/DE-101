print("Введите натуральное число")
a = int(input())
k = 0
ch = 0
print("Делители числа: ")
for i in range(2, a+1):
    if a%i == 0:
        k =  a//i
        print(k)
        ch  = ch + k
print("Сумма делителей числа",  a, ": " ,ch);
if ch == a:
    print (a, " - совершенное число!");
   