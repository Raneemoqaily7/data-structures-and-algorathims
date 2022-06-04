from hashtable.hashtable import HashTable
import pytest

def test_Set_key_value():
    hashtable =HashTable()
    hashtable.set("Owner" ,"John")
    hashtable.set("Dog" , "Jessi")
    hashtable.set("Mobile" ,"+9624567469")
    actual =hashtable.map
    expected =[[{'Mobile': '+9624567469'}], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [{'Owner': 'John'}], None, None, None, None, None, None, None, None, [{'Dog': 'Jessi'}], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    assert actual == expected


def test_get_value ():
    hashTable =HashTable()
    hashTable.set("Owner" ,"John")
    hashTable.set("Dog" , "Jessi")
    
    actual = hashTable.get("Dog")
    expected =[{'Dog': 'Jessi'}]
    assert actual ==expected

def test_contains():
    hashTable =HashTable()
    hashTable.set("Owner" ,"John")
    actual = hashTable.contains("name")
    expected =False
    assert actual ==expected


def test_collision_case():
    hashTable =HashTable()
    hashTable.set("Owner" ,"John")

    hashTable.set("Dog" , "Jessi")
    hashTable.set("goD" , "Yes")
    actual = hashTable.map 
    expected = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [{'Owner': 'John'}], None, None, None, None, None, None, None, None, [{'Dog': 'Jessi'}, {'goD': 'Yes'}], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    assert actual == expected

def test_hash ():
    hashTable =HashTable()
    hashTable.set("Dog" , "Jessi")
    actual = hashTable.hash ("Dog")
    expected =32
    assert actual == expected


def test_value_bucket_collision():
    hashTable =HashTable()
    hashTable.set("Dog" , "Jessi")
    hashTable.set("goD" , "Yes")
    actual =hashTable.get("Dog")
    expected =[{'Dog': 'Jessi'}, {'goD': 'Yes'}]
    assert actual == expected



def test_keys():
    hashTable =HashTable()
    hashTable.set("Owner" ,"John")

    hashTable.set("Dog" , "Jessi")
    hashTable.set("goD" , "Yes")
    actual =hashTable.keys()
    expected =['Owner', 'Dog', 'goD']
    assert actual == expected









