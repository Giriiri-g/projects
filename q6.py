#WAP to take a number as input and print the multiplication table of the number


#                                                               Q6 print multiplication table
#                                                               _____________________________



"""
input number
for loop
range 10
print(num, "\b*", i, "=", num*i)
"""

num = int(input("please enter the number that you want the multiplication table for :"))
for i in range(11) :
    print(num, "*", i, "=", num*i)
