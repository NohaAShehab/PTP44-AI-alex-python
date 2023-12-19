

# class Student:
#     def __init__(self,name, email, grade):
#         self.name = name
#         self._email = email
#         self.__grade = grade
#
#     def __str__(self):
#         "must return with string "
#         # return 'Student object '
#         return f'{self.name}'
#
#     def __repr__(self):
#         "must return with string "
#         return f'Student(name={self.name}, email={self._email}, grade={self.__grade})'
#
#     def __len__(self):
#         """ must return with an integer """
#         # return len(self.name)
#         return len(self.__dict__)
#
#     def __call__(self):
#         print("--- the object is being called ---")
#
# s = Student("ahmed", 'ahmed@gmail.com',5456)
# print(s)  # interpreter check if __str__ overriden in the class --> call it ?
# # if not  __repr__ --> overriden ? call , neither both ? ---> print object address.
# print(s.__dict__)  # represent object properties into a dict .
# print(len(s))
#
# s()


###
names =  ['ahmed', 'mohamed', 'ali', 'bassem', 'Carmen', 'noha', 'yahia']

def filternames(names):
    newl =[]
    for name in names:
        if name[0].lower() in 'abc':
            newl.append(name)

    return newl


print(filternames(names))


##
""" list comprehensions """
newnames = [ name for name in names if name[0].lower() in 'abc']
print(newnames)

### lambda --> anonymous function

x = lambda num: num*10
print(x, type(x))

print(x(6))

# ll = lambda  name: name[0].lower() in 'abc'
# # print(ll("noha"))
# # print(ll("ahmed"))
#
# newnames =[]
# for name in names:
#     if ll(name):
#         newnames.append(name)
#
# print(newnames)


#
# newnames =[]
# fn =  lambda  name: name[0].lower() in 'abc'
# for name in names:
#     if  fn(name):
#         newnames.append(name)
#
# print(newnames)

### map . filter

# studentnames =  ['ahmed', 'mohamed', 'ali', 'bassem', 'Carmen', 'noha', 'yahia']
#
# fitered_names = filter(lambda name:name[0] in 'abc', studentnames)
# print(fitered_names)  # filtered object
# fitered_names = list(fitered_names)
# print(fitered_names)







""" map values """

values = [10, 39, 'iti', 'ahmed', 'ali', 55.55]
# list -->multiply values by 10?

newvalues =map(lambda val: val*10, values)
print(newvalues)
mapvalues= list(newvalues)
print(mapvalues)





"customized exception class "

# class NohaException(Exception):
#     pass
#
#
# name = 'noha'
# if name=='noha':
#     raise NohaException("0000000")
#



""""

instances ={"quename": values }

"""

