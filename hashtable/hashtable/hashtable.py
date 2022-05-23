class HashTable :
    def __init__(self , size =10):
        self.size =size
        self.map =[None]*size


    def hash (self , key):
        """
        Function takes an  rguments: key and returns Value associated with that key in the table
        """
        #Cat

        sum_of_ascii =0
        for ch in key :
            char_ascii = ord(ch)
            sum_of_ascii+=char_ascii

        hashed_key = sum_of_ascii   % self.size

        return hashed_key


    def add (self , k ,value ):
        hashed_key = self.hash(k)
        added = self.map[hashed_key] =value
        return added


    def get (self ,k ):
        hashed_key =self.hash(k)
        return self.map[hashed_key]


    def delete (self , k):
        hashed_key =self.hash(k)
        self.map[hashed_key] = None

    def contains(self ,k):
        hashed_key = self.hash(k)
        for i in range (self.size):
            if i == hashed_key :
                return True
            else :
                return False







if __name__=="__main__":
    hashtable =HashTable()
    print(hashtable.hash("march 6"))
    
    # hashtable.add("aCt" , "Jessica")
    hashtable.add("Owner" ,"John")
    hashtable.add("Dog" , "Jessi")
    hashtable.add("Mobile" ,"+9624567469")
    
    print(hashtable.get("Dog"))
    print(hashtable.get("Owner"))
    print (hashtable.map)
    hashtable.delete("Dog")
    print(hashtable.contains("Owner"))
    print (hashtable.map)



