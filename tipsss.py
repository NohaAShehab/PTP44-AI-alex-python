

class Student:
    # special class variable
    __slots__ = ('name', 'grade')
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade



s = Student("ahmed", 100)
Student.__slots__ = ('name', 'grade', 'email', 'ffff')

# s.email = 'ahmed@gmail.com'