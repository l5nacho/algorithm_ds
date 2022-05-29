def is_palindrome(word):
    palindrome = list(word)
    first = 0
    last = len(palindrome) - 1

    while first < last:
        palindrome[first], palindrome[last] = palindrome[last], palindrome[first]
        first = first + 1
        last = last -1

    new_word = ''.join(palindrome)
    if word == new_word:
        print(f'Palabra {word} es un palindromo')

    else:
        print(f'Palabra {word} NO es un palindromo')

def palindromo(word):
    if word == word[::-1]:
        print(f'Palabra {word} es un palindromo')
    else:
        print(f'Palabra {word} NO es un palindromo')



if __name__ == '__main__':
    palindromos = ['radar', 'atomico', 'madam', 'telefono']

    for i in palindromos:
        is_palindrome(i)

    for i in palindromos:
        palindromo(i)