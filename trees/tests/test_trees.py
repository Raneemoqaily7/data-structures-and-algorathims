from trees.trees import Binary_Tree ,build_tree

def test_in_order():
    numbers = [2,4,5,1,2,8,345,2,6]
    numbers_tree = build_tree(numbers)
    actual = numbers_tree.in_order()
    expected = [1, 2, 4, 5, 6, 8, 345]
    assert actual == expected


def test_pre_order():
    numbers = [2,4,5,1,2,8,345,2,6]
    numbers_tree = build_tree(numbers)
    actual = numbers_tree.pre_order()
    expected = [2, 1, 4, 5, 6, 8, 345]
    assert actual == expected

def test_post_order():
    numbers = [2,4,5,1,2,8,345,2,6]
    numbers_tree = build_tree(numbers)
    actual = numbers_tree.post_order()
    expected = [1, 4, 5, 6, 8, 345, 2]
    assert actual == expected

