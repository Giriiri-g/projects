space = 4
no = 0
for i in range(5):
    out=""
    if i<2:
        out += " "*space
        out+=str(i+1) + ("   "+str(i+1))*no
        space-=2
        no+=1
    else:
        out += " "*space
        out+=str(i+1) + ("   "+str(i+1))*no
        space+=2
        no-=1
    print(out)
