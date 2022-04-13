


class Node :
    def __init__(self , value) :
        self.value =value
        self.left =None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root =None


    def pre_order(self):
        """
        input == > None
        doing == > Traverse the tree by looking to root then left of root , then right of root
        Output == > print values of nodes Tree with pre_order ==>(root , left , right)
        """
        print ("-----pre_order-----")  # just to seperate between the outputs of the methods
        node =self.root
        list1 =[]
        def _walk(node):
        
            
            list1.append(node.value)

            if node.left :
                _walk(node.left)
            
            if node.right :
                _walk(node.right)

        _walk(node)
        return list1
        

    def in_order(self):
        """
        Input : None
        doing: Traverse the tree by by looking (left ,root , right)
        Output :Print the nodes value of the tree in this order(left , root , right)
        """
        print ("-----in_order-----")  # just to seperate between the outputs of the methods
        list2=[]
        node = self.root
        def _build(node):
            if node.left :
                 _build(node.left)
            
            list2.append (node.value)

            if node.right:
                _build(node.right) 

            
                 
        _build(node) 
        return list2 
       

    def post_order(self):
        """
        Input : None
        doing : Traverse the tree by looking left , right then to the  root
        Output ==> print the nodes values of tre in post order (left , right , node)
        """
        print ("-----post_order-----")  # just to seperate between the outputs of the methods
        list3=[]
        node = self.root
        def _traverse(node):
            if node.left:
                _traverse(node.left)
            if node.right:
                _traverse(node.right)

            list3.append(node.value)
            

        _traverse(node)
        return list3

class Binary_Search_Tree(BinaryTree):
    # def __init__(self, fname, lname, year):
    # super().__init__(fname, lname)
    # self.graduationyear = year
    


    def add_child (self,value):
        
        

        if value < .value :
            if node.left :
                node.left.add_child(value)

            else :
                node.left = value

        elif value > node.value :
            if node.right :
                node.right.add_child(value)

            else :
                node.right = value
  
        
# def build_tree(elements):
#     root =Binary_Search_Tree()
#     for i in range(1,len(elements)):
#         root.add_child(elements[i])

#     return root 


if __name__ =="__main__":
    node1=Node(1)
    node2=Node(2)
    node1.left=node2
    
    node3=Node(3)
    node1.right=node3
    node4=Node(4)
    node2.left=node4

    # numbers = [2,4,5,1,2,8,345,2,6]
    # numbers_tree = build_tree(numbers)
    

    tree = BinaryTree()
    tree.root=node1
    print(tree.in_order())
    # print(tree.pre_order())
    # print(tree.post_order())

    tree1=Binary_Search_Tree()
    tree1.root=node1
    tree1.add_child(7)