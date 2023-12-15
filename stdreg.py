from sys import *
import time
def log():
    f = open("reg.txt", "a")
    named_tuple = time.localtime()
    time_string = time.strftime("%d/%m/%Y", named_tuple)
    f.write("\n")
    f.write(time_string)
    f.write("\n")
    print("log :")
    x = stdin.readlines()
    x = str(x)
    print("\n\n\n\n\n")
    stdreg = ["HARINE M", "HARINI S", "HEMA R", "INDHRA N", "INDIRA YALINI J", "JANANI T", "KEERTHANA DEVI M", "LAKSHMI PRABAA S", "MONA CHRISLINE V", "MONISHA J", "MOSHIKA J", "PRASHITHA R", "PREETHI T", "SHALINI S", "SHIMRUTHIEE R", "SIVADHARSHINI S", "SUBHA DHARANI P", "VENOTHINI S", "VINCENT CLAUDIA S", "ARUL MARTIN M", "DHANA PRAKASH S", "DHANURAJA T", "DHANUSH KUMAR B", "HEMANTH KUMAR M", "JAHAGANAPATHI S", "JOTHISH RS", "MADHESH P", "MONISH A", "MUGILAN K", "POTRI SELVAN R S", 'RANJITH KANNA A', 'SHYLESH KUMAR V', 'SUJAN S', 'THILACK R', 'VIJAY MITHRAN R S', 'VIJEYA KARTHY L', 'VILMER SAMUEL R']
    for i in stdreg:
        if i not in x:
            f.write(i)
            f.write("\n")
            print(i)
    f.close()
