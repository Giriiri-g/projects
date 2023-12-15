## for text files

"""
read
write
append
"""

def readtxt(filepath):
    if not isinstance(filepath, str):
        return ValueError ("invalid file path")
    try:
        f = open(filepath, 'r')
        for i in range(len(f.readlines())-1):
            f.readlines()[i] = f.readlines()[i].rstrip(1)
        return f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError ("No such file in the specified directory:", filepath)

def writetxt(Data, filepath):
    if not isinstance(filepath, str):
        return ValueError ("invalid file path")
    f = open(filepath, 'a+')
    if isinstance(Data, list):
        f.truncate()
        f.flush()
        for i in Data:
            f.write(i + "\n")
            f.flush()
        print("Data written")
    if isinstance(Data, tuple):
        f.truncate()
        f.flush()
        for i in Data:
            f.write(i+'\n')
            f.flush()
        print("Data written")
    if isinstance(Data, dict):
        f.truncate()
        f.flush()
        for i in Data:
            f.write(i + ":" + Data[i] + '\n')
            f.flush()
        print("Data written")
    if isinstance(Data, str):
        f.truncate()
        f.flush()
        f.write(Data)
        f.flush()
        print("Data written")
    
def appendtxt(Data, filepath):
    if not isinstance(filepath, str):
        return ValueError ("invalid file path")
    f = open(filepath, 'a+')
    if isinstance(Data, list):
        for i in Data:
            f.write(i + '\n')
            f.flush()
        print("Data written")
    if isinstance(Data, tuple):
        for i in Data:
            f.write(i + '\n')
            f.flush()
        print("Data written")
    if isinstance(Data, dict):
        for i in Data:
            f.write(i + ":" + Data[i] + '\n')
            f.flush()
        print("Data written")
    if isinstance(Data, str):
        f.write(Data)
        f.flush()
        print("Data written")
    


def startwith(value, filepath):
    if not isinstance(filepath, str):
        return ValueError ("invalid file path")
    if not isinstance(value, str):
        return ValueError ("invalid literal for startwith()")
    try:
        f = open(filepath, 'r')
    except FileNotFoundError:
        return FileNotFoundError ("No such file in the specified Directory")
    except SyntaxError:
        return SyntaxError ("The filepath separator should with \\ or /")
    z = f.readlines()
    for i in z:
        i = i.split(" ")
        for y in i:
            y = "#" + y
            print(y)

def stattxt(filepath):
    if not isinstance(filepath, str):
        return ValueError ("invalid file path")
    try:
        f = open(filepath, 'r')
    except FileNotFoundError:
        raise FileNotFoundError ("No such file in the specified Directory")
    import Data
    y = f.read()
    Data.stat(y)

def remover(char, fromfilepath, tofilepath):
    if not isinstance(fromfilepath, str):
        return ValueError ("invalid file path")
    if not isinstance(tofilepath, str):
        return ValueError ("invalid file path")
    if not isinstance(char, str):
        return ValueError ("invalid file path")
    try:
        from_ = open(fromfilepath, 'r')
        to_ = open(tofilepath, 'a')
        y = from_.readlines()
        for i in y:
            if char in i:
                to_.write(i)
                to_.flush()
                y.remove(i)
    except FileNotFoundError:
        raise FileNotFoundError ("No such file in the specified Directory")
    
## binary file handling

def writebin(filepath):
    import pickle
    if not isinstance(filepath, str):
        return ValueError ("invalid file path")
    try:
        fout = open(filepath, 'ab')
    except FileNotFoundError:
        raise FileNotFoundError ("No such file in the specified Directory")
    roll = int(input("Enter Roll no. : "))
    name = input("Enter Name : ")
    mark = float(input("Enter Mark : "))
    l = [roll, name, mark]
    pickle.dump(l, fout)
    print("The data was written to the file")
    fout.close()


def readbin(filepath):
    import pickle
    if not isinstance(filepath, str):
        return ValueError ("invalid file path")
    try:
        fin = open(filepath, 'rb')
        while True:
            l = pickle.load(fin)
            print("Roll no.: ", l[0])
            print("Name    : ", l[1])
            print("Mark    : ", l[2])
            print("_"*35 + "\n")
    except EOFError:
        print("End Of File reached")
    except FileNotFoundError:
        raise FileNotFoundError ("No such file in the specified Directory")
    fin.close()
