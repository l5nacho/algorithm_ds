class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:

    def __init__(self):
        self.head = None
        self.num_nodes = 0

    def insert_beginning(self, new_node):
        self.num_nodes += 1
        new_node = Node(data=new_node)

        '''Esto es si la lista está vacia'''
        if self.head is None:
            self.head = new_node

        else:
            '''Añade un nuevo nodo al principio
            de la lista'''
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, node):
        self.num_nodes += 1
        node = Node(data=node)

        '''Esto es si la lista está vacia'''
        if self.head is None:
            self.head = node

        else:
            '''Añade un nuevo nodo al final
            de la lista'''
            nodo = self.head
            while nodo.next is not None:
                nodo = nodo.next
            nodo.next = node

    def find_middle(self, node):
        nodo = self.head
        counter = 0
        print(f'Buscando valor {node}')
        print('----------------')
        while nodo.data != node and nodo.next is not None:
            nodo = nodo.next
            counter += 1
        print('----------------')
        print('Fin de la busqueda')
        if nodo.data == node:
            print(f'El nodo {nodo.data} encontrado en la posicion {counter}')
        else:
            print('Nodo no encontrado')

    def middle_node_naive(self):
        nodo = self.head
        counter1 = 1
        counter2 = 1
        while nodo.next is not None:
            nodo = nodo.next
            counter1 += 1
        print(f'{counter1} - {counter1%2}')
        if counter1 % 2 != 0:
            counter1 = counter1//2 + 1
            nodo = self.head

            while counter2 < counter1:
                nodo = nodo.next
                counter2 += 1
                print(f'{counter1} {counter2}')
            print(f'Nodo central es {nodo}')

        elif counter1 % 2 == 0:
            counter1 = counter1//2
            nodo = self.head
            while counter2 < counter1 and nodo.next is not None:
                nodo = nodo.next
                counter2 += 1
            print(f'Nodo central está entre {nodo} y {nodo.next}')

    def middle_node_pointer(self):
        nodo1 = self.head
        nodo2 = self.head
        while nodo2.next is not None:
            nodo1 = nodo1.next
            nodo2 = nodo2.next
            if nodo2.next is not None:
                nodo2 = nodo2.next
        print(nodo1)

    def reverse_linked_list(self):
        print('Empieza el reverse')
        current_node = self.head
        next_node = None
        prev_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node


    def remove(self, data):

        previous_node = None
        current_node = self.head

        print(self)

        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        print(f'El nodo anterior es {previous_node}')
        print(f'El nodo ahora es {current_node}')

        if current_node is None:
            return 'Nodo no encontrado'
        if previous_node is None:
            self.head = current_node.next
        else:
            previous_node.next = current_node.next

        print(self)


    def __repr__(self):
        '''Muestra en pantalla los
        elementos de la lista'''
        a_list = []
        nodo = self.head
        a_list.append(nodo.data)
        while nodo.next is not None:
            nodo = nodo.next
            a_list.append(nodo.data)

        return '->'.join(a_list)

    def __len__(self):
        '''igual que el metodo size,
        devuelve el número de elementos'''
        return self.num_nodes

    def __iter__(self):
        '''Igual que el metodo traverse
        permite iterar a traves de la lista'''
        node = self.head

        while node is not None:
            yield node
            node = node.next


if __name__ == '__main__':
    primer_nodo = Node(data='a')
    segundo_nodo = 'b'
    tercer_nodo = 'c'
    cuarto_nodo = 'd'
    quinto_nodo = 'e'
    sexto_nodo = 'f'
    septimo_nodo = 'g'
    octavo_nodo = 'h'
    llist = LinkedList()
    llist.head = primer_nodo
    llist.insert_end(segundo_nodo)
    llist.insert_end(tercer_nodo)
    llist.insert_end(cuarto_nodo)
    # llist.insert_end(quinto_nodo)
    # llist.insert_end(sexto_nodo)
    # llist.insert_end(septimo_nodo)
    # llist.insert_end(octavo_nodo)
    print(llist)
    # llist.find_middle('d')
    # llist.find_middle('f')
    # llist.find_middle('z')
    llist.middle_node_naive()
    llist.middle_node_pointer()
    llist.reverse_linked_list()
    print(llist)



