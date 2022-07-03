def LinearSearch(array, item):
    """ Linear search algorithm
    
    Args:
        array: The array to search
        item: The item to search for
    """
    for i in range(len(list)):
        if array[i] == item:
            return i
    return -1

def BinarySearch(array, item):
    """ Binary search algorithm
    
    Args:
        array: The array to search
        item: The item to search for
    """
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1