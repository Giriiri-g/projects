#WAP to check if a number if prime or not

#                                                   check prime
#                                                   ___________

"""
input number
find factor -> range beteween 2 and less than num
if num % i == 0 notprime
if none found fn == prime
"""

def isprim() :
    isprim = True
    nm = int(input("please give a number to check if prime :"))
    for i in range(2,nm):
        if nm % i == 0:
            isprim = False
    if isprim == True:
        print("The given number is Prime")
    if isprim == False:
        print("The given number is not a Prime number")

isprim()
