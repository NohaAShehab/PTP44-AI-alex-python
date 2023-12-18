# class Employee:
#     no_of_employees = 0  # class variable
#     def __init__(self, name='', email='', salary=233):  # the constructor
#         self.name=name  # instance variable ?
#         self.email = email
#         self.salary=salary
#
#     # instance method --->first parameter represent instance --> self
#     def display_emp_details(self, message ='hello'):
#         print(f"name={self.name}, email={self.email}, salary={self.salary}")
#         print(message)
#
#
# """ access class variable """
# print(Employee.no_of_employees)
# Employee.no_of_employees=100
#
# emp = Employee("ahmed", 'ahmed@gmail.com', 4565)


""" """

# class Employee:
#     no_of_employees = 0  # class variable
#     def __init__(self, name='', email='', salary=233):  # the constructor
#         self.name=name  # instance variable ?
#         self.email = email
#         self.salary=salary
#         Employee.no_of_employees +=1
#
#     # instance method --->first parameter represent instance --> self
#     def display_emp_details(self, message ='hello'):
#         print(f"name={self.name}, email={self.email}, salary={self.salary}")
#         print(message)
#
#
#
#
# print(Employee.no_of_employees)
#
# emp = Employee("ahmed",'ahmed@gmail.com', 45555)
# print(Employee.no_of_employees)

""" destructor """

# class Employee:
#     no_of_employees = 0  # class variable
#
#     def __init__(self, name='', email='', salary=233):  # the constructor
#         self.name = name  # instance variable ?
#         self.email = email
#         self.salary = salary
#         Employee.no_of_employees += 1
#
#     # instance method --->first parameter represent instance --> self
#     def display_emp_details(self, message='hello'):
#         print(f"name={self.name}, email={self.email}, salary={self.salary}")
#         print(message)
#
#     def __del__(self):
#         # Employee.no_of_employees -=1
#         self.__class__.no_of_employees -= 1
#
# print(Employee.no_of_employees)
#
# emp = Employee("ahmed", 'ahmed@gmail.com', 45555)
# print(Employee.no_of_employees)


""" function represent class behaviour"""


# class Employee:
#     no_of_employees = 0  # class variable
#
#     def __init__(self, name='', email='', salary=233):  # the constructor
#         self.name = name  # instance variable ?
#         self.email = email
#         self.salary = salary
#         Employee.no_of_employees += 1
#
#     def __del__(self):
#         # Employee.no_of_employees -=1
#         self.__class__.no_of_employees -= 1
#
#     # def get_emp_count(self):
#     #     return self.__class__.no_of_employees
#
#     # you can call the function using class name
#     @classmethod  # this function depends on the class only
#     def display_total_employees(cls):  # cls represent class itself
#         print(f'cls = {cls}')
#         print(Employee.no_of_employees)
#         print(cls.no_of_employees)
#
#
# print(Employee.no_of_employees)
# print(Employee.display_total_employees())
#
# emp = Employee("ahmed", 'ahmed@gmail.com', 45555)


""" -----> """
# class Employee:
#     no_of_employees = 0  # class variable
#     # loosely dynamically typed lang.
#     def __init__(self, name, email , salary):  # the constructor
#         self.name = name  # instance variable ?
#         self.email = email
#         self.salary = salary
#         Employee.no_of_employees += 1
#
#     def __init__(self,name):
#         self.name = name
#         self.email = ''
#         self.salary = 2333
#         Employee.no_of_employees +=1
#
#     def __del__(self):
#         # Employee.no_of_employees -=1
#         self.__class__.no_of_employees -= 1
#
#
#
# emp= Employee("ahmed", 'ddd', 3333)
# emp2= Employee("ddd")

# class Employee:
#     no_of_employees = 0  # class variable
#     # loosely dynamically typed lang.
#     def __init__(self, name, email , salary):  # the constructor
#         self.name = name  # instance variable ?
#         self.email = email
#         self.salary = salary
#         Employee.no_of_employees += 1
#
#
#     def __del__(self):
#         # Employee.no_of_employees -=1
#         self.__class__.no_of_employees -= 1
#
#     """ use class method decorator---> write function --> works on the class behaviour
#         create new object form the --> object factory
#     """
#     @classmethod
#     def create_object(cls, name):
#         return cls(name,'', 10000)
#
#
#
# emp= Employee("ahmed", 'ddd', 3333)
#
#
# emp2 = Employee.create_object('ahmed')

# """ class complex """
#
# class MyComplex:
#     def __init__(self, realpart, imagpart):
#         self.realpart = realpart
#         self.imagpart = imagpart
#
#     @classmethod
#     def add_nums(cls, num1, num2):
#         if isinstance(num1, cls) and isinstance(num2, cls):
#             realpart = num1.realpart + num2.realpart
#             imagpart = num1.imagpart + num2.imagpart
#             num3 = cls(realpart, imagpart)
#             return num3
#         raise  TypeError(f'num1, num2 must be from {cls} type')
#
#
#
# numm = MyComplex(4,5)
# nummm2= MyComplex(55,55)
#
# num3 = MyComplex.add_nums(numm, nummm2)
#
#
# num44= MyComplex.add_nums(numm, 10)
#
#
#
