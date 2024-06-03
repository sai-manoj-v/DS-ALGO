from heap import Heap


class MinHeap(Heap):

    def __init__(self, size):
        super().__init__(size)

    def _down_heap(self, i):
        """
        Iteratively finds the smallest element between the two children of the parent node
        and swaps parent and smallest
        :param i: Current node
        :return: Void
        """
        left, right = self._left(i), self._right(i)
        min_element = i
        if left < self._size and self.arr[left] < self.arr[min_element]:
            min_element = left
        if right < self._size and self.arr[right] < self.arr[min_element]:
            min_element = right
        if min_element != i:
            self.arr[i], self.arr[min_element] = self.arr[min_element], self.arr[i]
            self._down_heap(min_element)

    def _up_heap(self, i):
        """
        Iteratively compare the current element with its parent and swap the smallest element
        :param i: Current node
        :return: Void
        """
        parent = self._parent(i)
        if i > 0 and self.arr[i] < self.arr[parent]:
            self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
            self._up_heap(parent)


test = MinHeap(10)

test.insert(10)
test.insert(15)
test.insert(8)
test.insert(12)
test.insert(20)
test.insert(30)
test.insert(1)
test.insert(5)
test.insert(5)
test.insert(5)
test.insert(17)
test.insert(19)

print(test.delete())

print(test)