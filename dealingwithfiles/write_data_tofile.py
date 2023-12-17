"""

dealing with db, files, cloud , network ---> wrap code between try and except
"""

""" 
    write data to the file
    
    when you try to open file with mode w --> 
    if file doesn't exist -> python will try to create it
    - permissions ? -
    
    when you open file with w mode - -> 
    python will start writing to file from the beginning of the file
    remove old content 
"""
try:
    fileobj = open("users.txt", 'w')  # TextIOWrapper object
except Exception as e:
    print(e)
else:
    print(fileobj)
    # fileobj.write("############################\n")
    # fileobj.write("---- we support hamas ----\n")
    # fileobj.write("---- ITI ------")
    """ write lines"""
    fileobj.writelines(['ahmed\n', 'ali\n', 'iti\n', 'test\n', '10'])
    fileobj.close()