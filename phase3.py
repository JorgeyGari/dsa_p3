from graph import Graph


class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        ...

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        if self._directed:  # If the graph is undirected, we don't need to do anything
            edges = []  # Here we will store every edge
            for v in self._vertices:
                adj = []  # Here we will store the neighbors (adjacent vertices) of each vertex

                for w in self._vertices[v]:
                    adj.append(w)  # Stores every vertex w with a node of the form v -> w (w is adjacent to v)

                for w in adj:
                    self.remove_edge(v, w.vertex)  # Remove every edge
                    edges.append([w.vertex, v])  # ...and store it in the reverse order

            for e in edges:
                self.add_edge(e[0], e[1])  # Once we have deleted all edges, we can add them back (reversed)

        return self

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        ...


# Testing zone
labels = ['A', 'B', 'C', 'D', 'E']

g = Graph2(labels)

g.add_edge('A', 'C')  # A->C
g.add_edge('A', 'D')  # A->D
g.add_edge('B', 'A')  # B->A
g.add_edge('C', 'B')  # C->B
g.add_edge('C', 'D')  # C->D
g.add_edge('E', 'A')  # E->A

print(g)
g.transpose()
print(g)
