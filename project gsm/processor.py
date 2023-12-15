import mysql.connector as sql
from datetime import date
from tkinter import messagebox, Tk

id_ = "101256"
qt_ = "2"


## [ EMPTY DATA ]
if (id_ == "") or (qt_==""):
    root = Tk()
    mess = messagebox.showerror('Insufficient Data!', '[ERROR]: The required columns are empty\nsorry for the inconvineance')
    if mess == messagebox.OK:
        root.destroy()    



else:

## [ PULLING DATA FROM SQL ]
    dbm = sql.Connect(user="root", host="localhost", passwd="qweasd", database="GSM")
    crsr = dbm.cursor()
    crsr.execute(f"select * from stock where id = {id_};")
    for i in crsr:
        i=list(i)
        
    #[101256, 'amul milk', 25, Decimal('22.00'), 'A1', datetime.date(2022, 2, 6), 'amul.co']



## [ EXCEPTIONAL HANDLING AND ADDING TO CART ]

# item = ['101256', 'amul milk', '2', '22.0', '44.0']


    def updatecsv(id_, qt_, item):
        try:
            import csv
            in_yes = False
            buffer = []
            f = open("cart.csv", 'r')
            while True:
                y = next(csv.reader(f))
                if y[0] == id_:
                    in_yes=True
                    y[2] = str(int(y[2]) + int(qt_))
                    y[4] = str(float(y[3])*int(y[2]))
                    buffer.append(y)
                else:
                    buffer.append(y)
        except StopIteration:
            f.close()
            f = open("cart.csv", 'w', newline="")
            y = csv.writer(f)
            if in_yes == False:
                buffer.append(item)
            y.writerows(buffer)
            f.close()


    try:
        if date.today() >= i[5]:
            root = Tk()
            mess = messagebox.showerror('Item expired!', '[ERROR]: The entered item is expired\nsorry for the inconvineance')
            if mess == messagebox.OK:
                root.destroy()
        elif int(qt_) > i[2]:
            root = Tk()
            mess = messagebox.showerror('Not enough stock!', f'[ERROR]: The required quantity is not available in stock\n\nOnly {i[2]} item is left in stock\n\nsorry for the inconvineance')
            if mess == messagebox.OK:
                root.destroy()
        else:
            item = [i[0], i[1], int(qt_), float(i[3]), float(i[3])*int(qt_)]
            updatecsv(id_, qt_, item)
    except NameError:
        root = Tk()
        mess = messagebox.showerror('Item not found!', '[ERROR]: The entered item is not found\nplease check the ID of the item again\nsorry for the inconvineance')
        if mess == messagebox.OK:
            root.destroy()
    except:
        pass
