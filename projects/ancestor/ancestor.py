from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    ancestor_graph = Graph()

    ''' This code has only one outer loop, but feels more readable '''
    # for i in ancestors:
    #     for j in i:
    #         if j not in ancestor_graph.vertices:
    #             ancestor_graph.add_vertex(j)
    #         ancestor_graph.add_edge(i[0], i[1])

    ''' More readaable but two loops '''
    # ancestors is a list of tuples
    for i in ancestors:
        for j in i:
            ancestor_graph.add_vertex(j)

    for i in ancestors:
        ancestor_graph.add_edge(i[0], i[1])

    print(ancestor_graph.vertices)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
        
earliest_ancestor(test_ancestors, 1)