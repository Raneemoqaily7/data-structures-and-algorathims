

class Vertex:
  
    def __init__(self, value):
        self.value = value
        self.edges = []


class Graph:
    def __init__(self):
        self.adjacency_list = {}


    def add_node(self, value):
        '''
        Arguments: value
        Returns: The added node
        Add a node to the grap
                '''
        new_vertex = Vertex(value)
        self.adjacency_list[value] = new_vertex
        return new_vertex



 
    def get_nodes(self):
        
        '''
        Arguments: none
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        '''

        return self._adjacency_list.keys()


    
    def get_neighbors(self, vertex):
        '''
        Arguments: node
        Returns a collection of edges connected to the given node
        Include the weight of the connection in the returned collection
        '''
        return self.adjacency_list[vertex].edges


    def size(self):


        '''
       Arguments: none
        Returns the total number of nodes in the graph
        '''
        return len(self.adjacency_list)


    

    def __str__(self):
       
     
        output = ''
        for key in self.adjacency_list:
            output += f'{key} -> {self.adjacency_list[key].edges}  ,    '
        return  output
    




    
    def add_edge(self, vertex1, vertex2, weight=None):
        
        if vertex1 not in self.adjacency_list:
            self.add_node(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_node(vertex2)
        if weight is None:
            self.adjacency_list[vertex1].edges.append(vertex2)
            self.adjacency_list[vertex2].edges.append(vertex1)
        else:
            self.adjacency_list[vertex1].edges.append((vertex2, weight))
            self.adjacency_list[vertex2].edges.append((vertex1, weight))







if __name__ == '__main__':
    graph = Graph()
    graph.add_node(1)
    graph.add_node(4)
    graph.add_node(7)
    graph.add_node(4)
    graph.add_edge(1, 5)
    graph.add_edge(1, 2)
    graph.add_edge(4, 7)
    graph.add_edge(7, 1)
   
    print(graph)


