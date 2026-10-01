def addstu_man():
    stu_data = []
    q = "y"
    while q.lower() == "y":
        s = input("Enter student name: ")
        stu_data.append(s)
        q = input("Type 'y' if you wish to continue adding and 'n' if you don't: ")
    return stu_data

def searchstu_man(stu_data):
    name = input("Enter name to search: ")
    if name in stu_data:
        print("Student",name," found in the record")
    else:
        print("Student",name," not found.")



students = addstu_man()
searchstu_man(students)
