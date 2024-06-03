from binay_tree import BinaryTree
from node import Node


# Binary Search Tree is just a sorted Binary Tree
class BinarySearchTree(BinaryTree):

    def __init__(self):
        super().__init__()

    def insert(self, value):
        if self.root is None:
            self.addRoot(value)
            return

        head = self.root
        while True:
            if value < head.element:
                if head.left is None:
                    self.addLeft(value, head)
                    return
                head = head.left
            else:
                if head.right is None:
                    self.addRight(value, head)
                    return
                head = head.right

    # Search traversal with O(h) where h is height of the tree.
    def search(self, value):
        if self.root is None or self.root.element == value:
            return self.root

        pointer = self.root
        while pointer is not None:
            if value == pointer.element:
                return pointer
            elif value > pointer.element:
                pointer = pointer.right
            else:
                pointer = pointer.left
        return None


test = BinarySearchTree()
test.insert(20)
test.insert(30)
test.insert(10)
test.insert(60)
test.insert(25)
test.insert(5)
test.insert(14)
test.insert(12)
test.insert(16)
print("In Order")
test.traverse_inorder()
print("\n\nPre Order")
test.traverse_preorder()
print("\n\nPost Order")
test.traverse_postorder()
print("\n\nLevel Order")
test.traverse_level_order()
#print(test.search(10).parent.element)
