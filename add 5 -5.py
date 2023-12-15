L = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in L:
    if i%2 == 0:
        n = L.index(i)
        L.insert(n, i+5)
    if i%2 == 1:
        L.insert(L.index(i), i-5)
print(L)