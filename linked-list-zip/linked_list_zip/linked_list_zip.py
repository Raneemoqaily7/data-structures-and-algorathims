
class Node :
    def __init__(self , value =None ,next =None ):
       
        self.next = next
        self.value = value


class LinkedList :
    def __init__(self):
        self.head=None
        self.next=None
        # self.l1=None
        # self.l2=None
#  [3]->[2]->[1]

    def push (self,new_value)  :
        node =Node (new_value)
        node.next =self.head
        self.head=node 
    #   ] 1,,2,3]  
    #   [4  ,5,6]
    # 1-->4 ->
   
    @staticmethod
    def zip_lists(l1,l2):
        """
        a function called zip lists Arguments: 2 linked lists Return: New Linked List
         Zip the two linked lists together into one so that the nodes alternate between the two lists 
        and return a reference to the the zipped list.
        """
        
     #[1,2,3]
     # [4,5,6]       
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
    l1.push(1)
    l1.push(2)
    l1.push(3)
    l2.push(4)
    l2.push(5)
    l2.push(6)
    
    
    print(l1)
    print(l2)
    l1.zip_lists(l1 ,l2)
    print(l1)
    
    