def trw(lista):
    lista_final = []
    if len(lista) < 3:
        print('La longitud del array tiene que ser mayor que 3')

    else:
        max_l = max_left(lista)
        max_r = max_right(lista)
        print(max_l)
        print(max_r)
        for i in range(len(lista)):
            if min(max_l[i], max_r[i]) - lista[i] >= 0:
                lista_final.append(min(max_l[i], max_r[i]) - lista[i])

            if min(max_l[i], max_r[i]) - lista[i] < 0:
                lista_final.append(0)

    return sum(lista_final)


def max_left(a_list):
    left = 0
    left_val = [0]

    for i in range(1, len(a_list)):
        if max(a_list[i-1], a_list[i]) > left:
            left_val.append(max(a_list[i-1], a_list[i]))
            left = max(a_list[i-1], a_list[i])
        else:
            left_val.append(left)
    return left_val


def max_right(b_list):
    b_list_rev = [b_list[x] for x in range(len(b_list) - 1, -1, -1)]
    right = 0
    right_val = [0]

    for i in range(1, len(b_list_rev)):
        if max(b_list_rev[i-1], b_list_rev[i]) > right:
            right_val.insert(0, max(b_list_rev[i-1], b_list_rev[i]))
            right = max(b_list_rev[i-1], b_list_rev[i])
        else:
            right_val.insert(0, right)

    return right_val

if __name__ == '__main__':
    lista_valores = [1,0,2,1,3,1,2,0,3]
    print(trw(lista_valores))

