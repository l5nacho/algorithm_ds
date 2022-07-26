
class HashTable:

    def __init__(self):
        """
        Dependiendo del load factor, puede que cambie el tamaño de
        la estructura de datos que subyace el hash table
        """
        self.capacity = 10
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def insert(self, key, value):

        index = self.hash_function(key)



    def hash_function(self, key):
        """
        Tranforma una string a un número con la funcion ord
        (transforma un caracter a su representacion ASCII)
        Luego hace modulo con capacity para generar un valor que
        equivalga a un valor del indice

        :param key: string
        :return: integer
        """

        hash_sum = 0

        for letter in key:
            hash_sum = hash_sum + ord(letter)

        return hash_sum % self.capacity
