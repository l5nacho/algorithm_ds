
class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

    def __repr__(self):
        return self.name


def depth_first_search(actual_node):

    stack = [actual_node]
    actual_node.visited = True

    while stack:
        node = stack.pop()
        print(node)

        for n in node.adjacency_list:
            stack.append(n)
            n.visited = True

if __name__ == '__main__':


    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node3.adjacency_list.append(node5)
    node5.adjacency_list.append(node4)

    depth_first_search(node1)
