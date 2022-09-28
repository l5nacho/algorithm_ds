
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
    # Nodos en la representacion del arbol
    def __init__(self, rank, node_id, parent=None):

        self.rank = rank
        self.node_id = node_id
        self.parent = parent

class DisjointSet:

    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        #Lista de los representantes
        self.root_nodes = []
        self.make_sets()

    def find(self, node):

        current_node = node

        # Iteramos hasta llegar al representante (root node)
        while current_node.parent is not None:
            current_node = current_node.parent

        # Aplicamos path compression
        # Asignamos el current node a la variable root
        # Volvemos a asignar current_node a node
        root = current_node
        current_node = node

        # Todos los nodos tienen que apuntar al root (path compression)
        while current_node is not root:
            temp = current_node.parent
            current_node.parent = root
            current_node = temp







    def make_sets(self):

        for v in self.vertex_list:
            node = Node(0, len(self.root_nodes))
            v.node = node
            self.root_nodes.append(node)

