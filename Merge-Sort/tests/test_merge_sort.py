from merge_sort.merge import Mergesort
def test_merge_sort_one():
    assert [2, 6, 8, 9, 14] == Mergesort([8,14,2,9,6])

def test_merge_sort_two():


    assert [0, 1, 2, 7, 11, 52, 89] == Mergesort([0,1,7,89,2,11,52])
