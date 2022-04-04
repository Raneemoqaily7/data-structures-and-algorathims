class Node:
    def __init__(self,value):
        
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


    def inserts (self,value):
        """
        Insert method take an Argument : value and 

        return nothing to add a new node with that value to the head

         of the list with an O(1) Time performance.
        """
        node = Node(value)
        node.next=self.head
        self.head=node

    

    def __str__(self) :
        result =""
        if self.head is None:
            result="Empty linked list"
        else :
            
            current=self.head
            
            while current is not None:
                result+=f'{ current.value } ->' 
                current=current.next
            result+="NULL" 
        return result
        


    def to_string(self)  :
     """
     string method that take Arguments: none and 
     Returns: a string representing all the values in the Linked List, formatted as:

     "[ a ] -> [ b ] -> [ c ] -> NULL"
      """

     return self.__str__()  



    def includes (self,value):
      """
      includes  method that take  Arguments: value and Returns: Boolean
     
     Indicates whether that value exists as a Node`s value somewhere within the list.

    """
      if value is None:
          raise TypeError("Value Is Not included")
      current =self.head
      while current:
          if current.value ==value:
              return True
          current =current.next
      return False
      


if __name__=="__main__":
    ll=LinkedList()
    ll.head=Node(9)
  
    ll.x=Node(8)
    ll.inserts(4)
    
    
    ll.inserts(7)
    print(ll.includes(8))
    print(ll)
    


    
    
    
    

