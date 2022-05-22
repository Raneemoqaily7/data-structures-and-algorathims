class HashTable :
    def __init__(self , size =1024):
        self.size =size
        self.map =[None]*size


    def get (self , key):
        """
        Function takes an  rguments: key and returns Value associated with that key in the table
        """
        #Cat

        sum_of_ascii =0
        for ch in key :
            char_ascii =ord(ch)
            sum_of_ascii+=char_ascii

        hashed_key = (sum_of_ascii * 19) % self.size
        return hashed_key





if __name__=="__main__":
    hashtable =HashTable()
    print(hashtable.get("cloud"))