class Heap:

    def __init__(self, max_size=0):
        self.arr = [None] * max_size
        self._size = 0

    def _parent(self, i):
        """
        Uses array implementation to determine parent of the current node using complete binary tree analogy
        :param i: Current index of the node
        :return: Index of the parent node
        """
        return (i - 1) // 2

    def _left(self, i):
        """
        Uses array implementation to determine left child of the current node using complete binary tree analogy
        :param i: Current index of the node
        :return: Left child of the current node if exists
        """
        return 2 * i + 1

    def _right(self, i):
        """
        Uses array implementation to determine right child of the current node using complete binary tree
        :param i: Current index of the node
        :return: Right child of the current node if exists
        """
        return 2 * i + 2

    def _up_heap(self, i):
        """
        Iteratively compare the current element with its parent and swap the smallest element
        :param i: Current node
        :return: Void
        """
        raise NotImplementedError("not implemented on the parent class")

    def _down_heap(self, i):
        """
        Iteratively finds the largest element between the two children of the parent node
        and swaps parent and largest
        :param i: Current node
        :return: Void
        """
        raise NotImplementedError("Not implemented on the parent class")

    def delete(self):
        """
        Removes the first the top element from the heap
        First swaps the top element with the last element, and then down heap the top element
        :return: popped element
        """
        if self.is_empty():
            return

        self._swap(0, self._size - 1)
        item = self.arr[self._size - 1]
        self._size -= 1
        self._down_heap(0)
        return item

    def insert(self, element):
        if self._size == len(self.arr):
            return

        self._size += 1
        self.arr[self._size - 1] = element
        self._up_heap(self._size - 1)

    def get_top(self):
        return self.arr[0]

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def __str__(self):
        res = ''
        for i in range(self._size):
            res += str(self.arr[i]) + ' '
        return res
