
class HashTable (object) :
    def __init__(self , size =50):
        self.size =size
        self.map =[None]*size


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


    def set(self,key,value):
        """
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        Should a given key already exist, replace its value from the value argument given to this method.
        """
       
        index = self.hash(key)
        if not self.map[index]:
            self.map[index] = [{f"{key}":f"{value}"}]

        elif self.map[index]:
            if key in self.keys():
                for dic in self.map[index]:
                    if key in dic.keys():
                        dic[key] = value
            else:
                self.map[index].append({f"{key}":f"{value}"})

                            
    def get(self,key):
        """
        Arguments: key
        Returns: Value associated with that key in the table
        """
        
        index = self.hash(key)
        if not self.map[index]:
            return None
        for dic in self.map[index]:
            if key in dic.keys():
                return dic[key]
   
    def contains(self,key):

        """
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already
        """
        if type(key) is not str:
            raise Exception("Key must be a string")
        index = self.hash(key)
        if not self.map[index]:
            return False
        for dic in self.map[index]:
            if key in dic.keys():
                return True
            return False

       
    def keys (self):
      
        """
       method  returns the collection of keys.
        """
        keys = []
        for index in self.map :
            if index:
                for dic in index:
                        [keys.append(key) for key in dic.keys()]
                        
        return keys

                
                

        
       
def repeatedword(string):

    """
    function called repeated word that finds the first word to occur more than once in a string
    Arguments: string
    Return: string
    """
    hashtable = HashTable()
    word = ''
    for letter in string :
        letter =letter.lower ()

        if ord (letter) in range (ord("a"), ord ("z")+1):
            word +=letter



        elif len(word):

            if  not hashtable.contains (word):
                hashtable.set (word , None)
                word = ''

            else :
                return word

    if len (word) and hashtable.contains(word):
        return word 

    return None 
        

    
        







if __name__=="__main__":
    hashtable =HashTable()
    
    

    # hashtable.set("Owner" ,"John")
    # hashtable.set("Dog" , "Jessi")
    # hashtable.set("goD" , "Yes")
    # hashtable.set("Mobile" ,"+9624567469")
    
    # print(hashtable.get("Dog"))
    # print(hashtable.contains("Owner"))
    # print(hashtable.contains("name"))
    # print (hashtable.map)
    # hashtable.delete("Dog")
    # print(hashtable.contains("Owner"))
    # print (hashtable.hash("Dog"))
    # print (hashtable.map)
    # print(hashtable.keys())
    print (repeatedword("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))

