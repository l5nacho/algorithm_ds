import sys

class DijkstraAlgorithm:

    def __init__(self, adjacency_matrix, start_vertex):
        self.adjacency_matrix = adjacency_matrix
        self.start_vertex = start_vertex
        self.v = len(adjacency_matrix)
        self.visited = [False for _ in range(len(adjacency_matrix))]
        self.distances = [float('inf') for _ in range(len(adjacency_matrix))]
        self.distance[start_vertex] = 0

    def get_min_vertex(self):

        # Busca el vertex con la menor distancia
        min_vertex_value = sys.maxsize
        min_vertex_index = 0

        for index in range(v):
            if not self.visited[index] and self.distances[index] < min_vertex_value:
                min_vertex_index = self.distances[index]
                min_vertex_index = index

        return min_vertex_index



