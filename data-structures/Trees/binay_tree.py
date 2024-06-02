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