

"""



"""
import os

""" 1- time """
import time
print(time.time())  #current time stamp

import time

# formatted_date = time.strptime(" 17 Dec 2023",
#                                " %d %b %Y")
# print(formatted_date)  # struct_time

import time
#
# formmated_time = time.strptime("12/17/2023 9:56", "%m/%d/%Y %H:%M")
# print(formmated_time)
#

formmated_time = time.strptime("17-12-2023 9:56", "%d-%m-%Y %H:%M")

print(formmated_time)
# formmated_time2 = time.strptime("3/30/2023 9:56", "%m/%d/%Y %H:%M")
# print(formmated_time2 > formmated_time)

""" os """

# print(os.getcwd())
# print(os.getlogin())
# print(os.system('ls -la'))
#
# os.system('touch abc')
# os.system('mkdir mydir')

""" re """

import  re

""" check if string  ---:> follow specific pattern ? 
    emails
    urls
    ip address
    phone number
    password
"""

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

email = input("Please enter your email:  ")

# res = re.match(pattern, email)
# """ if strings matches the pattern --> re.match will return with match object ?
#     return with match object if the beginning part of the string matches the pattern
# """
# print(res)
#
# if res:
#     print("--- valid emails ---")
# else:
#     print("---- not valid ")

res = re.fullmatch(pattern, email)
""" if strings matches the pattern --> re.match will return with match object ?
    return with match object if the beginning part of the string matches the pattern 
"""
# print(res)
#
# if res:
#     print("--- valid emails ---")
# else:
#     print("---- not valid ")