from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        visited = [] # Declare a list of booleans to check the visited vertices
        count = -1
        for v in self._vertices:
            visited.append(False)   # For now, no vertices have been visited
            count += 1
            if v.__eq__(start): # If this vertex is the one we start at, we save it and its index in the visited list
                vertex = v
                c = count
        order = self.DFS(vertex, end, c, visited)   # Perform a DFS search to traverse the subgraph
        # print(order)
        # ¿Y si llamásemos a la función varias veces con sus adjacent q no sean el q está primero?
        num = -1
        for v in order:
            num += 1
            if v.__eq__(end):
                return num

    def DFS(self, vertex, end, c, visited: list):
        "Performs a DFS search of the indicated subgraph"
        order = []  # Declare the list that will contain the DFS
        return self.dfs(vertex, end, c, visited, order)

    def dfs(self, vertex, end, c, visited, order):
        # Otra opción es buscar una condición que ponerle a un nodo para que se considere visitado
        visited[c] = True
        # print(vertex)
        order.append(vertex)    # As we visit the node, we append it to our list
        # print(order)
        for v in self.getAdjacents(vertex):
            count = -1
            for x in self._vertices:
                count += 1
                if x.__eq__(v):
                    c = count
            if visited[c] == False: # como ignora los vertices q ya ha visitado, si hay una ruta alternativa mas corta no la considera
                self.dfs(v, end, c, visited, order)
            else:
                ... # Creo q aquí falta alguna linea hdp, o tal vez un poco mas arriba
            # O bien metemos más en la lista y luego vemos cuando se repite la q estamos buscando y de alguna manera restamos
            # o intentamos vaciar la lista cuando vuelva a aparecer end, el problema es q no hay forma de llegar (o al menos yo no la encuentro)

        return order

    def getAdjacents(self, vertex) -> list:
        ads = []
        for v in self._vertices:
            # All vertices adjacent to vertex will be appended to the list
            if self.contain_edge(vertex, v):    # We append it if the graph contains the edge that unites them
                ads.append(v)
        return ads


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

vert = ['A', 'B', 'C', 'D', 'E']
dg = Graph2(vert)
dg.add_edge('A', 'C')
dg.add_edge('A', 'D')  # A->D
dg.add_edge('B', 'A')  # B->A
dg.add_edge('C', 'B')  # C->B
dg.add_edge('C', 'D')  # C->D
dg.add_edge('E', 'A')  # E->A

print(dg)
dg.transpose()
print(dg)
num = dg.min_number_edges('A', 'E')
print(num)