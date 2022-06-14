class Node:

    def __init__(self, data, parent):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0

class AVLTree:

    def __init__(self):
        # El nodo root es el punto de entrada al arbol
        self.root = None

    def insert(self, data):
        if not self.root:
            # Si no hay nodo root añadimos uno con parent None
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):

        if data < node.data:
            # Hay que mirar si el nodo left es None, si lo es añadimos nodo,
            # si no seguimos llamando a la función
            if not node.left_node:
                node.left_node = Node(data, node)
                # Falta implementar el metodo
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
            else:
                self.insert_node(data, node.left_node)

        else:
            if not node.right_node:
                node.right_node = Node(data, node)
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
            else:
                self.insert_node(node, node.right_node)

        # Falta implementar el metodo
        self.handle_violation(node)

