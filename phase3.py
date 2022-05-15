import sys

from graph import Graph


class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        # Firstly, we check both start and end are in the graph
        error = -1
        for v in self._vertices.keys():
            if v.__eq__(start):
                error = 0
            if v.__eq__(end):
                error = 0
                vertex = v  # Save the vertex of the string end
        if error == -1:
            print("Error: Invalid vertex")
            return -1

        # We perform the Dijkstra algorithm to find the smallest path when all edges have weight 1
        distances = self.dijkstra(start, end)
        mne = distances[vertex]  # We are only interested in the distance from start to end

        return mne

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        if self._directed:  # If the graph is undirected, we don't need to do anything
            edges = []  # Here we will store every edge in the graph

            for v in self._vertices:
                adj = []  # Here we will store the neighbors (adjacent vertices) of each vertex

                for w in self._vertices[v]:
                    adj.append(w)  # Stores every vertex w with a node of the form v -> w (w is adjacent to v)

                for w in adj:
                    self.remove_edge(v, w.vertex)  # Remove every edge...
                    edges.append([w.vertex, v])  # ...and store them in the reverse order

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
        # Simply apply the function min_number_edges() and check if every combination of edges has an actual value...
        for v in self._vertices:
            for w in self._vertices:
                if self.min_number_edges(v, w) == sys.maxsize:  # ...and, if it doesn't...
                    return False  # ...then the graph is not (strongly) connected
        return True  # The graph is (strongly) connected otherwise

    # Auxiliary functions
    def dijkstra(self, start, end) -> dict:
        """ an implementation of the Dijkstra algorithm,
        returns a dictionary containing the shortest distance to each vertex"""
        visited = {}  # Declare a list of booleans to check the visited vertices
        previous = {}  # Declare a list of vertices where we will store the previous node for each node
        distances = {}  # Declare a list of integers where we will store the distances between vertices
        for v in self._vertices.keys():
            visited[v] = False  # For now, no vertices have been visited
            previous[v] = None  # For now, we define the previous vertex for any vertex as None
            distances[v] = sys.maxsize  # We will start with the maximum possible size in all distances (for comparing)
        distances[start] = 0
        below = -1  # To check whether the path we are looking exists

        for v in self._vertices:
            min = sys.maxsize  # To compare with the distances
            for vertex in self._vertices.keys():
                if distances[vertex] <= min and not visited[vertex]:
                    min = distances[vertex]  # Update the new smallest
                    min_vertex = vertex  # Update the index of the smallest
            visited[min_vertex] = True  # Mark the vertex as visited
            for a in self.getAdjacents(min_vertex):
                if a == end:
                    below = 0  # We have to take into account the case where there is no way to get from start to end
                w = 1  # The weight will be always 1
                if not visited[a] and distances[a] > distances[min_vertex]:
                    distances[a] = distances[min_vertex] + w  # Update the distance
                    previous[a] = min_vertex  # Update the previous vertex from where we got the new distance

        # If the end vertex was not visited, we say its distance is 0
        if below == -1:
            distances[end] = 0

        return distances

    def getAdjacents(self, vertex) -> list:
        """ returns a list containing the neighbors of a given vertex"""
        ads = []  # Declare the list
        for v in self._vertices.keys():
            # All vertices adjacent to vertex will be appended to the list
            if self.contain_edge(vertex, v):  # We append it if the graph contains the edge that joins them
                ads.append(v)

        return ads
