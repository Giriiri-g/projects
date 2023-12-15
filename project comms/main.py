"""
NOTE:
to do:
$ insert multiple Labels in the root since multicolored text cannot exist
$ user names in red, your name in orange, message in green
$ Entry at bottom
$ a send button at bottom right
$ select a font and set number of lines ie number of labels
$ two labels in a line, username length to be smaller than specified length
$ multi lined messages
$ all messages to be stored in encrypted bin like gsm, do not delete message
$ next time connecting load, message
$ threading is required, one for root.mainloop(), one for listening
$ root.mainloop() holds the power when it runs
$ scroll messages  
$ connect disconnect buttons at top
$ rowspan = 12
$ disable buttons when clicked
$ 15 lines of message
$ 28 lines in a page total
$ 1 line entry
$ when force closed, save data
$ save messages in a bin file encrypted each time loading messages send the bin file to server and server respond with decrypted mess
$ bind ctrl key for emotes, and display a ring of emotes in the centre
$ the emotes button will overlap the labels
$ when ctrl is left delete,☺ the emote ring
$ only smiley emoji available, others character art :) ;) :( <3
$ laughing, ☺☻, sad:'), wow :o, 
"""






from tkinter import *
import threading
import socket


root = Tk()
root.config(bg="black")
root.geometry("1366x768")
root.title("Green comms")
root.iconbitmap("logo.ico")

lines_21 = {"":"", "":"", "":"", "":"", "":"", "":"", "":"", "":"", "":"", "":"", "":"", "":"", "":"", "":"", "":"", "":"", "":"", "":"", "":"", "":"", "":""}
print(len(lines_21))

item_list = ['                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ', '                                                                                   ']
users = []
tcost = "$0"


def connect():
    global connected, conn, disconn
    connected=True
    conn["state"]= DISABLED
    disconn["state"]= NORMAL
def disconnect():
    global connected, conn, disconn
    connected=False
    disconn["state"]= DISABLED
    conn["state"]= NORMAL
def send(e):
    for user in users:
        user.send(e)

def recieve(user):
    while True:
        try:
            mess = user.recv(1024)
            send(mess)
        except:
            users.pop(user)
            send(f"{user} disconnected!".encode('ascii'))
            break
def con():
    while True:
        user, address = server.accept()
        print(f"{user} has joined with {address}")
        user.send("")
def _quit():
    global root
    root.destroy()
def decrypt(x):
    cipher = ['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9', '3', '2', '3', '8', '4', '6', '2', '6', '4', '3', '3', '8', '3', '2', '7', '9', '5', '0', '2', '8', '8', '4', '1', '9', '7', '1', '6', '9', '3', '9', '9', '3', '7', '5', '1', '0', '5', '8', '2', '0', '9', '7', '4', '9', '4', '4', '5', '9', '2', '3', '0', '7', '8', '1', '6', '4', '0', '6', '2', '8', '6', '2', '0', '8', '9', '8', '6', '2', '8', '0', '3', '4', '8', '2', '5', '3', '4', '2', '1', '1', '7', '0', '6', '7', '9']
    if len(x)> 100:
        chunks = [x[i:i+100] for i in range(0, len(x), 100)]
        decrypt = ""
        for i in chunks:
            i = list(i)
            for j in range(len(i)):
                decrypt += chr(ord(i[j]) - int(cipher[j]))
    else:
        decrypt = ""
        x = list(x)
        for i in range(len(x)):
            decrypt += chr(ord(x[i]) - int(cipher[i]))
    return decrypt


def encrypt(x):
    cipher = ['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9', '3', '2', '3', '8', '4', '6', '2', '6', '4', '3', '3', '8', '3', '2', '7', '9', '5', '0', '2', '8', '8', '4', '1', '9', '7', '1', '6', '9', '3', '9', '9', '3', '7', '5', '1', '0', '5', '8', '2', '0', '9', '7', '4', '9', '4', '4', '5', '9', '2', '3', '0', '7', '8', '1', '6', '4', '0', '6', '2', '8', '6', '2', '0', '8', '9', '8', '6', '2', '8', '0', '3', '4', '8', '2', '5', '3', '4', '2', '1', '1', '7', '0', '6', '7', '9']
    if len(x)> 100:
        chunks = [x[i:i+100] for i in range(0, len(x), 100)]
        encrypt = ""
        for i in chunks:
            i = list(i)
            for j in range(len(i)):
                encrypt += chr(ord(i[j]) + int(cipher[j]))
    else:
        encrypt = ""
        x = list(x)
        for i in range(len(x)):
            encrypt += chr(ord(x[i]) + int(cipher[i]))
    return encrypt

def display(mess, user):
    with open("D:\\preparations\\idlex-1.18\\projects\\project comms\\bin.csv", "a", newline="") as f:
        import csv
        y = csv.writer(f)
        y.writerow([encrypt(user), encrypt(mess)])
    with open("D:\\preparations\\idlex-1.18\\projects\\project comms\\bin.csv", "r") as f:
        import csv
        


online=""
conn = Button(root, text="CONNECT", command=connect, fg="#FF0000", bg="#000000", font=("Courier", 15), height=3, width=10)
disconn = Button(root, text="DISCONNECT", command=disconnect, fg="#FF0000", bg="#000000", font=("Courier", 15), height=3, width=10)
qt = Button(root, text="Quit", command=_quit, fg="#FF0000", bg="#000000", font=("Courier", 15), height=3, width=6)
snd = Button(root, text="SEND", command=send, fg="#FF0000", bg="#000000", font=("Courier", 15), width=6)
onl = Label(root, text="online :    "+online, fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=84, height=3, anchor="nw")



conn.grid(row=1, column=1, rowspan=3)
disconn.grid(row=1, column=2, rowspan=3)
snd.grid(row=25, column=6)
qt.grid(row=1, column=6)
onl.grid(row=1, column=3, columnspan=3)

connected=False

user0 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user1 = Label(root, text="hel :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user2 = Label(root, text="alex :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user3 = Label(root, text="ram :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user4 = Label(root, text="neheu :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user5 = Label(root, text="natallie :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user6 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user7 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user8 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user9 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user10 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user11 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user12 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user13 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user14 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user15 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user16 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user17 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user18 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user19 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)
user20 = Label(root, text="test :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)

user21 = Label(root, text="YOU :", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=10, height=1)



line0 = Label(root, text=item_list[0], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line1 = Label(root, text="test☺☺☺☺☻", fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line2 = Label(root, text=item_list[1], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line3 = Label(root, text=item_list[2], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line4 = Label(root, text=item_list[3], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line5 = Label(root, text=item_list[4], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line6 = Label(root, text=item_list[5], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line7 = Label(root, text=item_list[6], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line8 = Label(root, text=item_list[7], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line9 = Label(root, text=item_list[8], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line10 = Label(root, text=item_list[9], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line11 = Label(root, text=item_list[1], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line12 = Label(root, text=item_list[1], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line13 = Label(root, text=item_list[1], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line14 = Label(root, text=item_list[1], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line15 = Label(root, text=item_list[1], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line16 = Label(root, text=item_list[1], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line17 = Label(root, text=item_list[1], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line18 = Label(root, text=item_list[1], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line19 = Label(root, text=item_list[1], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")
line20 = Label(root, text=item_list[1], fg="#39FF14", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=102, height=1, anchor="w")

input_ = Entry(root, fg="white", bg="#000000", font=("Courier", 15), borderwidth=2, relief="sunken", width=95)

line0.grid(row=4, column=2, columnspan=5)
line1.grid(row=5, column=2, columnspan=5)
line2.grid(row=6, column=2, columnspan=5)
line3.grid(row=7, column=2, columnspan=5)
line4.grid(row=8, column=2, columnspan=5)
line5.grid(row=9, column=2, columnspan=5)
line6.grid(row=10, column=2, columnspan=5)
line7.grid(row=11, column=2, columnspan=5)
line8.grid(row=12, column=2, columnspan=5)
line9.grid(row=13, column=2, columnspan=5)
line10.grid(row=14, column=2, columnspan=5)
line11.grid(row=15, column=2, columnspan=5)
line12.grid(row=16, column=2, columnspan=5)
line13.grid(row=17, column=2, columnspan=5)
line14.grid(row=18, column=2, columnspan=5)
line15.grid(row=19, column=2, columnspan=5)
line16.grid(row=20, column=2, columnspan=5)
line17.grid(row=21, column=2, columnspan=5)
line18.grid(row=22, column=2, columnspan=5)
line19.grid(row=23, column=2, columnspan=5)
line20.grid(row=24, column=2, columnspan=5)



user0.grid(row=4, column=1)
user1.grid(row=5, column=1)
user2.grid(row=6, column=1)
user3.grid(row=7, column=1)
user4.grid(row=8, column=1)
user5.grid(row=9, column=1)
user6.grid(row=10, column=1)
user7.grid(row=11, column=1)
user8.grid(row=12, column=1)
user9.grid(row=13, column=1)
user10.grid(row=14, column=1)
user11.grid(row=15, column=1)
user12.grid(row=16, column=1)
user13.grid(row=17, column=1)
user14.grid(row=18, column=1)
user15.grid(row=19, column=1)
user16.grid(row=20, column=1)
user17.grid(row=21, column=1)
user18.grid(row=22, column=1)
user19.grid(row=23, column=1)
user20.grid(row=24, column=1)

user21.grid(row=25, column=1)


input_.grid(row=25, column=2, columnspan=4)
input_.bind("<Return>", send)


def tet():
    test.grid_forget()

test = Button(root, text="☺☻", command=tet, width=5, height=1)
test.grid(row=5, column=2)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 62489)) # (localhost, port) as a tuple
server.listen()




text = ""
user=""
display(text, user)
