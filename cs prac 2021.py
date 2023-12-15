import pickle
def Update():         #defining the function
  """TO UPDATE THE BINARY FILE"""
####################################################################################################################################################################################
  my_file_1 = open("Q.13,14,15.bin","rb")     #opening the 1st file
####################################################################################################################################################################################
  #initializing  the variables
  flag = 0
  list_1 = []
####################################################################################################################################################################################
  #user input to search the object to update
  find_roll_no = input("enter your roll.no to update your marks : ")
####################################################################################################################################################################################
  #to check wheather the  roll_no is valid or not
  try:
    find_roll_no.isdigit() == True
  except:
    print("invalid roll_no!")
    return
####################################################################################################################################################################################
  #finding the object to update
  try:
    while True:
      reading = p.load(my_file_1)
      if find_roll_no == reading[0]:
        flag += 1
        print("your existing mark :  ",reading[2])
        new_mark = input("enter your new mark : ")
        try:
          new_mark.isdigit() == True
        except:
          print("invalid marks!")
          return
        if new_mark == reading[2] :
          new_mark = reading[2]
        else:
          new_mark = int(new_mark)
        list_1.append([reading[0],reading[1],new_mark])
      else:
        list_1.append(reading)
####################################################################################################################################################################################
  #if end of file reached
  except EOFError:
    pass
####################################################################################################################################################################################
  #if search object is not found
  if flag == 0:
    print("roll_no not found!")
####################################################################################################################################################################################
  #writting the data into the anothor file
  else:
    my_file_1.close()  #closing the 1st file
    my_file_2 = open("Q.15.bin","wb")    #opening the 2nd file
    for line in list_1:     
      p.dump(line,my_file_2)    #writing into the 2nd file
    print("data updated!")   
    my_file_2.close()        #closing the 2nd file
####################################################################################################################################################################################
  print("")
  print("               ------------------------------ END OF PROGRAM ------------------------------           ")
####################################################################################################################################################################################
Update()       #calling the function   
#end of code