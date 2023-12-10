
""" ranges """

""" generate list of numbers 1 , 10 ? """
nums = []
# count = 0
# while True:
#     count +=1
#     nums.append(count)
#     if count == 10:
#         break
#
# print(nums)

""" range function """

# myrange = range(10)
# print(myrange)  # range object start=0 , end= 10 , step=1
#
# for num in myrange:
#     nums.append(num)
#
# print(nums)

myrange = range(0,11,2)
print(myrange)  # range object start=0 , end= 10 , step=1

for num in myrange:
    nums.append(num)

print(nums)

""" range can be casted to a list """

myr2= list(myrange)
print(myr2)

""" generate descending list """
rrr = range(10,-1,-1)
print(list(rrr))


""" break , continue ? """

""" write an application to simuate atm password check process ? """

# for turn in range(1,4):
#     password = input("Enter your password: ")
#     if password =='abc':
#         print("--- logged in successfully ---")
#         break
#     else:
#         print("----please enter valid password ")
#
# if turn==3:
#     print("--- account has been locked")


# for turn in range(1,4):
#     password = input("Enter your password: ")
#     if password =='abc':
#         print("--- logged in successfully ---")
#         break
#     else:
#         print("----please enter valid password ")
#
# else:
#     print("--- account has been locked ")
#     print("---- this block will be executed if the loop wasn't broken ")



# for item in range(10):
#     print(f" item ={item}")
#     if item==4:
#         break
#
# else:
#     print("""--- this block will be executed if block wasn't broken,,
#          for executed to its end ----""")

for i in range(3):
    password =  input("please enter your password: ")
    if password == "abc":
        print("login successful")
        break
    else:
        print("-----invalid password-----")
else:
    print("---- your account has been locked --------")