from pydsa import array

def test_array_type():
    arr = array.new()
    assert arr.type == 'Array'

def test_array_insert():
    arr = array.Array()
    arr.Insert(1, 2, 3, 4, 5)
    assert arr.elements == [1, 2, 3, 4, 5]

def test_array_insert_2():
    arr = array.new(max_size=10)
    arr.Insert(2)
    arr.Insert(1)
    arr.Insert(2)
    assert arr.elements == [2, 1, 2]

def test_array_insert_3():
    arr = array.new(max_size=10)
    arr.Insert('2')
    arr.Insert('1')
    arr.Insert('2')
    arr.Insert('1')
    arr.Insert('2')
    assert arr.elements == ['2', '1', '2', '1', '2']
    
def test_array_delete():
    arr = array.new(max_size=10)
    arr.Insert(2)
    arr.Insert(1)
    arr.Insert(2)
    arr.Insert(1)
    arr.Insert(2)
    arr.Delete(1)
    assert arr.elements == [2, 2, 1, 2]

def test_array_delete_2():
    arr = array.new(max_size=10)
    arr.Insert(2)
    arr.Insert(1)
    arr.Insert(2)
    arr.Insert(1)
    arr.Insert(2)
    arr.Delete(2)
    assert arr.elements == [2, 1, 1, 2]
    
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
    assert str(arr) == '[2, 1, 2, 1, 2]'