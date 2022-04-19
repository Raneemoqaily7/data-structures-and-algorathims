class QNode:
    def __init__(self,value=None,next=None):
      self.value =value
      self.next=next

class Queue:
    def __init__(self):
        self.front =None
        self.rear =None 

    def enqueue(self ,new_value):
        """
        enqueue function takes new value as argument 
        and add node with the new value to the rear of the queue 
        
        """
        node = QNode (new_value)
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

class Node ():
    def __init__(self,value ) :
        self.value =value
        self.right=None
        self.left =None


class BinaryTree :
    def __init__(self):
        self.root =None

    
    def in_order(self):
        """
        Input :None 
        doing : Traverse the tree in the order left ,root,right
        Output : print the node's values in  the in_order (left , root ,right)
        """
        list1=[]
        node = self.root
        def _traverse(node):
           
            if node.left:
                _traverse(node.left)

            list1.append(node.value)

            if node.right:
                _traverse(node.right)

        _traverse(node)
        return list1

    def pre_order(self):
        """
        Input :None 
        doing : Traverse the tree in the order root ,left , right  
        Output : print the node's values in  the in_order ( root ,left ,right)
        """
        list2=[]
        node = self.root
        def _build(node):
            list2.append(node.value)

            if node.left:
                _build(node.left)

            

            if node.right:
                _build(node.right)

        _build(node)
        return list2
    
    def post_order(self):
        """
        Input :None 
        doing : Traverse the tree in the order left , right , root 
        Output : print the node's values in  the in_order (left ,right ,root)
        """
        list3=[]
        node = self.root
        def _build(node):
            

            if node.left:
                _build(node.left)

            

            if node.right:
                _build(node.right)

            list3.append(node.value)

        _build(node)
        return list3


    def find_maximum_value(self):
        """
        Input : None
        doing :Find the maximum value stored in the tree
        Output :number(the max value in the tree)
        
        """
        if self.root is  None:

            raise Exception("tree is Empty !!")
        
        elif self.root.right is None and self.root.left is None:
            return self.root.value

        else:
       
        
        
            node =self.root
            maximum = node.value
            def _traverse(node):
                nonlocal maximum
                if node :
                     max1=node.value

                if max1>maximum:
                    maximum =max1
            
                if node.left:
                    _traverse(node.left)

                

                if node.right:
                    _traverse(node.right)

            _traverse(node)
            return maximum


def breadth_first (tree ):
       
        if tree.root is None :
            raise Exception ("Tree is Empty")


        elif tree.root.left is None and tree.root.right is None :
            return tree.root.value


        else :

            queue =Queue()
            root =tree.root
            queue.enqueue(root)
            list1 =[]
            
            while not queue.is_empty():
                frontNode =queue.dequeue()
                list1.append(frontNode.value)

                if frontNode.left:
                    queue.enqueue(frontNode.left)
                if frontNode.right:
                    queue.enqueue(frontNode.right)
                

            return list1




      




class BinarySearchTree(BinaryTree):
    
        
    def Add(self, value):
        """
        input: value
        doing: add a value in the correct place 
        output: the tree wth the new node with that value in the correct location
        """
         
        current = self.root
        
        while current:

            if current.right and value > current.value:

                current = current.right 

            elif current.left and value < current.value:

                current = current.left
                           
            else:
                if value < current.value  and current.left is None:

                    current.left = Node(value)


                elif  value > current.value  and current.left is None:

                    current.right = Node(value)

                break   


        

    def Contains(self , value):
        
        """
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        """

        current =self.root

        while current is not None:

            if current.value ==value:
                return True

            if value < current.value:
                current=current.left

            if value > current.value:
                current = current.right

        return False



            
      

        





if __name__=="__main__":
    node1=Node(4)
    node2=Node(2)
    node3 =Node(8)
    node4=Node(9)
    node5=Node(89)
    node6=Node(990)
    node7=Node(29)
    node1.left=node2
    node1.right=node3
    node2.left =node5
    node2.right=node6
    node3.right=node4
    node3.left =node7
    
    

    
    tree=BinaryTree()
    tree.root=node1
    print(tree.pre_order())
    print(tree.find_maximum_value())
    
    print(breadth_first(tree))
    # print(tree.pre_order())
    # print(tree.post_order())
    tree1 = BinarySearchTree()
    tree1.root = node1 
    node1=Node(4)
    node2=Node(2)
    node3 =Node(8)
    node4=Node(9)
    node2.left=node4
    node1.left=node2
    node1.right=node3
    
    tree1.Add(9)
    print(tree1.post_order())
#    4
# 2      8     ==> 
    print(tree1.Contains(9))

            






































# class Binary_Tree:
#     def __init__(self,value):
#         self.value = value
#         self.left = None 
#         self.right = None 

#     def add_child (self,value):
#         if value == self.value :
#             return
#         if value < self.value :
#             if self.left :
#                 self.left.add_child(value)

#             else :
#                 self.left = Binary_Tree(value)

#         if value > self.value :
#             if self.right :
#                 self.right.add_child(value)

#             else :
#                 self.right = Binary_Tree(value)

#     def in_order (self):
#         elements = []
#         #traverse left subtree
#         if self.left:
#             elements+=self.left.in_order()

#         # base node 
#         elements.append(self.value)

#         if self.right:
#             elements+=self.right.in_order()

#         return elements


#     def pre_order (self):
#         elements = []

#          # base node 
#         elements.append(self.value)
#         #traverse left subtree
#         if self.left:
#             elements+=self.left.in_order()

       

#         if self.right:
#             elements+=self.right.in_order()

#         return elements

#     def post_order (self):
#         elements = []

         
#         #traverse left subtree
#         if self.left:
#             elements+=self.left.in_order()

       

#         if self.right:
#             elements+=self.right.in_order()

#         # base node 
#         elements.append(self.value)

#         return elements



# def build_tree(elements):
#     root =Binary_Tree(elements[0])
#     for i in range(1,len(elements)):
#         root.add_child(elements[i])

#     return root 


# if __name__ == "__main__":
#     numbers = [2,4,5,1,2,8,345,2,6]
#     numbers_tree = build_tree(numbers)
#     print(numbers_tree.in_order())
#     print(numbers_tree.pre_order())
#     print(numbers_tree.post_order())
#     numbers_tree.add_child(55)



















































# # class TreeNode:
# #     def __init__(self,value):
# #         self.value=value
# #         self.children =[]
# #         self.parent = None


# #     def add_children(self,child):
# #         child.parent =self
# #         self.children.append(child)

    # def get_level(self):
    #     level = 0
    #     p = self.parent
    #     while p:
    #         level +=1
    #         p = p.parent

    #     return level



# #     def  __str__(self):
# #         # if self.parent :
            
# #         #     spaces = " " * self.get_level()
# #         #     print(spaces + "|--"+ self.value)
# #         # else :
# #         #     spaces = " " * self.get_level()
# #         #     print(spaces + self.value)
# #         spaces = " " * self.get_level()*3
# #         prefix = spaces + "|__" if self.parent else ""
# #         print (prefix + self.value)
        
        
# #         if self.children:

# #             for child in self.children:
# #                 child.__str__()
            
        


# # def build_tree():
# #     root = TreeNode("Electronics")

# #     laptop = TreeNode("Laptop")
# #     laptop.add_children(TreeNode("Dell1"))
# #     laptop.add_children(TreeNode("Dell2"))

# #     Tv =TreeNode("Tv")
# #     Tv.add_children(TreeNode("Tv1"))
# #     Tv.add_children(TreeNode("Tv2"))

# #     root.add_children(laptop)
# #     root.add_children(Tv)

# #     return root


# # if __name__=="__main__":
    
# #     root=build_tree()
# #     root.get_level()
# #     root.__str__()

 