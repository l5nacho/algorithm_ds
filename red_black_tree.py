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
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):

        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)

            else:
                node.left_node = Node(data, parent=node)
                # self.settle_violation()

        if data > node.data:
            if node.right_node:
                self.insert_node(data, node.right_node)

            else:
                node.right_node = Node(data, parent=node)
                # self.settle_violation()
                
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
        cambiar las referencias a los nodos hijo"""
        if t is not None:
            t.parent = node

        temp_parent = node.parent
        temp_left_node.parent = temp_parent
        node.parent = temp_left_node



if __name__ == '__main__':
    rbtree = RBTree()

    rbtree.insert(10)
    rbtree.insert(5)
    rbtree.insert(15)
    rbtree.insert(20)
    rbtree.insert(0)
    rbtree.insert(25)
    rbtree.insert(18)
    rbtree.insert(8)
    rbtree.insert(1)


    print(rbtree.traverse())
    print(rbtree.iterate())