"""
● Read a text file line by line and display each word separated by a #.

● Read a text file and display the number of vowels/consonants/uppercase/lowercase characters
in the file.

● Remove all the lines that contain the character 'a' in a file and write it to another file.

● Create a binary file with name and roll number. Search for a given roll number and display the
name, if not found display appropriate message.

● Create a binary file with roll number, name and marks. Input a roll number and update the marks.

● Write a random number generator that generatesrandom numbers between 1 and 6 (simulates
a dice).

● Create a CSV file by entering user-id and password, read and search the password for given user-
id.
"""

## [Read a text file line by line and display each word separated by a #.]
def seperate(filepath):
    try:
        f = open(filepath, 'r')
    except FileNotFoundError:
        print("File Not Found!")
    y = f.readlines()
    for line in y:
        _return = ""
        line = line.split()
        for word in line:
            if word.isspace():
                pass
            elif " " in word:
                _return += word.replace(" ", "") + " # "
            else:
                _return += word + " # "
        print(_return)

## [Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file.]

def stattxt(filepath):
    try:
        f = open(filepath, 'r')
    except FileNotFoundError:
        print("File Not Found!")
    x = f.read()
    vow = 0
    cnsnt = 0
    uprcse=0
    lwrcse=0
    for i in x:
        if i.isalpha():
            if i.lower() in ['a', 'e', 'i', 'o', 'u']:
                vow += 1
            else:
                cnsnt += 1
        if i.isupper():
            uprcse += 1
        if i.islower():
            lwrcse += 1
    print("vowels      :", vow)
    print("Consonants  :", cnsnt)
    print("Upper case  :", uprcse)
    print("Lower case  :", lwrcse)

## [Remove all the lines that contain the character 'a' in a file and write it to another file.]

def removea(fromfilepath, tofilepath):
    try:
        from_ = open(fromfilepath, 'r')
        to_ = open(tofilepath, 'a')
        y = from_.readlines()
        flag = 0
        for i in range(len(y)):
            if 'a' in y[i] or 'A' in y[i]:
                flag += 1
            else:
                to_.writelines(y[i])
        print("Data changed")
        print(flag, "rows affected")
    except FileNotFoundError:
        print("file not found")

## [Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message.]

def searchbin(roll):
    import pickle
    f = open("D:\\preparations\\testfile.dat", 'rb')
    freq = 0
    try:
        while True:
            row = pickle.load(f)
            if row[0] == roll:
                print(row)
                freq += 1
    except EOFError:
        if freq == 0:
            print("Student Not Found!")

## [Create a binary file with roll number, name and marks. Input a roll number and update the marks.]

def updatebin(roll, newmarks):
    try:
        import pickle
        freq = 0
        buffer = []
        f = open("D:\\preparations\\testfile.dat", 'rb')
        while True:
            y = pickle.load(f)
            if y[0] == roll:
                print("old Data :", y)
                y[2] = newmarks
                buffer.append(y)
                print("new Data :", y)
                freq += 1
            else:
                buffer.append(y)
    except EOFError:
        f.close()
        f = open("D:\\preparations\\testfile.dat", 'wb')
        f.truncate()
        for i in buffer:
            pickle.dump(i, f)
        print("Data changed")
        print(freq, "rows affected")

## [Write a random number generator that generatesrandom numbers between 1 and 6 (simulates a dice).]

def dice():
    import random
    print("dice face :", random.randint(1, 6))

## [Create a CSV file by entering user-id and password, read and search the password for given user- id.]

def searchcsv(user_id):
    import csv
    f = open("D:\\preparations\\idlex-1.18\\userlog.csv", 'r')
    flyer = 0
    try:
        while True:
            row = next(csv.reader(f))
            if row[0] == user_id:
                print(row)
                flyer += 1
    except StopIteration:
        if flyer == 0:
            print("User Not Found!")

def writecsv(user_id, user_name, password):
    import csv
    f = open("D:\\preparations\\idlex-1.18\\userlog.csv", 'a', newline="")
    l = [user_id, user_name, password]
    y = csv.writer(f)
    y.writerow(l)

def readcsv():
    import csv
    f=open("D:\\preparations\\idlex-1.18\\userlog.csv",'r')
    try:
        fline = '{:<16}{:<16}{:>25}'.format("User ID","User name","Password")
        print(fline)
        print("-"*57)
        while True:
            l = next(csv.reader(f))
            data = '{:<16}{:<16}{:>25}'.format(l[0], l[1], l[2])
            print(data)
    except StopIteration:
        pass
