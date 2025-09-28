class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
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

        new_node.prev = current_node
        current_node.next = new_node

    def preppend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        current_node = self.head

        new_node.next = current_node
        current_node.prev = new_node

    def delete(self, key):
        current_node = self.head

        if current_node and current_node.data == key:
            current_node = current_node.next
            current_node.prev = None
            return

        previous_node = None

        while current_node and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = current_node.next
        current_node.prev = previous_node

    def print_list(self):
        current_node = self.head

        while current_node.next:
            print(
                f"{current_node.prev} <-> {current_node} <-> {current_node.next}")
            current_node = current_node.next

        print(f"{current_node.prev} <-> {current_node}")


dbllist = DoublyLinkedList()
dbllist.append(10)
dbllist.append(9)
dbllist.append(8)
dbllist.append(7)

dbllist.preppend(11)

dbllist.delete(8)

dbllist.print_list()
