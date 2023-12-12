
""" every .py file is a python module """

# print("--- welcome to my first python module -----")
name = 'ahmed'
email = 'ahmed@gmail.com'


def saywelcome(name):
    print(f"welcome {name} to python course")



""" where is main in python ? 

    python consider all the module to main 
"""
"if I want somelines must be run only when this module run"

if __name__=='__main__':
    print("--- welcome to my first python module -----")

