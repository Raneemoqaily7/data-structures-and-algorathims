class Node:
    def __init__(self,value):
        
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def inserts (self,value):
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
        return self.__str__()  



    def includes (self,value):
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
    


    
    
    
    

