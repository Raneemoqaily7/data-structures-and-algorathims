




class Node :                                                     
  def __init__(self,value,next):
     self.value=value
     self.next=next

                             
class LinkedList:
  def __init__(self):
    self.head=None


  def append (self,value):
    if self.head is None:
      self.head=Node(value,None)
      return
    else :
      current =self.head
      while current.next is not  None:
        current =current.next
      current.next = Node(value,current.next)
      return
      
      
        

  def insert_before(self,value,new_value):
    
    if self.head.value == value:
      node=Node(new_value,self.head)
      self.head=node
      return

      
    current=self.head
    while current :
      if self.head is None:
        break
      if current.next.value == value:
        node=Node(new_value,current.next)
        node.next=current.next
        current.next=node

        return
# [,5,6,1,,2,3,4]
  def insert_after(self,value,new_value):
    current=self.head
    while current:
      if current.value==value:
        current.next=Node(new_value,current.next)
      current=current.next
    return





      # if self.head.value==value:
      #  node=Node(new_value,self.head.next)
      #  self.head.next=node
      #   return

    # current=self.head
    # while current :
    #   if self.head is None:
    #     self.head =node
    #   #   break
    #   if current.next.value == value:
    #      node=Node(new_value,current.next)
    #      current.next=node
    #      node=current
    #      return


      
     
    



  def __str__(self):
    result ="head ->"
    if self.head is None:
     result ="Empty Linked List"
    else :
      current =self.head
      while current is not None:
          
        result+= f' {current.value} -> ' 
        current =current.next
      result+="X"
    return result

   #[1,2,,x,3,4,5]
  

    

    
    

if __name__ =="__main__":
  ll = LinkedList()
  ll.append("Husam")
  ll.append("Amjad")
  ll.append("Awes")
  ll.insert_after("Awes","Raneem")
 
  
  
  print(ll)
  