# Graphs
<!-- Short summary or background information -->
Graphs are non-linear data structures made up of two major components:

Vertices – Vertices are entities in a graph. Every vertex has a value associated with it. For example, if we represent a list of cities using a graph, the vertices would represent the cities.

Edges – Edges represent the relationship between the vertices in the graph. Edges may or may not have a value associated with them. For example, if we represent a list of cities using a graph, the edges would represent the path between the cities.

Neighbor - The neighbors of a node are its adjacent nodes, i.e., are connected via an edge.

Degree - The degree of a vertex is the number of edges connected to that vertex.

## Challenge
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

- add node
  - Arguments: value
  - Returns: The added node
  - Add a node to the graph


- add edge
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two nodes in the graph
  - If specified, assign a weight to the edge
  - Both nodes should already be in the Graph


- get nodes
  - Arguments: none
  - Returns all of the nodes in the graph as a collection (set, list, or similar)


- get neighbors
  - Arguments: node
  - Returns a collection of edges connected to the given node
  - Include the weight of the connection in the returned collection


- size
  - Arguments: none
  - Returns the total number of nodes in the graph

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

- add_node -->  Time Complexity :  Big O(1) ,  space Big O(1)
- add_edge --> Time Complexity :Big O(1), space Big O(1)
- get_nodes -->  Time Complexity :Big O(1), space Big O(1)
- get_neighbors --> Time Complexity :Big O(1), space Big O(1)
- size --> Time Complexity : Big O(1), space Big O(1)

## API
<!-- Description of each method publicly available in your Graph -->

- class Vertex():

    A class to creat a vertex
    Input: no input
    
- class Graph():

class to implement Graph object with the given methods:

- add_node():


        Add a node to the graph , Input:  value  ,Output:vertex after added node

- add_edge():

Input: two vertexes to be connected by the edge, weight (optional) ,Returns: nothing ,Adds a new edge between two nodes in the graph
If specified, assign a weight to the edge,  Both nodes should already be in the Graph

Input: two vertexes 
Both nodes should already be in the Graph


get_nodes():

Returns all of the vertexes in the graph as a collection

get_neighbors():

Returns a collection of vertexes connected to the given vertex with the weights of their connections



size():

Returns the total number of nodes in the graph