from graph.graph import Vertex ,Graph 




def test_add_node_to_the_graph ():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    
    

    actual=graph.__str__()
    expected = "1 -> [] ,2 -> [] ,3 -> [] ,"

    assert actual == expected




def test_add_edge_to_the_graph ():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    

    actual=graph.__str__()
    expected = "1 -> [2, 3] ,2 -> [1, 3] ,3 -> [2, 1] ,"

    assert actual == expected





def test_get_neighbors ():

    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
   
    actual = graph.get_neighbors(1)
    expected = [2, 3]
    assert actual == expected




def test_retrieve ():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)

    actual =graph.get_nodes()
    expected = {1, 2, 3}
    assert actual == expected





def  test_graph_with_only_one_node():
    graph = Graph()
    graph.add_node(1)


    actual=graph.__str__()
    expected = "1 -> [] ,"

    assert actual == expected

def test_empty_graph():
    graph = Graph()
    actual = graph.__str__()
    expected = ""
    assert actual == expected


def test_size():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)

    actual = graph.size()
    expected = 3
    assert actual == expected

def test_weight():

    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    
    graph.add_edge(1, 2 ,5)
    graph.add_edge(2, 3 ,6)
    graph.add_edge(3, 1 ,4)

    actual = graph.__str__()
    expected ="1 -> [(2, 5), (3, 4)] ,2 -> [(1, 5), (3, 6)] ,3 -> [(2, 6), (1, 4)] ,"
    assert actual == expected
