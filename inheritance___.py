import os

# class Person:
#     pass
#
# # p = Person()
# """ inheritance"""
# class Employee(Person):
#     pass
#
#
# emp = Employee()
# print(isinstance(emp, Person))

""" how the object created ? """
# class Person:
#     def __init__(self):
#         print("--- I am a person --> from parent class ---")
#         self.name='person'
#
# class Employee(Person):
#     pass
#
#
# emp = Employee()
# print(isinstance(emp, Person))

""" ---> inheritance___ """
# class Person:
#     def __init__(self):
#         print("--- I am a person --> from parent class ---")
#         self.name='person'
#
#     def displayPerson(self):
#         print(f"I am {self.name}")
#
# class Employee(Person):
#     def __init__(self):
#         self.email = 'test@gmail.com'
#         print("--- I am a an employees ------ ")
#
#
# emp = Employee()
# emp.displayPerson()

""" calling parent constructor """
# class Person:
#     def __init__(self):
#         print("--- I am a person --> from parent class ---")
#         self.name='person'
#
#     def displayPerson(self):
#         print(f"I am {self.name}---> parent()")
#
# class Employee(Person):
#     def __init__(self):
#         self.email = 'test@gmail.com'
#         print("--- I am a an employee ------ ")
#         super().__init__()
#
#     def displayPerson(self):
#         super().displayPerson()
#         print(f"---- I am an employee ----- {self.email}---> child")
#
#
# emp = Employee()
# emp.displayPerson()


#
# class A:
#     def displayItem(self):
#         print("I am A ===> A class ")
#
# class B(A):
#     pass
#
# class C(B):
#     pass
#
#
# class D(C):
#     def displayItem(self):
#         super().displayItem()
#         print("-- I am D ===> D class ")
#
#
# d = D()
# d.displayItem()

""" python support multiple inheritance  """


class Teacher:
    def __init__(self, name):
        self.name = name

    def myinfo(self):
        print("--- I am a teacher ---")


class Engineer:
    def __init__(self, name):
        self.name = name.upper()

    def myinfo(self):
        print("I am an engineer ---")


class Instructor(Teacher, Engineer):
    pass


# inn = Instructor("lina")
# inn.myinfo()


# class Test:
#     def __init__(self, name):
#         self.name = name
#
#
# class Exam:
#     def __init__(self, grade):
#         self.grade = grade
#
#
# class Eval(Exam, Test):
#     def __init__(self):
#         super().__init__(44)  # call first parent that have __init__ function
#
#
# ev = Eval()
