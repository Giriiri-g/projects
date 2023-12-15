## [Array Class Definition]

class Array:
     def __init__(self, size=0):
          self.size = size
          self.data = [None] * size

     def __getitem__(self, index):
          if self.size-1 <index or index<0:
               print("Index out of Bounds")
               return
          return self.data[index]

     def __setitem__(self, index, value):
          if self.size-1 <index or index<0:
               print("Index out of Bounds")
               return
          self.data[index] = value

     def __len__(self):
          return self.size

     def __str__(self):
          return f"Array({self.data})"

     def __delitem__(self, index):
          if self.size-1<index or index<0:
               print("Index out of Bounds")
               return
          self.data.pop(index)
          self.size -= 1

     def __iter__(self):
          return iter(self.data)

     def __add__(self, arrobj):
          size = self.size + arrobj.size
          array = Array(size)
          array.data = self.data + arrobj.data
          return array
     
     def insert(self, item, index):
          if index==-1:
               self.size+=1
               self.data.append(item)
               return self
          if self.size-1 <index or index<0:
               print("Index out of Bounds")
               return
          self.size+=1
          self.data.insert(index, item)
          return self
     
     def indexof(self, item):
          if item in self.data:
               return self.data.index(item)
          else:
               print(f"{item} Not Found In The Array")
               return

     def sort(self):
          self.data = self.qsort(self.data)
          return self

     
     def qsort(self, arr):
          if len(arr) <= 1:
               return arr
          piv = arr[0]
          l = [x for x in arr[1:] if x < piv]
          r = [x for x in arr[1:] if x >= piv]
          return self.qsort(l) + [piv] + self.qsort(r)

     def bsearch(self, ele):
          self.sort()
          ll, ul = 0, self.size-1
          while ll<=ul:
               piv = (ll+ul)//2
               if self.data[piv]==ele:
                    return piv
               elif self.data[piv]>ele:
                    ul-=1
               else:
                    ll+=1
          return None





## [Array - Labsheet 1]

# Q1     Write a program to search for an element in a sorted array efficiently.

print("____________________________________________________________________________________________")
print("\n\nQ1     Write a program to search for an element in a sorted array efficiently.\n\n")

size = int(input("Enter the size of the Array : "))
arr = Array(size)
for i in range(size):
    arr[i] = int(input(f"Enter the {i}th Element :"))
print(arr.sort())
ele = int(input("Enter an element to search for in the array : "))
index = arr.bsearch(ele)
if index==None:
     print(f"The Element {ele} is not Founf in the Array : {arr}.")
else:
     print(f"The Element {ele} is Found at Index {index}: Array[{index}] = {ele}.")


#  Q2   Write a program to search for the second occurrence of ‘6’ in an array and replace it with ‘7’

print("____________________________________________________________________________________________")
print("\n\nQ2   Write a program to search for the second occurrence of ‘6’ in an array and replace it with ‘7’\n\n")
size = int(input("Enter the size of the Array : "))
arr = Array(size)
for i in range(size):
    arr[i] = int(input(f"Enter the {i}th Element :"))
firstOccurence = False
print(arr)
for i in range(size):
     if arr[i]==6 and firstOccurence:
          arr[i] = 7
          break
     elif arr[i]==6:
          firstOccurence = True
print(arr)


#   Q3    Write a program to perform the following operations on array
#              a. Creation
#              b. Insertion (at start, at end, using index, based on value)
#              c. Deletion (at start, at end, using index, based on value)
#              d. Traversal
#              e. Searching an element. (based on value, based on index)

print("____________________________________________________________________________________________")
print("""\n\n
   Q3    Write a program to perform the following operations on array
              a. Creation
              b. Insertion (at start, at end, using index, based on value)
              c. Deletion (at start, at end, using index, based on value)
              d. Traversal
              e. Searching an element. (based on value, based on index)

\n""")
size = int(input("Enter the size of the Array : "))
arr = Array(size)
for i in range(size):
    arr[i] = int(input(f"Enter the {i}th Element :"))

print(f"Created Array : {arr}")

print(f"""\n\nInserting an Element in the Array: {arr}
     1. Start
     2. End
     3. Index
     4. Insert the Element in the sorted Array: {arr.qsort(arr.data)}
""")
ch = int(input("Enter your Choice: "))
if ch<=0 or ch>4:
     print("Invalid Choice: choose between [1,4]")
else:
     item = int(input("Enter a Item to Insert into the Array :"))
     if ch==1:     
          print("Array Before Inserting :", arr)
          print("Array After  Inserting :", arr.insert(item, 0))
     elif ch==2:
          print("Array Before Inserting :", arr)
          print("Array After  Inserting :", arr.insert(item, -1))
     elif ch==3:
          index = int(input("Enter the Index to Insert the Element :"))
          print("Array Before Inserting :", arr)
          print("Array After  Inserting :", arr.insert(item, index))
     
     else:
          arr.sort()
          print("Array Before Insertion :", arr)
          if arr[size-1]<item:
               arr.insert(item, -1)
          else:
               for i in arr:
                    if i>=item:
                         arr.insert(item, arr.indexof(i))
                         break
          print("Array after Insertion :", arr)

print(f"""\n\nDeleting an Element from the Array: {arr}
     1. Start
     2. End
     3. Index
     4. Delete the Element based on its Value
""")
ch = int(input("Enter your Choice: "))

if ch==1:     
     print("Array Before Deletion :", arr)
     del arr[0]
     print("Array After  Deletion :", arr)
elif ch==2:
     print("Array Before Deletion :", arr)
     del arr[arr.size-1]
     print("Array After  Deletion :", arr)
elif ch==3:
     index = int(input("Enter the Index to Delete the Element :"))
     print("Array Before Deletion :", arr)
     del arr[index]
     print("Array After  Deletion :", arr)

elif ch==4:
     item = int(input("Enter a Item to Delete from the Array :"))
     if item not in arr:
          print(f"Item not in Array, Array is unchanged {arr}")
     else:
          if arr.data.count(item)>1:
               ch = input("Multiple Elements is found with the same value!, y- Delete all values, n- Delete only the first occurence :")
               print("Array Before Deletion :", arr)
               if ch.lower()=="y":
                    for i in range(arr.data.count(item)):
                         arr.data.remove(item)
                         arr.size-=1
               elif ch.lower()=="n":
                    arr.data.remove(item)
                    arr.size-=1
               else:
                    print("Invalid Choice, setting to Delete all Occurence!")
                    for i in range(arr.data.count(item)):
                         arr.data.remove(item)
                         arr.size-=1
               print("Array after Deletion :", arr)
          else:
               print("Array Before Deletion :", arr)
               del arr[arr.indexof(item)]
               print("Array after Deletion :", arr)
else:
     print("Invalid Choice: choose between [1,4]")


print("\n\nTraversing through the Array:")
for i in arr:
     print(i, end=" ")



print(f"""\n\nSearching an Element in the Array: {arr}
     1. based on value
     2. based on index
""")
ch = int(input("Enter your Choice: "))

if ch==1:     
     ele = int(input("Enter an element to search for in the array : "))
     index = arr.bsearch(ele)
     if index==None:
          print(f"The Element {ele} is not Founf in the Array : {arr}.")
     else:
          print(f"The Element {ele} is Found at Index {index}: Array[{index}] = {ele}.")
elif ch==2:
     index = int(input("Enter the Index to Find the Element in the Array : "))
     if arr.size-1 <index or index<0:
          print("Index out of Bounds")
     else:
          ele = arr[index]
          print(f"The Element {ele} is Found at Index {index}: Array[{index}] = {ele}.")



#  Q4   Given an array with n numbers split it from a specified position, and move the first 
#       part of array and append it to the end.

print("____________________________________________________________________________________________")
print("\n\nQ4       Given an array with n numbers split it from a specified position, and move the first part of array and append it to the end.\n\n")
n = int(input("Enter the size of the Array : "))
arr = Array(n)
for i in range(n):
    arr[i] = int(input(f"Enter the {i}th Element :"))

print(f"Created Array : {arr}")

index = int(input("Enter the Index to split the Array : "))
if n-1 <index or index<0:
          print("Index out of Bounds")
else:
     arr.data = arr.data[index::] + arr.data[:index:]
     print(arr)



#  Q5     Given a sorted array of nums, remove the duplicates such that each element appears 
#         only once and return the new length
print("____________________________________________________________________________________________")
print("\n\nQ5  Given a sorted array of nums, remove the duplicates such that each element appears only once and return the new length\n\n")
size = int(input("Enter the size of the Array : "))
arr = Array(size)
for i in range(size):
    arr[i] = int(input(f"Enter the {i}th Element :"))

print(f"Created Array : {arr}")

print(f"Sorted Array : {arr.sort()}")

arr.data = list(set(arr))

arr.size = len(arr.data)

print(f"Array after deleting duplicate Elements : {arr}")



#  Q6  Given an array of integers, return indices of the two numbers
#         such that they add up to a specific target. You may assume
#         that each input would have exactly one solution, and you may
#         not use the same element twice.

print("____________________________________________________________________________________________")
print("\n\nQ6  Given an array of integers, return indices of the two numbers \nsuch that they add up to a specific target. You may assume that each \ninput would have exactly one solution, and you may not use the same element twice.\n\n")
size = int(input("Enter the size of the Array : "))
arr = Array(size)
for i in range(size):
    arr[i] = int(input(f"Enter the {i}th Element :"))

print(f"Created Array : {arr}")

target = int(input("Enter the Target :"))
orderedPairs=[]
for i in range(size):
     for j in range(size):
          if i!=j:
               if arr[i] + arr[j]==target and {i, j} not in orderedPairs:
                    orderedPairs.append({i, j})
                    print(f"The Elements that add upto {target} are {arr[i]} and {arr[j]} at Indices {i} and {j} Respectively.")
del target, orderedPairs

#  Q7     Given an array nums and a value val, remove all instances of that value in the array
#         and return the new length. The order of elements can be changed

print("____________________________________________________________________________________________")
print("\n\nQ7     Given an array nums and a value val, remove all instances of that value in the array and return the new length.\n The order of elements can be changed\n\n")

size = int(input("Enter the size of the Array : "))
arr = Array(size)
for i in range(size):
    arr[i] = int(input(f"Enter the {i}th Element :"))

print(f"Created Array : {arr}")


val = int(input("Enter a Value to Delete from the Array :"))
for i in range(arr.data.count(val)):
     arr.data.remove(val)
     arr.size-=1
print(f"The new size of The {arr} is : {arr.size}")

del val

#  Q8     Given an array of n elements to find if an integer x appears more than n/2 times in a
#         sorted array of n integers.

print("____________________________________________________________________________________________")
print("\n\nQ8     Given an array of n elements to find if an integer x appears more than n/2 times in a sorted array of n integers.\n\n")
n = int(input("Enter the size of the Array : "))
arr = Array(n)
for i in range(n):
    arr[i] = int(input(f"Enter the {i}th Element :"))

print(f"Created Array : {arr}")


uniqueElements = list(set(arr))
n /= 2
for i in uniqueElements:
     icount = arr.data.count(i)
     if icount>n:
          print(f"The Value {i} appeared {icount} times in the Array.")

del icount, n

#  Q9     Write a program to merge elements of two sorted arrays A and B of size p and
#         q, by maintaining the sorted order i.e. fill A with first p smallest elements and fill B
#         with remaining elements

print("____________________________________________________________________________________________")
print("\n\nQ9     Write a program to merge elements of two sorted arrays A and B of size p and q, by maintaining the sorted order i.e. fill A with first p smallest elements and fill B with remaining elements\n\n")

p = int(input("Enter the size of the Array A: "))
arrA = Array(p)
for i in range(p):
    arrA[i] = int(input(f"Enter the {i}th Element of A:"))

print(f"Created Array A: {arrA}")

q = int(input("Enter the size of the Array B: "))
arrB = Array(q)
for i in range(q):
    arrB[i] = int(input(f"Enter the {i}th Element of B:"))

print(f"Created Array B: {arrB}")

arrC = arrA + arrB

print("Sorted Array :", arrC.sort())

arrA.data = arrC.data[:p:]
arrB.data = arrC.data[p::]
print(f"Array A: {arrA}, Array B: {arrB}")
