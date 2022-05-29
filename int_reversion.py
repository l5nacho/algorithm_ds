def reverse_number(number: object) -> object:
    final_number = 0
    while number > 0:
        prueba = number % 10
        number = number // 10
        final_number = final_number * 10 + prueba

    print(final_number)

if __name__ == '__main__':
    reverse_number(123456)