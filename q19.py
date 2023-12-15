emp = {"rahul":60000, "jaha": 80000, "lol":50200, "alex":65000, "alice":30000}
intr = int(input("""add an employee                 : 1    fire an employee                : 2
give a raise to an employee     : 3    exit                            : 4
please give your interaction :"""))
if intr == 1:
    ad = input("please give your employee name :")
    sal = int(input("please give the salary of the employee :"))
    emp[ad] = sal
elif intr == 2:
    dl = input("please give the employee name to fire :")
    if dl in emp:
        emp.pop(dl)
    else:
        print("employee not found")
elif intr == 3:
    ad = input("please give your employee name :")
    sal = int(input("please enter the new salary of the employee :"))
    if ad in emp:
        emp[ad] = sal
    else:
        print("employee not found")
elif intr == 4:
    quit()
else:
    print("please enter the correct interaction")
