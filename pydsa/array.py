class Array:
    def __init__(self, type: type = None, max_size: int = None):
        """ Initialize an array.

        Args:
            type (type, optional): type of the array's elements. Defaults to None.
            max_size (int, optional): maximum array elements. Defaults to None.

        Raises:
            Exception: if max_size is not an integer.
            Exception: if max_size is less than 1.
            Exception: if type is not int, str, float, bool or None.
        """
        self._elements = []
        self._pointer = 0
        self.max_size = max_size
        self._type = type
        self._accepted_types = [
            {'type': int, 'name': 'int', 'default': 0},
            {'type': str, 'name': 'str', 'default': ''},
            {'type': float, 'name': 'float', 'default': 0.0},
            {'type': bool, 'name': 'bool', 'default': False},
            {'type': chr, 'name': 'chr', 'default': ' '}
        ]
        self._accepted_groups = [tuple, list, set]
        self._Initialize()
        
    def _Initialize(self):
        if self.max_size is not None:
            if type(self.max_size) is not int:
                raise Exception('max_size must be an integer')
            if self.max_size < 1:
                raise Exception('max_size must be greater than 0')
            self.max_size = int(self.max_size)
        
        if self._type is not None:
            if self._type not in [types_list['type'] for types_list in self._accepted_types]:
                types = ''
                for i in self._accepted_types:
                    types += str(i['name']) + ', '
                types = types[:-2] + ' or None'
                raise Exception('type must be ' + types)

        if self.max_size is not None:
            for i in self._accepted_types:
                if i['type'] == self._type:
                    self._elements = [i['default']] * self.max_size
                    break
    
    def _Clear(self, index: int = None):
        if index is None:
            self._elements = []
            self._pointer = 0
            self._Initialize()
        else:
            if index < 0:
                index = self._pointer + index
            if index < 0 or index >= self._pointer:
                raise Exception('Index out of range')
            default_value = [types_list for types_list in self._accepted_types if types_list['type'] == self._type][0]['default']
            self._elements = self._elements[: index] + self._elements[index + 1 :] + [default_value]
            self._pointer -= 1
            
    def _TypeValidator(self, element):
        Response = [
            {'code': 0, 'message': 'OK'},
            {'code': 1, 'message': 'Type mismatch'},
            {'code': 2, 'message': 'Type not accepted'},
            {'code': 3, 'message': 'Type is None'},
            {'code': 4, 'message': 'Type is a group'}
        ]
        
        if self._type is None and type(element) in [types_list['type'] for types_list in self._accepted_types]:
            self._type = type(element)
            self._Initialize()
            return Response[0]
        elif self._type is not None and type(element) is self._type:
            return Response[0]
        elif type(element) in self._accepted_groups:
            return Response[4]
        elif self._type is not None and type(element) is not self._type:
            return Response[1]
        elif type(element) is None:
            return Response[3]
        else:
            return Response[2]
    
    def IsFull(self):
        """ Check if the array is full.

        Returns:
            bool: True if the array is full, False otherwise.
        """
        return self.max_size is not None and self._pointer == self.max_size

    def IsEmpty(self):
        """ Check if the array is empty.
        
        Returns:
            bool: True if the array is empty, False otherwise.
        """
        return self._pointer == 0
    
    def _Append(self, element):
        if self.IsFull():
            raise Exception('Array is full')
        else:
            if self._TypeValidator(element)['code'] == 0:
                if self.max_size is None:
                    self._elements.append(element)
                else:
                    self._elements[self._pointer] = element
                self._pointer += 1
            elif self._TypeValidator(element)['code'] == 4:
                for i in element:
                    self._Append(i)
            else:
                raise Exception(self._TypeValidator(element)['message'])
    
    def Insert(self, *args):
        """ Insert elements into the array.
        
        Args:
            *args: elements to be inserted.
        """
        for element in args:
            self._Append(element)
    
    def Update(self, index: int, element):
        """ Update an element in the array.

        Args:
            index (int): index of the element to be updated.
            element (any): new element.
        """
        if self._TypeValidator(element)['code'] == 0:
            self._elements[index] = element
        else:
            raise Exception(self._TypeValidator(element)['message'])
    
    def Delete(self, index: int = None):
        """ Delete an element from the array.

        Args:
            index (int, optional): index of the element to be deleted. Defaults is last element.
        """
        if index is None:
            if self.IsEmpty():
                raise Exception('Array is empty')
            else:
                self._Clear(self._pointer - 1)
        else:
            self._Clear(index)
    
    def Search(self, element):
        """ Search for an element in the array.

        Args:
            element (any): element to be searched.

        Returns:
            int: index of the element if found, -1 otherwise.
        """
        for i in range(self._pointer):
            if element == self._elements[i]:
                return i
        return -1
    
    def Traverse(self, index: int = None):
        """ Traverse the array.

        Args:
            index (int, optional): index of the element to be traversed. Defaults to None.
        """
        if index is None:
            for i in self._elements:
                print(i)
        else:
            print(self._elements[index])
    
    def __str__(self):
        return str(self._elements)
    
    def __repr__(self):
        return self.type + ' : ' + self.__str__()
    
    @property
    def length(self):
        return self._pointer
    
    @property
    def size(self):
        return self.max_size
    
    @property
    def type(self):
        if self._type is None:
            return '<class \'array\'>'
        return '<class \'' + str(self._type)[8 : -2] + ' array\'>'
    
    @property
    def value(self):
        return self._elements
    
    @value.setter
    def value(self, value):
        self._Clear()
        self.Insert(value)
    
    @value.deleter
    def value(self):
        self._Clear()

def new(type: type = None, max_size: int = None):
    """ Create a new array.

    Args:
        type (type): type of the array.
        max_size (int, optional): maximum size of the array. Defaults to None.

    Returns:
        Array: new array.
    """
    return Array(type, max_size)

def is_full(array: Array):
    """ Check if the array is full.

    Args:
        array (Array): array to be checked.

    Returns:
        bool: True if the array is full, False otherwise.
    """
    return array.IsFull()

def is_empty(array: Array):
    """ Check if the array is empty.

    Args:
        array (Array): array to be checked.

    Returns:
        bool: True if the array is empty, False otherwise.
    """
    return array.IsEmpty()

def search(array: Array, element):
    """ Search for an element in the array.

    Args:
        array (Array): array to be searched.
        element (any): element to be searched.

    Returns:
        int: index of the element if found, -1 otherwise.
    """
    return array.Search(element)

def traverse(array: Array, index: int = None):
    """ Traverse the array.

    Args:
        array (Array): array to be traversed.
        index (int, optional): index of the element to be traversed. Defaults to None.
    """
    array.Traverse(index)

def len(array: Array):
    """ Get the length of the array.

    Args:
        array (Array): array to be checked.

    Returns:
        int: length of the array.
    """
    return array.length

def size(array: Array):
    """ Get the size of the array.

    Args:
        array (Array): array to be checked.

    Returns:
        int: size of the array.
    """
    return array.size

def remove_duplicates(array: Array):
    """ Remove duplicate elements from the array.

    Args:
        array (Array): array to be checked.
    """
    for i in range(array.length):
        for j in range(i + 1, array.length):
            if array._elements[i] == array._elements[j]:
                array._Clear(j)