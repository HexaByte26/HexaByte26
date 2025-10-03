class DiskStorage:
    def __init__(self):
        self.capacity = 10
        self.disks = ["___"] * self.capacity
        self.top_index = 0
    
    def is_empty(self):
        return self.top_index == 0
    
    def is_full(self):
        return self.top_index == self.capacity
        
    def push_disk(self, disk_item):
        if self.is_full():
            return
            
        self.disks[self.top_index] = disk_item
        self.top_index += 1
        
    def pop_disk(self):
        if self.is_empty():
            return
            
        self.disks[self.top_index] == "__"
        self.top_index -= 1
    
    def peek_top_disk(self):
        print(self.disks[self.top_index])
        
    def show_disks(self):
        for disk_index in range(self.capacity - 1, -1, -1):
            print(self.disks[disk_index])

disk_storage = DiskStorage()
disk_storage.push_disk("Harry Potter")
disk_storage.push_disk("Maze Runner")
disk_storage.push_disk("Hangover")

disk_storage.show_disks()

disk_storage.pop_disk()

disk_storage.peek_top_disk()