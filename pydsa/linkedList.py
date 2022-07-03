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

class __LinkedList:
    def __init__(self, head: Node = None):
        self.__head = head
        self.__tail = head
        self.__length = 0 if head is None else 1
        self.__Initialize()
    
    def __Initialize(self):
        if self.__tail is not None:
            while self.__tail.next is not None:
                self.__tail = self.__tail.next
                self.__length += 1
        
    def Insert(self, data):
        """ Inserts a new node at the end of the list

        Args:
            data: The data to be inserted
        """
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            newNode.prev = self.__tail
            self.__tail = newNode
        self.__length += 1
    
    def Delete(self, data):
        """ Deletes the first node with the given data
        
        Args:
            data: The data to be deleted
        """
        if self.__head is None:
            return
        
        if self.__head.data == data:
            self.__head = self.__head.next
            self.__length -= 1
            return
        
        current = self.__head
        
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self.__length -= 1
                return
            
            current = current.next
        return
    
    def Search(self, data):
        """ Searches for the first node with the given data
        
        Args:
            data: The data to be searched
        """
        if self.__head is None:
            return False
        
        if self.__head.data == data:
            return self.__head
        
        current = self.__head
        while current.next is not None:
            if current.data == data:
                return current
            current = current.next
        return False
    
    def Display(self):
        """ Displays the list in a human readable format """
        if self.__head is None:
            print("Empty list")
            return
        
        current = self.__head
        while current is not None:
            print(current.data, end = "" if current.next is None else " -> ")
            current = current.next
        print()
    
    def DeleteAll(self):
        """ Deletes all nodes in the list """
        self.__head = None
        self.__tail = None
        self.__length = 0
    
    def DeleteFirst(self):
        """ Deletes the first node in the list """
        if self.__head is None:
            return
        
        self.__head = self.__head.next
        self.__length -= 1
        
    def DeleteLast(self):
        """ Deletes the last node in the list """
        if self.__tail is None:
            return
        
        self.__tail = self.__tail.prev
        self.__length -= 1
    
    def GetByIndex(self, index):
        """ Gets the node at the given index
        
        Args:
            index: The index of the node to be returned
        """
        if index < 0 or index >= self.__length:
            return None
        
        current = self.__head
        for _ in range(index):
            current = current.next
        return current
    
    def DeleteByIndex(self, index):
        """ Deletes the node at the given index
        
        Args:
            index: The index of the node to be deleted
        """
        if index < 0 or index >= self.__length:
            return
        current = self.GetByIndex(index)
        current.prev.next = current.next
        current.next.prev = current.prev
    
    def IsEmpty(self):
        """ Returns True if the list is empty, False otherwise """
        return self.__length == 0
    
    def __len__(self):
        return self.__length
    
    def __str__(self):
        if self.__head is None:
            return ''
        
        current = self.__head
        string = ''
        while current is not None:
            string += str(current.data)
            if current.next is not None:
                string += ' -> '
            current = current.next
        return string
    
    def __repr__(self):
        return '<class \'linked list\'> : ' + (str(self) if self.__head is not None else 'null')
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__head is None:
            raise StopIteration
        current = self.__head
        self.__head = self.__head.next
        return current
    
    @property
    def length(self):
        return self.__length
    
    @property
    def head(self):
        return self.__head
    
    @property
    def tail(self):
        return self.__tail

def new(head: Node = None):
    """ Creates a new linked list with the given head node """
    return __LinkedList(head)