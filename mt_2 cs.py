def countA(filepath):
    if not isinstance(filepath, str):
        raise ValueError ("invalid file path")
    try:
        f = open(filepath,'r')
        freq = 0
        y = f.read()
        y = y.split(" ")
        for i in y:
            if len(i) == 0:
                i = " "
            if i[0] == "A":
                freq += 1
        print('Count of words starting with "A" is', freq)
    except FileNotFoundError:
        raise FileNotFoundError ("No such File in the specified Directory")

def copy(fromfilepath, tofilepath):
    if not isinstance(fromfilepath, str):
        raise ValueError ("invalid file path")
    if not isinstance(tofilepath, str):
        raise ValueError ("invalid file path")
    try:
        from_ = open(fromfilepath, 'r')
        to_ = open(tofilepath, 'a')
        y = from_.read()
        to_.write(y)
        to_.flush()
        print("Data copied")
    except FileNotFoundError:
        raise FileNotFoundError ("No such File in the specified Directory")



def A5letter(filepath):
    if not isinstance(filepath, str):
        raise ValueError ("invalid file path")
    try:
        f = open(filepath,'r')
        freq = 0
        y = f.read()
        y = y.split(" ")
        for i in y:
            if len(i) == 5:
                if i[0] == "A":
                    freq += 1
                    print(i)
        print("There are totally", freq, "number of words starting with A and have a length of 5")
    except FileNotFoundError:
        raise FileNotFoundError ("No such File in the specified Directory")

def writebin(roll, mk1, mk2, mk3):
    if not isinstance(roll, int):
        raise ValueError ("invalid literal for roll no. with base 10")
    if not isinstance(mk1, float):
        raise ValueError ("invalid literal for marks with floating point value")
    if not isinstance(mk2, float):
        raise ValueError ("invalid literal for marks with floating point value")
    if not isinstance(mk3, float):
        raise ValueError ("invalid literal for marks with floating point value")
    f = open("STUDENTS.Dat", 'ab')
    import pickle
    row = [roll, mk1, mk2, mk3]
    pickle.dump(row, f)
    print("Data was written into the file")
    f.close()

def readbin():
    f = open("STUDENTS.Dat", 'rb')
    print("roll----------marks1-----marks2-----marks3")
    try:
        while True:
            load = pickle.load(f)
            print(load[0] + " " * 10 + load[1] + " " * 5 + load[2] + " "*5 + load[3])
            print(int(load[1])+ int(load[2]) + int(load[3]))
    except EOFError:
        print("End Of File reached")


def Display_Player(N):
    if not type(N) == int:
        raise ValueError ("invalid literal (int type required)")
    import csv
    f = open("SPORTS.Dat", 'r')
    csvreader = csv.reader(f)
    for row in csvreader:
        if row[0] > N:
            print(row)

def removea():
    file_1 = open("Thonny\LICENSE.txt")
    file_2 = open("practical ex2.txt", 'w')
    y = []
    fileread = file_1.readlines()
    for line in fileread:
        if "a" in line or "A" in line:
                line = line.replace("a", "A")
        else:
            y.append(line)
    file_2.writelines(y)
