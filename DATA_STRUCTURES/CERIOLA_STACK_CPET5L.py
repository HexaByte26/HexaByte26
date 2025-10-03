class DiskStorageStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.place_holder = "_______"
        self.disks = [self.place_holder] * self.capacity
        self.top_disk_index = 0

    def is_empty(self):
        return self.top_disk_index == 0

    def is_full(self):
        return self.top_disk_index == self.capacity

    def push_disk(self, disk_item):
        if self.is_full():
            print("\nLog: Cannot push to a full Disk Storage")
            return

        self.disks[self.top_disk_index] = disk_item
        self.top_disk_index += 1

        print(f"\nLog: Disk '{disk_item}' has been pushed in the Disk Storage")

    def pop_disk(self):
        if self.is_empty():
            print("\nLog: Cannot pop from an empty Disk Storage")
            return

        self.top_disk_index -= 1

        print(f"\nLog: Disk '{self.disks[self.top_disk_index]}' has been popped from the Disk Storage")

        self.disks[self.top_disk_index] = self.place_holder

    def peek_top_disk(self):
        if self.is_empty():
            print(f"\nLog: the disk storage is currently empty")
            return
        
        print(f"\nLog: '{self.disks[self.top_disk_index - 1]}' is the top most disk")

    def get_disks_num(self):
        print(f"\nLog: Currently there are {self.top_disk_index} disk(s) inside of the Disk Storage")

    def show_disks(self):
        print("-------T-O-P-------\n")
        for disk_index in range(-1, -1 * self.capacity - 1, -1):
            print(self.disks[disk_index])
        print("\n----B-O-T-T-O-M-----")

import os

def clr_terminal():
    os.system('cls')

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

        while running:
            print("=========== Disk Storage Management ===========")
            disk_storage.show_disks()
            for num, operation in enumerate(operations, start=1):
                print(f"{num}.{ operation}")

            try:
                selected_operation = int(input("> Enter a number to select an operation: "))
            except ValueError:
                print("Log: Input must be a number")
                input("\n----- Press enter to continue -----\n")

                clr_terminal()

                continue

            if selected_operation == 1:
                disk = input("> Enter the name of the disk: ")
                disk_storage.push_disk(disk)

                input("\n----- Press enter to continue -----\n")

                clr_terminal()

            elif selected_operation == 2:
                disk_storage.pop_disk()
                
                input("\n----- Press enter to continue -----\n")

                clr_terminal()

            elif selected_operation == 3:
                disk_storage.peek_top_disk()

                input("\n----- Press enter to continue -----\n")

                clr_terminal()

            elif selected_operation == 4:
                disk_storage.get_disks_num()

                input("\n----- Press enter to continue -----\n")

                clr_terminal()

            elif selected_operation == 5:
                disk_storage.show_disks()

                input("\n----- Press enter to continue -----\n")

                clr_terminal()

            elif selected_operation == 6:
                running = False

                print("Log: You quit the program\n\n")

            else:
                print("Log: Input must be 1 - 6")

                input("\n----- Press enter to continue -----\n")

                clr_terminal()

if __name__ == "__main__":
    main()