t = int(input("Enter the number of test cases :"))
testcases = []
def validity(size):
     if (("m" in size) and ("x" in size)):
          return False
     if ((size.count("l")>1) or (size.count("s")>1) or (size.count("m")>1)):
          return False
     if (size[-1] not in ["s", "m", "l"]):
         return False
     return True
for i in range(t):
     size = input("")
     dup = size.lower().split(" ") # xxs m
     if (validity(dup[0]) and validity(dup[1])):
          testcases.append(size)
     else:
          print("Invalid Input")

for i in testcases:
     i = i.split(" ")
     if i[0] == i[1]:
          print("=")
     elif (("L" in i[0]) and ("M" in i[1])):
         print(">")
     elif (("L" in i[1]) and ("M" in i[0])):
         print("<")
     elif (("S" in i[0]) and ("M" in i[1])):
         print("<")
     elif (("S" in i[1]) and ("M" in i[0])):
         print(">")
     elif (("S" in i[0]) and ("L" in i[1])):
         print("<")
     elif (("S" in i[1]) and ("L" in i[0])):
         print(">")
     elif ("L" in i[0]):
         if (i[0].count("X")>i[1].count("X")):
              print(">")
         else:
              print("<")
     else:
         if (i[0].count("X")>i[1].count("X")):
              print("<")
         else:
              print(">")
