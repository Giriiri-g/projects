class Deque:
    def __init__(self, size):
        self.data = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size

    def isFull(self):
        return (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1)

    def isEmpty(self):
        return self.front == -1

    def insertFront(self, item):
        if self.isFull():
            print("[ ERROR ]: Deque Overflow!")
            return

        if self.front == -1:
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1

        self.data[self.front] = item

    def insertLast(self, item):
        if self.isFull():
            print("[ ERROR ]: Deque Overflow!")
            return

        if self.front == -1:
            self.front = self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1

        self.data[self.rear] = item

    def deleteFront(self):
        if self.isEmpty():
            print("[ ERROR ]: Deque Underflow!")
            return None

        item = self.data[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1

        return item

    def deleteLast(self):
        if self.isEmpty():
            print("[ ERROR ]: Deque Underflow!")
            return None

        item = self.data[self.rear]

        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1

        return item

    def getFront(self):
        if self.isEmpty():
            print("[ ERROR ]: Deque Underflow!")
            return None

        return self.data[self.front]

    def getRear(self):
        if self.isEmpty():
            print("[ ERROR ]: Deque Underflow!")
            return None

        return self.data[self.rear]

    def display(self):
        if self.front == -1:
            print("[ ERROR ]: Deque Underflow!")
            return

        print("Front =", self.front, ", Rear =", self.rear)
        if self.front <= self.rear:
            for i in range(self.front, self.rear + 1):
                print(self.data[i], end=" ")
        else:
            for i in range(self.front, self.size):
                print(self.data[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.data[i], end=" ")

        print()

size = 5
deque_obj = Deque(size)

deque_obj.insertFront(1)
deque_obj.insertFront(2)
deque_obj.insertLast(3)
deque_obj.insertLast(4)

deque_obj.display()

item = deque_obj.deleteFront()
print("Deleted front item:", item)

item = deque_obj.deleteLast()
print("Deleted last item:", item)

deque_obj.display()
