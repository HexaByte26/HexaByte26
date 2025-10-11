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
            self.left.traverse_in_order()
        if self.right:
            self.right.traverse_in_order()

    def traverse_post_order(self):
        if self.left:
            self.left.traverse_in_order()
        if self.right:
            self.right.traverse_in_order()
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

    def print_tree_dfs(self):
        assert self.root is not None

        print("Depth First Search:")
        print("Traverse In Order:")
        self.root.traverse_in_order()
        print()

        print("\nTraverse Pre Order:")
        self.root.traverse_pre_order()
        print()

        print("\nTraverse Post Order:")
        self.root.traverse_post_order()
        print()

    def print_tree_bfs(self):
        assert self.root is not None

        result = []
        queue = []

        current_node = self.root
        result.append(current_node.data)
        queue.append(current_node)
        while True: 
            current_node = queue.pop(0)
            if current_node.left:
                result.append(current_node.left.data)
                queue.append(current_node.left) 
            if current_node.right:
                result.append(current_node.right.data)
                queue.append(current_node.right)

            if len(queue) == 0:
                break
        
        print("\n\nBreadth First Search:")
        for data in result:
            print(data, end="->")

btree = BinaryTree()
# btree.insert(btree.root, 10)
# btree.insert(btree.root, 5)
# btree.insert(btree.root, 8)
# btree.insert(btree.root, 3)
# btree.insert(btree.root, 15)
# btree.insert(btree.root, 13)
# btree.insert(btree.root, 18)
datas = [20, 10, 30, 5, 15, 25, 35, 3, 8, 13, 18, 23, 28, 33, 38]
for item in datas:
    btree.insert(btree.root, item)

btree.print_tree_dfs()
btree.print_tree_bfs()