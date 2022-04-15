class Stack:
    def __init__(self, max_size: int = None):
        self._items = []
        self._pointer = 0
        self._max_size = max_size
    
    def IsFull(self):
        """ Returns True if the stack is full, False otherwise """
        return self._max_size is not None and self._pointer == self._max_size
    
    def IsEmpty(self):
        """ Returns True if the stack is empty, False otherwise """
        return self._pointer == 0
    
    def Push(self, item):
        """ Pushes an item onto the stack
        
        Args:
            item: The item to be pushed onto the stack
        """
        if self.IsFull():
            raise Exception('Stack is full')
        self._items.append(item)
        self._pointer += 1
    
    def Pop(self):
        """ Pops an item off the stack
        
        Returns:
            The item popped off the stack
        """
        if self.IsEmpty():
            raise Exception('Stack is empty')
        self._pointer -= 1
        return self._items.pop()
    
    def Peek(self):
        """ Returns the top item on the stack without removing it
        
        Returns:
            The top item on the stack
        """
        if self.IsEmpty():
            raise Exception('Stack is empty')
        return self._items[-1]
    
    def __len__(self):
        return self._pointer
    
    def __str__(self):
        return str(self._items)
    
    def __repr__(self):
        return '<class \'stack\'> : ' + str(self._items)
    
    def __iter__(self):
        return self._items.__reversed__().__iter__()
    
    def __next__(self):
        if len(self._items) == 0:
            raise StopIteration
        return self._items.pop()
    
    @property
    def length(self):
        return self._pointer
    
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, items):
        self._items = []
        self._pointer = 0
        for i in items:
            self.Push(i)
    
    @items.deleter
    def items(self):
        self._items = []
        self._pointer = 0
    
def new(max_size: int = None):
    """ Returns a new stack
    
    Args:
        max_size: The maximum size of the stack
    """
    return Stack(max_size)