#smallest of 3 numbers
#character vowel or cnsonent
#grade evaluation in amrita



## [ smallest of the three numbers]

a = int(input("Enter the first Number: "))
b = int(input("Enter the second Number: "))
c = int(input("Enter the third Number: "))

if a<=b and a<=c:
     print(f"{a} is the smallest Number.")
elif b<=a and b<=c:
     print(f"{b} is the smallest Number.")
else:
     print(f"{c} is the smallest Number.")


## [ vowel or consonant ]

char = input("Enter a Character: ")
if len(char)>1 or char == "":
     print("Invalid Input: Enter a character.")
else:
     if char in ["a", "e", "i", "o", "u"]:
          print(f"{char} is a Vowel.")
     else:
          print(f"{char} is a Consonant.")

## [ Grade Evaluation ]

dsa = int(input("Enter your marks in DSA: "))
icn = int(input("Enter your marks in ICN: "))
ipy = int(input("Enter your marks in IPY: "))
adm = int(input("Enter your marks in ADM: "))
os = int(input("Enter your marks in OS: "))
gita = int(input("Enter your marks in Gita: "))
moc = int(input("Enter your marks in MOC: "))
bio = int(input("Enter your marks in BIO: "))
fundai = int(input("Enter your marks in FUNDAI: "))


total_credits = 23
sgpa = dsa*3 + icn*3 + ipy*2 + adm*1 + gita*2 + os*3 + moc*4 + bio*2 + fundai*3/2300

if credit == 10 :
     print(f"Your SGPA is {sgpa}")
     print("Grade: O")
elif credit > 9.5:
     print(f"Your SGPA is {sgpa}")
     print("Grade: A+")
elif credit > 9:
     print(f"Your SGPA is {sgpa}")
     print("Grade: A")
elif credit > 8:
     print(f"Your SGPA is {sgpa}")
     print("Grade: B+")
elif credit > 7:
     print(f"Your SGPA is {sgpa}")
     print("Grade: B")
elif credit > 6:
     print(f"Your SGPA is {sgpa}")
     print("Grade: C")
elif credit > 5:
     print(f"Your SGPA is {sgpa}")
     print("Grade: PASS")
elif credit > 0:
     print(f"Your SGPA is {sgpa}")
     print("Grade: FAIL")
