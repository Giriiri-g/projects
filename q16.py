#WAP to find the frequency of vowels, digits, white spaces in a given string

#                                                                   #count vowels, digits, white spaces

"""
input string
l = s[::1]

"""

cnsn = 0
dgt = 0
vwl = 0
spc = 0
s = input("please enter a string to analyse :")
l = list(s)
for i in l:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vwl += 1
    else:
        cnsn += 1
    if i.isdigit():
        dgt += 1
    if i == " " :
        spc += 1
print("\nThese are the frequency of variable characters\n")
print("consonents   :", cnsn)
print("digits       :", dgt)
print("vowels       :", vwl)
print("white spaces :", spc)
