import time
import random
def askforInt(message='Please enter number:'):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print(f"--- try again: {message}")



# num = input("please enter number ")
# print(num.isdigit())

def askforname(message='Please enter name:'):
    while True:
        name = input(message)
        if not name.isspace() and not name.isdigit():
            return name
        print("--- please enter valid name: ")


def generate_id():
    # id = round(time.time())
    # return  id
    id = round(random.randint(0, 1000000))
    return id


if __name__=='__main__':
    print(generate_id())