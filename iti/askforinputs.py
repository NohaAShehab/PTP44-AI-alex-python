

def askforInt(message="Please enter a number"):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print("Please enter a valid number")



def askforString(messsage="Please enter a string"):
    while True:
        mystrs= input(messsage)
        if mystrs.isalpha():
            return mystrs
        print("---- please enter valid string ----")
