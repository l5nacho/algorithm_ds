
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
        print(self.size)

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
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_heap_up(parent_index)

    def get_max(self):
        """
        El valor más alto del heap es siempre el mayor en los max heap
        """
        return self.heap[0]

    def poll(self):
        """
        Devuelve el maximo (heap[0]) y lo borra -> lo cambia por el menor valor
        Luego hay que heapify el heap, es decir recorrer el arbol hacia abajo
        para comprobar que las reglas no se han roto
        """

        max_item = self.get_max()

        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        self.size -= 1

        # heapify
        self.heap_fix_down(0)

        # Devolvemos el valor que era el máximo, esto nos sirve para algunas operaciones como
        # ordenar un array
        return max_item

    def heap_fix_down(self, index):

        """
        Recursivamente mira el heap hacia abajo y cambia las referencias si
        el heap no cumpliese las reglas (en el caso de un Maximum Heap) que los hijos
        siempre sean menores que el padre
        """

        left_index = 2 * index + 1
        right_index = 2 * index + 2

        largest_index = index

        # Miramos si el left_child es mayor que el padre (no sería un heap valido)
        # si lo es, asignamos largest index a este para cambiarlo

        if left_index < self.size and self.heap[left_index] > self.heap[largest_index]:
            largest_index = left_index

        # Ahora comparamos el right_child contra el largest_index (puede haberse asignado el
        # left_index o no) si es mayor asignamos right_index al largest_index
        if right_index < self.size and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index

        # Comprobamos si el index es igual al largest_index, si no lo es, es que el heap no
        # era valido y tenemos que modificar las referencias y seguir comprobando recursivamente

        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.heap_fix_down(largest_index)

    def heap_sort(self):
        sorted_heap = []

        for _ in range(self.size):
            max_item = self.poll()
            sorted_heap.append(str(max_item))

        return ' -> '.join(sorted_heap)

if __name__ == '__main__':
    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)

    print(heap.heap)
    print(heap.heap_sort())
