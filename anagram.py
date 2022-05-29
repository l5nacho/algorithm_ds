def anagram_check(word1, word2):
    if len(word1) != len(word2):
        return False

    str1 = sorted(word1)
    str2 = sorted(word2)
    counter = 0
    lista_bool = []
    while counter < len(str1):
        lista_bool.append(str1[counter] == str2[counter])
        counter += 1

    return all(lista_bool)


def anagram_check2(word1, word2):
    if len(word1) != len(word2):
        return False

    str1 = sorted(word1)
    str2 = sorted(word2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


if __name__ == '__main__':
    print(anagram_check2('restfull', 'fleuster'))
