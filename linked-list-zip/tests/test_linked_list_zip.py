from linked_list_zip.linked_list_zip import   LinkedList ,  Node    
import pytest

def test_zip_list_one () :
        l1=LinkedList()
        l2=LinkedList()
        l1.push(1)
        l1.push(2)
        l1.push(3)
        l2.push(4)
        l2.push(5)
        l2.push(6)
        l1.zip_lists(l1 ,l2)
        actual = l1.__str__()
        expected ="3 -->  6 -->  2 -->  5 -->  1 -->  4 -->  null"
        assert actual == expected



def test_zip_list_two () :
        l1=LinkedList()
        l2=LinkedList()
        l1.push("a")
        l1.push("b")
        l1.push("c")
        l2.push("A")
        l2.push("B")
        l2.push("C")
        l1.zip_lists(l1 ,l2)
        actual = l1.__str__()
        expected ="c -->  C -->  b -->  B -->  a -->  A -->  null"
        assert actual == expected



def test_zip_list_three () :
        l1=LinkedList()
        l2=LinkedList()
        l1.push("a")
        l1.push("b")
        l1.push("c")
        # l2.push("A")
        # l2.push("B")
        # l2.push("C")
        l1.zip_lists(l1 ,l2)
        actual = l1.__str__()
        expected ="c -->  b -->  a -->  null"
        assert actual == expected


def test_zip_list_four () :
        l1=LinkedList()
        l2=LinkedList()
    
        l2.push("A")
        l2.push("B")
        l2.push("C")
        l1.zip_lists(l1 ,l2)
        actual = l2.__str__()
        expected ="C -->  B -->  A -->  null"
        assert actual == expected


def test_zip_list_five():
    l1=LinkedList()
    l2=LinkedList()
    with pytest.raises(Exception):
       l1.zip_lists(l1 ,l2)



