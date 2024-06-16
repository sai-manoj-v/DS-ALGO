from binary_search_tree import BinarySearchTree
from node import Node

class AVLTree(BinarySearchTree):

    def __init__(self):
        super().__init__()

    def get_height(self, node):
        if node is None:
            return 0
        return node.get_height()

    def get_balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Rotations
    # Right rotation
    def right_rotate(self, node):

        # Rotation
        left_node = node.left
        left_nodes_right = left_node.right
        left_node.right = node
        node.left = left_nodes_right

        # Height updates
        node.set_height(1 + max(self.get_height(node.left), self.get_height(node.right)))
        left_node.set_height(1 + max(self.get_height(left_node.left), self.get_height(left_node.right)))

        return left_node

    def left_rotate(self, node):

        # Rotation
        right_node = node.right
        right_noes_left = right_node.left
        right_node.left = node
        node.right = right_noes_left

        # Height updates
        node.set_height(1 + max(self.get_height(node.left), self.get_height(node.right)))
        right_node.set_height(1 + max(self.get_height(right_node.left), self.get_height(right_node.right)))

        return right_node

    def insert(self, value):
        self.balance_while_insert(self.root, value)

    def balance_while_insert(self, node, value):

        # Regular insertion with recursion
        if node is None:
            return Node(value)
        elif value < node.element:
            node.left = self.balance_while_insert(node.left, value)
        else:
            node.right = self.balance_while_insert(node.right, value)

        # Update height of the current node
        node.set_height(1 + max(self.get_height(node.left), self.get_height(node.right)))

        # Calculate balance factor and perform required rotations
        balance_factor = self.get_balance_factor(node)
        if balance_factor > 1:
            # Meaning height of the left sub-tree is greater than the height of right sub-tree
            if value < node.left.element:
                # Meaning the insertion caused a left-left imbalance and hence hinting on performing right rotation
                return self.right_rotate(node) # return to update it through the traversal
            else:
                # Meaning the insertion caused a left-right imbalance and hence hinting on performing left rotation
                # first and then right rotation
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        if balance_factor < -1:
            # Meaning height of the right sub-tree is greater than the height of the right sub-tree
            if value > node.right.element:
                # Meaning the insertion caused a right-right imbalance and hence hinting on performing left rotation
                return self.left_rotate(node) # return to update it through the traversal
            else:
                # Meaning the insertion caused a right-left imbalance and hence hinting on performing right left
                # rotation first and then left rotation
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node # return the node even if there are no updations to propogate it through the traversal

    def delete(self, value):
        return self.balance_while_delete(self.root, value)

    def balance_while_delete(self, node, value):
        # Regular BST deletion
        if not node:
            return node
        elif value < node.element:
            node.left = self.balance_while_delete(node.left, value)
        elif value > node.element:
            node.right = self.balance_while_delete(node.right, value)
        else:
            if node.left is None:
                nodes_right = node.right
                node = None
                return nodes_right
            elif node.right is None:
                nodes_left = node.left
                node = None
                return nodes_left
            temp = self._min_inorder(node.right)
            node.element = temp.element
            node.right = self.balance_while_delete(node.right, temp.element)

        # if the tree is empty after deletion, return
        if node is None:
            return node

        # Update height of the current node
        node.set_height(1 + max(self.get_height(node.left), self.get_height(node.right)))

        # Balance the tree based on the heights of left and right sub-trees
        balance_factor = self.get_balance_factor(node)
        if balance_factor > 1:
            # Meaning the deletion has caused a left imbalance.
            if self.get_balance_factor(node.left) >= 0:
                # Meaning the left sub-tree of the node has more height and denotes left-left imbalance
                return self.right_rotate(node)
            else:
                # Meaning the right sub-tree of the node as more height and denotes left-right imbalance
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        if balance_factor < -1:
            # Meaning the deletion caused a right imbalance
            if self.get_balance_factor(node.right) <= 0:
                # Meaning the right sub-tree of the node has more height and denotes right-right imbalance
                return self.left_rotate(node)
            else:
                # Meaning the left sub-tree of the node has more height and denotes right-left imbalance
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        # Finally return the node for propagating changes throughout the traversal.
        return node
