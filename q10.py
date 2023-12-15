#WAP to find the factorial of a given number

#                                                           give the factorial
#                                                           __________________

"""
input the number
int(num)
i = 0
while loop
i<= num
factorial = factorial*i
out loop
print(factorial)
"""





fctn = int(input("please enter the desired number to find the factorial of :"))

i = 1
fct = 1
while i <= fctn:
    fct *= i
    i += 1
print(fct)