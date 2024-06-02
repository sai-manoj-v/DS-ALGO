class Node:
    __slots__ = 'element', 'parent', 'left', 'right'

    def __init__(self, element, parent=None, left=None, right=None):
        self.element = element
        self.parent = parent
        self.left = left
        self.right = right
