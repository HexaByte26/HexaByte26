class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def traverse_in_order(self):
        if self.left:
            self.left.traverse_in_order()
        print(self.data, end="->")
        if self.right:
            self.right.traverse_in_order()

    def traverse_pre_order(self):
        print(self.data, end="->")
        if self.left:
            self.left.traverse_pre_order()
        if self.right:
            self.right.traverse_pre_order()

    def traverse_post_order(self):
        if self.left:
            self.left.traverse_post_order()
        if self.right:
            self.right.traverse_post_order()
        print(self.data, end="->")


class BinaryTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, root, data):
        new_node = Node(data)
        if self.is_empty():
            self.root = new_node
            return

        if data < root.data:
            if root.left:
                self.insert(root.left, data)
            else:
                root.left = new_node
        else:
            if root.right:
                self.insert(root.right, data)
            else:
                root.right = new_node

    def print_tree(self):
        if not self.is_empty():
            print("Traverse In Order:")
            self.root.traverse_in_order()
            print()
            print()
            print("Traverse Pre Order:")
            self.root.traverse_pre_order()
            print()
            print()
            print("Traverse Post Order:")
            self.root.traverse_post_order()
            print()
            print()
        else:
            print("Tree is empty")


btree = BinaryTree()
btree.insert(btree.root, 10)
btree.insert(btree.root, 5)
btree.insert(btree.root, 15)
btree.insert(btree.root, 8)
btree.insert(btree.root, 13)
btree.insert(btree.root, 3)
btree.insert(btree.root, 18)

btree.print_tree()
