class Tree:

    def __init__(self, root = None, length = 0):
        self.root = root
        self.length = length

    def is_root(self, n):
        return self.root == n

    def is_leaf(self, n):
        return self.childrenCount(n) == 0

    def is_empty(self):
        return self.length == 0
    
    def children(self, n):
        raise NotImplementedError(
            'Method not implemented - must be implemented by subclass')

    def childrenCount(self, n):
        raise NotImplementedError(
            'Method not implemented - must be implemented by subclass')

    def depth(self, n):
        if self.is_root():
            return 0
        else:
            return 1 + self.depth(self.parent(n))

    def height(self, n):
        if self.is_leaf(n):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(n))
        
    def __len__(self):
        return self.length