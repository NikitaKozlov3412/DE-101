# Наследование

class Person:
 
    def __init__(self, name):
        self.__name = name   # имя человека
 
    @property
    def name(self):
        return self.__name
 
    def display_info(self):
        print(f"Name: {self.__name} ")
 
 
class Employee(Person):
 
    def work(self):
        print(f"{self.name} works")
 
 
tom = Employee("Tom")
print(tom.name)     # Tom
tom.display_info()  # Name: Tom 
tom.work()          # Tom works

print("\n")


# Множественное наследование

#  класс работника
class Employee:
    def work(self):
        print("Employee works")
 
 
#  класс студента
class Student:
    def study(self):
        print("Student studies")
 
 
class WorkingStudent(Employee, Student):        # Наследование от классов Employee и Student
    pass
 
 
# класс работающего студента
tom = WorkingStudent()
tom.work()      # Employee works
tom.study()     # Student studies

print("\n")

'''
При этом наследуемые классы могут более сложными по функциональности, 
например:
'''

class Employee:
 
    def __init__(self, name):
        self.__name = name
 
    @property
    def name(self):
        return self.__name
 
    def work(self):
        print(f"{self.name} works")
 
 
class Student:
 
    def __init__(self, name):
        self.__name = name
 
    @property
    def name(self):
        return self.__name
 
    def study(self):
        print(f"{self.name} studies")
 
 
class WorkingStudent(Employee, Student):
    pass

 
tom = WorkingStudent("Tom")
tom.work()      # Tom works
tom.study()     # Tom studies

print("\n")

# очередность применения классов

print(WorkingStudent.__mro__)
print(WorkingStudent.mro())

print("\n")
