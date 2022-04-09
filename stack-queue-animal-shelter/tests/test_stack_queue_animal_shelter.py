from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter ,deque

def test_enqueu_one():
    animal =AnimalShelter()
    animal.enqueu("dog")
    animal.enqueu("cat")
    Actual =animal.__str__()
    expected = "deque(['cat', 'dog'])"
    assert Actual == expected


def test_enqueu_two():
    animal =AnimalShelter() 
    Actual =animal.enqueu("fish")
    expected = "this shilter only dogs or cats"
    assert Actual == expected

def test_enqueu_three():
    animal =AnimalShelter() 
    Actual =animal.deque("fish")
    expected = "null"
    assert Actual == expected

def test_enqueu_four():
    animal =AnimalShelter()
    animal.enqueu("dog")
    animal.enqueu("cat")
    animal.enqueu("cat")
    animal.enqueu("dog")
    Actual =animal.__str__()
    expected = "deque(['dog', 'cat', 'cat', 'dog'])"
    assert Actual == expected