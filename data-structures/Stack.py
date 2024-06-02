class Stack:

    class _Node:
        def __init__(self, val, next=None):
            self._val = val
            self._next = next

    def __init__(self):
        self._head = None
        self.length = 0

    def push(self, value):
        if self._head is None:
            self._head = self._tail = self._Node(value, None)
        else:
            self._head = self._Node(value, self._head)
            self.length += 1

    def pop(self):
        if self._head is None:
            return 'Empty Stack'
        else:
            res = self._head
            self._head = self._head._next
            self.length -= 1
            return res._val

    def __str__(self) -> str:
        res = ''
        temp = self._head
        while temp:
            res += str(temp._val)
            if temp._next:
                res += ' <---- '
            temp = temp._next
        return res

test = Stack()
test.push(1)
test.push(3)
print(test)
test.pop()
print(test)
test.push(2)
test.push(3)
print(test)