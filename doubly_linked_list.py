from time import sleep
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.data


class DoublyLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_nodes = 0

    def __repr__(self):
        node = self.head
        a_list = []
        a_list.append(node.data)

        while node.next is not None:
            node = node.next
            a_list.append(node.data)

        return ' -> '.join(a_list)

    def traverse_reverse(self):
        node = self.tail
        a_list = []
        a_list.append(node.data)

        while node.previous is not None:
            node = node.previous
            a_list.append(node.data)

        return ' -> '.join(a_list)

    def insert_beggining(self, data):
        nodo = Node(data=data)
        self.num_of_nodes += 1

        if self.head is None:
            self.head = nodo
            self.tail = nodo
        else:
            self.head.previous = nodo
            nodo.next = self.head
            self.head = nodo

    def insert_end(self, data):
        nodo = Node(data=data)
        self.num_of_nodes += 1

        if self.tail is None:
            self.tail = nodo
            self.head = nodo
        else:
            self.tail.next = nodo
            nodo.previous = self.tail
            self.tail = nodo

    def del_beggining(self):
        node = self.head.next
        self.head = node


if __name__ == '__main__':
    doubly_link_list = DoublyLinkList()
    print('Inicio')
    doubly_link_list.insert_beggining('c')
    print(doubly_link_list)
    doubly_link_list.insert_beggining('b')
    print(doubly_link_list)
    doubly_link_list.insert_beggining('a')
    print(doubly_link_list)
    doubly_link_list.insert_end('x')
    print(doubly_link_list)
    doubly_link_list.insert_end('y')
    print(doubly_link_list)
    doubly_link_list.insert_end('z')
    print(doubly_link_list)
    print(doubly_link_list.traverse_reverse())
    print('final')