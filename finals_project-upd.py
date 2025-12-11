class Item:
    def __init__(self, data):
        self.data = data
        self.next = None


class Container:
    def __init__(self):
        self.items = None
        self.next = None
        self.max_items = 10
        self.item_count = 0

    def is_empty(self):
        return self.items is None
    
    def is_full(self):
        return self.item_count == self.max_items

    def order_item(self, data):
        if self.is_full():
            return
        
        if self.is_empty():
            self.items = Item(data)
            self.item_count += 1
            return
        
        current_item = self.items
        while current_item.next:
            current_item = current_item.next
        current_item.next = Item(data)

    def ship_item(self):
        if self.is_empty():
            return
    
        shipped_item = self.items.data
        self.items = self.items.next
        return shipped_item
    
    def show_items(self):
        if self.is_empty():
            return
        
        current_item = self.items
        while current_item.next:
            print(current_item.data, end="->")
            current_item = current_item.next

        print(current_item.data)


class Storage:
    def __init__(self):
        self.containers = None
        self.max_containers = 10
        self.container_count = 0
    
    def is_full(self):
        return self.container_count == self.max_containers
    
    def is_empty(self):
        return self.containers is None
    
    def add_container(self):
        if self.is_full():
            return
        
        if self.is_empty():
            self.containers = Container()
            self.container_count += 1
            return
        
        current_container = self.containers
        while current_container.next:
            current_container = current_container.next
        
        current_container.next = Container()

    def show_containers(self):
        if self.is_empty():
            return
        
        current_container = self.containers
        while current_container.next:
            current_container.show_items()
            current_container = current_container.next

        current_container.show_items()
        

input = int(input("Set log amount: \n ")) #Sample lang for setting number of logs

class Logs:
    def __init__(self, Log_capacity = input): #fixed array, Stack Array Implement
        self.logs_stack = []
        self.log = Log_capacity
        self.top = -1
    
    def Log_Amount(self):
        return len(self.logs_stack)
        
    def log_empty(self):
        return self.top == -1
    
    def log_full(self):
        if self.log is None:
            return False
        return self.top == self.log - 1 
    
    def New_log(self, CurrentLog):
        if self.log is not None and self.log_full():
            print("Log is currently full.")
            return
        self.logs_stack.append(CurrentLog)
        self.top += 1 
        print(f"Added new log: {CurrentLog}")
    
    def Remove_Log(self):
        if self.log_empty():
            print("Log is currently empty.")
            return None
        CurrentLog = self.logs_stack.pop()
        self.top -= 1 
        return CurrentLog
    
    def Log_Check(self):
        if self.log_empty():
            print("Nothing to peek. Log is currently empty.")
            return None
        return self.logs_stack[self.top]