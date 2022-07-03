class __Stack:
    def __init__(self, max_size: int = None):
        self.__items = []
        self.__pointer = 0
        self.__max_size = max_size
    
    def IsFull(self):
        """ Returns True if the stack is full, False otherwise """
        return self.__max_size is not None and self.__pointer == self.__max_size
    
    def IsEmpty(self):
        """ Returns True if the stack is empty, False otherwise """
        return self.__pointer == 0
    
    def Push(self, item):
        """ Pushes an item onto the stack
        
        Args:
            item: The item to be pushed onto the stack
        """
        if self.IsFull():
            raise Exception('Stack is full')
        self.__items.append(item)
        self.__pointer += 1
    
    def Pop(self):
        """ Pops an item off the stack
        
        Returns:
            The item popped off the stack
        """
        if self.IsEmpty():
            raise Exception('Stack is empty')
        self.__pointer -= 1
        return self.__items.pop()
    
    def Peek(self):
        """ Returns the top item on the stack without removing it
        
        Returns:
            The top item on the stack
        """
        if self.IsEmpty():
            raise Exception('Stack is empty')
        return self.__items[-1]
    
    def __len__(self):
        return self.__pointer
    
    def __str__(self):
        return str(self.__items)
    
    def __repr__(self):
        return '<class \'stack\'> : ' + str(self.__items)
    
    def __iter__(self):
        return self.__items.__reversed__().__iter__()
    
    def __next__(self):
        if len(self.__items) == 0:
            raise StopIteration
        return self.__items.pop()
    
    @property
    def length(self):
        return self.__pointer
    
    @property
    def items(self):
        return self.__items
    
    @items.setter
    def items(self, items):
        self.__items = []
        self.__pointer = 0
        for i in items:
            self.Push(i)
    
    @items.deleter
    def items(self):
        self.__items = []
        self.__pointer = 0
    
def new(max_size: int = None):
    """ Create a new stack
    
    Args:
        max_size: The maximum size of the stack
    """
    return __Stack(max_size)