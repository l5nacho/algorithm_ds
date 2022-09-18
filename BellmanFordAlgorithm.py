
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
