class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current_node = self.head

        while current_node.next:
            print(current_node.data, end="->")
            current_node = current_node.next

        print(current_node.data)


llist = LinkedList()
llist.append(9)
llist.append(8)
llist.append(7)
llist.prepend(10)

llist.print_list()
