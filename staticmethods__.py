

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#
#
#
# emp1= Employee('ahmed', 10000)
#
#
# def netsaly(salary):
#     return  salary*.8
#
# print(netsaly(emp1.salary))
#
#
# print(netsaly(43489475))

"""

"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # def netsaly(salary):  # Usually first parameter of a method is named 'self'
    #     print(salary)
    #     # return salary * .8

    @staticmethod  # this function doesn't depend on instance or the class ---> helper function
    def netsaly(salary):
        print(salary)
        return salary * .8

emp1= Employee('ahmed', 10000)

print(Employee.netsaly(89473824))
print(Employee.netsaly(emp1.salary))





