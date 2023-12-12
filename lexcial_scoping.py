
"""
    variable define in the python script, python module
    variable with global scope ---> can be accessed anywhere in the python script
"""
course = 'python'  # global variable

# print(course)
# print(f'course: {course}')
# print(course.upper())


"""
    

"""


# def myfunction():
#     """ variable defined inside the function ---> scope --> local scope
#         local variable can be accessed only inside the function.
#     """
#     track = 'ai'  # track variable ---> local variable
#     print(f'track is {track}')
#
# myfunction()
# # print(track)  #NameError: name 'track' is not defined
#


""" use global variable inside the function ? """


def printCourse():
    """ print global variable from inside function """
    print(f" course = {course} --> from inside the function ")


# printCourse()

# def modifyglobalCourse():
#     course = 'machine learning01'  # new local variable
#     print(f" course = {course} --> after updating it  ")
#
#
# modifyglobalCourse()
# print(course)


# def modifyglobalCourse():
#     global course  # use the global one
#     course = 'machine learning01'  # new local variable
#     print(f" course = {course} --> after updating it  ")
#
#
# modifyglobalCourse()
# print(course)


# """ indentation and scoping """
#
# for i in range(5):
#     print(i)
#
# print(f"after for i = {i}")

""" check this """

# def outerfunction():
#     """ local variable can be accessed anywhere in the function """
#     city = 'Alex'  # local variable
#
#     def innerfunction():
#         print(f"from inner function city = {city}")
#
#     innerfunction()
#
#
# print("---- calling outer function --------")
# outerfunction()
#
#

""" modify local variable from inside inner function ? """


# def outerfunction():
#     """ local variable can be accessed anywhere in the function """
#     city = 'Alex'  # local variable
#
#     def innerfunction():
#         print(f"from inner function city = {city}")
#
#     # innerfunction()
#
#     def modifyCity():
#         city = 'Alexandria'  # new local variable in the inner function
#         print(f' after modify from the function >>> city={city}')
#
#     modifyCity()
#     print(city)
#
# outerfunction()
#
#
# print("---- calling outer function --------")
# outerfunction()
#


def outerfunction():
    city = 'alex'
    def modifycity():
        nonlocal city
        city ='alexendria'
        print(f"city ={city} from inside the modify func.")
    modifycity()
    print(city)


outerfunction()


























