from stack import Stack


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent

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

        stack = Stack()
        stack.push(self.root.data)
        nodo = self.root
        lista = []

        while stack is not None:
            if nodo.left_node:
                nodo = nodo.left_node
                stack.push(nodo.data)
                print(stack)
            lista.append(stack.pop())

            if nodo.right_node:
                nodo = nodo.right_node
                stack.push(nodo.data)
                print(stack)

        print(lista)





if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(7)
    bst.insert(2)
    bst.insert(18)
    print(f'El valor minimo es {bst.get_min_value()}')
    print(f'El valor maximo es {bst.get_max_value()}')
    # print(bst.traverse())
    print(bst.iterate())

