"""
Write a program to implement a Singly Linked List to do the following cases:

Case1: Insertion at beginning

Case2: Insertion at End

Case 3:Insertion at Specific position

Case4: Deletion from beginning

Case5: Deletion from End

Case 6:Deletion from a specific position

Case7: Find the length of a linked list

Case 8: Reverse the Linked list
"""
class Node:
     def __init__(self, data):
          self.data = data
          self.link = None

     def __str__(self):
          if self.link is not None:
               print(" data    link")
               print("+---+-------------+")
               print("|{:^3}|{:^13}|".format(self.data, id(self.link)))
               print("+---+-------------+")
               print("{:^14}  |".format(id(self)))
               print(" "*16+"|")
               print(" "*16+"|")
               print(" "*16+"V")
          else:
               print(" data    link")
               print("+---+-------------+")
               print("|{:^3}|{:^13}|".format(self.data, "None"))
               print("+---+-------------+")
               print("{:^19}".format(id(self)))
          return ""


def insert_at_beginning(head, data):
     ptr = Node(data)
     ptr.link = head
     head = ptr
     return head


def insert_at_end(head, data):
     ptr = head
     while ptr.link is not None:
          ptr = ptr.link
     ptr.link = Node(data)
     return head


def insert_at_index(head, data, ind):
     if ind < 0:
          print("[ERROR]: Index out of Range")
          return head
     count = 0
     ptr = head
     while count < ind-1:
          count += 1
          ptr = ptr.link
          if ptr.link is None:
               break
     newnode = Node(data)
     newnode.link, ptr.link = ptr.link, newnode
     return head


def delete_from_beginning(head):
     head = head.link
     return head


def delete_from_end(head):
     if head is None or head.link is None:
          return None
     prev_node = None
     curr_node = head
     while curr_node.link is not None:
          prev_node = curr_node
          curr_node = curr_node.link
     prev_node.link = None
     return head


def delete_from_index(head, ind):
     if ind < 0:
          print("[ERROR]: Index out of Range")
          return head
     if ind == 0:
          head = head.link
          return head
     count = 0
     ptr = head
     while count < ind - 1:
          count += 1
          ptr = ptr.link
          if (ptr.link).link is None:
               ptr.link = None
               return head
     ptr.link = (ptr.link).link
     return head


def length(head):
     count = 0
     ptr = head
     while ptr is not None:
          count += 1
          ptr = ptr.link
     return count


def reverse(head):
     prev_node = None
     curr_node = head
     while curr_node is not None:
          next_node = curr_node.link
          curr_node.link = prev_node
          prev_node = curr_node
          curr_node = next_node
     return prev_node


def display(head):
     print(" " * 5 + "head")
     print("+-------------+")
     print(f"|{id(head)}|")
     print("+-------------+")
     print(" " * 7 + "|")
     print(" " * 7 + "|")
     print(" " * 7 + "|")
     print(" " * 7 + "V")
     while head is not None:
          print(head)
          head = head.link
          

temp = Node(12)
head = temp
head = insert_at_end(head, 24)
head = insert_at_end(head, 36)
head = insert_at_end(head, 48)
display(head)
head = reverse(head)
display(head)
