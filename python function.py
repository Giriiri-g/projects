from sys import *
dg = 0
alpha = 0
vow = 0
void = 0

#1. Write a function which takes radius of circle as a parameter and returns its area and circumference.

def circ(radius, unit):
    if str(radius).isalnum() == True:
        raise ValueError ("invalid literal for circ() with base 10")
    elif unit == "cm" or unit == "Cm":
        return ("area =", 3.14159*rad*rad,"cm^2", "circumference =", 2*3.14159*rad, "cm")
    elif unit == "mm" or unit == "Mm":
        return ("area =", 3.14159*rad*rad,"mm^2", "circumference =", 2*3.14159*rad, "mm")
    elif unit == "m" or unit == "M":
        return ("area =", 3.14159*rad*rad,"m^2", "circumference =", 2*3.14159*rad, "m")
    else:
        raise ValueError ("invalid unit for circ() with cm, mm, m")

#2. Write a function that takes basic pay, number of days as input parameters. Default value of number of days is to be set as 30. 
#The function should return the total salary as basic + 20% of basic as DA. 

def sal(bp, nod = 30):
    ys = (bp/nod)*365.5
    da = ys*0.2
    return ys + da

#3. Write a function which takes as input an arbitrary long string and outputs its stats such as number of digits, number of vowels, number of spaces etc.

def stat():
    x = stdin.readlines()
    x = str(x)
    print("\n\n\n\n\n")
    for i in x:
        if i.isdigit() == True:
            dg += 1
        elif i.isspace() == True:
            void += 1
        elif i in ['a', 'e', 'i', 'o', 'u']:
            vow += 1
        elif i.isalpha() == True:
            alpha += 1
    print("digits :", dg)
    print("whitespaces :", void)
    print("vowels :", vow)
    print("Alphabeta :", alpha)
