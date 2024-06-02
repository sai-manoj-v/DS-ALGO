class CircularQueue:
    
    class _Node:
        def __init__(self, value, next=None):
            self._val = value
            self._next = next 
            
    def __init__(self):
        self._tail = None
        self._length = 0

    def enqueue(self, value):
        newNode = self._Node(value, None)
        if self._length == 0:
            newNode._next = newNode
        else:
            newNode._next = self._tail._next
            self._tail._next = newNode
        self._tail = newNode
        self._length += 1

    def dequeue(self):
        if self._length == 0:
            return 'Empty Queue'
        elif self._length == 1:
            self._tail = None
        else:
            self._tail._next = self._tail._next._next
        self._length -= 1
    
    def rotate(self):
        if self._length > 0:
            self._tail = self._tail._next

    def __str__(self) -> str:
        res = ''
        temp = self._tail._next
        while temp and temp != self._tail:
            res += str(temp._val)
            if temp._next:
                res += ' ----> '
            temp = temp._next
        res += str(self._tail._val)
        return res


test = CircularQueue()

test.enqueue(1)
print(test)
test.enqueue(2)
print(test, )
test.enqueue(3)
print(test)
test.dequeue()

print(test)