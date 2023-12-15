## [Third Question]

def string_same(str1, str2):
    if len(str1) != len(str2):
        print("Invalid input")
        return
    else:
        x = 0 # hello cello
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                print(str1[i])
                x +=1
        print(x)  


## [First Question]

spaces = 4
for i in range(1, 4):
     sum_ = ""
     sum_ += " "*spaces
     spaces-=2
     sum_ += str(i) +(" "*3 + str(i))*(i-1)
     print(sum_)
j = 1
spaces = 0
for i in range(4, 6):
     spaces+=2
     sum_=""
     sum_ += " "*spaces
     sum_ += str(i) + (" "*3 + str(i))*j
     j-=1
     print(sum_)
