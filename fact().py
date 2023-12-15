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
