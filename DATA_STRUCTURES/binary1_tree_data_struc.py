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
    
    def add_node(self, root, data):
        if self.is_empty():
            self.root = Node(data)
            return
        
        if data < root.data:
            if root.left:
                root.left.add_node(root.left, data)
            else:
                root.left = Node(data)
        else:
            if root.right:
                root.right.add_node(root.right, data)
            else:
                root.right = Node(data)

    def print_tree(self):
        print("Traverse In Order:")
        self.root.traverse_in_order()
        print()
        print("Traverse Pre Order:")
        self.root.traverse_pre_order()
        print()
        print("Traverse Post Order:")
        self.root.traverse_post_order()
        print()

btree = BinaryTree()
btree.add_node(btree.root, 10)
btree.add_node(btree.root, 5)
btree.add_node(btree.root, 15)
btree.add_node(btree.root, 8)
btree.add_node(btree.root, 18)

btree.print_tree()