chem = float(input("Enter your chemistry marks"))
cs = float(input("Enter your computer science marks"))
phy = float(input("Enter your physics marks"))
eng = float(input("Enter your english marks"))
math = float(input("Enter your math marks"))
p = (chem + cs + math + eng + phy)/5
if p >= 90:
    print("your overall grade is :Grade A")
elif  p >= 80: 
    print("your overall grade is :Grade B")
elif p >= 70: 
    print("your overall grade is :Grade C")
elif p >= 60: 
    print("your overall grade is :Grade D")
elif p >= 40: 
   print("your overall grade is :Grade E")
else: 
    print("your overall grade is :Grade F")