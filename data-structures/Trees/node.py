class Node:
    __slots__ = 'element', 'parent', 'left', 'right', '_height'

    def __init__(self, element, parent=None, left=None, right=None, height=1):
        self.element = element
        self.parent = parent
        self.left = left
        self.right = right
        self._height = 1

    def get_height(self):
        return self._height

    def set_height(self, new_height):
        self._height = new_height
