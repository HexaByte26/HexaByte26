class Matrix:
    def __init__(self):
        global rows
        global columns
        self.row_size = 4
        self.column_size = 4
        self.place_holder = "_"
        self.grid = []
        for _ in range(self.row_size):
            row = []
            for _ in range(self.column_size):
                row.append(self.place_holder)
            self.grid.append(row)

    def connect_vert(self, start_vert, destination_vert):
        self.grid[destination_vert][start_vert] = 1

    def print_matrix(self):
        for row in self.grid:
            print(row)
            print()


mtrx = Matrix()
mtrx.connect_vert(1, 3)
mtrx.print_matrix()