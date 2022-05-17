from insertion_sort.sort import InsertionSort


def test_one ():
    array =[8,4,23,42,16,15]
    actual =InsertionSort(array)
    expected =[4, 8, 15, 16, 23, 42]
    assert actual ==expected


def test_two():
    array =[88,0,9]
    actual =InsertionSort(array)
    expected =[0, 9, 88]
    assert actual ==expected

def test_three():
    array =[9]
    actual =InsertionSort(array)
    expected =[9]
    assert actual ==expected
