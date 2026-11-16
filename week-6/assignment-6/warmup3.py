#   print(name)
#         ^^^^
#NameError: name 'name' is not defined

def getName():
    name = input("Enter name: ")
    return name

studentName = getName()
print(studentName)