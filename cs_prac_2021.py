##                                                                                                      
#                                                                  check prime


def isprime(x):
    if not isinstance(x, int):
        raise ValueError ("invalid literal for isprime() with base 10")
    for i in range(2, x):
        if x%i == 0:
            return False
    return True


##
"WAFP to generate random numbers between one and six every time it is called (stimulates dice)"

def dice():
    import random
    return random.randint(1, 6)


##
"""
write a python function to take three arguments - x,y and op. x and y are the integer
values and op will be an operator (+, -, *, /, %, //, **). The function should return the
result of the arithematic operation
"""

def calc(x, op , y):
    if not isinstance(op, str):
        raise ValueError ("The operator should be in string format")
    elif op == "*":
        return x*y
    elif op == '-':
        return x-y
    elif op == '+':
        return x+y
    elif op == '/':
        if y == 0:
            return "y cannot be zero"
        return x/y
    elif op == '==':
        return x == y
    elif op == '//':
        return x//y
    elif op == '%':
        return x%y
    elif op == 'is':
        return x is y
    elif op == '&':
        return x & y
    elif op == 'and':
        return x and y
    elif op == 'or':
        return x or y
    elif op == '**':
        return x**y
    elif op == '!=':
        return x != y
    else:
        raise ValueError ("")
##
"""
take three number and return largest
three int parameters
return max()
"""
def max_(*x):
    if not isinstance(x, str):
        raise ValueError ("invalid literal for max_()")
    return max(x)

##
"""
isarmstrong(x):
    one int input
    convert to string
    sum variable
    iterate over
    sum += i**3
    if sum == x:
    True
ispall(s):
    one string input
    if s[::-1] = s:
    return True
isprft(x):
    one int input
    find factors:
        factor = []
        for i in range(1, x):
            if x%i == 0:
            factor.append(i)
        return factors
    if sum(l) == x:
    return True
"""

def isarmstrong(x):
    if type(x) != int:
        raise TypeError ("invalid literal for isarmstrong() with base 10")
    if x<0:
        x /= -1
        x = int(x)
    x = str(x)
    sum_ = 0
    for i in x:
        sum_ += int(i)**3
    if sum_ != int(x):
        return False
    else:
        return True

def ispal(s):
    if type(s) != str:
        raise TypeError ("invalid literal for ispal()")
    if s[::-1] == s:
        return True
    else:
        return False

def isprft(x):
    if type(x) != int:
        raise TypeError ("isprft() takes number as input")
    if x<0:
        raise TypeError ("The domain of perfect number does not include negative number")
    factor = 0
    for i in range(1, x):
        if x%i == 0:
            factor += i
    if factor == x:
        return True
    else:
        return False
##
"""
factorial(n):
    check int type
    if n == 0:
    return 1
    elif n<0:
        raise ValueError ("invalid input, factorial function is only applicable for numbers greater or equal to zero ----->", n)
    fact = 1
    for i in range(1,n)
    fact *= i
    return fact
"""

def factorial(n):
    if type(n) != int:
        raise TypeError ("invalid literal for factorial() with base 10")
    if n == 0:
        return 1
    elif n<0:
        raise ValueError ("invalid input, factorial function is only applicable for numbers greater or equal to zero ----->", n)
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

##

def sumfloat(*x):
    sum_ = 0
    for i in range(len(x)):
        if not (type(x[i]) == int or type(x[i]) == float):
            raise ValueError ("type of one of the values given is not integer or floating point --------->", x[i])
        sum_ += x[i]
    return sum_

##
def removea(fromfilepath, tofilepath):
    try:
        from_ = open(fromfilepath, 'r')
        to_ = open(tofilepath, 'w')
        y = from_.readlines()
        for i in range(len(y)-1):
            if 'a' in y[i] or 'A' in y[i]:
                y.pop(i)
        to_.writelines(y)
    except FileNotFoundError:
        print("file not found")


##
def updatebin(filepath, roll, newmarks):
    try:
        import pickle
        freq = 0
        buffer = []
        f = open(filepath, 'rb')
        while True:
            y = pickle.load(f)
            if y[0] == roll:
                print("old Data :")
                print(y)
                y[2] = newmarks
                buffer.append(y)
                print("new Data :")
                print(y)
                freq += 1
            else:
                buffer.append(y)
        f.close()
        f = open(filepath, 'wb')
        f.writelines(y)
    except FileNotFoundError:
        print("file not found")
        return
    except EOFError:
        print("Data changed")
        print(freq, "rows affected")

##
def biggest(filepath):
    try:
        f = open(filepath, 'r')
        y = f.read().split()
        d = {}
        for i in y:
            d[len(i)] = i
        x = max(d)
        print("The largest word is", d[x])
    except FileNotFoundError:
        print("File Not Found")


        
def read_binary():
    import pickle
    fin=open("testfile.dat",'rb')
    try:
        fline = '{:<5}{:<15}{:>7}'.format("roll","name","marks")
        print(fline)
        while True:
            l=pickle.load(fin)
            data = '{:<5}{:<15}{:>7}'.format(l[0], l[1], l[2])
            print(data)
    except EOFError:
        pass

def display(filepath):
    try:
        f = open(filepath, 'r')
        import Data
        Data.stat(f.read())
    except FileNotFoundError :
        print("File Not Found!")
