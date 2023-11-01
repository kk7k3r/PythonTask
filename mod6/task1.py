class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0
    
    def push(self, value):
        if (self.start is None):
            self.start = Node(value)
            self.end = self.start
        else:
            self.end.next = Node(value)
            self.end = self.end.next
        self.count += 1
    
    def get(self, index):
        self.index_is_valid(index)
        curr = self.start
        while (index != 0):
            curr = curr.next
            index -= 1
        return curr.value
    
    def remove(self, index):
        self.index_is_valid(index)
        prev = None
        curr = self.start
        while(index != 0):
            prev = curr
            curr = curr.next
            index -= 1
        if (prev == None):
            self.start = curr.next
        elif (curr.next == None):
            self.end = prev
            prev.next = None
        else:
            prev.next = curr.next
        self.count -= 1

    def insert(self, index, value):
        if (index > self.count or self.count < 0):
            raise Exception()
        prev = None
        curr = self.start
        while(index != 0):
            prev = curr
            curr = curr.next
            index -= 1
        if (prev == None):
            prev = Node(value)
            prev.next = self.start
            self.start = prev
        elif (curr == None):
            curr = Node(value)
            self.end.next = curr
            self.end = curr
        else:
            prev.next =  Node(value)
            prev.next.next = curr
        self.count += 1
        
    def __iter__(self):
        self.iter_count = 0
        self.current_iter_elem = self.start
        return self
    
    def __next__(self):
        if(self.current_iter_elem is None):
            raise StopIteration
        val = self.current_iter_elem.value
        self.current_iter_elem = self.current_iter_elem.next
        return val
            
            
    def index_is_valid(self, index):
        if (index >= self.count or index < 0):
            raise Exception()
        return;


a = LinkedList()
a.push(1)
a.push(2)
a.push(3)
a.remove(2)
a.insert(2, 4)
for i in a:
    print(i)