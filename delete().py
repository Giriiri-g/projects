import pickle
def delete():
    name = input("Enter the name :")
    l = []
    f = open("cricketers.dat", "rb")
    try:
        l.append(pickle.load(f))
    except EOFError:
        pass
    for i in range(len(l)):
        if l[i][0].lower() == name.lower():
            l.pop(i)
    f.close()
    f = open('cricketers.dat', 'wb')
    f.truncate()
    for i in l:
        pickle.dump(i)
