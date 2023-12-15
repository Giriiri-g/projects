#WAP to find max of all the numbers in a list
#not using max() function
#                                                               max of numbers in a list
#                                                               ________________________




"""
MAX :
    ask for a LIST
    create a empty variable -> evar   __negative real numbers?
    for loop in char of l
    if char greater than evar
    overwrite evar by char
    out of loop
    print evar as max
"""



l = eval(input("please give your set of numbers :"))
evar = l[0]
for i in l :
    if i > evar :
        evar = i
print("\nThe maximum value of the given numbers is:", evar)
        

