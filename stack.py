"""
$ check fancy diplay in stack object in class file "stack.py"
$ implement pointer system rear pointer front pointer
$ dequeue from front p
$ incrementing pointers automatically
"""




##                                                             [ STACK IMPLEMENTATION ]

class stack:
     stack = list()
     size = 9999999
     def setmaxtop(self, maxtop):
          self.size = maxtop
     def display(self):
          if len(self.stack) == 0:
               print("[]")
               return
          print("[ ", end="")
          for i in self.stack:
               print(i, end=" ")
          print("]")
     def top(self):
          print(self.stack[-1])
     def push(self, item):
          if self.size<=len(self.stack):
               print("[ERROR]: STACK OVERFLOW")
               return
          self.stack.append(item)
     def pop(self):
          if len(self.stack) == 0:
               print("[ERROR]: STACK UNDERFLOW")
               return
          print(self.stack.pop())
     def fdiaplay(self):
          if len(self.stack) == 0:
               print("|  |")
               print("+--+")
               return
          for i in self.stack:
               print("|{4:^}|".format(i))
          print("+----+")




##                                                               [ QUEUE ]

class queue:
     def __init__(self, size):
          self.data = [None]*size
          self.front = -1
          self.rear = -1
          self.size = size

     def __iter__(self):
          return iter(self.data)
          
     def display(self):
          if self.front == -1:
               print("F = -1")
               print(" [ ]")
               print("R = -1")
          else:
               print(" " + " "*self.front+"  " + "F")
               print("[", end="")
               for i in self:
                    print("{^:5}".format(i), end="")
               print("]")
               print(" " + " "*self.rear+"  " + "R")
     def enqueue(self, item):
          if self.front == self.size-1:
               print("[ ERROR ]: Queue OverFlow!")
               return
          self.front+=1
          self.data[self.front] = item
     def dequeue(self):
          if self.rear == -1:
               print("[ ERROR ]: Queue UnderFlow!")
               return
          if self.front == self.rear:
               ret = self.data[self.front]
               self.front, self.rear = -1, -1
               return ret
          self.rear += 1
          return self.data[self.rear-1]

     def isEmpty(self):
          if self.rear == -1:
               return True
          return False

     def isFull(self):
          if self.front == self.size -1:
               return True
          return False
     def getrear(self):
          if self.rear == -1:
               print("[ ERROR ]: Queue UnderFlow!")
               return
          return self.data[self.rear]

     def getfront(self):
          if self.front == -1:
               print("[ ERROR ]: Queue UnderFlow!")
               return
          return self.data[self.front]





