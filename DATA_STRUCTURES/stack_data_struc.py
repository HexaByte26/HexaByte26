class Stack_Array:
    def __init__(self):
        self.top_index = -1
        self.capacity = 5
        self.stack = [0] * self.capacity
        self.item_count = 0

    def push(self, data):
        if self.is_empty():
            self.top_index += 1
            self.item_count += 1
            self.stack[self.top_index] = data
            return

        if self.is_full():
            print(f"Stack is full")
            return

        self.top_index += 1
        self.item_count += 1
        self.stack[self.top_index] = data

    def pop(self):
        if self.is_empty():
            print(f"Stack is empty")
            return

        print(f"{self.stack[self.top_index]} is removed from the stack")

        self.stack[self.top_index] = 0
        self.top_index -= 1
        self.item_count -= 1

    def is_empty(self):
        if self.item_count == 0:
            return True

    def is_full(self):
        if self.item_count == self.capacity:
            return True

    def peek(self):
        print(
            f"{self.stack[self.top_index]} is the top most item in the stack")

    def size(self):
        pass


stack = Stack_Array()
stack.push(10)
stack.push(9)
stack.push(8)

stack.peek()

stack.pop()

stack.peek()
