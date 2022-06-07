class Hashmap(object):
   
    def __init__(self,size = 1024):
        self.size = size
        self.map = [None] * size

    def hash(self,key):
        """
        hash(self, key): method that takes a key and returns the index of that key in the map.

        """
        
        
        sum_ascii_value = 0
        for char in key:
            char_value =  ord(char)
            sum_ascii_value += char_value
        sum_ascii_value = (sum_ascii_value*19) % self.size
        return sum_ascii_value

    def set(self,key,value):
       
        
        
            
        index = self.hash(key)
        
        

        if self.map[index]:
            if key in self.keys():
                for dic in self.map[index]:
                    if key in dic.keys():
                        dic[key] = value
            else:
                self.map[index].append({f"{key}":f"{value}"})
        else:
            self.map[index] = [{f"{key}":f"{value}"}]        
                            
    def get(self,key):
      
        
        
        index = self.hash(key)
        
        if not self.map[index]:
            return None
        
        for dic in self.map[index]:
            if key in dic.keys():
                return dic[key]
   
    def contains(self,key):
        
        
        index = self.hash(key)
        
        if not self.map[index]:
            return False
        
        for dic in self.map[index]:
            if key in dic.keys():
                return True
            return False
     
    def keys(self):
      
        keys = []
        for index in self.map :
            if index:
                for dic in index:
                        [keys.append(key) for key in dic.keys()]
                        
        return keys


def tree_intersection(tree1,tree2):
  
   
    
     
    hash= Hashmap()
    
    def tree_traversal(root1,root2):
        
        if root1.value == root2.value:
            hash.set(str(root1.value), None)
              
        if root1.right and root2.right:
            tree_traversal(root1.right,root2.right)
             
        if root1.left and root2.left:
            tree_traversal(root1.left,root2.left)
            
            
    tree_traversal(tree1.root,tree2.root)
    
    return set(hash.keys())

class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None


if __name__ == '__main__':
    tree1 = BinaryTree()
    node1= TNode(150)
    tree1.root = node1
    node1.left= TNode(5)
    node1.right= TNode(20)
    node1.right.left= TNode(600)
    node1.right.right= TNode(350)
    node1.left.right= TNode(160)
    node1.left.left= TNode(89)
    node1.right.right.right= TNode(980)
    node1.right.right.left= TNode(300)
    node1.left.right.right= TNode(65)
    node1.left.right.left= TNode(8)

    tree2 = BinaryTree()
    node2= TNode(42)
    tree2.root= node2	
    node2.left= TNode(500)
    node2.right= TNode(0)
    node2.right.left= TNode(600)
    node2.right.right= TNode(350)
    node2.left.right= TNode(160)
    node2.left.left= TNode(15)
    node2.right.right.right= TNode(980)
    node2.right.right.left= TNode(4)
    node2.left.right.right= TNode(65)
    node2.left.right.left= TNode(8)

    tree1 = BinaryTree()
    tree1.root = TNode(65)
    tree1.root.right = TNode(15)
    tree1.root.left = TNode(90)
    tree1.root.left.left = TNode(98)
    tree1.root.right.left = TNode(70)


    tree2= BinaryTree()
    tree2.root = TNode(65)
    tree2.root.right = TNode(20)
    tree2.root.left = TNode(90)
    tree2.root.left.left = TNode(98)
    tree2.root.right.left = TNode(70)

    print(tree_intersection(tree1,tree2))