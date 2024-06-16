from tree import Tree
from node import Node


# Binary Tree is a tree with just two children for each node
class BinaryTree(Tree):

    def __init__(self):
        super().__init__()

    def sibling(self, n):
        if n.parent is None:
            return None
        else:
            if n == n.parent.left:
                return n.parent.right
            else:
                return n.parent.left

    def children(self, n):
        if n.left is not None:
            yield n.left
        if n.right is not None:
            yield n.right

    def childrenCount(self, n):
        c = 0
        if n.left is not None:
            c += 1
        if n.right is not None:
            c += 1
        return c

    def node_count(self):
        self._count_children(self.root)

    def _count_children(self, node):
        if node is None:
            return 0
        return 1 + self._count_children(node.left) + self._count_children(node.right)

    def addRoot(self, value):
        if self.root is not None:
            raise ValueError('Root already exists')
        else:
            self.root = Node(value)
            self.length = 1

    def addLeft(self, value, position):
        if position.left is not None:
            raise ValueError('Left already exists')
        else:
            position.left = Node(value, position)
            self.length += 1

    def addRight(self, value, position):
        if position.right is not None:
            raise ValueError('Right already exists')
        else:
            position.right = Node(value, position)
            self.length += 1

    # Tree Properties
    # Full Tree - Each node only has 0 or 2 child nodes
    def is_full_tree(self):
        return self._check_if_full_tree(self.root)

    def _check_if_full_tree(self, node):
        if node is None:
            return True

        if node.left is None and node.right is None:
            return True

        if node.left is not None and node.right is not None:
            return self._check_if_full_tree(node.left) and self._check_if_full_tree(node.right)

        return False

    # Perfect Binary Tree - Each internal node has a degree of 2 (2 child) and all the child are at same level
    def is_perfect_tree(self):
        d = self.left_depth(self.root)
        return self._check_if_perfect_tree(self.root, d)

    def _check_if_perfect_tree(self, node, d, level = 0):
        if node is None:
            return True

        if node.left is None and node.right is None:
            return d == level+1

        if node.left is None or node.right is None:
            return False

        return self._check_if_perfect_tree(node.left, d, level+1) and self._check_if_perfect_tree(node.right, d, level+1)

    # Complete Binary Tree - All leaves are at same level, filled from left to right
    def is_complete_tree(self):
        self._check_if_complete(self.root, self.node_count())

    def _check_if_complete(self, node, node_count, index = 0):
        if node is None:
            return True

        if index >= node_count:
            return False

        return self._check_if_complete(node.left, node_count, 2*index+1) and self._check_if_complete(node.right, node_count, 2*index+2)

    # Balanced Tree - Height of any left and right sub-tree shouldn't differ by one
    # Reference - https://www.youtube.com/watch?v=LU4fGD-fgJQ&ab_channel=BackToBackSWE
    def is_balanced(self):
        return self._check_if_balanced(self.root)

    def _check_if_balanced(self, node):
        if node is None:
            return True, 0

        left = self._check_if_balanced(node.left)
        right = self._check_if_balanced(node.right)

        height = max(left[1], right[1]) + 1

        if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
            return True, height
        else:
            return False, height

    # Traversals
    # Depth First Traversals - Explore each branch as far as possible before back tracking
    def traverse_inorder(self):
        """
        Print contents of the tree in Inorder Traversal.
        Type: DFS
        Time complexity : O(n)
        Space complexity : Considering the stack of calls, O(h) otherwise O(1)
        :return: None - Print contents
        """
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.element, end=" ")
            self._inorder(node.right)

    def traverse_preorder(self):
        """
        Print contents of the tree in Preorder Traversal.
        Type: DFS
        Time complexity : O(n)
        Space complexity : O(h) if considering the stack of calls, otherwise O(1)
        :return: None - Print contents
        """
        self._preorder(self.root)

    def _preorder(self, node):
        if node:
            print(node.element, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def traverse_postorder(self):
        """
        Print contents of the tree in Postorder Traversal
        Type: DFS
        Time complexity : O(n)
        Space complexity : O(h) if considering the stack of calls, otherwise O(1)
        :return: None - Print contents
        """
        self._postorder(self.root)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.element, end=" ")

    # Breadth First Traversals - Explore each level before going to next level
    def traverse_level_order(self):
        """
        Print contents of the tree in Level Order Traversal
        Type: BFS
        Time complexity : O
        :return:
        """
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.element, end=" ")

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)



