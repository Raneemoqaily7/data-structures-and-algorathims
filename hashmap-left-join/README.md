# Hashmap LEFT JOIN
<!-- Short summary or background information -->
Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

The basic idea of a hashtable is the ability to store the key into this data structure, and quickly retrieve the value. This is done through what we call a hash. A hash is the ability to encode the key that will eventually map to a specific location in the data structure that we can look at directly to retrieve the value.

## Challenge
<!-- Description of the challenge -->

Write a function that LEFT JOINs two hashmaps into a single data structure.

Write a function called left join
Arguments: two hash maps
The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic


## WhiteBoard

[left_Join WhiteBoard](./assets/WhatsApp%20Image%202022-06-06%20at%206.39.04%20PM.jpeg)



## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O time  :O(n)

## Solution
<!-- Embedded whiteboard image -->

Code [code](./hashmap_left_join/hashmap.py)


Test [Test](./tests/test_hashmap_left_join.py)

