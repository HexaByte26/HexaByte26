class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.queue = None
        self.front = None
        self.rear = None
        self.length = 0

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.queue = new_node
            self.front = new_node
            self.rear = new_node
            return
        
        current_node = self.queue
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")

        self.queue = self.queue.next
        self.front = self.queue
        self.length -= 1

    def print_queue(self):
        current_node = self.front
        while current_node.next:
            print(current_node.data, end="->")
            current_node =  current_node.next

        print(self.rear.data)

queue = Queue()
queue.enqueue(0)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.print_queue()

queue.dequeue()

queue.print_queue()

queue.enqueue(4)

queue.print_queue()

queue.dequeue()

queue.print_queue()