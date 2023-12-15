#WAP to find a element in a list without index()

#                                                   Index of a element
#                                                   __________________

"""
input search
input list = l
for i in range(0,lem(l))
if l[i] = srch:
    ntfnd = False
    print element found at index, i, "element =", srch
out loop
if ntfnd = True:
    print("element not found")
"""

l = eval(input("please give your desired list :"))
srch = input("please enter a element of your choice to search :")
nt = True
for i in range(0,len(l)):
    if l[i] == srch:
        nt = False
        print("element found at index", i, "; element =", srch)
if nt == True:
    print("element not found")
