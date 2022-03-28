from inspect import stack
import queue
from stack_queue_pseudo.stack_queue_peseudo import Stack,Node,Queue,pseudo_queue
import pytest

def test_push_one():
    stack=Stack()
    stack.push(1)
    actual =stack.__str__()
    expected="1 -->"
    assert actual== expected

def test_push_two():
    
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    actual=stack.__str__()
    expected="3 -->2 -->1 -->"
    assert actual== expected

def test_push_three():
    stack=Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    actual=stack.__str__()
    expected="c -->b -->a -->"
    assert actual==expected

def test_pop_one():
    stack=Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    stack.pop()
    actual =stack.pop()
    expected="b"
    assert actual==expected

def test_pop_two():
    stack=Stack()
    stack.push("a")
    
    actual=stack.pop()
    excepted="a"
    assert actual==excepted


def test_pop_three():
    stack=Stack()
    stack.push("a")
    stack.push("b")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    
    actual =stack.pop()
    expected=4
    assert actual==expected

def test_pop_four():
   
      #raise error
     with pytest.raises(Exception): #(Exception)
         stack.pop()
    
def test_peek_one():
    stack=Stack()
    stack.push("a")
    stack.push("b")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    actual=stack.peek()
    expected=4
    assert actual==expected

def test_peek_two():
    stack=Stack()
    stack.push("HELLO")
    actual=stack.peek()
    expcted="HELLO"
    assert actual==expcted

def test_is_empty_one():
    stack=Stack()
    stack.push("HELLO")
    # actual =stack.is_empty()
    # expcted=False
    assert stack.is_empty()==False

def test_is_empty_two():
    stack =Stack()
    actual =stack.is_empty()
    expcted=True
    assert actual==expcted

def test_enqueue_one():
    queue=Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual=queue.__str__()
    expcted="1 --2 --3 --"
    assert actual==expcted

def test_enqueue_two():
    queue=Queue()

    queue.enqueue("a")
    queue.enqueue(1)
    queue.enqueue("b")
    queue.enqueue(2)
    actual=queue.__str__()
    expcted="a --1 --b --2 --"
    assert actual==expcted

def test_dequeue_one():
    queue=Queue()
    queue.enqueue("a")
    queue.enqueue(1)
    queue.enqueue("b")
    queue.enqueue(2)
    actual=queue.dequeue()
    expected="a"
    assert actual==expected

def test_dequeue_two():
    
    
    with pytest.raises(Exception): #(Exception)
         stack.dequeue()

def test_queue_peek_one():
    queue=Queue()
    queue.enqueue("hello")
    queue.enqueue("python")
    queue.enqueue("world")
    actual =queue.peek()
    excepted = "hello"
    assert actual==excepted

def test_queue_peek_one():
    queue=Queue()
    queue.enqueue("hello")
    actual =queue.peek()
    excepted = "hello"
    assert actual==excepted

def test_queue_is_empty():
    queue=Queue()
    actual =queue.is_empty()
    excepted = True
    assert actual==excepted


def test_queue_is_empty_two():
    queue=Queue()
    queue.enqueue("hello")
    actual =queue.is_empty()
    excepted = False
    assert actual==excepted








        
         







    

