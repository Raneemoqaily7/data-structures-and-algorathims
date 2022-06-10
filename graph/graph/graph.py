class Vertex:
  
    def __init__(self, value):
        self.value = value
        self.edges = []


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]


    def add_node(self, value):


        '''
        Arguments: value
        Returns: The added node
        Add a node to the graph
        '''
        new_node = Vertex(value)
        return new_node

        


    def add_edge(self, node1, node2, *wieght):
        '''
        Arguments: 2 nodes to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two nodes in the graph
        If specified, assign a weight to the edge
        Both nodes should already be in the Graph
        '''
        if len(wieght) == 0:
            self.graph[node1][node2] = 1
            self.graph[node2][node1] = 1





    def get_nodes(self):
        '''
        Arguments: none
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        '''
        nodes = set()
        for i in range(self.V):
            nodes.add(self.graph[i])
        return nodes

    

    def __str__(self):
        output = ''
        for i in range(self.V):
            output += f'{self.graph[i]} \n'
        return output



    

if __name__ == '__main__':
    graph = Graph(4)
    graph.add_node(1)
    graph.add_node(0)
    graph.add_node(3)
    graph.add_node(2)
    graph.add_edge(1, 0)
    graph.add_edge(2, 0)
    graph.add_edge(0, 2)
    graph.add_edge(1, 0)
    graph.add_edge(3, 2)
    graph.add_edge(3, 2)
    print(graph)
   