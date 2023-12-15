from sys import *
import time




#                                                               Finding factors of a number


#________________________________________________________________________________
def fact(x):
    if isinstance(x, str) == True:
        raise ValueError ("invalid literal for fact() with base 10")
    if isinstance(x, int) == False:
        raise ValueError ("invalid literal for fact() with base 10")
    l = []
    for i in range(1, x):
        if  x%i == 0:
            l.append(i)
    return l
#________________________________________________________________________________


#                                                               finding algebric roots of quadratic equation

#___________________________________________________________________________________________________
def aroot(a, b, c):
    """3 arguments required. a,b,c as the coefficients of equation.
    Any argument left behind will be considered as Zero as default
    order mismatch will not be considered as an Error (will be considered as human Error)
    output will be given in any order of roots
    only gives algebric roots of quadratic equations"""
    x = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    y = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    return (x,y)
#___________________________________________________________________________________________________



#                                                           Temperature conversion


#_______________________________________________________________________________________________
def temp(dg, ch):
        if ch == "C":
            print("\n\n", dg, "celsius degrees =", 1.8*dg + 32, "farenheit")
        elif ch == "F":
            print("\n\n", dg, "farenheit degrees =", 5*(dg-32)/9, "celsius")
        else :
            raise ValueError ("\n\nplease enter an appropriate unit such as C or F\n\n\n")
#_______________________________________________________________________________________________


#                                                           character frequency

#_____________________________________________________________________________________
def cf(d):
    if isinstance(d, str) == False:
        raise ValueError ("invalid literal for cf()")
    cf = {}
    for i in d :
        if i in cf:
            cf[i] += 1
        if i not in cf:
            cf[i] = 1
    for i in cf:
        print(i, ":", cf[i])
#_____________________________________________________________________________________


#                                                       check prime


#___________________________________________________________________________
def isprime(x):
    if isinstance(x, str) == True:
        raise ValueError ("invalid literal for isprime() with base 10")
    if isinstance(x, int) == False:
        raise ValueError ("invalid literal for isprime() with base 10")
    for i in range(2, x):
        if x%i == 0:
            return False
    return True
#___________________________________________________________________________



#                                                       check perfect


#_______________________________________________________________________________
def prft(n):
    if isinstance(n, str) == True:
        raise ValueError ("invalid literal for prft() with base 10")
    if isinstance(n, int) == False:
        raise ValueError ("invalid literal for prft() with base 10")    
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False
#_______________________________________________________________________________




#                                                       decimal conversion


#___________________________________________________________________________________________________________________________________________
def dec(deci, base):
    if base == 2:
        sum_ = 0
        x = 1
        for i in str(deci):
            if i not in ['0','1']:
                raise ValueError ("invalid literal for dec() with base 2:", deci)
            sum_ += int(i)*2**(len(str(deci))-x)
            x += 1
        return sum_
    elif base == 8:
        sum_ = 0
        x = 1
        for i in str(deci):
            if i not in ['0','1', '2', '3', '4', '5','6', '7']:
                raise ValueError ("invalid literal for dec() with base 8:", deci)
            sum_ += int(i)*8**(len(str(deci))-x)
            x += 1
        return sum_
    elif base == 16:
        sum_ = 0
        x = 1
        for i in str(deci):
            if i not in ['0', '1', '2', '3', '4', '5', '6', '7','8','9','A','B','C','D','E','F']:
                raise ValueError ("invalid literal for dec() with base 16:", deci)
            if i == 'A':
                i = 10
            if i == 'B':
                i = 11
            if i == 'C':
                i = 12
            if i == 'D':
                i = 13
            if i == 'E':
                i = 14
            if i == 'F':
                i = 15
            sum_ += int(i)*16**(len(deci)-x)
            x += 1
        return sum_
    else:
        raise ValueError ("invalid literal for dec() with base 2, 8, 16:", base)
#___________________________________________________________________________________________________________________________________________





#                                                       area and circumference of a circle

#_________________________________________________________________________________________________
def circ(radius, unit):
    dg = 0
    alpha = 0
    vow = 0
    void = 0
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
#_________________________________________________________________________________________________




#                                                                   total sal


#__________________________________________
def sal(bp, nod = 30):
    ys = (bp/nod)*365.5
    da = ys*0.2
    return ys + da
#__________________________________________





#                                                                   statistics of a string



#____________________________________________________________________
def stat(x):
    dg = 0
    void = 0
    vow = 0
    alpha = 0
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
#____________________________________________________________________



#                                                                                       check validity of date



#______________________________________________________________________________________________________________
def vdate(DD, MM, YYYY):
    if isinstance(DD, str) == True:
        raise ValueError ("invalid literal for vdate() with base 10")
    if isinstance(DD, int) == False:
        raise ValueError ("invalid literal for vdate() with base 10")
    if isinstance(MM, str) == True:
        raise ValueError ("invalid literal for vdate() with base 10")
    if isinstance(MM, int) == False:
        raise ValueError ("invalid literal for vdate() with base 10")
    if isinstance(YYYY, str) == True:
        raise ValueError ("invalid literal for vdate() with base 10")
    if isinstance(YYYY, int) == False:
        raise ValueError ("invalid literal for vdate() with base 10")
    if DD>0 or DD<32: 
        return False
    if MM>0 or MM< 13: 
        return False
    if YYYY>0: 
        return ValueError ("please enter the date in the correct format(DD, MM, YYYY)")
    
    lpy = False
    if YYYY%4 == 0:
        lpy = True
    if YYYY%100 == 0:
        lpy = False
        if YYYY%400 == 0:
            lpy = True
    
    if MM in [1, 3, 5, 7, 8, 10, 12]:
        if DD <= 31:
            return True
        else:
            return False
    elif MM in [4, 6, 9, 11]:
        if DD <= 30:
            return True
        else:
            return False
    else:
        if lpy == True:
            if DD<=29:
                return True
            else:
                return False
        if lpy == False:
            if DD<=28:
                return True
            else:
                return False
#______________________________________________________________________________________________________________





#                                                                                       factorial


#_______________________________________________
def fct(x):
    fct = 1
    for i in range(1, x+1):
        fct *= i
    return fct
def fct_(x):
    if x==0:
        return 1
    else:
        return x*fct_(x-1)
#_______________________________________________



#                                                                                   check palindrome



#___________________________________________________________________________________

def ispal(x):
    if isinstance(x, str) == False:
        raise ValueError ("SyntaxError: invalid syntax")
    rev = x[::-1]
    if x == rev:
        return True
    else:
        return False
#___________________________________________________________________________________


#                                                  log




#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
def log():
    f = open("reg.txt", "a")
    named_tuple = time.localtime()
    time_string = time.strftime("%d/%m/%Y", named_tuple)
    f.write("\n")
    f.write(time_string)
    f.write("\n")
    print("log :")
    x = stdin.readlines()
    x = str(x)
    print("\n\n\n\n\n")
    stdreg = ["HARINE M", "HARINI S", "HEMA R", "INDHRA N", "INDIRA YALINI J", "JANANI T", "KEERTHANA DEVI M", "LAKSHMI PRABAA S", "MONA CHRISLINE V", "MONISHA J", "MOSHIKA J", "PRASHITHA R", "PREETHI T", "SHALINI S", "SHIMRUTHIEE R", "SIVADHARSHINI S", "SUBHA DHARANI P", "VENOTHINI S", "VINCENT CLAUDIA S", "ARUL MARTIN M", "DHANA PRAKASH S", "DHANURAJA T", "DHANUSH KUMAR B", "HEMANTH KUMAR M", "JAHAGANAPATHI S", "JOTHISH RS", "MADHESH P", "MONISH A", "MUGILAN K", "POTRI SELVAN R S", 'RANJITH KANNA A', 'SHYLESH KUMAR V', 'SUJAN S', 'THILACK R', 'VIJAY MITHRAN R S', 'VIJEYA KARTHY L', 'VILMER SAMUEL R']
    for i in stdreg:
        if i not in x:
            f.write(i)
            f.write("\n")
            print(i)
    f.close()
#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________





#                                                                               encrypt


#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
def decrypt(x):
    cipher = ['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9', '3', '2', '3', '8', '4', '6', '2', '6', '4', '3', '3', '8', '3', '2', '7', '9', '5', '0', '2', '8', '8', '4', '1', '9', '7', '1', '6', '9', '3', '9', '9', '3', '7', '5', '1', '0', '5', '8', '2', '0', '9', '7', '4', '9', '4', '4', '5', '9', '2', '3', '0', '7', '8', '1', '6', '4', '0', '6', '2', '8', '6', '2', '0', '8', '9', '8', '6', '2', '8', '0', '3', '4', '8', '2', '5', '3', '4', '2', '1', '1', '7', '0', '6', '7', '9']
    if isinstance(x, str) == False:
        raise ValueError ("invalid string")
    x = list(x)
    decrypt = ""
    for i in range(len(x)):
        decrypt += chr(ord(x[i]) - int(cipher[i]))
    return decrypt
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________






#                                                                               decrypt


#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
def encrypt(x):
    cipher = ['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9', '3', '2', '3', '8', '4', '6', '2', '6', '4', '3', '3', '8', '3', '2', '7', '9', '5', '0', '2', '8', '8', '4', '1', '9', '7', '1', '6', '9', '3', '9', '9', '3', '7', '5', '1', '0', '5', '8', '2', '0', '9', '7', '4', '9', '4', '4', '5', '9', '2', '3', '0', '7', '8', '1', '6', '4', '0', '6', '2', '8', '6', '2', '0', '8', '9', '8', '6', '2', '8', '0', '3', '4', '8', '2', '5', '3', '4', '2', '1', '1', '7', '0', '6', '7', '9']
    if isinstance(x, str) == False:
        raise ValueError ("invalid string")
    x = list(x)
    encrypt = ""
    for i in range(len(x)):
        encrypt += chr(ord(x[i]) + int(cipher[i]))
    return encrypt
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________





#                                                               pow

#__________________________________________________
def pow_(x, n):
    """
evaluates and returns x^n
"""
    if n==0:
        return 1
    else:
        return x*pow_(x, n-1)
#__________________________________________________
