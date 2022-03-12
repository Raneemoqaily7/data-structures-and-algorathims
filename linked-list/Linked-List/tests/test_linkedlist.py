from linked_list.linked_list import LinkedList,Node

def test_check_linkedlist():
    actual =LinkedList()
    excepted =None
    assert actual.head == excepted

def test_inserts():
    insert = LinkedList()
    insert.inserts(4)
    assert '4 ->NULL'==insert.to_string()

def test_include():
    list=LinkedList()
    list.inserts(4)
    assert list.includes(4)==True
    assert list.includes("raneem")==False



