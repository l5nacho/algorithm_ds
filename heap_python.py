import heapq

def is_min_heap(heap, index):

    index = index
    size = (len(heap) - 2) // 2
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if index < size and heap[index] < heap[left_index] and heap[index] < heap[right_index]:
        index += 1
        is_min_heap(heap, index)

    else:
        return False

    return True


if __name__ == '__main__':

    lista = [2, 4, 0, -3, 7, -5, 6, 17, 9, 21, 47, 34, 1, 8]
    print(lista)
    print(is_min_heap(lista, 0))
    heapq.heapify(lista)
    print(lista)
    print(is_min_heap(lista, 0))
    print(max_to_min(lista))

