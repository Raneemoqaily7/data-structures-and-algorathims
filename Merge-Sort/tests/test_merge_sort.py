from merge_sort.merge import merge,mergeSort
def test_one():
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    actual =mergeSort(arr, 0, n-1)
    expected = "5 6 7 11 12 13 %"
    assert actual == expected



def test_two():
    arr = [5,8,0,6]
    n = len(arr)
    actual =mergeSort(arr, 0, n-1)
    expected = "0 5 6 8 %"
    assert actual == expected

