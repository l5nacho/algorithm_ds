
class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

    def __repr__(self):
        return self.name

def bfs(node):

    queue = [node]
    node.visited = True

    while queue:

        actual_node = queue.pop(0)
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            if not n.visited:
                n.visited = True
                queue.append(n)


if __name__ == '__main__':
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    bfs(node1)