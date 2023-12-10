
"tuple like  a list ---> tuple is immutable data type ? -- after creation , cannot be changed"



"1- define a tuple "
t = ()
mytuple = tuple()
# 
# 
""" tuple is immutable datatype ,can hold different data from differnt types"""
# 
myt = (2,33.33 , True, 'iti', None, 'iti', ['python', 'ml1'])
#
# myt[2]= 'updated'  #TypeError: 'tuple' object does not support item assignment

"1- get len of tuple"
# 
print(len(myt))
"""1- access elements using index """
print(myt[4])
print(myt[6][1])

""" count element occurrence in the tuple """
print(myt.count("iti"))
""" get index of element in the tuple ? first occurrence """
print(myt.index('iti'))
# 
# """loop over tuple ?  """
count = 0
# for item in myt:
#     print(f" index={count}item = {item}")
#     count +=1

# for abbass in myt:
#     print(f"{abbass}")

# for index, item in enumerate(myt): # generate index for iterable
#     print(f"index: {index}, item: {item}")


""" ---> check if element exists in tuple """

print("ml1" in myt)
#




# 
""" concat tuple ? """
t1 = ("items", "iti", "Mydata", 33,444.44,['ff', 'fff'])
t2= ('python', 'ml1', 'la')
t3 = t1+ t2  # generate new tuple
print(t3)



""" empty tuples is falsy value"""
tt = ()
if tt:
    print("---hii")
else:
    print("==--bye----")
# 
""" min, max ---> items in tuple must be from the same type > ,< """
print(min(4,3,5,6))

#
# 
""" cast string to a tuple """
message = 'helloGhaza'
message_tuple = tuple(message)  # put each char as an element in the tuple
print(message_tuple)
# 
""" tuple of strings ---> join them as one string """
# 
names=('ahmed','mohamed', 'ali', 'test', 'iti')
# 
names_str = '_'.join(names)
print(names_str)
# 
""" convert names_str to a tuple """
names_lst =tuple( names_str.split("_"))
print(names_lst)

""" why we use tuples """

""" tuple of one item ? """
courses= ("python",)
print(courses, type(courses))




