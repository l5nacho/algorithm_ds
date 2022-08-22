
class Edge:

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node:

    def __init__(self, name):
        self.name = name
        self.visited = False
        # El nodo de donde viene el path
        self.predecessor = None
        # Lista con los nodos a los que tiene acceso
        self.adjacency_list = []
        # Distancia minima desde el source hasta el nodo
        self.min_distance = float('inf')

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance

