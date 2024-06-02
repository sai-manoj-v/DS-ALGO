class DoubleLinkedList:

    class _Node:
        def __init__(self, val, prev=None, next=None):
            self._val = val
            self._prev = prev
            self._next = next

    def __init__(self):
        self._head = self._tail = None
        self.length = 0

    def insertAtEnd(self, value):
        if self._head is None:
            self._head = self._tail = self._Node(value)
        else:
            self._tail._next = self._Node(value, self._tail, None)
            self._tail = self._tail._next
        self.length += 1

    def insertAtStart(self, value):
        if self._head is None:
            self._head = self._tail = self._Node(value)
        else:
            self._head = self._Node(value, None, self._head)
            self._head._next._prev = self._head
        self.length += 1

    def insertAt(self, position, value):
        if position < 2:
            self.insertAtStart(value)
            return 'Position less than zero will always insert at the start'
        elif position > self.length:
            self.insertAtEnd(value)
            return ('Position greater than current length will always insert at the end')
        else:
            i = 1
            temp = self._head
            while temp:
                if i == position:
                    newNode = self._Node(value, temp._prev, temp)
                    temp._prev._next = newNode
                    temp._prev = newNode
                    break
                i += 1
                temp = temp._next
        self.length += 1

    def deleteAtStart(self):
        if self._head is None:
            return 'Empty Linked List'
        else:
            self._head = self._head._next
            self.length -= 1

    def deleteAtEnd(self):
        if self._head is None:
            return 'Empty Linked List'
        else:
            self._tail = self._tail._prev
            if self._tail is not None:
                self._tail._next = None 
            self.length -= 1

    def deleteAt(self, position):
        if position < 2:
            self.deleteAtStart()
            return 'Position less than zero will always delete at the start'
        elif position > self.length:
            self.deleteAtEnd()
            return ('Position greater than current length will always delete at the end')
        else:
            i = 1
            temp = self._head
            while temp:
                if i == position-1:
                    temp._next = temp._next._next
                    if temp._next:
                        temp._next._prev = temp
                    break
                temp = temp._next
                i += 1
        self.length += 1

    def __str__(self) -> str:
        res = ''
        temp = self._head
        while temp:
            res += str(temp._val)
            if temp._next:
                res += ' <----> '
            temp = temp._next
        return res


test = DoubleLinkedList()
test.insertAtStart(1)
test.insertAtEnd(3)
test.insertAt(2, 2)
print(test)

test.deleteAtStart()
test.deleteAtEnd()
test.deleteAt(1)
print(test)
print('End')