import pytest
from trees.trees import Node ,BinaryTree,BinarySearchTree

def test_max_tree_one():
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

    
    tree=BinaryTree()
    tree.root=node1
    
    actual =tree.find_maximum_value()
    expected =1000
    assert actual == expected

def test_max_tree_single_node_case():
    node1=Node(0)
    
    tree=BinaryTree()
    tree.root=node1
    actual =tree.find_maximum_value()
    expected=0
    assert actual == expected

def test_max_tree_empty_case():
    node1=None
    
    tree=BinaryTree()
    tree.root=node1
    with pytest.raises (Exception):
        BinaryTree.find_maximum_value()

    





def test_pre_order_one():
    node1=Node(1)
    node2=Node(2)
    node1.left=node2
    
    node3=Node(3)
    node1.right=node3
    node4=Node(4)
    node2.left=node4
    
    tree = BinaryTree()
    tree.root=node1
    actual = tree.pre_order()
    expected =[1, 2, 4, 3]
    assert actual == expected

def test_in_order_two():
    node1=Node(1)
    node2=Node(2)
    node1.left=node2
    
    node3=Node(3)
    node1.right=node3
    node4=Node(4)
    node2.left=node4
    
    tree = BinaryTree()
    tree.root=node1
    actual = tree.in_order()
    expected =[4, 2, 1, 3]
    assert actual == expected

def test_post_order_three():
    node1=Node(1)
    node2=Node(2)
    node1.left=node2
    
    node3=Node(3)
    node1.right=node3
    node4=Node(4)
    node2.left=node4
    
    tree = BinaryTree()
    tree.root=node1
    actual = tree.post_order()
    expected =[4, 2, 3, 1]
    assert actual == expected


def test_single_root_node():
    node1=Node(1)
    tree = BinaryTree()
    tree.root=node1
    actual = tree.post_order()
    expected =[1]
    assert actual == expected

def test_add_value_to_the_right():
    node1=Node(4)
    tree1 = BinarySearchTree()
    tree1.root = node1 
    
    node2=Node(2)
    node3 =Node(8)
    node4=Node(9)
    
    node1.left=node2
    node1.right=node3
    node3.right=node4
    tree1.Add(9)
    actual =tree1.pre_order()
     
    expected = [4, 2, 8, 9]
    assert actual == expected

def test_add_value_to_the_left():
    node1=Node(4)
    tree1 = BinarySearchTree()
    tree1.root = node1 
    
    node2=Node(2)
    node3 =Node(8)
    
    
    node1.left=node2
    node1.right=node3
    
    tree1.Add(1)
    actual =tree1.pre_order()
     
    expected = [4, 2, 1, 8]
    assert actual == expected

def test_collection_from_pre_order_traversal():
    tree1 = BinarySearchTree()
    node1=Node(4)
    tree1.root = node1 
    
    node2=Node(2)
    node3 =Node(8)
    node4=Node(9)
    node1.left=node2
    node1.right=node3
    node3.right=node4
    tree1.Add(9)

    actual =tree1.pre_order()
    expected =[4, 2, 8, 9]
    assert actual == expected

def test_collection_from_in_order_traversal():
    tree1 = BinarySearchTree()
    node1=Node(4)
    tree1.root = node1 
    
    node2=Node(2)
    node3 =Node(8)
    node4=Node(9)
    node1.left=node2
    node1.right=node3
    node3.right=node4
    tree1.Add(9)

    actual =tree1.in_order()
    expected =[2, 4, 8, 9]
    assert actual == expected

def test_collection_from_post_order_traversal():
    tree1 = BinarySearchTree()
    node1=Node(4)
    tree1.root = node1 
    
    node2=Node(2)
    node3 =Node(8)
    node4=Node(9)
    node1.left=node2
    node1.right=node3
    node3.right=node4
    tree1.Add(9)

    actual =tree1.post_order()
    expected =[2, 9, 8, 4]
    assert actual == expected



def test_Contains_existing_value():

    tree1 = BinarySearchTree()
    node1=Node(4)
    tree1.root = node1 
    
    node2=Node(2)
    node3 =Node(8)
    node4=Node(9)
    node1.left=node2
    node1.right=node3
    node3.right=node4
    tree1.Contains(9)

    actual =tree1.Contains(9)
    expected =True
    assert actual == expected

def test_Contains_not_existing_value():

    tree1 = BinarySearchTree()
    node1=Node(4)
    tree1.root = node1 
    
    node2=Node(2)
    node3 =Node(8)
    node4=Node(9)
    node1.left=node2
    node1.right=node3
    node3.right=node4
    tree1.Contains(9)

    actual =tree1.Contains(177)
    expected =False
    assert actual == expected







