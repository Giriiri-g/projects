#WAP to rank students upto to top 6 like a list
#students - alex = 45, alice = 46, mohan = 32, rahul = 37, harsh = 49, adharsh = 42, steve = 35, hawkin = 40
stdlst = {45 : "alex", 46 : "alice", 32 : "mohan", 37 : "rahul", 49 : "harsh", 42 : "adharsh", 35 : "steve", 40 : "hawkin"}
for i in range(6):
    print(max(stdlst), ":", stdlst[max(stdlst)])
    del stdlst[max(stdlst)]