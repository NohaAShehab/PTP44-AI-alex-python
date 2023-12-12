
""" import module inside onther one ? """
# import modules_packages
#
# print(modules_packages.name)
#
# modules_packages.saywelcome('ali')

""" alias the module """

# import modules_packages as m
# print(m.name)

"""

    import pandas as pd 
    import numpy as np 
    import tensorflow as tf 
"""

# from modules_packages import saywelcome
# saywelcome("ahmed")
#
# from modules_packages import name
# print(name)

# from modules_packages import  saywelcome as sw
#
# sw('iti')


""" import packagename.modulename """
# import  iti.askforinputs
# print(iti.askforinputs.askforString())
#
# import  iti.askforinputs as myin
# print(myin.askforString())


""" import part of module in package"""

# from iti.askforinputs import  askforInt
#
# print(askforInt("please enter number: "))

# import ai
# ai.printHi()

# from ai import printHi
# printHi()

# from ai.testtting import  teststring
# name='ddd'
# print(teststring(name))

from ai import  teststring
print(teststring(44))
