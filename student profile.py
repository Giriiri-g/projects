d = {}
while True :
    print("""
1. add a student's profile
2. delete a student's profile
3. view student profile
""")
    x = int(input("\nplease enter which interaction to commit(1,2,3) :"))
    if x == 1:
        name = input("\nplease enter the name of the student :")
        roll = input("please enter the roll number of the student(05) :")
        clssec = input("please enter the class and section(11A) :")
        mrk = input("please enter the average marks :")
        d[name] = roll + clssec + mrk
    elif x == 2:
        name = input("\nplease enter the name of the student :")
        d.pop(name)
        print("profile deleted successflly")
    elif x == 3:
        name = input("\nplease enter the name of the student :")
        if name not in d:
            print("student not found")
            exit()
        print("name :", name)
        print("roll number :", d[name][:2])
        print("class and section", d[name][2:5])
        print("average marks :", d[name][5:])
