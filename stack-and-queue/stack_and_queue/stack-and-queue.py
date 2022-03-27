from inspect import stack


class Node :
    def __init__(self,value=None,next=None):
      self.value =value
      self.next=next


class Stack:
    def __init__(self):
        self.top =None
    

    def push (self,new_value):
        node =Node(new_value)
        node.next=self.top
        self.top =node

    def pop (self) :
        if self.top is None:
            raise Exception ("Empty Stack")

        #[1,2,3]
        else:
            temp = self.top
            self.top =self.top.next
            temp.next=None
            return temp.value
            
        
    def peek(self):
        if self.top is None :
            raise Exception ("Empty Stack")

        else :
            temp =self.top
            return temp.value

    def is_empty(self):
        if self.top ==None:
            return True
        
        return False



    def __str__(self):
        if self.top is None:
            return "Empty Stack"

        
        else  :
            current=self.top
            output =""
            while current is not None :
                output+=f'{current.value} --'
                
                current=current.next
            return output

    
        









if __name__=="__main__":

    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peek())
   


    