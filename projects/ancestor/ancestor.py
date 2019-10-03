from graph import Graph
from util import Queue, Stack

# APPROACH #1
# BRUTE FORCE, WORKS
# (does DFS from each vertex in Graph, returns longest path to starting_node)
# def earliest_ancestor(ancestors, starting_node):
#     ancestor_graph = Graph()

#     for i in ancestors:
#         for j in i:
#             ancestor_graph.add_vertex(j)

#     for i in ancestors:
#         ancestor_graph.add_edge(i[0], i[1])

#     longest_ancestor = []

#     for i in ancestor_graph.vertices:
#         temp_longest = ancestor_graph.dfs(i, starting_node)
#         if temp_longest[0] is not None:
#             if len(temp_longest) > len(longest_ancestor):
#                 longest_ancestor = temp_longest
#             elif len(temp_longest) == len(longest_ancestor):
#                 if temp_longest[0] < longest_ancestor[0]:
#                     longest_ancestor = temp_longest        
    
#     return longest_ancestor[0]



# APPROACH #2
# flips direction of graph
# then DFT to find all paths   
def earliest_ancestor(ancestors, starting_node):
    ancestor_graph = Graph()

    for i in ancestors:
        # Flip direction on each edge
        ancestors[ancestors.index(i)] = (i[1], i[0])

    # add all vertices
    for i in ancestors:
        for j in i:
            ancestor_graph.add_vertex(j)

    # add all edges
    for i in ancestors:
        ancestor_graph.add_edge(i[0], i[1])

    # set up list of potential paths
    potential_paths = []
    potential_paths.append([starting_node])

    # stack for DFT
    stack = Stack()
    stack.push(starting_node)
    while stack.size() > 0:
        temp_vertex = stack.pop()

        for i in ancestor_graph.vertices[temp_vertex]:
            stack.push(i)

            # If the previous vertex in a potential path matches the curent temp_vertex
            # Add a new, longer list for each "child" of that vertex (actually parent from original graph, since we flipped it)
            for path in potential_paths:
                if path[-1] == temp_vertex:
                    potential_paths.append([*path, i])

    # get length of longest paths
    max_path_length = len(max(potential_paths, key=len))
    # create list of the final vertex of all paths that are the longest
    longest_paths_end_vertex = [x[-1] for x in potential_paths if len(x) == max_path_length]
    # return the lowest vertex of all longest paths
    return min(longest_paths_end_vertex)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 6))