
"1- define a list "
l = []
mylist = list()


""" list is mutable datatype ,can hold different data from differnt types"""

myl = [2,33.33 , True, 'iti', None, 'iti', ['python', 'ml1']]

"1- get len of list"

print(len(myl))
"""1- access elements using index """
print(myl[4])
print(myl[6][1])
"2- list is mutable data type =---< modify elements at existing index  "
myl[4]='updated'
print(myl)
# myl[20]='updated' # IndexError: list assignment index out of range

""" count element occurence in the list """
print(myl.count("iti"))
""" get index of element in the list ? first occurrence """
print(myl.index('iti'))

"""loop over list ?  """
count = 0
# for item in myl:
#     print(f" index={count}item = {item}")
#     count +=1

for abbass in myl:
    print(f"{abbass}")

for index, item in enumerate(myl): # generate index for iterable
    print(f"index: {index}, item: {item}")


""" ---> check if elemen exists in list """

print("ml1" in myl)
print('n' in "noha")

"append element to the list ? at the end of the list. "

myl.append("new element ")
print(myl)

""" insert element in certain position"""

myl.insert(4, 'inserted_element')
print(myl)


""" pop element from list ---> pop last element  ?"""
popped_element = myl.pop()  # return with the popped_element
print(popped_element)
print(myl)

""" pop element at specific index """

popped_element = myl.pop(4)
print(popped_element)
print(myl)

""" remove element from list  --> remove first occurrence of """
myl.remove('iti')
print(myl)

# for item in myl:
#     if 'ml1' in item:
#         print("found")

print("m" in "mirna")  # in operator --> string
print("iti" in myl) # in operator ---> list

""" check if ml1 in the list or nested list """
print('ml1' in myl)

# for item in myl:
#     if 'ml1' in item:
#         print("--- found ")

# for item in myl:
#     if type(item)== type([]):
#         if 'ml1' in item:
#             print(f"found in {item}")
# print("-----")

""" isinstance """

print(isinstance("iti", int ))
print(isinstance("mirna", str ))


# print("ml1" in myl)
# for item in myl:
#     if isinstance(item, list):
#         if 'ml1' in item:
#             print(f"found in {item}")
# print("-----")

""" concat list ? """
l1 = ["items", "iti", "Mydata", 33,444.44,['ff', 'fff']]
l2= ['python', 'ml1', 'la']
l3 = l1+ l2  # generate new list
print(l3)

""" extend a list ? """

l1.extend(l2)  # update l1 with items of l2
print(f"l1={l1}")

""" sort the list ?  ===> list elements must be from the same type  """
names = ['ahmed', 'test', 'ali', 'sara' , 'Nawal', 'Mohamed']
# names.sort()  # sort data in the same object (same list)
# print(names)

names.sort(reverse=True)
print(names)

""" reverse the list ..."""
myl.reverse()
print(myl)

""" empty lists is falsy value"""
ll = []
if ll:
    print("---hii")
else:
    print("==--bye----")

""" min, max ---> items in list must be from the same type > ,< """

# myl.__add__(mylist)


""" cast string to a list """
message = 'helloGhaza'
message_list = list(message)  # put each char as an element in the list
print(message_list)

""" list of strings ---> join them as one string """

names=['ahmed','mohamed', 'ali', 'test', 'iti']

names_str = '_'.join(names)
print(names_str)

""" convert names_str to a list """
names_lst = names_str.split("_")
print(names_lst)