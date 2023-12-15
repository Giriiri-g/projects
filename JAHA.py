def update():
    import pickle as p
    my_file_1 = open("D:\\preparations\\testfile.dat","rb")
    flag = 0
    list_1 = []
    find_roll_no = int(input("enter your roll.no to update your marks : "))
    try:
        while True:
            reading = p.load(my_file_1)
            if find_roll_no == reading[0]:
                flag += 1
                print("your existing mark :  ",reading[2])
                new_mark = input("enter your new mark : ")
                try:
                    new_mark.isdigit() == True
                except:
                    print("invalid marks!")
                    return
                if new_mark == reading[2] :
                    new_mark = reading[2]
                else:
                    new_mark = int(new_mark)
                    list_1.append([reading[0],reading[1],new_mark])
            else:
                list_1.append(reading)
    except EOFError:
        pass
    if flag == 0:
        print("roll_no not found!")
    else:
        my_file_1.close()
        my_file_2 = open("Q.15.bin","wb")
        for line in list_1:
            p.dump(line,my_file_2)
        print("data updated!")
        my_file_2.close()
update()