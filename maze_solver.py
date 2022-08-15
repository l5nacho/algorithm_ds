from collections import deque

class MazeSolver:

    def __init__(self, matrix):
        self.matrix = matrix
        # 4 movimientos posibles
        # LEFT [1,0], RIGHT [0,1], UP [0,-1], DOWN [0,1]
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        # Marcamos todos los valores de la matriz como visitados = False
        self.visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
        self.min_distance = None

    def is_valid(self, row, col):

        # Comprobamos si se puede mover por el eje X
        if row < 0 or row >= len(self.matrix):
            return False

        # Comprobamos si se puede mover por el eje y
        if col < 0 or col >= len(self.matrix):
            return False

        # Comprobamos si el punto de la matriz es un muro (0)
        if self.matrix[row][col] == 0:
            return False

        # Comprobamos si el row o la columna tienen la marca de visitados
        # En este caso comprobamos un punto en la matriz
        if self.visited[row][col]:
            return False

        return True

    def search(self, i, j, destination_x, destination_y):

        self.visited[i][j] = True

        queue = deque()

        # Añadimos a la queue una tupla con el puntos de la matriz
        # y con el valor dist
        queue.append((i, j, 0))

        while queue:
            (i, j, dist) = queue.popleft()
            print(i, j , dist)

            # Si coinciden los puntos con el destino, terminamos el bucle -> hemos encontrado el punto.
            if i == destination_x and j == destination_y:
                self.min_distance = dist
                break

            # Hacemos un range(4) porque son los movimientos posibles
            for move in range(4):
                next_x = i + self.move_x[move]
                next_y = j + self.move_y[move]

                if self.is_valid(next_x, next_y):
                    self.visited[next_x][next_y] = True
                    queue.append((next_x, next_y, dist + 1))

    def show_result(self):
        if self.min_distance:
            print(f"El camino mas corto para el destino es de {self.min_distance} pasos")

        else:
            print('Caminante no hay camino, se hace camino al andar')

if __name__ == '__main__':

    m = [
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
         ]

    maze_solver = MazeSolver(m)
    maze_solver.search(0, 0, 4, 4)
    maze_solver.show_result()


