## [subcode]
"""
main(filepath)
all other function => sub function
use of exec funcction
oths:
insert                                       /
read = display                               /
write                                        /
append                                       /
search                                       /
update                                       /
delete                                       /
"""



## [insert]
def insertbin(roll, name, marks, row):
    """
    insertbin function inserts your students information into the specified file
    in the main function
    it takes 4 arguments
    roll, name, marks, row
    roll    -> should be an integer
    name    -> should be a string
    marks   -> should be an integer or float
    row     -> should be an integer (places the newly given row below the specified row)
    """
    if not isinstance(roll, int):
        print("Roll number should be an integer")
        return
    elif not isinstance(name, str):
        print("Name should be a string")
        return
    elif not (isinstance(marks, int) or isinstance(marks, float)):
        print("Marks should be integer or decimal")
        return
    elif not isinstance(row, int):
        print("Row number should be an integer")
        return
    global filepath
    try:
        f = open("D:\\preparations\\testfile.dat", 'rb')
        import pickle
        count = 0
        buffer = []
        while True:
            if count == row:
                buffer.append([roll, name, marks])
                count += 1
            else:
                buffer.append(pickle.load(f))
                count += 1
    except EOFError :
        f.close()
        f = open("D:\\preparations\\testfile.dat", 'wb')
        f.truncate()
        for i in buffer:
            pickle.dump(i, f)
        print("Data inserted")
        print("1 row affected")

## [update]
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

## [read]
def readbin():
    import pickle
    fin=open("D:\\preparations\\testfile.dat",'rb')
    try:
        fline = '{:<8}{:<15}{:>7}'.format("roll","name","marks")
        print(fline)
        print("-"*30)
        while True:
            l=pickle.load(fin)
            data = '{:<8}{:<15}{:>7}'.format(l[0], l[1], l[2])
            print(data)
    except EOFError:
        pass

## [search]
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

## [write]
def writebin():
    f = open("D:\\preparations\\testfile.dat", 'wb')
    import pickle
    noofrows = int(input("No. of rows: "))
    for i in range(noofrows):
        roll = int(input("Roll Number :"))
        name = input("Name :")
        marks = float(input("Marks :"))
        pickle.dump([roll, name, marks], f)

## [append]
def appendbin():
    f = open("D:\\preparations\\testfile.dat", 'ab')
    noofrows = int(input("No. of rows: "))
    for i in range(noofrows):
        roll = int(input("Roll Number :"))
        name = input("Name :")
        marks = float(input("Marks :"))
        pickle.dump([roll, name, marks], f)

## [delete]

def deletebin(roll=None, name=None):
    try:
        import pickle
        freq = 0
        buffer = []
        f = open("D:\\preparations\\testfile.dat", 'rb')
        while True:
            y = pickle.load(f)
            if (y[0] == roll) or (y[1] == name):
                print("old Data :")
                print(y)
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
