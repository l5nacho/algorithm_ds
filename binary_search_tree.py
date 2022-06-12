from stack import Stack


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent

    def __repr__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        """Solo podemos acceder al nodo root que se inicializa como None
        lo primero que hay que hacer es añadir este nodo"""
        self.root = None

    def insert(self, data):
        """Comprueba si el objeto BST que hemos creado
        tiene un nodo root, si no lo tiene lo creamos con
        los datos que le pasemos, si lo tiene llamamos al
        metodo insert node para que lo añada"""
        if self.root is None:
            self.root = Node(data)

        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        """Recorre el BST recursivamente y añade el nodo a la
        izquierda o la derecha según comparando el valor con el
        nodo"""

        if data < node.data:
            if node.left_node is None:

                # Si no hay nodo left lo crea, con el data y con
                # el nodo padre (segundo parametro)
                node.left_node = Node(data, node)

            else:
                # Si hay nodo left continua recorriendo el BST
                self.insert_node(data, node.left_node)

        else:
            if node.right_node is None:
                # Si no hay nodo right lo crea, con el data y con
                # el nodo padre (segundo parametro)
                node.right_node = Node(data, node)
            else:
                # Si hay nodo right continua recorriendo el BST
                self.insert_node(data, node.right_node)

    def get_min_value(self):
        if self.root is None:
            return None
        else:
            return self.minimum_value(self.root)

    def minimum_value(self, node):
        if node.left_node:
            return self.minimum_value(node.left_node)

        return node.data

    def get_max_value(self):
        if self.root is None:
            return None
        else:
            return self.maximum_value(self.root)

    def maximum_value(self, node):
        if node.right_node:
            return self.maximum_value(node.right_node)

        return node.data

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
        result =[]

        while queue:
            l = queue.pop(0)
            result.append(l)

            if l.left_node is not None:
                queue.append(l.left_node)
            if l.right_node is not None:
                queue.append(l.right_node)

        return result



    def remove(self, data):

        if self.root:
            self.remove_node(self.root, data)

    def remove_node(self, node, data):

        if node is None:
            return None

        if data < node.data:
            self.remove_node(node.left_node, data)
        elif data > node.data:
            self.remove_node(node.right_node, data)
        else:
            print(f"Nodo encontrado: {node}")
            # Eliminando nodo hoja (sin hijos)
            if node.left_node is None and node.right_node is None:
                print(f"Eliminando nodo hoja: {node}")
                if node.parent is not None and node.parent.left_node == node:
                    node.parent.left_node = None
                if node.parent is not None and node.parent.right_node == node:
                    node.parent.right_node = None
                if node.parent is None:
                    self.root = None
                del node
            # Eliminando nodo con un solo hijo
            elif node.left_node is None and node.right_node is not None:
                print(f"Eliminando nodo con un solo hijo a la derecha: {node}")
                parent = node.parent
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node
                if parent is None:
                    self.root = node.right_node

                node.right_node.parent = parent
                del node

            elif node.right_node is None and node.left_node is not None:
                print(f"Eliminando nodo con un solo hijo a la izquierda: {node}")
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.left_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.left_node
                if parent is None:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node

            # Eliminando nodo con dos hijos
            else:
                print(f"Eliminando nodo con dos hijos: {node}")
                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(predecessor, data)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)

        return node

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(7)
    bst.insert(2)
    bst.insert(18)
    bst.insert(12)
    bst.insert(-5)
    bst.insert(45)
    bst.insert(11)

    print(f'El valor minimo es {bst.get_min_value()}')
    print(f'El valor maximo es {bst.get_max_value()}')
    print(bst.traverse())
    print(bst.iterate())
    bst.remove(5)
    print(bst.iterate())

