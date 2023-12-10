

""" describe myinfo"""
name = ['noha', 31, 'mansoura', 'iti']  # unlabele data

"dictionary comma key:value pair, doesn't allow key duplications"


"1- define a dictionary"
my_dict = {'name':'noha', 'age':31, 'city':'mansoura','name':"Noha Shehab"}
print(my_dict)

""" from python 3.7 --> ordered dict """

"""dict mutable datatype """
'modify values in the dict '
my_dict['city'] = 'mansoura'.upper()
print(my_dict)

my_dict['courses']=['python', 'mysql']
print(my_dict)


"""get len of dict """
print(len(my_dict))

""" check if value exists in dict """
print(31 in my_dict)  # check if value exists in dict keys

print("age" in my_dict)

""" loop over the dict ? """

for myitem in my_dict:
    print(f'myitem={myitem}, {my_dict[myitem]}')

# """ get dict keys """
# dkeys = my_dict.keys()
# print(dkeys)
# # for k in dkeys:
# #     print(k)
#
# dkeys = list(dkeys)
# print(dkeys)

""" get dict values """
dvalues = my_dict.values()
print(dvalues)
# for k in dkeys:
#     print(k)

dvalues = list(dvalues)
print(dvalues)

print(31 in my_dict.values())


""" get keys , values together """

ditems= my_dict.items()
print(ditems)

ditems = list(ditems)
print(ditems)

for k , v in my_dict.items():
    print(f'k={k}, v={v}')


""" update dict """

myd2 = {'courses':['django', 'ml1'], 'updated':1}
print(my_dict)
my_dict.update(myd2)
print(my_dict)

""" pop value of specific key from dict """

popped_vallue = my_dict.pop('name')
print(popped_vallue)
print(my_dict)

""" remove key value pair """

del my_dict['age'] #remove key value pair from memory
my_dict.clear()  # remove all value pairs from dict