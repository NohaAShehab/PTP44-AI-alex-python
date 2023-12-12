
print("---------")
# num= int(input("Enter a number: "))
# print(num)

# num= input("Enter a number: ")
# if num.isnumeric():
#     num=int(num)
#     print(num)


#############################################

# try:
#     num = int(input("Enter a number: "))
#     print(num)
#     print("-------------------------")
#     print(num/0)
# except:
#     print("--- problem happened ----")


# try:
#     num = int(input("Enter a number: "))
#     print(num)
#     print("-------------------------")
#     print(num/0)
# except Exception as e :
#     print(f"--- problem happened {e} ----")

# print(int(input("eee")))

# try:
#     num1 =int(input("Enter a number : "))
#     num2 = int(input("Enter another number : "))
#     res = num1/num2
#     # print(name)
# except ValueError as ve:
#     print(ve)
#     print("-- num1 and num2 must be integers  ")
#
# except ZeroDivisionError as ze :
#     print(ze)
#     print("---- cannot divided by zero")
#
# except Exception as e:
#     print(e)
#
# else:
#     """ this block will be executed if there is no problem"""
#     print(f'res = {res}')
# finally:
#     print("============ this block executed always ========")
#
# print("-----------------------")
#


def askfornumber():
    try:
        num = int(input("Enter a number: "))
    except Exception as e:
        print(e)
        return False
    else:
        res = num*10
        print(res)
        return res
    finally:
    #     """ finally precedes return in the function """
    #     print("--- goodbye function endded ")
        print("-------------------")


"""

    fun(4,5): 
    [4,5,6,7,8]
    
    -------------------
    
    'abdulrahmanvxz'
    
    abdu
    lr
    ahm
    anvxz
    
    ['apple', 'banana', 'cherry']
    noha 
    -----
    n
    p 
    -pp--
    
    apple ===> won the game 
    
    == > you lose the game 
"""

r=askfornumber()
print(r)