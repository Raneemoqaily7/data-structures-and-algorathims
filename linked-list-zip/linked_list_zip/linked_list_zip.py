
class Node :
    def __init__(self , value =None ,next =None ):
       
        self.next = next
        self.value = value


class LinkedList :
    def __init__(self):
        self.head=None
        self.next=None
      


    def push (self,new_value)  :
        node =Node (new_value)
        node.next =self.head
        self.head=node 
    #   [1,2,3]  
    #   [4,5,6]
    # 1-->4 ->2->5->3->6
   
    
    def zip_lists(self,l1,l2):
        """
        a function called zip lists Arguments: 2 linked lists Return: New Linked List
         Zip the two linked lists together into one so that the nodes alternate between the two lists 
        and return a reference to the the zipped list.
        """
        if l1.head is None and l2.head is None :
            raise Exception (" Two Empty list ")

        elif l2.head is None :
            return l1

        elif l1.head is None :
            return l2

          

        else :         
            current1 = l1.head
            current2 = l2.head
    
            while current1 and current2:

                next1 = current1.next             
                next2 = current2.next

                current1.next = current2
                current2.next = next1
    
                current1 = next1
                current2 = next2
                
        
            return l1 
           
            

            
    def __str__(self):
      
        current =self.head 
        output =""
        while current is not None :
            output+=f'{current.value} -->  '
            current =current.next 
        output += "null"
        return output 
   

             
            


        


if __name__ =="__main__":
  
    l1=LinkedList()
    l2=LinkedList()
    # l1.push("a")
    # l1.push("b")
    # l1.push("c")
    l2.push("A")
    l2.push("B")
    l2.push("C")
    
    
    
    print(l1.zip_lists(l1 ,l2))

    
    