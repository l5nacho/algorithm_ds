def dutch_flag(lista, mid=1):
    i = 0
    j = 0
    k = len(lista) - 1

    print(f'La lista sin modificar es {lista}')
    while j <= k:
        print(f'el valor a cambiar es {lista[j]}, i es {i}, j es {j} y k es {k}')

        if lista[j] < mid:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j += 1

        elif lista[j] == mid:
            j += 1

        elif lista[j] > mid:
            lista[j], lista[k] = lista[k], lista[j]
            k -= 1
        print(f'la lista queda: {lista}')
    return lista

if __name__ == '__main__':
    lista_1 = [0,1,0,2,1,0,1,2]
    print(f'Antes de ordenar la lista es {lista_1} despues es {dutch_flag(lista_1)}')