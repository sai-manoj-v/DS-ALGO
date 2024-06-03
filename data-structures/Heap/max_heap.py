from heap import Heap


class MaxHeap(Heap):

    def __init__(self, size):
        super().__init__(size)

    def _up_heap(self, i):
        """
        Iteratively compare the current element with its parent and swap the largest element
        :param i: Current node
        :return: Void
        """
        parent = self._parent(i)
        if i > 0 and self.arr[i] > self.arr[parent]:
            self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
            self._up_heap(parent)

    def _down_heap(self, i):
        """
        Iteratively finds the largest element between the two children of the parent node
        and swaps parent and largest
        :param i: Current node
        :return: Void
        """
        left, right = self._left(i), self._right(i)
        max_element = i
        if left < self._size and self.arr[left] > self.arr[max_element]:
            max_element = left
        if right < self._size and self.arr[right] > self.arr[max_element]:
            max_element = right
        if max_element != i:
            self.arr[i], self.arr[max_element] = self.arr[max_element], self.arr[i]
            self._down_heap(max_element)
