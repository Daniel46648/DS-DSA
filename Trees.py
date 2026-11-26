class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""full is when each node points to either 0 or 2 Nodes
perfect is when the tree is completely symmetrical, a complete
tree is when you fill the tree from left to right with no gap
a parent has 2 child nodes, 2 child nodes from the same parent
are called sibling, child nodes can also be parents, there cant
be a Node with 2 parent Nodes, a Node without children is called leaf"""

#BST
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

