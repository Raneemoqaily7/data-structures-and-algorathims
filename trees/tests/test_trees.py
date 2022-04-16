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


def test_max_value():
    
    node1=Node(1000)
    node2=Node(2)
    node3 =Node(8)
    node4=Node(9)
    node1.left=node2
    node1.right=node3
    node3.right=node4
    node4=Node(89)
    node3.left =node4
    node5=Node(990)
    node2.left =node5