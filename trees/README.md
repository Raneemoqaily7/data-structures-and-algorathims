# Trees

**Node** - A Tree node is a component which may contain its own values, and references to other nodes
**Root** - The root is the node at the beginning of the tree
**K** - A number that specifies the maximum number of children any node may have in a k-ary tree. In a binary tree, k = 2.
**Left** - A reference to one child node, in a binary tree
**Right** - A reference to the other child node, in a binary tree
**Edge** - The edge in a tree is the link between a parent and child node
**Leaf**- A leaf is a node that does not have any children
**Height** - The height of a tree is the number of edges from the root to the furthest leaf

## Challenge
- Create a Binary Tree class and Node class
- Define a method for each of the depth first traversals: pre order , in order ,post order


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
-   in_order == > Big O space log (n)
-   post_order ==> Big O space log (n)
-   pre_order  ==>Big O space log (n)

- Add ==>O(n)
- Containes == > O(n)

## API
<!-- Description of each method publicly available in each of your trees -->
-   in_order == > Traverse the tree in the order   left ,root,right
-   post_order ==> Traverse the tree in the order   left ,right ,root
-   pre_order  ==>Traverse the tree in the order   root ,left ,right 

- Add ==> Adds a new node with that value in the correct location in the binary search tree.
- Containes ==> Returns: boolean indicating whether or not the value is in the tree at least once.
       

       