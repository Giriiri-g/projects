class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

    def __str__(self):
        return str(self.data)


def insert_at_beginning(head, tail, data):
    new_node = Node(data)
    if head is None:
        new_node.link = new_node
        head = new_node
        tail = new_node
    else:
        new_node.link = head
        tail.link = new_node
        head = new_node
    return head, tail


def insert_at_end(head, tail, data):
    new_node = Node(data)
    if head is None:
        new_node.link = new_node
        head = new_node
        tail = new_node
    else:
        new_node.link = head
        tail.link = new_node
        tail = new_node
    return head, tail


def insert_at_index(head, tail, data, index):
    if index < 0:
        print("[ERROR]: Index out of Range")
        return head, tail
    count = 0
    ptr = head
    while count < index - 1:
        if ptr.link is head:
            print("[ERROR]: Index out of Range")
            return head, tail
        ptr = ptr.link
        count += 1
    new_node = Node(data)
    new_node.link = ptr.link
    ptr.link = new_node
    if ptr is tail:
        tail = new_node
    return head, tail


def delete_from_beginning(head, tail):
    if head is None:
        return None, None
    if head is tail:
        return None, None
    head = head.link
    tail.link = head
    return head, tail


def delete_from_end(head, tail):
    if head is None or head.link is None:
        return None, None
    ptr = head
    while ptr.link is not tail:
        ptr = ptr.link
    ptr.link = head
    tail = ptr
    return head, tail


def delete_from_index(head, tail, index):
    if index < 0:
        print("[ERROR]: Index out of Range")
        return head, tail
    if index == 0:
        head = head.link
        tail.link = head
        return head, tail
    count = 0
    ptr = head
    while count < index - 1:
        if ptr.link is head:
            print("[ERROR]: Index out of Range")
            return head, tail
        ptr = ptr.link
        count += 1
    ptr.link = ptr.link.link
    if ptr.link is head:
        tail = ptr
    return head, tail


def length(head, tail):
    if head is None:
        return 0
    count = 1
    ptr = head.link
    while ptr is not head:
        count += 1
        ptr = ptr.link
    return count


def reverse(head, tail):
    if head is None or head.link is head:
        return head, tail
    prev_node = tail
    curr_node = tail.link
    next_node = curr_node.link
    while curr_node is not tail:
        curr_node.link = prev_node
        prev_node = curr_node
        curr_node = next_node
        next_node = next_node.link
    curr_node.link = prev_node
    head = curr_node
    return head, tail



def display(head, tail):
    if head is None:
        print("Head -> None <- Tail")
        return
    print("Head ->", end=" ")
    ptr = head
    while True:
        print(ptr, end=" -> ")
        ptr = ptr.link
        if ptr is head:
            break
    print("Head <- Tail")


# [Menu driven program]
print("""
__________________________
 Circular Linked List
__________________________

1.  Add an Element at the Beginning
2.  Add an Element at the End
3.  Add an Element at a specific Index
4.  Delete an Element from the Beginning
5.  Delete an Element from the End
6.  Delete an Element from a specific Index
7.  Find the Length of the Linked List
8.  Reverse the Circularly Linked List
9.  Display the List
10. Exit""")
head = None
tail = None
while True:
    ch = int(input("Enter your Choice (1-10): "))
    if ch < 1 or ch > 10:
        print("[ERROR]: Invalid Choice!")
        print("Shutting Down...")
        print("Exited the Program.")
        break
    if ch == 10:
        print("Shutting Down...")
        print("Exited the Program.")
        break
    if ch == 9:
        display(head, tail)
        continue
    print("_" * 40)
    print("Before:", end=" ")
    display(head, tail)

    if ch == 1:
        data = int(input("Enter the data to insert: "))
        head, tail = insert_at_beginning(head, tail, data)
    elif ch == 2:
        data = int(input("Enter the data to insert: "))
        head, tail = insert_at_end(head, tail, data)
    elif ch == 3:
        data = int(input("Enter the data to insert: "))
        index = int(input("Enter the index to insert at: "))
        head, tail = insert_at_index(head, tail, data, index)
    elif ch == 4:
        head, tail = delete_from_beginning(head, tail)
    elif ch == 5:
        head, tail = delete_from_end(head, tail)
    elif ch == 6:
        index = int(input("Enter the index to delete from: "))
        head, tail = delete_from_index(head, tail, index)
    elif ch == 7:
        print(f"The Length of the List is {length(head, tail)}")
        continue
    else:
        head, tail = reverse(head, tail)
    print("After:", end=" ")
    display(head, tail)
    print("_" * 40)
