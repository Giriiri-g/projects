import mysql.connector as conn
db=conn.connect(host="localhost",user="root",passwd="qweasd",database="GSM")
crsr=db.cursor()

def addstock(id_,stock):
     global db
     global crsr
     crsr.execute(f"Update stock set stock=stock+{stock} where id={id_}")
     db.commit()

def modifystock(id_,name,stock,MRP,exp_date,vendor,BatchNo=None):
     crsr.execute(f"Delete FROM stock WHERE id={id_}")
     crsr.execute(f"INSERT INTO Stock VALUES({id_},'{name}',{stock},{MRP},'{BatchNo}','{exp_date}','{vendor}')")
     db.commit()

def deletestock():
    crsr.execute(f"Delete FROM stock WHERE id={id_}")
    db.commit()

#main func

con=True
while con:
     print('''1.add
2.modify
3.delete''')

     x=input("Enter your Choice: ")

     if x=='1':
         id_=int(input("Enter the ID of the item: "))
         stock=int(input("Enter the number of stock: "))
         addstock(id_,stock)
     
     elif x=='2':
         id_=int(input("Enter the ID of the item: "))
         name=input("Enter the Name of the product: ")
         stock=int(input("Enter the number of stocks: "))
         MRP=float(input("Enter the Price of the Product: "))
         BatchNo=input("Enther the batch number: ")
         exp_date=input("Enter the expiry date of the product: ")
         vendor=input("Enter the vendor: ")
         modifystock(id_,name,stock,MRP, exp_date,vendor,BatchNo)

     elif x=='3':
         id_=int(input("Enter the ID of the item: "))
         deletestock(id_)
     
     else:
         print("Invalid Choice")
