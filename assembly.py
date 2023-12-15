## [Q1]


path = input("Enter the absolute path of the file :")
try:
     if path[-3::] != "asm":
          print("[ERROR]: FILE TYPE NOT .asm")
     else:
          f = open(path, 'r')
          lines = f.readlines()
          nwlines=[]
          for i in lines:
               if "//" in i:
                    i = i[:i.index("//"):]
               i=i.replace(" ", "")
               i=i.replace("\t", "")
               i=i.replace("\n", "")
               if i !="":
                    nwlines.append(i)
          f.close()
          path=path.split("\\")
          path.pop(-1)
          path.append("_no_whitespace.asm")
          path = "\\".join(path)
          f=open(path, 'w')
          f.write("\n".join(nwlines))
          f.close()
except FileNotFoundError:
     print("[ERROR]: File Not Found!")

## [Q2]


path = input("Enter the absolute path of the file :")
try:
     if path[-3::] != "asm":
          print("[ERROR]: FILE TYPE NOT .asm")
     else:
          f = open(path, 'r')
          lines = f.readlines()
          symbols = []
          for i in lines:
               if i[0] =="(":
                    symbols.append(i[1:-2:])
               if i[0]=="@":
                    if (not i[1].isdigit()):
                         if i[1:-1:] not in symbols:
                              symbols.append(i[1:-1:])
          f.close()
          path=path.split("\\")
          path.pop(-1)
          path.append("symbolsandvariables.asm")
          path = "\\".join(path)
          f=open(path, 'w')
          f.write("\n".join(symbols))
          f.close()
except FileNotFoundError:
     print("[ERROR]: File Not Found!")



## [Q3]


path = input("Enter the absolute path of the file :")
try:
     if path[-3::] != "asm":
          print("[ERROR]: FILE TYPE NOT .asm")
     else:
          f = open(path, 'r')
          lines = f.readlines()
          symbols = {"R0":0, "R1":1, "R2":2, "R3":3, "R4":4, "R5":5, "R6":6, "R7":7, "R8":8, "R9":9, "R10":10, "R11":11, "R12":12, "R13":13, "R14":14, "R15":15}
          varcnt=15
          for i in lines:
               if i[0] =="(":
                    symbols[i[1:-2:]] = lines.index(i)
          for i in lines:
               if i[0]=="@":
                    if not i[1].isdigit():
                         if i[1::] not in symbols:
                              varcnt+=1
                              symbols[i[1::]] = varcnt
          f.close()
          write = ["+----------+----------+", "| symbols  |  value   |", "+----------+----------+"]
          for i in symbols:
               write.append("|{:^10}|{:^10}|".format(i, symbols[i]))
          write.append("+----------+----------+")
          path=path.split("\\")
          path.pop(-1)
          path.append("symboltable.asm")
          path = "\\".join(path)
          f=open(path, 'w')
          f.write("\n".join(list(write)))
          f.close()
except FileNotFoundError:
     print("[ERROR]: File Not Found!")

## [Q4]

A_instruc = input("Enter a A instruction :")
bin_ = bin(int(A_instruc[1::]))[2::]
bin_16 = "0"*(16-len(bin_)) +bin_
print(bin_16)
f = open("output.hack", "w")
f.write(bin_16+"\n")
f.close()

## [Q5]
try:
     d = {"A":"100", "D":"010", "M":"001", "AMD":"111", "MD":"011", "AM":"101", "AD":"110"}
     j={"JLT":"100", "JEQ":"010", "JGT":"001", "JLE":"110", "JNE":"101", "JGE":"011", "JMP":"111"}
     compm = {"0":"101010", "1":"111111", "-1":"111010", "D":"001100", "A":"110000", "!D":"001101", "!A":"110001", "-D":"001111", "-A":"110011", "D+1":"011111", "A+1":"110111", "D-1":"001110", "A-1":"110010", "D+A":"000010", "D-A":"010011", "A-D":"000111", "D&A":"000000", "D|A":"010101"}
     comp = {"M":"110000", "!M":"110001", "-M":"110011", "M+1":"110111", "M-1":"110010", "D+M":"000010", "D-M":"010011", "M-D":"000111", "D&M":"000000", "D|M":"010101"}
     C_instruc = input("Enter a C instruction :")
     C_instruc = C_instruc.split(";")
     C_instruc[0] = C_instruc[0].split("=")
     out="111"
     # [[D, D+A], JMP]
     if len(C_instruc[0])==1:
          if "M" in C_instruc[0][0]:
               out+= "1"
               out+=comp[C_instruc[0][0]]
          else:
               out+="0"
               out+=compm[C_instruc[0][0]]
          out+="000"
     else:
          if "M" in C_instruc[0][1]:
               out+= "1"
               out+=comp[C_instruc[0][1]]
          else:
               out+="0"
               out+=compm[C_instruc[0][1]]
          out+=d[C_instruc[0][0]]
     if len(C_instruc)==1:
          out+="000"
     else:
          out+=j[C_instruc[1]]
except KeyError:
     print("Invalid Instruction, please follow the table")
f = open("output.hack", "w")
f.write(out+"\n")
print(out)
f.close()
