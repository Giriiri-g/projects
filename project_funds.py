"""
## [ plan ]

set focus function
set data scroller
create database
upgrade above 3.6
set the size of labels and buttons
add function to buttons
copy data reader and set data manipulations
"""

from tkinter import *

root = Tk()
root.config(bg="black")
root.geometry("1366x768")
root.title("Funds")
root.iconbitmap("dollar-sign-11532873583of7tqx0dke.ico")




def cadd(e=None):
    id_ = identry.get()
    qt_ = qtentry.get()
    identry.delete(0, END)
    qtentry.delete(0, END)
    identry.focus_set()
    ## [ EMPTY DATA ]
    if (id_ == "") or (qt_==""):
        root = Tk()
        mess = messagebox.showerror('Insufficient Data!', '[ERROR]: The required columns are empty\nsorry for the inconvineance')
        if mess == messagebox.OK:
            root.destroy()    

    elif not ((len(id_) == 6) and id_.isdigit() and qt_.isdigit() and (int(qt_)>=0)):
        root = Tk()
        mess = messagebox.showerror('Value Error!', '[ERROR]: The given value is not in the right format\nsorry for the inconvineance')
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
                in_yes = False
                buffer = []
                f = open("cart.csv", 'r')
                while True:
                    y = next(csv.reader(f))
                    if y[0] == id_:
                        in_yes=True
                        y[2] = str(int(y[2]) + int(qt_))
                        y[4] = str(float(y[3])*int(y[2]) + round((float(y[3])*float(y[5])*int(y[2]))/100, 1)).strip('0')
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
            if datetime.date.today() >= i[5]:
                root = Tk()
                mess = messagebox.showerror('Item expired!', '[ERROR]: The entered item is expired\nsorry for the inconvineance')
                if mess == messagebox.OK:
                    root.destroy()
            elif int(qt_) > int(i[2]):
                root = Tk()
                mess = messagebox.showerror('Not enough stock!', f'[ERROR]: The required quantity is not available in stock\n\nOnly {i[2]} item is left in stock\n\nsorry for the inconvineance')
                if mess == messagebox.OK:
                    root.destroy()
            else:
                item = [i[0], i[1], int(qt_), float(i[3]), float(i[3])*int(qt_) + round((float(i[3])*float(i[7])*int(qt_))/100, 1), i[7]]
                updatecsv(id_, qt_, item)
                crsr.execute(f"update stock set stock.stock = stock - {qt_} where ID = {id_}")
                dbm.commit()
                display()
        except NameError:
            root = Tk()
            mess = messagebox.showerror('Item not found!', '[ERROR]: The entered item is not found\nplease check the ID of the item again\nsorry for the inconvineance')
            if mess == messagebox.OK:
                root.destroy()


def cclear():
    global item_list
    f = open("cart.csv", "r")
    y = csv.reader(f)
    dbm = sql.Connect(user="root", host="localhost", passwd="qweasd", database="GSM")
    crsr = dbm.cursor()
    try:
        while True:
            item = next(y)
            crsr.execute(f"update stock set stock = stock + {int(item[2])} where id = {int(item[0])}")#int(item[2])
            dbm.commit()
    except StopIteration:
        f.close()
        f = open("cart.csv", "w", newline="")
        f.flush()
        f.close()
        item_list = ['                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ']
        display()


def cmod():
    global tcost
    global item_list
    root = Tk()
    mes = simpledialog.askstring("modify item", "Enter the item ID :")
    stk = simpledialog.askstring("modify item", "Enter the new stock :")
    if mes != "":
        if stk == "0":
            f = open("cart.csv", 'r')
            y = csv.reader(f)
            cart = []
            try:
                while True:
                    item = next(y)
                    if mes == item[0]:
                        # putting items back in shelf
                        dbm = sql.Connect(user="root", host="localhost", passwd="qweasd", database="GSM")
                        crsr = dbm.cursor()
                        crsr.execute(f"update stock set stock = stock + {int(item[2])} where id = {int(item[0])}")
                        dbm.commit()
                    else:
                        cart.append(item)
            except StopIteration:
                f.close()
                f = open("cart.csv", "w", newline="")
                z = csv.writer(f)
                z.writerows(cart)
                f.close()
                root.destroy()
                item_list = ['                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ']
                tcost = "$0"
                display()
                upddisplay()
        elif stk.isdigit():
            f = open("cart.csv", 'r')
            y = csv.reader(f)
            cart = []
            try:
                while True:
                    item = next(y)
                    if mes == item[0]:
                        # putting items back in shelf
                        dbm = sql.Connect(user="root", host="localhost", passwd="qweasd", database="GSM")
                        crsr = dbm.cursor()
                        crsr.execute(f"update stock set stock = stock + {int(item[2])} where id = {int(item[0])}")
                        dbm.commit()
                    else:
                        cart.append(item)
            except StopIteration:
                f.close()
                f = open("cart.csv", "w", newline="")
                z = csv.writer(f)
                z.writerows(cart)
                f.close()
                root.destroy()
                item_list = ['                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ']
                tcost = "$0"
                display()
                id_ = mes
                qt_=stk
                if (id_ == "") or (qt_==""):
                    root = Tk()
                    mess = messagebox.showerror('Insufficient Data!', '[ERROR]: The required columns are empty\nsorry for the inconvineance')
                    if mess == messagebox.OK:
                        root.destroy()    
                elif not ((len(id_) == 6) and id_.isdigit() and qt_.isdigit() and (int(qt_)>=0)):
                    root = Tk()
                    mess = messagebox.showerror('Value Error!', '[ERROR]: The given value is not in the right format\nsorry for the inconvineance')
                    if mess == messagebox.OK:
                        root.destroy()
                else:
                    dbm = sql.Connect(user="root", host="localhost", passwd="qweasd", database="GSM")
                    crsr = dbm.cursor()
                    crsr.execute(f"select * from stock where id = {id_};")
                    for i in crsr:
                        i=list(i)
                    def updatecsv(id_, qt_, item):
                        try:
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
                        if datetime.date.today() >= i[5]:
                            root = Tk()
                            mess = messagebox.showerror('Item expired!', '[ERROR]: The entered item is expired\nsorry for the inconvineance')
                            if mess == messagebox.OK:
                                root.destroy()
                        elif int(qt_) > int(i[2]):
                            root = Tk()
                            mess = messagebox.showerror('Not enough stock!', f'[ERROR]: The required quantity is not available in stock\n\nOnly {i[2]} item is left in stock\n\nsorry for the inconvineance')
                            if mess == messagebox.OK:
                                root.destroy()
                        else:
                            item = [i[0], i[1], int(qt_), float(i[3]), float(i[3])*int(qt_)]
                            updatecsv(id_, qt_, item)
                            crsr.execute(f"update stock set stock.stock = stock - {qt_} where ID = {id_}")
                            dbm.commit()
                            display()
                            upddisplay()
                    except NameError:
                        root = Tk()
                        mess = messagebox.showerror('Item not found!', '[ERROR]: The entered item is not found\nplease check the ID of the item again\nsorry for the inconvineance')
                        if mess == messagebox.OK:
                            root.destroy()
                    except:
                        pass
        else:
            root = Tk()
            mess = messagebox.showerror('Insufficient Data!', '[ERROR]: The required columns are empty\nsorry for the inconvineance')
            if mess == messagebox.OK:
                root.destroy()
    else:
        root = Tk()
        mess = messagebox.showerror('Insufficient Data!', '[ERROR]: The required columns are empty\nsorry for the inconvineance')
        if mess == messagebox.OK:
            root.destroy()
                    
def cdel():
    global item_list
    global tcost
    root = Tk()
    mes = simpledialog.askstring("delete item", "Enter the item ID :")
    if mes == '':
        f = open("cart.csv", 'r')
        y = csv.reader(f)
        cart = []
        try:
            while True:
                cart.append(next(y))
        except StopIteration:
            if cart==[]:
                f.close()
            else:
                f.close()
                f = open("cart.csv", 'w', newline="")
                # putting items back in shelf
                dbm = sql.Connect(user="root", host="localhost", passwd="qweasd", database="GSM")
                crsr = dbm.cursor()
                crsr.execute(f"update stock set stock = stock + {int(cart[-1][2])} where id = {int(cart[-1][0])}")
                dbm.commit()
                
                cart.remove(cart[-1])
                x = csv.writer(f)
                x.writerows(cart)
                f.close()
                root.destroy()
                item_list = ['                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ']
                tcost = "$0"
                display()
    
    else:
        f = open("cart.csv", 'r')
        y = csv.reader(f)
        cart = []
        try:
            while True:
                item = next(y)
                if mes == item[0]:
                    # putting items back in shelf
                    dbm = sql.Connect(user="root", host="localhost", passwd="qweasd", database="GSM")
                    crsr = dbm.cursor()
                    crsr.execute(f"update stock set stock = stock + {int(item[2])} where id = {int(item[0])}")
                    dbm.commit()
                else:
                    cart.append(item)
        except StopIteration:
            f.close()
            f = open("cart.csv", "w", newline="")
            z = csv.writer(f)
            z.writerows(cart)
            f.close()
            root.destroy()
            item_list = ['                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ']
            tcost = "$0"
            display()

    


def _quit():
    global root
    cclear()
    root.destroy()



## [ CREATING BUTTONS ]


close = Button(root, text="close tab", command=cdel, fg="#47ff33", bg="black", font=("Courier", 15), width=11, height=6)
add = Button(root, text="add", command=cadd, fg="#47ff33", bg="black", font=("Courier", 15), width=11, height=6)
out = Button(root, text="transaction\nhistory", command=cclear, fg="#47ff33", bg="black", font=("Courier", 15), width=11, height=6)
quit_ = Button(root, text="Quit", command=_quit, fg="#47ff33", bg="black", font=("Courier", 15), width=11, height=2)
modify = Button(root, text="modify", command=cmod, fg="#47ff33", bg="black", font=("Courier", 15), width=11, height=6)
addbtm = Button(root, text="add", command=cadd, fg="red", bg="black", font=("Courier", 15), width=11, height=2)



## [ GRID ]


close.grid(row=0, column=6, rowspan=3)
add.grid(row=3, column=6, rowspan=3)
out.grid(row=6, column=6, rowspan=3)
quit_.grid(row=0, column=5)
modify.grid(row=9, column=6, rowspan=3)
addbtm.grid(row=12, column=6)



## [ CREATE LABELS ]

item_list = ['                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ']
head = "slno      id             name                     quantity       MRP       cost    "
tcost = "$0"

header = Label(root, text=head, fg="yellow", bg="black", font=("Courier", 15), borderwidth=2, relief="sunken", width=83, height=2)
i0 = Label(root, text=item_list[0], fg="white", bg="#1400a8", font=("Courier", 15), borderwidth=2, relief="sunken", width=83, height=2)
i1 = Label(root, text=item_list[1], fg="white", bg="#1400a8", font=("Courier", 15), borderwidth=2, relief="sunken", width=83, height=2)
i2 = Label(root, text=item_list[2], fg="white", bg="#1400a8", font=("Courier", 15), borderwidth=2, relief="sunken", width=83, height=2)
i3 = Label(root, text=item_list[3], fg="white", bg="#1400a8", font=("Courier", 15), borderwidth=2, relief="sunken", width=83, height=2)
i4 = Label(root, text=item_list[4], fg="white", bg="#1400a8", font=("Courier", 15), borderwidth=2, relief="sunken", width=83, height=2)
i5 = Label(root, text=item_list[5], fg="white", bg="#1400a8", font=("Courier", 15), borderwidth=2, relief="sunken", width=83, height=2)
i6 = Label(root, text=item_list[6], fg="white", bg="#1400a8", font=("Courier", 15), borderwidth=2, relief="sunken", width=83, height=2)
i7 = Label(root, text=item_list[7], fg="white", bg="#1400a8", font=("Courier", 15), borderwidth=2, relief="sunken", width=83, height=2)
i8 = Label(root, text=item_list[8], fg="white", bg="#1400a8", font=("Courier", 15), borderwidth=2, relief="sunken", width=83, height=2)
i9 = Label(root, text=item_list[9], fg="white", bg="#1400a8", font=("Courier", 15), borderwidth=2, relief="sunken", width=83, height=2)




## [ GRID LABEL ]

header.grid(row=1, column=0, columnspan=6)
i0.grid(row=2, column=0, columnspan=6)
i1.grid(row=3, column=0, columnspan=6)
i2.grid(row=4, column=0, columnspan=6)
i3.grid(row=5, column=0, columnspan=6)
i4.grid(row=6, column=0, columnspan=6)
i5.grid(row=7, column=0, columnspan=6)
i6.grid(row=8, column=0, columnspan=6)
i7.grid(row=9, column=0, columnspan=6)
i8.grid(row=10, column=0, columnspan=6)
i9.grid(row=11, column=0, columnspan=6)



# [ ROW 12 ]
payee = Entry(root, fg="red", bg="black", font=("Courier", 15), borderwidth=2, relief="sunken", width=25)
mons = Entry(root, fg="red", bg="black", font=("Courier", 15), borderwidth=2, relief="sunken", width=10)
loaner = Entry(root, fg="red", bg="black", font=("Courier", 15), borderwidth=2, relief="sunken", width=10)
comment = Entry(root, fg="red", bg="black", font=("Courier", 15), borderwidth=2, relief="sunken", width=10)


def fcs(e):
    payee.focus_set()

    


payee.grid(row=12, column=1)
mons.grid(row=12, column=2)
loaner.grid(row=12, column=3)
comment.grid(row=12, column=4)


identry.bind("<Return>", fcs)
payee.bind("<Return>", cadd)


psl = ""
pname = ""
pprice = ""


sl = Label(root, text=psl, fg="white", bg="#1400a8", font=("Courier", 15), borderwidth=2, relief="sunken", padx=25, pady=10)
name = Label(root, text=pname, fg="white", bg="#1400a8", font=("Courier", 15), borderwidth=2, relief="sunken", padx=150, pady=10)
pric = Label(root, text=pprice, fg="white", bg="#1400a8", font=("Courier", 15), borderwidth=2, relief="sunken", padx=85, pady=10)


sl.grid(row=12, column=1)
name.grid(row=12, column=3)
pric.grid(row=12, column=5)


line=0
def decrement(e):
    global line
    if line ==0:
        pass
    else:
        line-=1
        item_list = ['                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ']
        tcost = "$0"
        display()
def increment(e):
    global line
    f = open("cart.csv", 'r')
    cart=[]
    reader = csv.reader(f)
    try:
        while True:
            cart.append(next(reader))
    except StopIteration:
        f.close()
        pass
    line+=1
    item_list = ['                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ']
    tcost = "$0"
    display()
root.bind("<w>", increment)
root.bind("<s>", decrement)

identry.focus_set()


root.mainloop()
