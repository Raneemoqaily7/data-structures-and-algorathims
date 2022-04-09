
from stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_valid_brackets_one():
    
   
    actual = validate_brackets("()")
    expected=True
    assert actual == expected


def test_valid_brackets_two():
    
   
    actual = validate_brackets("({)}")
    expected=False
    assert actual == expected

def test_valid_brackets_three():
    
   
    actual = validate_brackets("{")
    expected=False
    assert actual == expected


def test_valid_brackets_four():
    
   
    actual = validate_brackets("{]")
    expected=False
    assert actual == expected

def test_valid_brackets_five():
    
   
    actual = validate_brackets("[a+b]*(x+2y)*{gg+kk}")
    expected=True
    assert actual == expected
   

