class Queue:
    def __init__(self, size):
        self.data = [None] * size
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
            print(" " + "     " * self.front + "  " + "F")
            print("[", end="")
            for i in range(self.size):
                if self.data[i] is None:
                    print("{:^5}".format("None"), end="")
                else:
                    print("{:^5}".format(self.data[i]), end="")
            print("]")
            print(" " + "     " * self.rear + "  " + "R")

    def enqueue(self, item):
        if self.isFull():
            print("[ ERROR ]: Queue Overflow!")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.data[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            print("[ ERROR ]: Queue Underflow!")
            return None

        item = self.data[self.front]

        if self.front == self.rear:
            self.front, self.rear = -1, -1
        else:
            self.front = (self.front + 1) % self.size

        return item

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def getrear(self):
        if self.rear == -1:
            print("[ ERROR ]: Queue Underflow!")
            return
        return self.data[self.rear]

    def getfront(self):
        if self.front == -1:
            print("[ ERROR ]: Queue Underflow!")
            return
        return self.data[self.front]

    def splitq(self):
        if self.front == -1:
            print("[ ERROR ]: Queue Underflow!")
            return None, None

        odd_queue = Queue(self.size)
        even_queue = Queue(self.size)

        for i in range(self.front, self.rear + 1):
            if (i - self.front) % 2 == 0:
                even_queue.enqueue(self.data[i])
            else:
                odd_queue.enqueue(self.data[i])

        return odd_queue, even_queue

    def getminElement(self):
        if self.front == -1:
            print("[ ERROR ]: Queue Underflow!")
            return None

        min_element = self.data[self.front]
        for i in range(self.front, self.rear + 1):
            if self.data[i] < min_element:
                min_element = self.data[i]

        return min_element




size = int(input("Enter the size of the queue: "))
queue_obj = Queue(size)

while True:
    print("\nMenu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Split Queue")
    print("5. Get Minimum Element")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the item to enqueue: ")
        queue_obj.enqueue(item)
    elif choice == 2:
        item = queue_obj.dequeue()
        if item is not None:
            print("Dequeued item:", item)
    elif choice == 3:
        print("Queue Contents:")
        queue_obj.display()
    elif choice == 4:
        odd_queue, even_queue = queue_obj.splitq()
        print("Odd-Positioned Queue:")
        odd_queue.display()
        print("Even-Positioned Queue:")
        even_queue.display()
    elif choice == 5:
        min_element = queue_obj.getminElement()
        if min_element is not None:
            print("Minimum Element in the Queue:", min_element)
    elif choice == 6:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please try again.")
