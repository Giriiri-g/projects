"""
Write a program to implement a Doubly  Linked List to do the following cases:

Case1: Insertion at beginning

Case2: Insertion at End

Case 3:Insertion at Specific position

Case4: Deletion from beginning

Case5: Deletion from End

Case 6:Deletion from a specific position

Case7: Find the length of a linked list

Case 8: Reverse the Linked list
"""

## [Class Definition]
class Node:
     def __init__(self, data):
          self.prev = None
          self.data = data
          self.next = None

          
     def __str__(self):
          if self.prev is None:
               print("      prev       data      next")
               print("+---------------+---+---------------+")
               print("|{:^15}|{:^3}|{:^15}|".format("None", self.data, id(self.next)))
               print("+---------------+---+---------------+")
               print(" "*11+"{:^15}   |".format(id(self)))
               print(" "*29+"|")
               print(" "*29+"|")
               print(" "*29+"V")
          elif self.next is not None:
               print("      prev       data      next")
               print("+---------------+---+---------------+")
               print("|{:^15}|{:^3}|{:^15}|".format(id(self.prev), self.data, id(self.next)))
               print("+---------------+---+---------------+")
               print(" "*11+"{:^15}   |".format(id(self)))
               print(" "*29+"|")
               print(" "*29+"|")
               print(" "*29+"V")
          else:
               print("      prev       data      next")
               print("+---------------+---+---------------+")
               print("|{:^15}|{:^3}|{:^15}|".format(id(self.prev), self.data, "None"))
               print("+---------------+---+---------------+")
               print("{:^33}".format(id(self)))
          return ""



## [Functions Definition]
def insert_at_beginning(head, data):
     ptr = Node(data)
     if head==None:
          return ptr
     ptr.next = head
     head.prev = ptr
     return ptr


def insert_at_end(head, data):
     if head==None:
          return Node(data)
     if head.next==None:
          ptr=Node(data)
          head.next = ptr
          ptr.prev = head
          return head
     ptr = head
     while ptr.next is not None:
          ptr = ptr.next
     newnode = Node(data)
     ptr.next = newnode
     newnode.prev = ptr
     return head


def insert_at_index(head, data, ind):
     if ind < 0:
          print("[ERROR]: Index out of Range")
          return head
     count = 0
     ptr = head
     while count < ind-1:
          count += 1
          ptr = ptr.next
          if ptr.next is None:
               print("[ERROR]: Index out of Range")
               return head
     newnode = Node(data)
     newnode.prev = ptr
     newnode.next = ptr.next
     ptr.next = newnode
     newnode.next.prev = newnode
     return head


def delete_from_beginning(head):
     if head is None or head.next is None:
          return None
     head = head.next
     head.prev = None
     return head


def delete_from_end(head):
     if head is None or head.next is None:
          return None
     prev_node = None
     curr_node = head
     while curr_node.next is not None:
          prev_node = curr_node
          curr_node = curr_node.next
     prev_node.next = None
     return head


def delete_from_index(head, ind):
     if ind < 0:
          print("[ERROR]: Index out of Range")
          return head
     if ind == 0:
          head = head.next
          head.prev = None
          return head
     count = 0
     ptr = head
     while count < ind:
          count += 1
          ptr = ptr.next
          if ptr is None:
               print("[ERROR]: Index out of Range")
               return head
     nextnode = ptr.next
     prevnode = ptr.prev
     prevnode.next = nextnode
     nextnode.prev = prevnode
     return head


def length(head):
     count = 0
     while head is not None:
          count += 1
          head = head.next
     return count


def reverse(head):
     if head is None or head.next is None:
          return head
     reversed_list = None
     saved_head = None
     while head is not None:
          saved_head=head.next
          head.next = reversed_list
          if reversed_list is not None:
               reversed_list.prev = head
          reversed_list = head
          head = saved_head
     reversed_list.prev = None
     return reversed_list


def display(head):
     if head is None:
          print(None)
          return
     while head is not None:
          if head.next is not None:
               print(head.data, end=" -> ")
          else:
               print(head.data)
          head = head.next

     
def fdisplay(head):
     print(" " * 6 + "head")
     print("+---------------+")
     print("|{:^15}|".format(id(head)))
     print("+---------------+")
     print(" " * 8 + "|")
     print(" " * 8 + "|")
     print(" " * 8 + "|")
     print(" " * 8 + "V")
     while head is not None:
          print(head)
          head = head.next


## [Menu driven program]
print("""
     __________________
     Doubly Linked List
     __________________

1.  Add an Element at the Begining
2.  Add an Element at the End
3.  Add an Element at a specific Index
4.  Delete an Element from the Begining
5.  Delete an Element from the End
6.  Delete an Element from a specific Index
7.  Find the Length of the Linked List
8.  Reverse the Doubly Linked List
9.  Fancy Display
10. Exit""")

head = None
while True:
     ch = int(input("   Enter your Choice 1-11: "))
     if ch<1 or ch>10:
          print("[ ERROR ]: Invalid Choice!")
          print("Shutting Down...")
          print("Exited the Program.")
          break
     elif ch==10:
          print("Shutting Down...")
          print("Exited the Program.")
          break
     elif ch==9:
          fdisplay(head)
          continue
     elif ch==7:
          print(f"The Length of the List is {length(head)}")
          continue
     print("_"*40)
     print("Before: ", end="")
     display(head)
     if ch==1:
          head = insert_at_beginning(head, 5)
     elif ch==2:
          head = insert_at_end(head, 10)
          head = insert_at_end(head, 25)
          head = insert_at_end(head, 30)
     elif ch==3:
          head = insert_at_index(head, 15, 1)
     elif ch==4:
          head = delete_from_beginning(head)
     elif ch==5:
          head = delete_from_end(head)
     elif ch==6:
          head = delete_from_index(head, 1)
     else:
          head = reverse(head)
     print("After: ", end="")
     display(head)
     print("_"*40)
