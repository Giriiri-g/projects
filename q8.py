#take date as input and check if the date is valid
#                                                       check if date is valid
#                                                       ______________________


"""
take date input
check len of string for the correct format
dd/mm/yyyy
slice into two
consider leap year
according to month pick date
leap year :
    divisible by 4 and not by 100 = leap year
    check by dividing by 400 if yes leap year if not not leap year
"""




d = input("please enter your desired date :")
if len(d) < 8 or len(d) > 8:
    print("please enter the date in the correct format(DD-MM-YYYY)")
    exit()
DD = int(d[:2])
MM = int(d[2:4])
YYYY = int(d[4:8])
lpy = False
if YYYY%4 == 0:
    lpy = True
if YYYY%100 == 0:
    lpy = False
    if YYYY%400 == 0:
        lpy = True
if MM > 12 or MM < 0:
    print("This is not a valid date, please provide with a appropriate date.")
    exit()
if DD > 31 or DD < 0:
    print("This is not a valid date, please provide with a appropriate date.")
    exit()
    
#___________________________________________________________________________
    
if lpy == False:
    if MM == 1 or MM == 3 or MM == 5 or MM == 7 or MM == 8 or MM == 10 or MM == 12:
        if DD <= 31:
            print(DD, "-", MM, "-", YYYY, "is a valid Date.")
        else:
            print("This is not a valid Date.")
    elif MM ==4 or MM == 6 or MM == 9 or MM == 11:
        if DD <= 30:
            print(DD, "-", MM, "-", YYYY, "is a valid Date.")
        else:
            print("This is not a valid Date.")
    else:
        if DD<=28:
            print(DD, "-", MM, "-", YYYY, "is a valid Date.")
        else:
            print("This is not a valid Date.")
elif lpy == True:
    if MM == 1 or MM == 3 or MM == 5 or MM == 7 or MM == 8 or MM == 10 or MM == 12:
        if DD <= 31:
            print(DD, "-", MM, "-", YYYY, "is a valid Date.")
        else:
            print("This is not a valid Date.")
    elif MM ==4 or MM == 6 or MM == 9 or MM == 11:
        if DD <= 30:
            print(DD, "-", MM, "-", YYYY, "is a valid Date.")
        else:
            print("This is not a valid Date.")
    else:
        if DD<=29:
            print(DD, "-", MM, "-", YYYY, "is a valid Date.")
        else:
            print("This is not a valid Date.")
