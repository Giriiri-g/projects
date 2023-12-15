t = int(input("Enter the number of test cases :"))
for i in range(t):
     m = 2
     n = int(input("Enter a prime number :"))
     while True:
          x = True
          x2 = False
          for j in range(2, int(m/2)):
               if m%j==0:
                    x = False
                    break
          if x :
               for k in range(2, int((m+n)/2)):
                    if (m+n)%k==0:
                         x2 = True
                         break
               if x2:
                    print(m)
                    break
          m+=1
