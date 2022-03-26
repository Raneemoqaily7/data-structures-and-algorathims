
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



                     
            

        
    

#[1,2,3,4,5]
    # def getKthNode(self,head,position):
    #     count=0
    #     if (head ):
    #         if count == position:
    #             print (head.value)

    #         else:
    #             list.getKthNode(head.next, position-1)

    #     else :
    #         print("index doesnt exist")

    
if __name__ == "__main__":
    list=LinkedList()
    
    list.push(1)
    list.push(2)
    list.push(3)
    list.push(4)
    
    print(list)

    print(list.reverse()) 
    print(list)



  

        