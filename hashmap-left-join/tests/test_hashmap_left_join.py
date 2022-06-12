import pytest
from hashmap_left_join.hashmap import Hashmap, left_join


def test_left_join_empty():
    hash1 = Hashmap()
    hash2= Hashmap()

    hash1.add('name', 'raneem')

    hash3 = left_join(hash1, hash2)
    assert hash3.get('name') == ['raneem', 'Null']






    
    







def test_two_collsion():
    hash1 = Hashmap()
    hash2 = Hashmap()

    hash1.add('fond', 'enamored')



    hash1.add('ofnd','test')

    hash2.add('fond', 'averse')
    hash2.add('guide', 'follow')

    hash3 = left_join(hash1, hash2)


    assert hash3.get('fond') == ['enamored', 'averse']
    assert hash3.get('ofnd') == ['test', 'Null']



def test_oneft_join():


    hash1 = Hashmap()
    hash2 = Hashmap()
    hash1.add('fond', 'enamored')
    hash1.add('wrath', 'anger')

    hash1.add('diligent', 'employed')

    hash1.add('outfit', 'garb')
    

    
    hash2.add('fond', 'averse')
    hash2.add('wrath', 'delight')
    hash2.add('diligent', 'idle') 
   

    hash3 = left_join(hash1, hash2)

    assert hash3.get('outfit') == ['garb', 'Null']
    assert hash3.get('fond') == ['enamored', 'averse']

    assert hash3.get('wrath') == ['anger', 'delight']



    assert hash3.get('diligent') == ['employed', 'idle']













