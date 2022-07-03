class __Queue:
    def __init__(self, max_size=None):
        self.__items = []
        self.__front = -1
        self.__rear = -1
        self.__max_size = max_size
    
    def IsFull(self):
        """ Returns True if the queue is full, False otherwise """
        return self.length == self.__max_size
    
    def IsEmpty(self):
        """ Returns True if the queue is empty, False otherwise """
        return self.__front == self.__rear
    
    def Enqueue(self, item):
        """ Pushes an item onto the queue
        
        Args:
            item: The item to be pushed onto the queue
        """
        if self.IsFull():
            raise Exception('Queue is full')
        self.__rear += 1
        self.__items.append(item)
    
    def Dequeue(self):
        """ Pops an item off the queue
        
        Returns:
            The item popped off the queue
        """
        if self.IsEmpty():
            raise Exception('Queue is empty')
        self.__front += 1
        return self.__items.pop(0)
    
    def Peek(self):
        """ Returns the top item on the queue without removing it
        
        Returns:
            The top item on the queue
        """
        if self.IsEmpty():
            raise Exception('Queue is empty')
        return self.__items[0]
    
    def __str__(self):
        return str(self.__items)
    
    def __repr__(self):
        return '<class \'queue\'> : ' + str(self.__items)
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        return self.__items.__iter__()
    
    def __next__(self):
        if len(self.__items) == 0:
            raise StopIteration
        return self.__items.pop(0)
    
    @property
    def length(self):
        return self.__rear - self.__front
    
    @property
    def items(self):
        return self.__items
    
    @items.setter
    def items(self, items):
        self.__items = []
        self.__front = self.__rear = -1
        for i in items:
            self.Enqueue(i)
    
    @items.deleter
    def items(self):
        self.__items = []
        self.__front = self.__rear = -1
        
def new(max_size: int = None):
    """ Create a new queue
    
    Args:
        max_size: The maximum size of the queue
    """
    return __Queue(max_size)

def is_full(queue):
    """ Returns True if the queue is full, False otherwise """
    return queue.IsFull()

def is_empty(queue):
    """ Returns True if the queue is empty, False otherwise """
    return queue.IsEmpty()