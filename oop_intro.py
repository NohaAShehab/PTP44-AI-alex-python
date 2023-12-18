# emp= {
#     "firstName": "John",
#     "lastName": "Smith",
#     "email": "j@gmail.com", "age": 18
# }
#
# emp2 = {
#     "fname": "ali",
#     "lname": "test",
#     'emp_email': 'mm@fff.com'
# }
#
# def printEmpInfo(empdata : dict ):
#     print(f'name={empdata["firstName"]}, lname={empdata["lastName"]}')
#
#
# printEmpInfo(emp)
# printEmpInfo(emp2)


""" create general architecture --->
    define properties you need to describe in the employee,
    generate functions in can instance class

"""
""" 1- create a class """
# class Employee:
#     pass
#
# # class Employee(object):
# #     pass
# #
# "2- object from class "
# emp = Employee()  # preserve new location in memory ?
# print(emp)  # <__main__.Employee object at 0x7fa04b7b0a90>
# print(isinstance(emp, Employee))
# print(isinstance(emp, object))
#
# """ loosely dynamically typed lang. ?"""
# emp.name='ahmed'
# emp.email = 'ahmed@gmail.com'
#
#
# emp2= Employee()
# emp2.fname= 'ali'
# emp2.lname='test'
# print(emp2)
# print(emp2.fname)

""" customize object creation """
# class Employee:
#
#     def __init__(self):  # the constructor
#         """ when you create an object --> constructor preserve place in memory
#             and self represent current object address
#             name , email , salary ---> instance variables
#         """
#         print(f"----  {self} --> this function will be called while creating the object ")
#         self.name='ahmed'  # instance variable ?
#         self.email = 'ahmed@gmail.com'
#         self.salary=100000
#
#
#
# emp = Employee()
# print(emp)
#
# emp2 = Employee()
# print(emp2.name)
# emp2.name='update'
# print(emp2.name)
# emp2.fname ='dddsf'
#

# class Employee:
#
#     def __init__(self, name, email, salary):  # the constructor
#         """ when you create an object --> constructor preserve place in memory
#             and self represent current object address
#             name , email , salary ---> instance variables
#         """
#         print(f"----  {self} --> this function will be called while creating the object ")
#         self.name=name  # instance variable ?
#         self.email = email
#         self.salary=salary
#
#
#
# emp = Employee("ahmed", 'ddd',4435)
# print(emp)
#
# emp2 = Employee("fdfsdf", 'sfsff', 23434)
# print(emp2.name)
# emp2.name='update'
# print(emp2.name)
# emp2.fname ='dddsf'
#
#

"""instance methods """
# class Employee:
#
#     def __init__(self, name='', email='', salary=233):  # the constructor
#         """ when you create an object --> constructor preserve place in memory
#             and self represent current object address
#             name , email , salary ---> instance variables
#         """
#         print(f"----  {self} --> this function will be called while creating the object ")
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
#
#
# emp = Employee("ahmed", 'ddd',4435)
# print(emp)
# emp.display_emp_details()
#
# emp2 = Employee("fdfsdf", 'sfsff', 23434)
# print(emp2.name)
# emp2.name='update'
# print(emp2.name)
# emp2.fname ='dddsf'
# emp2.display_emp_details('hello world -----')
#
#
# emp3 = Employee()
#

