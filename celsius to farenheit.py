#                                                       convert celsius to farenheit and farenheit to celsius.
#                                                       ______________________________________________________
#input celsius or farenheit
#and how much degrees
#convert and print in same statement
#dec



"""
ch = input("c or f")
dg = input("quantity")
if ch == c:
    print(calculate f)
elif ch == f:
    print(calculate c)
"""

import time
while True :
    print("\n\n__________________________________________________________________________________\n")
    time.sleep(1.5)
    ch = input("Please give your units in C ->(celsius) or F ->(farenheit):")
    dg = float(input("Please enter the degrees :"))
    if ch == "C":
        time.sleep(1)
        print("\n\n", dg, "celsius degrees =", 1.8*dg + 32, "farenheit")
    elif ch == "F":
        time.sleep(1)
        print("\n\n", dg, "farenheit degrees =", 5*(dg-32)/9, "celsius")
    elif ch == "exit" or ch == "Exit":
        exit()
    else :
        time.sleep(0.5)
        print("\n\nplease enter an appropriate unit such as C or F\n\n\n")
