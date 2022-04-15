class Queue:
    def __init__(self, max_size=None):
        self._items = []
        self._front = -1
        self._rear = -1
        self._max_size = max_size
    
    def IsFull(self):
        """ Returns True if the queue is full, False otherwise """
        return self.length == self._max_size
    
    def IsEmpty(self):
        """ Returns True if the queue is empty, False otherwise """
        return self._front == self._rear
    
    def Enqueue(self, item):
        """ Pushes an item onto the queue
        
        Args:
            item: The item to be pushed onto the queue
        """
        if self.IsFull():
            raise Exception('Queue is full')
        self._rear += 1
        self._items.append(item)
    
    def Dequeue(self):
        """ Pops an item off the queue
        
        Returns:
            The item popped off the queue
        """
        if self.IsEmpty():
            raise Exception('Queue is empty')
        self._front += 1
        return self._items.pop(0)
    
    def Peek(self):
        """ Returns the top item on the queue without removing it
        
        Returns:
            The top item on the queue
        """
        if self.IsEmpty():
            raise Exception('Queue is empty')
        return self._items[0]
    
    def __str__(self):
        return str(self._items)
    
    def __repr__(self):
        return '<class \'queue\'> : ' + str(self._items)
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        return self._items.__iter__()
    
    def __next__(self):
        if len(self._items) == 0:
            raise StopIteration
        return self._items.pop(0)
    
    @property
    def length(self):
        return self._rear - self._front
    
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, items):
        self._items = []
        self._front = self._rear = -1
        for i in items:
            self.Enqueue(i)
    
    @items.deleter
    def items(self):
        self._items = []
        self._front = self._rear = -1
        
def new(max_size: int = None):
    """ Returns a new queue
    
    Args:
        max_size: The maximum size of the queue
    """
    return Queue(max_size)