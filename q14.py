#WAP to check if a given number is a perfect number or not

#                                                           check perfect number
#                                                           ____________________


"""
input num
perfect number
6 -> 1,2,3(factors)
for loop
range 1,num
factor =>  if num % i == 0
if factor found add it to list
sum of list
if sum == num:
    it is a perfect number
important execption num!<1
"""


prfct = int(input("please anter a number to check if it is a perfect number :"))
if prfct<1:
    print("The given number is not a perfect number")
    quit()
fct = []
for i in range(1,prfct):
    if prfct % i == 0:
        fct.append(i)
if sum(fct) == prfct:
    print(prfct, "is a perfect number")
else:
    print("The given number is not a perfect number")
