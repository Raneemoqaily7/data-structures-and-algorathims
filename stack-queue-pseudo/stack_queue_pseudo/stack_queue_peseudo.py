from inspect import stack
import queue


class Node :
    def __init__(self,value=None,next=None):
      self.value =value
      self.next=next


class Stack:
    def __init__(self):
        self.top =None
        




    

    def push (self,new_value):
        """
        push function takes new_value as argument 
        add a node with the new value of the top of the stack
        """
        node =Node(new_value)
        node.next=self.top
        self.top =node

    def pop (self) :

        """
        pop function takes no argument 
        returns the value of node from the top of the stack
         and Removes the node from the top 
         and raise Exception when stack is Empty
        
        """
        if self.top is None:
            raise Exception ("Empty Stack")

        #[1,2,3]
        else:
            temp = self.top
            self.top =self.top.next
            temp.next=None
            return temp.value
            
        
    def peek(self):

        """
        peek function takes no argument
        return the value of the top of the stack
        raise exception when stack is empty 
        """
        if self.top is None :
            raise Exception ("Empty Stack")

        else :
            temp =self.top
            return temp.value

    def is_empty(self):

        """
        is empty function takes no argument
        return True if the stack is empty 
        otherwise return false 
        
        """
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
                        output+=f'{current.value} -->'
                        
                        current=current.next
                    return output
class Queue:
    def __init__(self):
        self.front =None
        self.rear =None 

    def enqueue(self ,new_value):
        """
        enqueue function takes new value as argument 
        and add node with the new value to the rear of the queue 
        
        """
        node = Node (new_value)
        if self.front is None:
            self.front= node
            return

        current=self.front
        while current.next is not None:

            current =current.next
        current.next =node
        return

    

#1,2,3,4
            
    def dequeue(self):
        """
        dequeue function takes non argument 
        returns the value from node from the front of the queue
         and Removes the node from the front of the queue
         and raise Exception when queue is Empty
        
        """
        if self.front is None:
            raise Exception ("Invalid Dequeue , Queue is Empty")

        else:
            temp =self.front
            self.front =self.front.next
            return temp.value


    def peek (self):
        """
        peek function takes no argument
        return the value of the front of queue 
        raise exception when queue is empty 
        """
        if self.front is None :
            raise Exception ("Queue is Empty")

        else : 
            temp = self.front
            return temp.value

    def is_empty(self):
        """
        is empty function takes no argument
        return True if the queue is empty 
        otherwise return false 
        
        """
        if self.front is None :
            return True 

        return False 

    def __str__(self):
        if self.front is None:
            return "Empty Qeue"


        else  :
            current=self.front
            output =""
            while current is not None :
                output+=f'{current.value} --'
                
                current=current.next
            return output

class Pseudo_queue:

        def __init__(self):
            self.s1=Stack()
            self.s2=Stack()


        def enqueue(self,x):
            """
            enqueue function takes value as Argument

            and Inserts value into the PseudoQueue, using a first-in, first-out approach
            """
            
            self.s1.push(x)



            #    self.s2.push(self.s1.pop())



        def dequeue (self):
            """
            dequeue function takes no argument 

            dequeue  Eetracts a value from the PseudoQueue, using a first-in, first-out approach.h
            
            """

            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())

            return self.s2.pop()
           
        
        def __str__(self):
                    if self.s1.top is None:
                        return "Empty Stack"

                    
                    else  :
                        current=self.s1.top
                        output =""
                        while current is not None :
                            output+=f'{current.value} -->'
                            
                            current=current.next
                        return output
        

           




                
        


    


    
        









if __name__=="__main__":

    stack=Stack()
    stack.push("HELLO")
    stack.push("b")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    # print(stack.is_empty())
    # print(stack.pop())
    # print(stack)
    # print(stack.peek())
    queue=Queue()
    queue.enqueue("hello")
    queue.enqueue("python")
    queue.enqueue("world")
    # queue.enqueue(2)
    # print(queue.dequeue())
    # print(queue.peek())

    # print(queue)
    pesudo=Pseudo_queue()
    pesudo.enqueue(20)
    pesudo.enqueue(15)
    pesudo.enqueue(10)
    pesudo.enqueue(5)
    print(pesudo.dequeue())
    print(pesudo)

   