# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 13:56:25 2024

@author: Администратор
"""

language = "english"
if language == "english":
    print("Hello")
print("End")


language = "english"
if language == "english":
    print("Hello")
    print("End")


language = "russian"
if language == "english":
    print("Hello")
else:
    print("Привет")
print("End")


language = "russian"
if language == "english":
    print("Hello")
    print("World")
else:
    print("Привет")
    print("мир")


language = "german"
if language == "english":
    print("Hello")
    print("World")
elif language == "german":
    print("Hallo")
    print("Welt")
else:
    print("Привет")
    print("мир")
    
    
language = "german"
if language == "english":
    print("Hello")
elif language == "german":
    print("Hallo")
elif language == "french":
    print("Salut")
else:
    print("Привет")


language = "english"
daytime = "morning"
if language == "english":
    print("English")
    if daytime == "morning":
        print("Good morning")
    else:
        print("Good evening")
        

language = "russian"
daytime = "morning"
if language == "english":
    if daytime == "morning":
        print("Good morning")
    else:
        print("Good evening")
else:
    if daytime == "morning":
        print("Доброе утро")
    else:
        print("Добрый вечер")
        
