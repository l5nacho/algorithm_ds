
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
        """
        Funcion para insertar par key/value, partimos de un indice que se
        genera con el hash_function, si ese indice no es None, puede que
        sea el mismo key (en cuyo caso hacemos un update) o puede que ese
        slot esté ocupado, en ese caso iteramos hasta que encontremos
        un valor del indice correcto

        :param key: string
        :param value: any
        :return: None
        """

        index = self.hash_function(key)

        while self.keys[index] is not None:
            # Si la key existe, tenemos que hacer un update del valor.
            # Es una propiedad de los diccionarios
            if self.keys[index] == key:
                self.values[index] = value
                return None

            index = (key + 1) % self.capacity

        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        """
        Busca una key dentro del hashtable, si el valor no coincide pero
        si el indice, hace linear probing con el siguiente valor

        :param key: string
        :return:
        """

        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (key + 1) % self.capacity

        return None


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
