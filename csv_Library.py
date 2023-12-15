"""
insert                                       /
read = display                               /
write                                        /
append                                       /
search                                       /
update                                       /
delete                                       /
"""

## [delete]

def deletecsv(user_id=None, user_name=None):
    try:
        import csv
        freq = 0
        buffer = []
        f = open("userlog.csv", 'r')
        while True:
            y = next(csv.reader(f))
            if (int(y[0]) == user_id) or (y[1] == user_name):
                print("old Data :")
                print('{:<15}{:<16}{:<16}'.format("User ID","User Name","Password"))
                print('{:<15}{:<16}{:<16}'.format(y[0], y[1], y[2]))
                freq += 1
            else:
                buffer.append(y)
    except StopIteration:
        f.close()
        f = open("userlog.csv", 'w', newline = '')
        z = csv.writer(f)
        z.writerows(buffer)
        f.close()
        print("Data changed")
        print(freq, "rows affected")

## [update]
def updatecsv(user_id=None, user_name=None, newpassword=None, newuserid=None, username=None):
    try:
        import csv
        freq = 0
        buffer = []
        f = open("userlog.csv", 'r')
        while True:
            y = next(csv.reader(f))
            if (y[1] == user_name) or (y[0] == user_id):
                print("old Data :", y)
                if newpassword != None:
                    y[2] = newpassword
                if newuserid != None:
                    y[0] = newuserid
                if newusername != None:
                    y[1] = newusername
                buffer.append(y)
                print("new Data :", y)
                freq += 1
            else:
                buffer.append(y)
    except StopIteration:
        f.close()
        f = open("userlog.csv", 'w', newline="")
        y = csv.writer(f)
        y.writerows(buffer)
        f.close()
        print("Data changed")
        print(freq, "rows affected")


## [insert]
def insertcsv(user_id, username, password, row):
    if not isinstance(user_id, int):
        print("User ID should be an integer")
        return
    elif not isinstance(username, str):
        print("User Name should be a string")
        return
    elif not isinstance(password, str):
        print("Password should be integer or decimal")
        return
    elif not isinstance(row, int):
        print("Row number should be an integer")
        return
    try:
        f = open("userlog.csv", 'r')
        import csv
        count = 0
        buffer = []
        while True:
            if count == row:
                buffer.append([user_id, username, password])
                count += 1
            else:
                buffer.append(next(csv.reader(f)))
                count += 1
    except StopIteration:
        f.close()
        f = open("userlog.csv", 'w')
        y = csv.writer(f)
        y.writerows(buffer)
        f.close()
        print("Data inserted")
        print("1 row affected")


## [search]

def searchcsv(user_id):
    import csv
    f = open("userlog.csv", 'r')
    flyer = 0
    try:
        fline = '{:<15}{:<16}{:<16}'.format("User ID","User Name","Password")
        print(fline)
        print("-"*47)
        while True:
            row = next(csv.reader(f))
            if int(row[0]) == user_id:
                data = '{:<15}{:<16}{:<16}'.format(row[0], row[1], row[2])
                print(data)
                flyer += 1
    except StopIteration:
        if flyer == 0:
            print("User Not Found!")

## [write]

def writecsv(user_id, user_name, password):
    import csv
    f = open("userlog.csv", 'w', newline="")
    l = [user_id, user_name, password]
    y = csv.writer(f)
    y.writerow(l)

## [append]

def appendcsv(user_id, user_name, password):
    import csv
    f = open("userlog.csv", 'a', newline="")
    l = [user_id, user_name, password]
    y = csv.writer(f)
    y.writerow(l)
## [read]

def readcsv():
    import csv
    fin = open("userlog.csv", 'r', newline="")
    try:
        fline = '{:<15}{:<16}{:<16}'.format("User ID","User Name","Password")
        print(fline)
        print("-"*47)
        while True:
            l = next(csv.reader(fin))
            data = '{:<15}{:<16}{:<16}'.format(l[0], l[1], l[2])
            print(data)
    except StopIteration:
        pass
