num = int(input("Enter your number for analysing :"))
i = 2
prime = True
while i <= int(num):
    if i < int(num) and num % i == 0:
        prime = False
        break
    i += 1
if num < 2:
    prime = False
if prime == True:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")