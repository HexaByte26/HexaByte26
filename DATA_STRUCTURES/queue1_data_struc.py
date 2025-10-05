class Queue:
    def __init__(self):
        self.place_holder = "___"
        self.size = 5
        self.queue = [self.place_holder] * self.size
        self.front = -1
        self.rear = -1
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0
    
    def is_full(self):
        return self.item_count == self.size

    def enqueue(self, data):
        if self.is_empty():
            self.front = -1
        
        self.rear += 1
        self.queue[self.rear] = data
        self.item_count += 1

        if self.rear == self.size - 1:
            self.rear = -1
            self.dequeue()

    def dequeue(self):
        if self.is_full():
            self.rear = -1

        self.front += 1
        self.queue[self.front] = self.place_holder
        self.item_count -= 1

    def get_front_queue(self):
        print(self.queue[self.front + 1])

    def get_rear_queue(self):
        print(self.queue[self.rear])

    def print_queue(self):
        print(self.queue)

queue = Queue()
queue.enqueue(10)
queue.enqueue(9)
queue.enqueue(8)
queue.enqueue(7)

queue.print_queue()

queue.dequeue()
queue.dequeue()

queue.print_queue()

queue.enqueue(6)
queue.enqueue(5)

queue.print_queue()
queue.get_front_queue()
queue.get_rear_queue()