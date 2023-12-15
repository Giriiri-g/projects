## [ q1 ]


def subset(A, B):
     A= list(A)
     B=list(B)
     for i in A:
          if i not in B:
               return False
     return True

A={0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
B={1, 2, 3}
print(subset(A, B))
print(subset(B, A))
print(subset({}, B))


## [ q2 ]


def equal(A, B):
     if A==B:
          return True
     return False

A={0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
B={1, 2, 3}
print(equal(A, B))

C={3, 2, 1}
B={1, 2, 3}
print(equal(C, B))


C={1, 2, 1}
B={1, 2, 3}
print(equal(C, B))

C={}
B={1, 2, 3}
print(equal(C, B))


## [ q3 ]




nA=int(input("Enter the numbber of elements in set A :"))
nB=int(input("Enter the numbber of elements in set B :"))
A=[]
B=[]
print("Enter the elements for set A :", end=" ")
for i in range(nA):
     element=int(input(""))
     A.append(element)
print("\nEnter the elements for set B :", end=" ")
for i in range(nB):
     element = int(input(""))
     B.append(element)

union=[]
for i in A+B:
     if i not in union:
          union.append(i)

print("The union of the sets A and B is ", set(union))
intersection=[]
for i in A+B:
     if i not in intersection:
          if ((i in A) and (i in B)):
               intersection.append(i)

print("The intersection of the sets A and B is ", set(intersection))

diff=[]
for i in A:
     if ((i not in diff) and (i not in B)):
          diff.append(i)

print("The difference of the set A-B is ", set(diff))


## [ q5 ]

"""
the function returns the cardinality of the cartesian product of the five sets
cardinality of cross product is just the product of cardinalities of the individual sets
thus if cardinalities are n1, n2, n3, n4, n5
then the function returns n1 x n2 x n3 x n4 x n5 as k
"""

## [ q6 ]


