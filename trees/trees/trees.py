
class Binary_Tree:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None 

    def add_child (self,value):
        if value == self.value :
            return
        if value < self.value :
            if self.left :
                self.left.add_child(value)

            else :
                self.left = Binary_Tree(value)

        if value > self.value :
            if self.right :
                self.right.add_child(value)

            else :
                self.right = Binary_Tree(value)

    def in_order (self):
        elements = []
        #traverse left subtree
        if self.left:
            elements+=self.left.in_order()

        # base node 
        elements.append(self.value)

        if self.right:
            elements+=self.right.in_order()

        return elements


    def pre_order (self):
        elements = []

         # base node 
        elements.append(self.value)
        #traverse left subtree
        if self.left:
            elements+=self.left.in_order()

       

        if self.right:
            elements+=self.right.in_order()

        return elements

    def post_order (self):
        elements = []

         
        #traverse left subtree
        if self.left:
            elements+=self.left.in_order()

       

        if self.right:
            elements+=self.right.in_order()

        # base node 
        elements.append(self.value)

        return elements



def build_tree(elements):
    root =Binary_Tree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root 


if __name__ == "__main__":
    numbers = [2,4,5,1,2,8,345,2,6]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order())
    print(numbers_tree.pre_order())
    print(numbers_tree.post_order())



















































# class TreeNode:
#     def __init__(self,value):
#         self.value=value
#         self.children =[]
#         self.parent = None


#     def add_children(self,child):
#         child.parent =self
#         self.children.append(child)

#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level +=1
#             p = p.parent

#         return level



#     def  __str__(self):
#         # if self.parent :
            
#         #     spaces = " " * self.get_level()
#         #     print(spaces + "|--"+ self.value)
#         # else :
#         #     spaces = " " * self.get_level()
#         #     print(spaces + self.value)
#         spaces = " " * self.get_level()*3
#         prefix = spaces + "|__" if self.parent else ""
#         print (prefix + self.value)
        
        
#         if self.children:

#             for child in self.children:
#                 child.__str__()
            
        


# def build_tree():
#     root = TreeNode("Electronics")

#     laptop = TreeNode("Laptop")
#     laptop.add_children(TreeNode("Dell1"))
#     laptop.add_children(TreeNode("Dell2"))

#     Tv =TreeNode("Tv")
#     Tv.add_children(TreeNode("Tv1"))
#     Tv.add_children(TreeNode("Tv2"))

#     root.add_children(laptop)
#     root.add_children(Tv)

#     return root


# if __name__=="__main__":
    
#     root=build_tree()
#     root.get_level()
#     root.__str__()

 