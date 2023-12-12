""" what is functions ? """
""" functions with mandatory arguments  or optional arguments """
""" functions with known min and max number of arguments """
"""
    void sayhello(){}

"""

# for i  in range(10):
#     pass #pass is a null operation — when it is executed, nothing happens.
# It is useful as a placeholder when a statement is required syntactically,
# but no code needs to be executed

print("---iti====")

# def sayhello():
#     pass  # pass is a null operation — when it is executed, nothing happen


# """ to call function """
# sayhello()
# # print("hi students")
# y = sayhello()
# print(y)  #None


""" check this """

# def sayhello():
#     return
#
#
# x = sayhello()
# print(x)

""" --> def function do something and return res """

# def say_hello():
#     print(f"We support Hamas")
#     return "Hamas"
#
#
# res=say_hello()
# print(res)
#
# say_hello()


# def welcome():
#     print("--- welcome ---- ")
#
# print("---iti----")
#
# welcome()
"""  function accept parameters and return with value   """
# def sumnums(num1, num2):
#     print(f"num1={num1}, num2 = {num2}")
#     res = num1 + num2
#     return res
#
# result = sumnums(3,5)
# print(f"result = {result}")
#
# result2 = sumnums("ahmed", "alli")
# print(f"result = {result2}")


"""---"""

# def sumnums(num1: int, num2: int):  # for documentary purpose
#     print(f"num1={num1}, num2 = {num2}")
#     res = num1 + num2
#     return res
#
# res = sumnums(1, 2)
# print(f'res={res}')
#
# res2 = sumnums('hello', 'world')
# print(f'res2={res2}')
#
# res3 = sumnums('ahmed',3)
# print(f'res3={res3}')

""" """
#
# def sumnums(num1: int, num2: int):  # for documentary purpose
#     print(f"num1={num1}, num2 = {num2}")
#     res = num1 + num2
#     return res

# res = sumnums(1, 2)
# print(f'res={res}')
#
# res2 = sumnums('hello', 'world')
# print(f'res2={res2}')
#
# res3 = sumnums('ahmed',3)
# print(f'res3={res3}')

""" to fix the problem """

#
# def sumnums(num1: int, num2: int):  # for documentary purpose
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 + num2
#         return res
#     print("---- num1 and num2 must be integers ")
#
#
# res1 = sumnums(1, 3)
# print(res1)
#
# res2 = sumnums("ahmed", "ali")
# print(res2)
#
# res3 = sumnums('ahmed', 3)
# print(res3)

""" arguments """

# def sayhello():
#     print("hello")


# sayhello('ahmed') #TypeError: sayhello() takes 0 positional arguments but 1 was given


# def say_hello(name):
#     print(f"hello {name}")
#
# say_hello("ahmed", "ali")
"""  functions with with optional arguments // default arguments """

# def sumnum(num1=33, num2=10):
#     print(f"num1 = {num1}, num2 ={num2}")
#
#
# sumnum(3, 4)
#
# sumnum(4)
# sumnum()

""" don't do this """
# def sumnum(num1=33, num2):  #SyntaxError: non-default argument follows default argument
#
#     print(f"num1 = {num1}, num2 ={num2}")


"""
    void sayhello(str name){
        str n = name ; 
        n = name;
        
        cout << "Hello " + name + endl;
    }
"""

#
""" functions ----> functions with unknown number of arguments """

#
# print()
# print("ahmed")
# print("=---", 'rr', 33, 555)
# print(2,34,55,6,7,77,77,7,77,7,7,7,3)

# def askforstudents(*students):  # *--> accept zero or more argument
#     print(students)    # tuple
#     for s in students:
#         print(f's ={s}, type(s) ={type(s)}')
#     else:
#         print('------------------------------------------- \n')
#
# askforstudents()
# askforstudents("ahmed",44,555,55,33.33, [44,444,44])
# askforstudents("ahmed",'mohamed', 'lina', 'mirna', 'test', 'abc', 'mahmoud')


# def askforinfo(name, *addintional_info):
#     print(name, addintional_info)
#
# askforinfo('masry', 444,4444, 'alex', 'test', True)


# def askforinfo(*addintional_info, name):
#     print(name, addintional_info)
#
# askforinfo(444,55,True,'iti', name='Masry')


# print(4,45,5,444, sep=',', end="#")
# print("Ahmed")


""" function with keyword arguments """


# def askforInfo(**info):  # function accept parameters inform of keyword=value --> argument
#     print(info)
#
# askforInfo()
# askforInfo(name='ahmed', city='alex')
# askforInfo(fname='ali', lname='mohamed',sep='ml')
# askforInfo(name='ddd', age=33)


def testfunction(num1, num2):
    res = num1 + num2
    return num1, num2, res  # tuple


rr = testfunction(3, 4)
print(rr, type(rr))
