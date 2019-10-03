"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            return None
        elif v2 not in self.vertices:
            return None
        else:
            self.vertices[v1].add(v2)

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited_vertices = [starting_vertex]

        while queue.size() > 0:
            temp_vertex = queue.dequeue()
            print(temp_vertex)
            
            for i in self.vertices[temp_vertex]:
                if i not in visited_vertices:
                    queue.enqueue(i)
                    visited_vertices.append(i)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited_vertices = [starting_vertex]

        while stack.size() > 0:
            temp_vertex = stack.pop()
            print(temp_vertex)

            for i in self.vertices[temp_vertex]:
                if i not in visited_vertices:
                    stack.push(i)
                    visited_vertices.append(i)


    def dft_recursive_util(self, v, visited):
        # this works because we're passing the pointer to the list (array)
        # not the array itself
        # so every time something is added to the Visited list
        # all recursive instances have access to it
        print(v)
        visited.append(v)
        for i in self.vertices[v]:
            if i not in visited:
                self.dft_recursive_util(i, visited)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        self.dft_recursive_util(starting_vertex, [])


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        potential_paths = []
        potential_paths.append([starting_vertex])

        queue = Queue()
        queue.enqueue(starting_vertex)
        visited_vertices = [starting_vertex]
        


        while queue.size() > 0:
            temp_vertex = queue.dequeue()
            # print(temp_vertex)
            
            for i in self.vertices[temp_vertex]:
                if i not in visited_vertices:
                    queue.enqueue(i)

                    for path in potential_paths:
                        # print(path)
                        if path[-1] == temp_vertex:
                            potential_paths.append([*path, i])

                    visited_vertices.append(i)

        potential_answers = []

        for path in potential_paths:
            if path[0] == starting_vertex and path[-1] == destination_vertex:
                potential_answers.append(path)

        return min(potential_answers, key=len)
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        potential_paths = []
        potential_paths.append([starting_vertex])

        stack = Stack()
        stack.push(starting_vertex)
        visited_vertices = [starting_vertex]

        while stack.size() > 0:
            temp_vertex = stack.pop()

            for i in self.vertices[temp_vertex]:
                if i not in visited_vertices:
                    stack.push(i)

                    for path in potential_paths:
                        if path[-1] == temp_vertex:
                            potential_paths.append([*path, i])
                    
                    visited_vertices.append(i)

        potential_answers = []

        for path in potential_paths:
            if path[0] == starting_vertex and path[-1] == destination_vertex:
                potential_answers.append(path)

        return min(potential_answers, key=len)




# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_edge(5, 3)
#     graph.add_edge(6, 3)
#     graph.add_edge(7, 1)
#     graph.add_edge(4, 7)
#     graph.add_edge(1, 2)
#     graph.add_edge(7, 6)
#     graph.add_edge(2, 4)
#     graph.add_edge(3, 5)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 6)

#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
#     print(graph.vertices)

#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
#     print("depth first")
#     graph.dft(1)

#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
#     print("breadth first")
#     graph.bft(1)

#     '''
#     Valid DFT recursive paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
#     print("dft recurisve")
#     graph.dft_recursive(1)
#     # print("dft recursive done")
#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
#     print("bfs search path")
#     print(graph.bfs(1, 6))

#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
#     print("dfs search path")
#     print(graph.dfs(1, 6))
