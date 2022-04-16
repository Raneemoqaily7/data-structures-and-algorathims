from trees.trees import QNode,Node,BinaryTree
import pytest

def test_breadth_first_one():
    node1=Node(4)
    node2=Node(2)
    node3 =Node(8)
    node4=Node(9)
    node5=Node(89)
    node6=Node(990)
    node7=Node(29)
    node1.left=node2
    node1.right=node3
    node2.left =node5
    node2.right=node6
    node3.right=node4
    node3.left =node7
    tree=BinaryTree()
    tree.root=node1
    actual =tree.breadth_first()
    expected =[4, 2, 8, 89, 990, 29, 9]
    assert actual ==expected

def test_breadth_first_two():
    node1=Node(4)
    node2=Node(2)
    node3 =Node(8)
    
    node1.left=node2
    node1.right=node3
   
    tree=BinaryTree()
    tree.root=node1
    actual =tree.breadth_first()
    expected =[4, 2, 8]
    assert actual ==expected

def test_breadth_first_three():
    node1=Node(4)
    tree=BinaryTree()
    tree.root=node1
    actual =tree.breadth_first()
    expected =4
    assert actual == expected

def test_breadth_first_four():
    tree=BinaryTree()
    with pytest.raises(Exception):
        tree.breadth_first("a")


