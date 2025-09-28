class Queue:
    def __init__(self):
        self.size = 5
        self.queue = [0] * self.size
        self.front = -1
        self.rear = -1
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def enqueue(self, data):
        self.rear += 1
        self.item_count += 1
        self.queue[self.rear] = data

    def deqqueue(self):
        self.front += 1
        self.item_count -= 1
        self.queue[self.front] = 0

    def print_queue(self):
        if self.front < 0:
            self.front *= -1

        if self.rear < 0:
            self.rear *= -1

        for index in range(self.rear, self.size):
            print(self.queue[index])

        for index in range(self.front + 1):
            print(self.queue[index])


q = Queue()
q.enqueue(10)
q.enqueue(9)
q.enqueue(8)
q.enqueue(7)

q.print_queue()
