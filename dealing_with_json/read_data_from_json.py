

""" 1- open file """
import json
#
try:
    myobj = open('books.json', 'r')
except Exception as e:
    print(e)
else:
    print(myobj)

    """ read content """
    data = myobj.read()  # string ?
    # # print(data)
    jsondata = json.loads(data)  # loads function ---> accept string
    # # conver data to suitable python datatypes
    print(jsondata)

    """ another way """
    # all_data = json.load(myobj)  # accepts ---> file object
    # print(all_data)
    myobj.close()

""" the allbooks.json file ? """
#
# try:
#     myobj = open("allbooks.json", 'r')
# except Exception as e:
#     print(e)
# else:
#     data = myobj.read() # string
#     data = json.loads(data)# loads accept string
#     print(data)