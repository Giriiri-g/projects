#WAp to calculate si and ci

"""
s = p*t*r/100
inpt p
inpt t
inpt r
calc s
c = (p*(1+r/100)**t) - p
"""

p = float(input("please enter the principal amount :"))
t = float(input("Enter the time required to pay complete amount :"))
r = float(input("Enter the rate of interest :"))
print("This is your simple interest :", p*t*r/100)
print("This is you compound interest :", (p*(1+r/100)**t) - p)
