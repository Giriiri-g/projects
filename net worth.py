salary = int(input("please enter your monthly salary :"))
interest = int(input("please enter your total interest payments and taxes :"))
rent = int(input("please enter your rent payments :"))
profits = int(input("please enter your profits from other forms of incomes :"))
grss = salary-interest - rent + profits
if grss <= 10000 :
  print("HRA = 20%, DA = 80%")
if grss <= 20000 :
  print("HRA = 25%, DA = 90%")
if grss > 20000 :
  print("HRA = 30%, DA = 95%")