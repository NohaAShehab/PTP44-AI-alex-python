def ask_for_num(message='Enter a number'):
    while True:
        try:
            num = int(input(message))
        except Exception as e:
            print(f"--- please try again and {message}")
        else:
            return num

# def divnums():
#     num1 = ask_for_num("please enter first number: ")
#     num2 = ask_for_num("please enter second number: ")
#     if num2==0:
#         raise ZeroDivisionError("division by zero is not allowed ")
#     print(f"num1 ={num1}, num2 = {num2}")
#     res = num1/ num2
#     return res
#
# print(divnums())


def sumnums(num1 :int, num2:int):
    if isinstance(num1, int) and isinstance(num2, int):
        res = int(num1) + int(num2)
        return res

    raise ValueError("num1 and num2 must be integers ")

print(sumnums(4,4))
print(sumnums('ahmed', 4))
