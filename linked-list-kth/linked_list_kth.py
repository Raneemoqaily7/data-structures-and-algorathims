
class Node :                                                     
    def __init__(self,value=None,next=None):
        self.value=value
        self.next= next

                             
class LinkedList:
    def __init__(self):
        self.head=None
        

        
    def push(self,new_value):
        new_node=Node(new_value)
        if self.head is None:
            
            self.head=new_node
       
        else :
           
            current=self.head
            while current.next is not None :
                current=current.next
            current.next =new_node


    def __str__(self):
        if self.head is None :
            return 'Empty Linked List'

        else :
            current =self.head
            output =""
            while current is not None :
                output+=f'{current.value} -->'
                
                current =current.next
            output += "NULL"
            return output
                
    

    def get_length(self):
        count =0
        current =self.head
        while current is  not  None :
            
            current=current.next
            count+=1
        return count

#[1,2,3,4] 

    def reverse(self):
        

      prev=None
      current =self.head
      while current is not None :
          next =current.next
          current.next=prev
          prev=current
          current =next
      self.head =prev



                     
            

        
    

# [1,2,3,4,5]
    def getKthNode(self,k):
        """
        function to get  kth from end
        argument: a number, k, as a parameter.
        Return the node’s value that is k places from the tail of the linked list.

        """
        
        l = self.get_length()
        if k > l or k<0 :
            raise Exception ("Invalid Index")

        else :
            count =0
            current =self.head
            while current is not None:
                if count==l-k-1 :
                    return current.value
                current = current.next
                count +=1
    




     

    
if __name__ == "__main__":
    list=LinkedList()
    
    list.push(1)
    list.push(2)
    list.push(3)
    list.push(4)
    
    print(list)

    
    print(list.getKthNode(1)) 
    print(list)



  

        