from doubly_linked_list import DoublyLinkList, Node

class Queue:

    def __init__(self):
        self.queue = DoublyLinkList()

    def __repr__(self):
        nodo = self.queue.head
        lista =[]
        lista.append(str(nodo.data))

        while nodo.next:
            nodo = nodo.next
            lista.append(str(nodo.data))

        return ' -> '.join(lista)

    def is_empty(self):
        return self.queue.num_of_nodes == 0

    def enqueue(self, data):
        self.queue.insert_end(data)

    def dequeu(self):
        data = str(self.queue.head.data)
        self.queue.del_beggining()
        return data

if __name__ == '__main__':
    queue = Queue()
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue)
    print(queue.dequeu())
    print(queue)
    print(queue.dequeu())
    print(queue)
    print(queue.dequeu())
    print(queue)