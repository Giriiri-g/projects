"""
1. Create a new list
2. Take input list
3. Iterate over elements
4. Add if not already added
5. If added  += 1 to the frequency"""
cf = {}
d = input("enter your string :")
for i in d :
    if i in cf:
        cf[i] += 1
    if i not in cf:
        cf[i] = 1
for i in cf:
    print(i, ":", cf[i])