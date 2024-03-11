class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = self.head
    
    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("Given previous node is  not found")
            return
        if prev_node is self.tail:
            self.append(new_data)
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node
        

test = LinkedList()
test.push(12)
test.append(14)
test.insert(12, 13)
print(test)