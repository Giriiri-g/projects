#WAP to find the sum of digits of a given number

#                                                           sum of digits
#                                                           _____________



"""
input num
for i in range len(num+1)
sum += s.index(i)
out loop
print(sum of digits of, num, "=", sum)
"""

while True:
    dsum = []
    snum = input("please enter your number :")
    for i in snum:
        dsum.append(int(i))
    print(sum(dsum))
