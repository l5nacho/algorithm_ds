
CAPACITY = 10

# Maximum heap (root node será el mayor)
class Heap:
    def __init__(self):
        self.size = 0
        self.heap = [0] * CAPACITY

    def insert(self, item):

        if self.size >= CAPACITY:
            return None

        self.heap[self.size] = item
        self.size += 1

        # Check heap properties

        self.fix_heap(self.size - 1)
