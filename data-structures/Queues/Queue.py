class Queue:

    class _Node:
        def __init__(self, val, next=None):
            self._val = val
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self.length = 0

    def enqueue(self, value):
        if self._head is None:
            self._head = self._tail = self._Node(value, None)
        else:
            self._tail._next = self._Node(value)
            self._tail = self._tail._next
            self.length += 1
    
    def dequeue(self):
        if self._head is None:
            return 'Empty Queue'
        else:
            res = self._head
            self._head = self._head._next
            if self._head is None:
                self._tail = None
            self.length -= 1

            return res._val
        
    def __str__(self) -> str:
        res = ''
        temp = self._head
        while temp:
            res += str(temp._val)
            if temp._next:
                res += ' ----> '
            temp = temp._next
        return res
    
test = Queue()
test.enqueue(1)
test.enqueue(2)
print(test.dequeue())
test.enqueue(3)
print(test)
