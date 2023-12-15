#count the frequency of elements in a list

"""
input list
empty dict d
for loop
for ch in l
if ch in d == True:
    d[ch] += 1
else:
    d[ch] = 1
out loop
for k,v in d:
    print(k, ":", v)
"""


l = input("please enter your desired list :")
d = {}
for ch in l:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
for item in d:
    print(item, ":", d[item])
