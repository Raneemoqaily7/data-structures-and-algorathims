


# class Animal:
#     def __init__(self,animal=None,next=None):
#         self.animal =animal
#         self.next=next

class Node :
    def __init__(self,animal=None):
      self.value =animal
      


class Animal:
    def __init__(self):
        self.top =None

    
   


# class AnimalShelter:
#     def __init__(self) :
#         self.animal =None

class AnimalShelter:
    def __init__(self) :
        self.catQ =Animal()
        self.DogQ=Animal()
        self.top =None
    
    def push(self,animal):
        animal =Node(animal)
        animal.next=self.top
        self.top =animal
       
    def enqueue(self,animal):
        count1=0
        count2=0
        while animal == "cat" :
           self.catQ.push(animal)
           count1 +=1
          
        while animal == "dog":
           self.DogQat.push(animal)
           count2 +=1
        return

    
    def __str__(self):
        if self.top is None:
            return "Empty Qeue"


        else  :
            current=self.top
            output =""
            while current is not None :
                output+=f'{current.value}   '
                
                current=current.next
           
            return output


    # def enqueue(self,animal):
    #     animal =Animal(animal)
    #     if self.animal is None:
    #        self.animal =animal
    #        return

    #     else :
    #         current =self.animal
    #         while current.next is not None:
    #             current =current.next
    #         current.next =animal
    #         return


          
           


#     def dequeue (self ,pre):
#         pass

    # def __str__(self):
    #     if self.animal is None:
    #         return "Empty Qeue"


    #     else  :
    #         current=self.animal
    #         output =""
    #         while current is not None :
    #             output+=f'{current.animal} --'
                
    #             current=current.next
    #         return output


        


if __name__=="__main__":
#     animal=AnimalShelter()
#     animal.enqueue("cat")
#     animal.enqueue("cat")
#     animal.enqueue("dog")
#     print (animal)


 animal =AnimalShelter() 
 animal.push("cat")
 animal.push("dog")
 animal.push("dog")
 print(animal)

