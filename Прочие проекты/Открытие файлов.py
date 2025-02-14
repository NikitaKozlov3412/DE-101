# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 13:27:05 2024

@author: Администратор
"""

import os

# Получаем текущую рабочую директорию
current_directory = os.getcwd()

print("Текущая рабочая директория:", current_directory)

from pathlib import Path

# Получаем текущую рабочую директорию
current_directory = Path.cwd()

print("Текущая рабочая директория:", current_directory)

my_file = open("игры за 30_10_2024.txt")

my_file = open("игры за 30_10_2024.txt", "r")

my_file.close()

# Открываем файл для чтения
with open("игры за 30_10_2024.txt", "r", encoding="utf-8") as my_file:
    # Читаем первые три строки
    for _ in range(3):
        line = my_file.readline()
        if line:  # Проверяем, что строка не пустая
            print(line.strip())  # Выводим строку без лишних пробелов и символов новой строки
        else:
            break  # Если строк больше нет, выходим из цикла
            