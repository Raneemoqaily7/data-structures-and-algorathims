class HashTable (object) :
    def __init__(self , size =50):
        self.size =size
        self.map =[None]*size


    def hash (self , key):
        """
        method takes an  rguments: key and returns Value associated with that key in the table
        """
        #Cat

        sum_of_ascii =0
        for ch in key :
            char_ascii = ord(ch)
            sum_of_ascii+=char_ascii

        hashed_key = sum_of_ascii   % self.size
        

        return hashed_key


    def set (self , k ,value ):
        """
       method takes key , value as aeguments and return nothing
        doung: hash the key, and set the key and value pair in the table, 
        handling collisions as needed.Should a given key already exist, 
        replace its value from the value argument given to this method.
        """
        idx =self.hash(k)
        if not self.map[idx]:
            self.map[idx] =[{k: value}]
        else :
            self.map[idx].append([k,value])
        return self.map


        
    

    def get (self ,k ):
        """
        method takes k as argumend and return value associated with that key in the map 
        """
        hashed_key =self.hash(k)
        return self.map[hashed_key]
        


    def delete (self , k):
        hashed_key =self.hash(k)
        self.map[hashed_key] = None




    def contains(self ,k):
        """
        method takes Arguments: key
        Returns: Boolean, indicating if the key exists in the map already.
        """
        hashed_key = self.hash(k)
        if self.map[hashed_key]:
            return True

        return False

       
    def keys (self):
        """
        Returns: Collection of keys
        """
        for i in range (len(self.map) ):
            if self.map[i]:
                        
                new_list =self.map
                new_val = set( new_v for new_dic in new_list for new_v in new_dic.values())
                return new_val

        
       
      
                
        







if __name__=="__main__":
    hashtable =HashTable()
    
    

    hashtable.set("Owner" ,"John")
    hashtable.set("Dog" , "Jessi")
    hashtable.set("goD" , "Yes")
    # hashtable.set("Mobile" ,"+9624567469")
    
    # print(hashtable.get("Dog"))
    # print(hashtable.contains("Owner"))
    # print(hashtable.contains("name"))
    # print (hashtable.map)
    # hashtable.delete("Dog")
    # print(hashtable.contains("Owner"))
    # print (hashtable.hash("Dog"))
    # print (hashtable.map)
    print(hashtable.keys())



