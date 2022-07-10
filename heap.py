
CAPACITY = 10

# Maximum heap (root node será el mayor)
class Heap:
    def __init__(self):

        """
        Size también representa el indice del heap.
        Heap tiene estructura de arbol pero también se puede
        representar como un array con indice
        """
        self.size = 0
        self.heap = [0] * CAPACITY

    def insert(self, item):

        if self.size >= CAPACITY:
            return None

        self.heap[self.size] = item
        self.size += 1

        # Check heap properties.
        # Se mira el elemento anterior. (size - 1)

        self.fix_heap_up(self.size - 1)

    def fix_heap_up(self, index):

        """
        Cada elemento del heap tiene dos hijos, el valor del indice de
        cada hijo se calcula de la siguiente manera:
        Hijo izquierdo -> (indice * 2) + 1
        Hijo derecho -> (indice * 2) + 2
        Para buscar el indice del padre del nodo, hay que hacer la operacion
        inversa al hijo izquierdo y hacer integer division
        """

        parent_index = (index - 1) // 2

        # Revisamos el heap desde el indice hasta el nodo root para ver si se han violado las
        # reglas del heap.
        # Si uno de los elementos es mayor que el padre, se cambian para respetar las reglas.

        if index.size > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_heap_up(parent_index)
