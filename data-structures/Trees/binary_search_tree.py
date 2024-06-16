from binary_tree import BinaryTree

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

    def delete(self, value):
        if self.root is None:
            return self.root
        return self._delete_helper(self.root, value)

    def _delete_helper(self, node, value):
        if value < node.element:
            node.left = self._delete_helper(node.left, value)
        elif value > node.element:
            node.right = self._delete_helper(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.element = self._min_inorder(node.right)
            node.right = self._delete_helper(node.right, node.element)
        return node

    def _min_inorder(self, node):
        min_value = node.element
        while node.left:
            min_value = node.left.element
            node = node.left
        return min_value

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

test.delete(14)
print("\n\nPre Order")
test.traverse_preorder()

print("\n\n" + str(test.is_perfect_tree()))
print("\n\n" + str(test.is_full_tree()))
# print(test.search(10).parent.element)
