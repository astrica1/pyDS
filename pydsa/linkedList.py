class Node:
    def __init__(self, data, next: object = None, prev: object = None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def Insert(self, data):
        node = Node(data)
        node.next = self.next
        node.prev = self
        self.next = node
        return node
    
    def Delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.prev
    
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return 'data: ' + str(self.data) + ' next: ' + str(self.next) + ' prev: ' + str(self.prev)
    
    def __eq__(self, other):
        if (self.data == other.data) and (self.next == other.next) and (self.prev == other.prev):
            return True
    
    def __ne__(self, other):
        return not self.__eq__(other)

class LinkedList:
    def __init__(self, head: Node = None):
        self._head = head
        self._tail = head
        self._length = 0 if head is None else 1
        self._Initialize()
    
    def _Initialize(self):
        if self._tail is not None:
            while self._tail.next is not None:
                self._tail = self._tail.next
                self._length += 1
        
    def Insert(self, data):
        """ Inserts a new node at the end of the list

        Args:
            data: The data to be inserted
        """
        newNode = Node(data)
        if self._head is None:
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.next = newNode
            newNode.prev = self._tail
            self._tail = newNode
        self._length += 1
    
    def Delete(self, data):
        """ Deletes the first node with the given data
        
        Args:
            data: The data to be deleted
        """
        if self._head is None:
            return
        
        if self._head.data == data:
            self._head = self._head.next
            self._length -= 1
            return
        
        current = self._head
        
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self._length -= 1
                return
            
            current = current.next
        return
    
    def Search(self, data):
        """ Searches for the first node with the given data
        
        Args:
            data: The data to be searched
        """
        if self._head is None:
            return False
        
        if self._head.data == data:
            return self._head
        
        current = self._head
        while current.next is not None:
            if current.data == data:
                return current
            current = current.next
        return False
    
    def Display(self):
        """ Displays the list in a human readable format """
        if self._head is None:
            print("Empty list")
            return
        
        current = self._head
        while current is not None:
            print(current.data, end = "" if current.next is None else " -> ")
            current = current.next
        print()
    
    def DeleteAll(self):
        """ Deletes all nodes in the list """
        self._head = None
        self._tail = None
        self._length = 0
    
    def DeleteFirst(self):
        """ Deletes the first node in the list """
        if self._head is None:
            return
        
        self._head = self._head.next
        self._length -= 1
        
    def DeleteLast(self):
        """ Deletes the last node in the list """
        if self._tail is None:
            return
        
        self._tail = self._tail.prev
        self._length -= 1
    
    def GetByIndex(self, index):
        """ Gets the node at the given index
        
        Args:
            index: The index of the node to be returned
        """
        if index < 0 or index >= self._length:
            return None
        
        current = self._head
        for _ in range(index):
            current = current.next
        return current
    
    def DeleteByIndex(self, index):
        """ Deletes the node at the given index
        
        Args:
            index: The index of the node to be deleted
        """
        if index < 0 or index >= self._length:
            return
        current = self.GetByIndex(index)
        current.prev.next = current.next
        current.next.prev = current.prev
    
    def IsEmpty(self):
        """ Returns True if the list is empty, False otherwise """
        return self._length == 0
    
    def __len__(self):
        return self._length
    
    def __str__(self):
        if self._head is None:
            return ''
        
        current = self._head
        string = ''
        while current is not None:
            string += str(current.data)
            if current.next is not None:
                string += ' -> '
            current = current.next
        return string
    
    def __repr__(self):
        return '<class \'linked list\'> : ' + (str(self) if self._head is not None else 'null')
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._head is None:
            raise StopIteration
        current = self._head
        self._head = self._head.next
        return current
    
    @property
    def length(self):
        return self._length
    
    @property
    def head(self):
        return self._head
    
    @property
    def tail(self):
        return self._tail

def new(head: Node = None):
    return LinkedList(head)