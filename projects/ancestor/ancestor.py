from graph import Graph
from util import Queue

# APPROACH #1
# WORKS
def earliest_ancestor(ancestors, starting_node):
    ancestor_graph = Graph()

    for i in ancestors:
        for j in i:
            ancestor_graph.add_vertex(j)

    for i in ancestors:
        ancestor_graph.add_edge(i[0], i[1])

    longest_ancestor = []

    for i in ancestor_graph.vertices:
        temp_longest = ancestor_graph.dfs(i, starting_node)
        if temp_longest[0] is not None:
            if len(temp_longest) > len(longest_ancestor):
                longest_ancestor = temp_longest
            elif len(temp_longest) == len(longest_ancestor):
                if temp_longest[0] < longest_ancestor[0]:
                    longest_ancestor = temp_longest        
    
    return longest_ancestor[0]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
        
print(earliest_ancestor(test_ancestors, 8))