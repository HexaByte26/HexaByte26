class EmptyStackError(Exception):
    pass


class FullStackError(Exception):
    pass


class DiskStorageStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.place_holder = "_______"
        self.disks = [self.place_holder] * self.capacity
        self.top_index = 0

    def is_empty(self):
        return self.top_index == 0

    def is_full(self):
        return self.top_index == self.capacity

    def push_disk(self, disk_item):
        if self.is_full():
            print("Log: Cannot push to a full Disk Storage")
            return

        self.disks[self.top_index] = disk_item
        self.top_index += 1

        print(f"Log: Disk {disk_item} has been pushed in the Disk Storage")

    def pop_disk(self):
        if self.is_empty():
            raise EmptyStackError("Log: Cannot pop from an empty Disk Storage")

        self.disks[self.top_index] = self.place_holder
        self.top_index -= 1

        print(f"Log: Disk {self.disks[self.top_index]} has been popped from the Disk Storage")

    def peek_top_disk(self):
        print(f"Log: {self.disks[self.top_index]} is the top most disk")

    def get_disks_num(self):
        print(f"Log: Currently there are {self.top_index} disks inside of the Disk Storage")

    def show_disks(self):
        print("-------T-O-P-------\n")
        for disk_index in range(self.capacity - 1, -1, -1):
            print(self.disks[disk_index])
        print("\n----B-O-T-T-O-M-----")


disk_storage = DiskStorageStack(10)
disk_storage.push_disk("Harry Potter")
disk_storage.push_disk("Maze Runner")
disk_storage.push_disk("Hangover")

disk_storage.show_disks()

disk_storage.pop_disk()

disk_storage.peek_top_disk()

disk_storage.pop_disk()
disk_storage.show_disks()
disk_storage.pop_disk()
disk_storage.show_disks()
disk_storage.pop_disk()
disk_storage.show_disks()

import os, time

def clr_terminal():
    os.system("cls")

def main():
    operations = ["Push a Disk", "Pop a Disk", "Peek a the top the Disk Storage", "Get the number of disks", "Show the disks inside the Disk Storage", "Quit"]

    running = True

    while running:
        try:
            capacity = int(input("> Enter a number for the capacity of Disk Storage: "))
        except ValueError:
            print("I> nput must be a number")
            continue

        disk_storage = DiskStorageStack(capacity)

        print("=========== Disk Storage Management ===========")
        for num, operation in enumerate(operations, start=1):
            print(f"{num}.{ operation}")

        try:
            selected_operation = int(input("> Enter a number to select an operation: "))
        except ValueError:
            continue

        if selected_operation == 1:
            disk = input("> Enter the name of the disk: ")
            disk_storage.push_disk(disk)

        elif selected_operation == 2:
            disk_storage.pop_disk()

        elif selected_operation == 3:
            disk_storage.peek_top_disk()

        elif selected_operation == 4:
            disk_storage.get_disks_num()

        elif selected_operation == 5:
            disk_storage.show_disks()

        elif selected_operation == 6:
            running = False

        else:
            print("Log: Input must be 1 - 6")
            continue

if __name__ == "__main__":
    main()