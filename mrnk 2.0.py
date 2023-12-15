def rnk():
    stdlst = dict()
    l = len(stdlst)
    for i in range(l):
        print(max(stdlst), ":", stdlst[max(stdlst)])
        del stdlst[max(stdlst)]