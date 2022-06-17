class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0

    def __repr__(self):
        return str(self.data)


class AVLTree:

    def __init__(self):
        # El nodo root es el punto de entrada al arbol
        self.root = None

    def insert(self, data):
        if self.root is None:
            # Si no hay nodo root añadimos uno con parent None
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):

        if data < node.data:
            # Hay que mirar si el nodo left es None, si lo es añadimos nodo,
            # si no seguimos llamando a la función
            if not node.left_node:
                node.left_node = Node(data, node)
                # Falta implementar el metodo
                # node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
            else:
                self.insert_node(data, node.left_node)

        else:
            if not node.right_node:
                node.right_node = Node(data, node)
                # node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
            else:
                self.insert_node(data, node.right_node)

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):

        if node is None:
            return None

        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)

        else:
            # Caso 1 -> Nodo no tiene hijos (nodo hoja)
            print(f'Nodo {node} encontrado con hijo {node.left_node} y {node.right_node} '
                  f'y padre {node.parent}')
            if not node.left_node and not node.right_node:
                print(f"Eliminando nodo hoja: {node}")

                parent = node.parent
                if parent and parent.left_node == node:
                    parent.left_node = None
                if parent and parent.right_node == node:
                    parent.right_node = None
                if not parent:
                    self.root = None

                del node
                # self.handle_violation(node)

            # Caso 2 -> Nodo tiene un solo hijo
            elif node.left_node and not node.right_node:
                print(f"Eliminando nodo con un solo hijo a la derecha: {node}")
                parent = node.parent

                if parent and parent.left_node == node:
                    parent.left_node = node.left_node
                if parent and parent.right_node == node:
                    parent.right_node = node.right_node
                if not parent:
                    self.root = None

                node.left_node.parent = parent
                del node

            elif not node.left_node and node.right_node:
                print(f"Eliminando nodo con un solo hijo a la izquierda: {node}")
                parent = node.parent

                if parent and parent.left_node == node:
                    parent.left_node = node.left_node
                if parent and parent.right_node == node:
                    parent.right_node = node.right_node
                if not parent:
                    self.root = None

                node.right_node.parent = parent
                del node

            # Caso 3 -> Tiene dos hijos
            # Reduccion matemática, cambiamos el nodo por el predecesor (mayor
            # valor de la rama de la izquierda) = mayor valor de los menores y
            # lo convertimos en nodo hoja o en nodo con un solo hijo.
            else:
                print(f"Eliminando nodo con dos hijos: {node}")
                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                print(f'{predecessor} {type(predecessor)} {data} {type(data)}')

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):

        if node.right_node:
            return self.get_predecessor(node.right_node)
        else:
            return node

    def traverse(self):

        if not self.root:
            return None
        else:
            return self.traverse_in_order(self.root)

    def traverse_in_order(self, node):

        if node.left_node:
            return self.traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node:
            return self.traverse_in_order(node.right_node)

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


if __name__ == '__main__':
    avl = AVLTree()

    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    avl.insert(7)
    avl.insert(2)
    avl.insert(18)
    avl.insert(12)
    avl.insert(-5)
    avl.insert(45)
    avl.insert(11)

    avl.traverse()
    print(avl.iterate())
    avl.remove(-5)
    print(avl.iterate())
    avl.remove(12)
    print(avl.iterate())
    avl.remove(17)
    print(avl.iterate())