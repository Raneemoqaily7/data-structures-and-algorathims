
from linked_list_insertions.linked_list_insertions import LinkedList

def test_append():
    list=LinkedList()
    list.append("Hello")
    assert 'head -> Hello -> X'== list.__str__()

def test_append_multiple():
    list=LinkedList()
    list.append("Hello")
    list.append("Raneem")

    assert 'head -> Hello ->  Raneem -> X'== list.__str__()

def test_insert_before_before():
  ll = LinkedList()
  ll.append("Hello")
  ll.append("Amjad")
  ll.append("Awes")
  ll.insert_before("Hello","Husam")

  assert 'head -> Husam ->  Hello ->  Amjad ->  Awes -> X'== ll.__str__()





def test_insert_before():
    list=LinkedList()
    list.append("Awes")
    list.insert_before("Awes","Amjad")
    assert "head -> Amjad ->  Awes -> X"==list.__str__()





def test_insert_after():
    ll=LinkedList()
    ll.append("Hello")
    ll.append("Amjad")
    ll.append("Awes")
    ll.insert_after("Awes","Amjad")
    assert 'head -> Hello ->  Amjad ->  Awes ->  Amjad -> X'==ll.__str__()


def test_insert_after_last():
  ll = LinkedList()
  ll.append("Husam")
  ll.append("Amjad")
  ll.append("Awes")
  ll.insert_after("Awes","Raneem")
  assert 'head -> Husam ->  Amjad ->  Awes ->  Raneem -> X'== ll.__str__()






