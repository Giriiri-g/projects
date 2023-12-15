
#below the float refers to integer here now it only takes integer as its input
a = float(input("enter you first value :"))
b = float(input("enter you second value :"))
#below there is no float that means it takes all various inputs even integers
c = input("which operation do you want to commence :")
# below "==" this means it is comparing wheter it is the assigned value or not the it returns a boolean value 
if c == "sum" :
#here it does only consider integer so it doesnt take ddecimal value and gives decimal value like 3.0    
    print("your sum is :", a+b)
# above the space is called indented block it is understood by the interpreter as a groups of code
elif c == "subraction" :
        print("your reduced value is :", a-b)
elif c == "multiplication" :
            print("your multipled value is :", a*b)
elif c == "division" :
                print("your divided value is :", a/b)
else :
# below the """ indicate multiline string it has to be opened and closed
    print("""
your operator is not
understood   by  the
    interpreter
""")
#do no forget to close any parenthesis even above all cases
#do not create a infinite loop