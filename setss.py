

"""
remove duplicates
un-ordered datatypes
no index for elements
"""

mys = set()
myset = {"ahmed", "iti", "banana", 'iti', 333, True, 33.33, None}
print(myset)

""" get len """
print(len(myset))

""" add element to the set """
myset.add(333)
print(myset)

"""pop element from the set """

popped = myset.pop()
print(popped)
print(myset)


""" remove element from the set """
myset.remove('iti')
print(myset)

""" update set ?  """
s1 ={"pizza","cheese", 'banana'}

myset.update(s1)
print(myset)


"check this "
# data = {"ahmed", "iti", "banana", 'iti', 333, ('python', 'machine learning', 33)}
# print(data)

# data = {"ahmed", "iti", "banana", 'iti', 333, ['python', 'machine learning', 33]}
# print(data)

"""  set accepts only hashable types in python ---> immutable datatypes int , str, float, none , tuple """

"variable ==? string len 100 "

# "iti", "iti"

# ss = {{"pizza","cheese","dddd"}, 44,444} #unhashable type: 'set'


""" noha ? 2 """

" this is itiiti iti "

'noha ---> nh'

""" iti ---> 0 , 2"""

"""
    3 
    
    [ [1], [2,4], [3,6,9] ]
    
    1  --> 1*1
    
    2 --> 2*1 , 2*2
    
    3 --> 3*1 ,3*2 , 3*3
    
"""
