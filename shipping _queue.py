class shippingqueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Shipping is currently empty. Dequeueing is not possible.")
            return
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            print("Shipping is currently empty.")
            return
        return self.queue[0]

    def display(self):
        print(self.queue)
    
ship_queue = shippingqueue()

#ship_queue.enqueue()
ship_queue.dequeue()
ship_queue.display()