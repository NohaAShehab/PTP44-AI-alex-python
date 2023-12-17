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
    fileobj = open("mycv.txt", 'a')  # TextIOWrapper object
except Exception as e:
    print(e)
else:
    print(fileobj)
    fileobj.write("Hello Ghaza\n")
    fileobj.write("----------------------------------------\n")
    fileobj.close()