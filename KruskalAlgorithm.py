
class Vertex:

    def __init__(self, name):
        self.name = name
        # Representacion del nodo en el disjoint set
        self.node = None

class Edge:

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

    # El algoritmo de kruskal ordena los pesos de los edges
    def __lt__(self, other_edge):
        return self.weight < other_edge.weight

class Node:

    def __init__(self, rank, node_id, parent):

        self.rank = rank
        self.node_id = node_id
        self.parent = parent
