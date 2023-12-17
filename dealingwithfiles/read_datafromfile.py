"""

dealing with db, files, cloud , network ---> wrap code between try and except
"""

try:
    fileobj= open("names.txt", 'r')  #TextIOWrapper object
except Exception as e:
    print(e)
else:
    print(fileobj)
    """ to get the data """
    data = fileobj.read()  # read all file content into one string ...
    print(data)

    """ move filepointer to the beginning of the file """
    fileobj.seek(0)
    """ read data from file line by line"""
    lines = fileobj.readlines()  # read filecontent into a list ---?
    print(lines)
    """ loop over the object to get lines """
    # lines = []
    # for l in fileobj:
    #     lines.append(l)
    # print(lines)
    fileobj.close()