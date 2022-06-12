class Hashmap(object):

    def __init__(self, size=1024):

        self.size = size
        self.map = [None] * size
      

    def hash(self, key):
     
        sum_of_ascii = 0

        for ch in key:

            ch_ascii = ord(ch)  
            sum_of_ascii += ch_ascii
        hashed_key = (sum_of_ascii * 19) % self.size

        return hashed_key




    def add(self, key, value):
      
        idx = self.hash(key)
        if not self.map[idx]:
            self.map[idx] = [[key, value]]
        else:
            self.map[idx].append([key, value])



    def get(self, key):
       
        index = self.hash(key)

        if not self.map[index]:

            return None

        for arr in self.map[index]:

            if arr[0] == key:

                return arr[1]




    def keys(self):
        
        keys = []
        for group in self.map:
            if group is not None:
                for arr in group:
                    keys.append(arr[0])


        return keys



    def contains(self, key):
      
        if self.get(key):





            return True
        else:

            return False

    def __str__(self):


        res = ""
        for group in self.map:
            if group is not None:
                res += f"{group} \n"
        return res


def left_join(hash1, hash2):

    """
     function called left join Arguments: two hash maps
     The first parameter is a hashmap that has word strings as keys, 
     and a synonym of the key as values.
     The second parameter is a hashmap that has word strings as keys, 
     and antonyms of the key as values.
    Return: The returned data structure that holds the results is up to you.
    It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

    """
       

    hash3 = Hashmap()

    for key in hash1.keys():        
        if hash2.contains(key):
            hash3.add(key, [hash1.get(key), hash2.get(key)])
        else:
            hash3.add(key, [hash1.get(key), 'Null'])
        
    return hash3


if __name__ == "__main__":


    hash1 = Hashmap()
    hash2 = Hashmap()


    hash1.add('wrath', 'anger')
    hash1.add('fond', 'enamored')
    
    hash1.add('diligent', 'employed')

    hash1.add('outfit', 'garb')

    hash1.add('guide', 'usher')

    
    hash2.add('wrath', 'delight')
    hash2.add('fond', 'averse')
    
    hash2.add('diligent', 'idle') 

    hash3 = left_join(hash1, hash2)


    print(hash3)
   



   