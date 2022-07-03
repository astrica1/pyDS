class __Array:
    def __init__(self, type = None, max_size: int = None):
        """ Initialize an array.

        Args:
            type (type, optional): type of the array's elements. Defaults to None.
            max_size (int, optional): maximum array elements. Defaults to None.

        Raises:
            Exception: if max_size is not an integer.
            Exception: if max_size is less than 1.
            Exception: if type is not int, str, float, bool or None.
        """
        self.__elements = []
        self.__pointer = 0
        self.max_size = max_size
        self.__type = type
        self.__accepted_types = [
            {'type': int, 'name': 'int', 'default': 0},
            {'type': str, 'name': 'str', 'default': ''},
            {'type': float, 'name': 'float', 'default': 0.0},
            {'type': bool, 'name': 'bool', 'default': False},
            {'type': chr, 'name': 'chr', 'default': ' '}
        ]
        self.__accepted_groups = [tuple, list, set]
        self.__Initialize()
        
    def __Initialize(self):
        if self.max_size is not None:
            if type(self.max_size) is not int:
                raise Exception('max_size must be an integer')
            if self.max_size < 1:
                raise Exception('max_size must be greater than 0')
            self.max_size = int(self.max_size)
        
        if self.__type is not None:
            if self.__type not in [types_list['type'] for types_list in self.__accepted_types]:
                types = ''
                for i in self.__accepted_types:
                    types += str(i['name']) + ', '
                types = types[:-2] + ' or None'
                raise Exception('type must be ' + types)

        if self.max_size is not None:
            for i in self.__accepted_types:
                if i['type'] == self.__type:
                    self.__elements = [i['default']] * self.max_size
                    break
    
    def __Clear(self, index: int = None):
        if index is None:
            self.__elements = []
            self.__pointer = 0
            self.__Initialize()
        else:
            if index < 0:
                index = self.__pointer + index
            if index < 0 or index >= self.__pointer:
                raise Exception('Index out of range')
            default_value = [types_list for types_list in self.__accepted_types if types_list['type'] == self.__type][0]['default']
            self.__elements = self.__elements[: index] + self.__elements[index + 1 :] + [default_value]
            self.__pointer -= 1
            
    def __typeValidator(self, element):
        Response = [
            {'code': 0, 'message': 'OK'},
            {'code': 1, 'message': 'Type mismatch'},
            {'code': 2, 'message': 'Type not accepted'},
            {'code': 3, 'message': 'Type is None'},
            {'code': 4, 'message': 'Type is a group'}
        ]
        
        if self.__type is None and type(element) in [types_list['type'] for types_list in self.__accepted_types]:
            self.__type = type(element)
            self.__Initialize()
            return Response[0]
        elif self.__type is not None and type(element) is self.__type:
            return Response[0]
        elif type(element) in self.__accepted_groups:
            return Response[4]
        elif self.__type is not None and type(element) is not self.__type:
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
        return self.max_size is not None and self.__pointer == self.max_size

    def IsEmpty(self):
        """ Check if the array is empty.
        
        Returns:
            bool: True if the array is empty, False otherwise.
        """
        return self.__pointer == 0
    
    def __Append(self, element):
        if self.IsFull():
            raise Exception('Array is full')
        else:
            if self.__typeValidator(element)['code'] == 0:
                if self.max_size is None:
                    self.__elements.append(element)
                else:
                    self.__elements[self.__pointer] = element
                self.__pointer += 1
            elif self.__typeValidator(element)['code'] == 4:
                for i in element:
                    self.__Append(i)
            else:
                raise Exception(self.__typeValidator(element)['message'])
    
    def Insert(self, *args):
        """ Insert elements into the array.
        
        Args:
            *args: elements to be inserted.
        """
        for element in args:
            self.__Append(element)
    
    def Update(self, index: int, element):
        """ Update an element in the array.

        Args:
            index (int): index of the element to be updated.
            element (any): new element.
        """
        if self.__typeValidator(element)['code'] == 0:
            self.__elements[index] = element
        else:
            raise Exception(self.__typeValidator(element)['message'])
    
    def Delete(self, index: int = None):
        """ Delete an element from the array.

        Args:
            index (int, optional): index of the element to be deleted. Defaults is last element.
        """
        if index is None:
            if self.IsEmpty():
                raise Exception('Array is empty')
            else:
                self.__Clear(self.__pointer - 1)
        else:
            self.__Clear(index)
    
    def Search(self, element):
        """ Search for an element in the array.

        Args:
            element (any): element to be searched.

        Returns:
            int: index of the element if found, -1 otherwise.
        """
        for i in range(self.__pointer):
            if element == self.__elements[i]:
                return i
        return -1
    
    def Traverse(self, index: int = None):
        """ Traverse the array.

        Args:
            index (int, optional): index of the element to be traversed. Defaults to None.
        """
        if index is None:
            for element in self.__elements:
                yield element
        else:
            yield self.__elements[index]
    
    def __str__(self):
        return str(self.__elements)
    
    def __repr__(self):
        return self.type + ' : ' + self.__str__()
    
    def __iter__(self):
        return self.__elements[: self.__pointer].__iter__()
    
    def __next__(self):
        self.__pointer += 1
        if self.__pointer < self.max_size:
            return self.__elements[self.__pointer - 1]
        raise StopIteration
    
    def __len__(self):
        return self.length
    
    def __getitem__(self, index):
        return self.__elements[index]
    
    def __setitem__(self, index, element):
        self.Update(index, element)
    
    def __delitem__(self, index):
        self.Delete(index)
    
    def __contains__(self, element):
        return self.Search(element) != -1
    
    def __add__(self, other):
        if self.type is None and other.type is not None:
            self.type = other.type
            self.__Initialize()
        if other.type == self.type:
            result = __Array()
            result.value = self.value + other.value
            return result
        else:
            raise Exception('Type mismatch')
    
    def __radd__(self, other):
        if self.type is None and other.type is not None:
            self.type = other.type
            self.__Initialize()
        if other.type == self.type:
            result = __Array()
            result.value = other.value + self.value
            return result
        else:
            raise Exception('Type mismatch')
    
    def __eq__(self, other):
        if self.type is None or other.type is None:
            return False
        if other.type == self.type:
            return self.value == other.value
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def ___type__(self):
        return self.type
        
    @property
    def length(self):
        return self.__pointer
    
    @property
    def size(self):
        return self.max_size
    
    @property
    def type(self):
        if self.__type is None:
            return '<class \'array\'>'
        return '<class \'' + str(self.__type)[8 : -2] + ' array\'>'
    
    @type.setter
    def type(self, type):
        if type is None:
            raise Exception('Type is None')
        for acceptable__type in self.__accepted_types:
            if acceptable__type['name'] in str(type):
                type = acceptable__type['type']
                break
        if self.__type is None:
            self.__type = type
            self.__Initialize()
        else:
            raise Exception('Type already set')
    
    @property
    def value(self):
        return self.__elements
    
    @value.setter
    def value(self, value):
        self.__Clear()
        self.Insert(value)
    
    @value.deleter
    def value(self):
        self.__Clear()

def new(type = None, max_size: int = None):
    """ Create a new array.

    Args:
        type (type): type of the array.
        max_size (int, optional): maximum size of the array. Defaults to None.

    Returns:
        Array: new array.
    """
    return __Array(type, max_size)

def is_full(array):
    """ Returns True if the queue is full, False otherwise """
    return array.IsFull()

def is_empty(array):
    """ Returns True if the queue is empty, False otherwise """
    return array.IsEmpty()

def search(array, element):
    """ Search for an element in the array.

    Args:
        array (Array): array to be searched.
        element (any): element to be searched.

    Returns:
        int: index of the element if found, -1 otherwise.
    """
    return array.Search(element)

def len(array):
    """ Get the length of the array.

    Args:
        array (Array): array to be checked.

    Returns:
        int: length of the array.
    """
    return array.length

def size(array):
    """ Get the size of the array.

    Args:
        array (Array): array to be checked.

    Returns:
        int: size of the array.
    """
    return array.size