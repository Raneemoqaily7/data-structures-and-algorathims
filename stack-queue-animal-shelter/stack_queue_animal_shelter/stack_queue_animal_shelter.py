from collections import deque

class AnimalShelter:
    def __init__(self):
        self.buffer = deque()


    def enqueu(self,animal):
        
        while animal =="dog" or animal == "cat":
            self.buffer.appendleft(animal)
            return

        else : 
           
                return "this shilter only dogs or cats"
       

    def deque(self,pref):
        
        while pref =="dog" or pref == "cat":
            return self.buffer.pop()

        else:
        

            return "null"
                
         

        
       
            

    def is_empty (self):
        return len(self.buffer)==0

    def size (self):
        return len(self.buffer)


    def __str__(self):
        
            return f'{self.buffer}'




if __name__ == "__main__":
    animal =AnimalShelter()
    animal.enqueu("dog")
    animal.enqueu("cat")
    animal.enqueu("cat")
    animal.enqueu("dog")
    print(animal.enqueu("fish"))
    print(animal.deque("fish"))
    


    print(animal)


    

    