"""
    wrapping data ---> limit accessibility
    --> apply check --> apply logic on data

    encapsulation
    access modifiers


"""


# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name  # public
#         self._email = email  # protected
#         self.__salary = salary  # private
#
#
# emp = Employee("ahmed", 'ahmed@gmail.com', 10000)
# print(f"public property name= {emp.name}")
# ethically don't do this
# print(f"protected property email = {emp._email}")
# # print(f" private property salary = {emp.__salary }") #AttributeError:
# # 'Employee' object has no attribute '__salary'
# print(f" private property salary = {emp._Employee__salary}")


""" dealing with private and protected attributes """
# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name  # public
#         self._email = email  # protected
#         self.__salary = salary  # private
#
#     def set_salary(self, salary):
#         if isinstance(salary, int ) or isinstance(salary, float) and salary>0:
#             self.__salary = salary
#         else:
#             raise ValueError('Salary must be number greater than zero')
#
#     def get_salary(self):
#         return  self.__salary *.8
#
# emp = Employee("ahmed", 'ahmed@gmail.com', 10000)
# print(f"public property name= {emp.name}")
#
# print(emp.get_salary())
#
# emp.set_salary(500000)
# print(emp.get_salary())
#
#
#

"""  property decorator """
# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name  # public
#         self._email = email  # protected
#         self.__salary = salary  # private
#
#     def set_salary(self, salary):
#         if isinstance(salary, int ) or isinstance(salary, float) and salary>0:
#             self.__salary = salary
#         else:
#             raise ValueError('Salary must be number greater than zero')
#
#     def get_salary(self):
#         return  self.__salary
#
#     @property
#     def salary(self):
#         return self.__salary*.8
#
#     @salary.setter
#     def salary(self, salary):
#         if isinstance(salary, int ) or isinstance(salary, float) and salary>0 :
#             self.__salary = salary
#         else:
#             raise ValueError('Salary must be number greater than zero')
#
# emp = Employee("ahmed", 'ahmed@gmail.com', 10000)
# print(f"public property name= {emp.name}")
#
# # emp.set_salary(200)
# emp.salary = 299999
# print(emp.salary)


# AttributeError: property 'salary' of 'Employee' object has no setter












"""check this """
# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name  # public
#         self._email = email  # protected
#         # self.__salary = salary  # private
#         # if isinstance(salary, int) or isinstance(salary, float) and salary > 0:
#         #     self.__salary = salary
#         # else:
#         #     raise ValueError('Salary must be number greater than zero')
#         self.salary = salary  # this will call the property setter
#     @property
#     def salary(self):
#         return self.__salary*5
#
#     @salary.setter
#     def salary(self, salary):
#         if isinstance(salary, int ) or isinstance(salary, float) and salary>0 :
#             self.__salary = salary
#         else:
#             raise ValueError('Salary must be number greater than zero')
#
# emp = Employee("ahmed", 'ahmed@gmail.com', 2900000)
#
# # emp.salary = 'test'
# print("---------------------------")
#
#
#

class Student:

    def __init__(self, stdname):
        self.email = 'dd@fff.com'
        self.name = stdname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_):
        if name_.isalpha():
            self.__name = name_.upper()
        else:
            raise ValueError("Name must be characters only")

s = Student('Ahmed')










