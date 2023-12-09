

"1- define a string "

name = ''
email= 'test@gmail.com'

"2- get len of the string"
print(len(name), len(email))

"3- count char occurence in the string "
print(email.count('i'))

"4- string is treated like an array ,,,, access string parts using index, start from 0"

print(email[10])

""" slicing the string """
print(email[1:4])
print(email[1:])
print(email[:11])
print(email[::])
print(email[::2])
print(email[::-1])

"""5- concatenating the string """

fname = 'noha '
midname= 'abdelhady '
lname='shehab'

# fullname = fname +  midname + midname + lname
# print(fullname)

"string intepolation ? "
fullname = fname +  midname * 2 + lname
print(fullname)

""" string is immutable datatype """
# email[10]='@'


""" get index of char in the string ===> index ---> index of the first occurrence of the char """
name = 'iti'
print(name.index('i'))


""" operations on the string --- > """
""" iterate over the string """

for char in 'noha':
    print(char)

""" format the string """
no_of_students = 19
coursename='python '
# msg = "we have "+ no_of_students + "students in "+ coursename
#
# print(msg)

# tmp = "we have {0} students in {1}"
# res = tmp.format(no_of_students, coursename)
# print(res)
# res =  tmp.format(coursename, no_of_students)  # return new string
# print(res)

# 'keyword arguments'
# tmp = "we have {numstudents} students in {course}"
# # print(tmp.format(course=coursename, numstudents=no_of_students))
#
#
# """f-format string--> depend in existing variables in the memory  """
#
# for char in 'iti':
#     # print("char = " + char)
#     print(f"char = {char}")
#
#
# 'check string content ---> '
# name= 'ahmed'  # string
# grade = "10" # strings
#
# print(grade.isalpha()) # return True if strings consists only from alphas (a-z)
#
# print(grade.isnumeric())  # return True if string consists only from digits (0-9)

# message = ' '
# print(message.isspace())


""" ask user to enter string? """

name = input('Enter your name: ')
print(name, type(name))

""" ask user to enter 2 numbers num1, num2 ----> res = num1 + num2 """
num1 = input("plese enter num1: ")
num2 = input("please enter num2: ")
if num1.isdigit() and num2.isdigit():
    res = int(num1) + int(num2)
    print(res, type(res))


""" format string to upper/ lower / title/ capitalize"""
name = 'noha shehab'
print(name.upper())
print(name.lower())
print(name.capitalize())  # first char
print(name.title())  #



