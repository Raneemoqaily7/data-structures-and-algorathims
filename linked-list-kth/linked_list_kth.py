class Node :                                                     
    def __init__(self,value,next):
        self.value=value
        self.next=next

                             
class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_value):
        new_node=Node(new_value)
        new_node.next=self.head
        self.head=new_node



    def getKthNode(self,head,position):
        count=0
        if (head ):
            if count == position:
                print (head.value)

            else:
                list.getKthNode(head.next, position-1)
        else :
            print("index doesnt exist")


if __name__ == "__main__":
    list=LinkedList()
    list.push(1)
    list.push(2)
    list.push(3)
    list.push(4)
    list.push(5)
    list.getKthNode(list,3)


  

        