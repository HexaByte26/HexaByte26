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

    def delete(self, key):
        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            return

        previous_node = None
        while current_node and current_node != key:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            print("Key doesn't exists inside the list")
            return

        previous_node.next = current_node.next

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
