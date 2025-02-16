# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:15:33 2024

@author: Администратор
"""
# Для записи файлов используется метод write.
# Это создаст новый файл с именем "newfile.txt" и запишет содержимое в него.
# Если файл уже существует, все его содержимое будет заменено, когда вы 
# откроете его в режиме записи с помощью «w».

file = open("файлик1.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("файлик1.txt", "r")
print(file.read())
file.close()

#Если вы хотите добавить содержимое в существующий файл, вы можете открыть 
#его, используя режим "a", который означает for "append":

file = open("файлик1.txt", "a")

file.write("\nThe Da Vinci Code")
file.close()

file = open("файлик1.txt", "r")
print(file.read())
file.close()

# Метод write возвращает количество байтов записанных в файл в случае успеха.
msg = "Hello world!"
file = open("файлик1.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()