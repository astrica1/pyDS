from pydsa import array

def test_array_type():
    arr = array.new()
    assert arr.type == '<class \'array\'>'

def test_array_type_2():
    arr = array.new(type=int)
    assert arr.type == '<class \'int array\'>'

def test_array_insert():
    arr = array.Array()
    arr.Insert(1, 2, 3, 4, 5)
    assert arr.value == [1, 2, 3, 4, 5]

def test_array_insert_2():
    arr = array.new(max_size=10)
    arr.Insert(2)
    arr.Insert(1)
    arr.Insert(2)
    assert arr.value == [2, 1, 2, 0, 0, 0, 0, 0, 0, 0]

def test_array_insert_3():
    arr = array.new()
    arr.Insert('2')
    arr.Insert('1')
    arr.Insert('2')
    arr.Insert('1')
    arr.Insert('2')
    assert arr.value == ['2', '1', '2', '1', '2']

def test_array_insert_4():
    arr = array.new(type=int)
    arr.value = 1, 2, 3, 4
    arr.Insert(5)
    assert arr.value == [1, 2, 3, 4, 5]

def test_array_insert_size_error():
    arr = array.new(max_size=10)
    try:
        arr.Insert(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    except Exception as e:
        assert str(e) == 'Array is full'

def test_array_insert_type_error():
    arr = array.new(type=float)
    try:
        arr.Insert(1, 2, 3, 4, 5)
    except Exception as e:
        assert str(e) == 'Type mismatch'

def test_array_insert_type_error():
    arr = array.new(type=float)
    try:
        arr.Insert(1, 2, 3, 4, 5)
    except Exception as e:
        assert str(e) == 'Type mismatch'
    
def test_array_delete():
    arr = array.new(max_size=10)
    arr.Insert(2)
    arr.Insert(1)
    arr.Insert(2)
    arr.Insert(1)
    arr.Insert(2)
    arr.Delete(1)
    assert arr.value == [2, 2, 1, 2, 0, 0, 0, 0, 0, 0]

def test_array_delete_2():
    arr = array.new(max_size=10)
    arr.Insert(2)
    arr.Insert(1)
    arr.Insert(2)
    arr.Insert(1)
    arr.Insert(2)
    arr.Delete(2)
    assert arr.value == [2, 1, 1, 2, 0, 0, 0, 0, 0, 0]

def test_array_delete_size_error():
    arr = array.new(max_size=10)
    try:
        arr.Delete()
    except Exception as e:
        assert str(e) == 'Array is empty'
    
def test_search():
    arr = array.new(max_size=10)
    arr.Insert('a', 'p', 'p', 'l', 'e')
    arr.Search('p') == 1
    
def test_array_str():
    arr = array.new(max_size=10)
    arr.Insert(2)
    arr.Insert(1)
    arr.Insert(2)
    arr.Insert(1)
    arr.Insert(2)
    assert str(arr) == '[2, 1, 2, 1, 2, 0, 0, 0, 0, 0]'
    
def test_array_remove_duplicate():
    arr = array.new(max_size=10)
    arr.value = 'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd'
    arr2 = array.new(max_size=10)
    arr2.value = 'h', 'e', 'l', 'o', 'w', 'r', 'd'
    array.remove_duplicates(arr)
    assert arr == arr2