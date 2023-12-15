## [q1]

def min_(L, n):
     min_=L[0]
     for i in range(1, n):
          if min_>L[i]:
               min_=L[i]
     return min_

## [q2]

def sum_(L, n):
     sum_=0
     for i in range(0, n):
          sum_+=L[i]
     return sum_

## [q3]

def possum_(L, n):
     sum_=0
     for i in range(0, n):
          if L[i]>0:
               sum_+=L[i]
     return sum_

## [q4]

def fibon(n):
     a=0
     b=1
     c=1
     c=a+b
     print(a, end=" ")
     while c<n:
          print(c, end=" ")
          c=a+b
          a=b
          b=c


## [q5]


n = int(input("Enter the number :"))
fct=1
for i in range(1, n+1):
     fct*=i
print("The factorial of {} is {}".format(n, fct))
