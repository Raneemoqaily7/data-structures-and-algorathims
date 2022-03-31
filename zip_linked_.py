class Node :                                                     
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

                             
class LinkedList:
    def __init__(self,next=None):
        self.head=None
        self.next=next

        
def merge_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # create dummy node to avoid additional checks in loop
    s = t = node() 
    while not (head1 is None or head2 is None):
        if head1.value < head2.value:
            # remember current low-node
            c = head1
            # follow ->next
            head1 = head1.next
        else:
            # remember current low-node
            c = head2
            # follow ->next
            head2 = head2.next

        # only mutate the node AFTER we have followed ->next
        t.next = c          
        # and make sure we also advance the temp
        t = t.next

    t.next = head1 or head2

    # return tail of dummy node
    return s.next
if __name__ == "__main__":
    list=LinkedList()
    
    list.push(1)
    list.push(2)
    list.push(3)
    list.push(4)
    print(list)
    list.getKthNode(list,3)