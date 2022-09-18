
class Vertex:

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.predecessor = None
        self.min_distance = int('inf')

class BellmanFordAlgorithm:

    def __init__(self, vertex_list, edge_list, start_vertex):
        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.start_vertex = start_vertex
        self.has_cycle = False

    def find_shortest_path(self):
        self.start_vertex.min_distance = 0

        # Iteramos n-1 veces sobre cada edge
        for _ in range(len(self.vertex_list) - 1):
            for edge in self.edge_list:
                u = edge.start_vertex
                v = edge.target_vertex

                dist = edge.start_vertex + edge.weight

                if dist < v.min_distance:

                    v.min_distance = dist
                    v.predecessor = u

        for edge in self.edge_list:
            if self.check_ciclo(edge):
                print('Detectado ciclo negativo')
                return None

    def check_cicle(self, edge):
        if edge.start_vertex + edge.weight < edge.target_vertex:
            self.has_cycle = True
            return True
        else:
            return False

    def get_shortest_path(self, vertex):

        node_list = []
        if not self.has_cycle:
            print(f'El camino más corto al vertex {vertex.name} tiene {vertex.min_distance} pasos')
            node = vertex

            while node is not None:
                node_list.append(node.name)
                node = node.predecessor

        else:
            print('ERROR: Hay un ciclo negativo')

