
"""
ABC --> abstract base class
to consturct an abstract class you must
    1- create class that inherits from ABC
    2 - create abstract mehtod  --> user decorator @abstractmethod
"""
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def myfun(self):
        pass

# emp = Employee()  #TypeError: Can't instantiate abstract class Employee with abstract method myfun


class Developer(Employee):
    # override abstract function in the parent class
    def myfun(self):
        print("--- this is developer class ")

dev = Developer()
# dev.myfun()


""" engineer class is considered to be abstract class ? as it inherits from Employee
    0--> employee is abstract class and doen't override the abstract method 
"""
class Enginner(Employee):
    pass

eng = Enginner()