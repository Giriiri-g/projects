#WAP to print fibonacci series upto to the users number

#                                                       Print fibonacci series
#                                                       ______________________


"""
fibonacci series
a1,a2,a3
a3 = a1 +a2
thrfre
fnum = 0
snum = 1
tnum = fnum + snum
overwrite:
    fnum = snum
    snum = tnum
"""


fnum = 0
snum = 1
tnum = 1
nmupt = int(input("enter a number upto which you need your fibonacci series :"))
series = [0,1]
while tnum <= nmupt:
    series.append(tnum)
    fnum = snum
    snum = tnum
    tnum = fnum + snum
print("This is your fibonacci series upto", nmupt, ":", series)
