class Color:
    RED = 1
    BLACK = 2

class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left_node = None
        self.right_node = None
        self.color = Color.RED

    def __repr__(self):
        return str(self.data)

class RBTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            self.settle_violation(self.root)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):

        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)

            else:
                node.left_node = Node(data, parent=node)
                self.settle_violation(node.left_node)

        if data > node.data:
            if node.right_node:
                self.insert_node(data, node.right_node)

            else:
                node.right_node = Node(data, parent=node)
                self.settle_violation(node.right_node)
                
    def traverse(self):

        if self.root is None:
            return None

        else:
            return self.traverse_in_order(self.root)

    def traverse_in_order(self, node):

        if node.left_node:
            self.traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)

    def iterate(self):
        queue = [self.root]
        lista = []

        while queue:
            l = queue.pop(0)
            lista.append(str(l.data))

            if l.left_node:
                queue.append(l.left_node)
            if l.right_node:
                queue.append(l.right_node)

        return ' -> '.join(lista)

    def rotate_right(self, node):

        """Vamos modificando los punteros para hacer la rotacion

                   node             temp_left_node
                   / \                 / \
                  /   \               /   \
                 /     \             /     \
     temp_left_node     x2          x1    node
           / \                            / \
          /   \                          /   \
        x1      t                       t      x2
        
        nodos x no rotan (mantienen misma relación)
        """

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        """Despues de rotar los nodos hay que 
        cambiar las referencias de los padres de cada nodo"""
        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        """Por ultimo, checkear la referencia del nodo padre del nodo
        rotado (temp_left_node) en caso de que tenga padre"""

        if temp_left_node.parent and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node

        if temp_left_node.parent and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

    def rotate_left(self, node):

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        """Despues de rotar los nodos hay que 
        cambiar las referencias de los padres de cada nodo"""
        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        """Por ultimo, checkear la referencia del nodo padre del nodo
        rotado (temp_left_node) en caso de que tenga padre"""

        if temp_right_node.parent and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if temp_right_node.parent and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node

    def settle_violation(self, node):

        while node != self.root and self.is_red(node) and self.is_red(node.parent):
            parent_node = node.parent
            grand_parent_node = parent_node.parent

            if parent_node == grand_parent_node.left_node:
                uncle = grand_parent_node.right_node

                # Casos de uso 1 y 4 -> Colorear nodos
                if uncle and self.is_red(uncle):
                    print(f'Coloreando {grand_parent_node} a rojo')
                    grand_parent_node.color = Color.RED
                    print(f'Coloreando {parent_node} a negro')
                    parent_node.color= Color.BLACK
                    print(f'Coloreando {uncle} a negro')
                    uncle.color = Color.BLACK
                    #Asignamos nodo a grand_parent_node para que siga iterando
                    node = grand_parent_node
                else:
                    # Caso de uso 2 -> Nodo uncle es negro y el nodo es right child
                    if node == parent_node.right_node:
                        self.rotate_left(parent_node)
                        node = parent_node
                        parent_node = node.parent

                    # Caso de uso 3 -> Rotacion del grandparent + parent y grandparent cambian color
                    print(f'Coloreando {parent_node} a negro')
                    parent_node.color = Color.BLACK
                    print(f'Coloreando {grand_parent_node} a rojo')
                    grand_parent_node.color = Color.RED
                    self.rotate_right(grand_parent_node)

            else:
                uncle = grand_parent_node.left_node

                if uncle and self.is_red(uncle):
                    print(f'Coloreando {grand_parent_node} a rojo')
                    grand_parent_node.color = Color.RED
                    print(f'Coloreando {parent_node} a negro')
                    parent_node.color= Color.BLACK
                    print(f'Coloreando {uncle} a negro')
                    uncle.color = Color.BLACK
                    #Asignamos nodo a grand_parent_node para que siga iterando
                    node = grand_parent_node

                else:
                    if node == parent_node.right_node:
                        self.rotate_right(parent_node)
                        node = parent_node
                        parent_node = node.parent
                    # Caso de uso 3 -> Rotacion del grandparent + parent y grandparent cambian color
                    print(f'Coloreando {parent_node} a negro')
                    parent_node.color = Color.BLACK
                    print(f'Coloreando {grand_parent_node} a rojo')
                    grand_parent_node.color = Color.RED
                    self.rotate_left(grand_parent_node)

        if self.root.color == Color.RED:
            print(f'Coloreando {self.root} (nodo root) a negro')
            self.root.color = Color.BLACK

    def is_red(self, node):
        if node is None:
            return False

        return node.color == Color.RED




if __name__ == '__main__':
    rbtree = RBTree()

    rbtree.insert(32)
    rbtree.insert(10)
    rbtree.insert(55)
    rbtree.insert(1)
    rbtree.insert(19)
    rbtree.insert(79)
    rbtree.insert(16)
    rbtree.insert(23)
    rbtree.insert(12)


    print(rbtree.traverse())
    print(rbtree.iterate())