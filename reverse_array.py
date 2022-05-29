array = [1, 2, 3, 4, 5,6]

print(array)


def reverse_array_old(array):
#NO VALIDO PORQUE NO MANTIENE CONSTANTE LA MEMORIA
#HAY QUE MODIFICAR EL ARRAY EXISTENTE
    array2 = []
    index = -1
    for i in array:
        array2.append(array[index])
        index = index - 1
    return array2

def reverse_array(array):
    lowindex = 0
    highindex = len(array) - 1

    while lowindex < highindex:
        # low = array[lowindex]
        # high = array[highindex]
        # array[lowindex] = high
        # array[highindex] = low
        array[lowindex], array[highindex] = array[highindex], array[lowindex]
        lowindex = lowindex + 1
        highindex = highindex - 1

    return array

if __name__ == '__main__':
    print(reverse_array(array))
