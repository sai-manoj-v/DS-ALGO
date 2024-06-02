class Deque:

    class _Node:
        def __init__(self, val, prev=None, next=None):
            self._val = val
            self._prev = prev
            self._next = next

    def __init__(self):
        self._head = self._tail = None
        self.length = 0

    def enqueue_first(self, value):
        if self._head is None:
            self._head = self._tail = self._Node(value, None, None)
        else:
            self._head = self._Node(value, None, self._head)
            self._head._next._prev = self._head
            self.length += 1

    def enqueue_last(self, value):
        if self._head is None:
            self._head = self._tail = self._Node(value, None)
        else:
            self._tail._next = self._Node(value, self._tail, None)
            self._tail = self._tail._next
            self.length += 1

    def dequeue_first(self):
        if self._head is None:
            return 'Empty Queue'
        else:
            res = self._head
            self._head = self._head._next
            if self._head is None:
                self._tail = None
            else:
                self._head._prev = None
            self.length -= 1

            return res._val

    def dequeue_last(self):
        if self._head is None:
            return 'Empty Queue'
        else:
            res = self._tail
            self._tail = self._tail._prev
            if self._tail is None:
                self._head = None
            else:
                self._tail._next = None
            self.length -= 1

            return res._val

    def __str__(self) -> str:
        res = ''
        temp = self._head
        while temp:
            res += str(temp._val)
            if temp._next:
                res += ' <----> '
            temp = temp._next
        return res



#-----------Tests-----------#

test = Deque()
test.enqueue_first(1)
test.enqueue_last(2)
test.enqueue_first(0)
print(test)

test.dequeue_first()
print(test)
test.dequeue_last()
print(test)
test.dequeue_first()
print(test)
test.enqueue_last(5)
print(test)
test.dequeue_last()
print(test)
