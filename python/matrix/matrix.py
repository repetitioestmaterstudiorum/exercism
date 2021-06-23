class Matrix:
    def __init__(self, matrix_string):
        self.matrix_rows = [x.split() for x in matrix_string.splitlines()]

    def row(self, index):
        return [int(x) for x in self.matrix_rows[index - 1]]

    def column(self, index):
        return [int(x[index - 1]) for x in self.matrix_rows if len(x) >= index]

# dev assertions
matrix = "9 88 7\n5 3 2\n6 6"
m = Matrix(matrix)
assert(m.row(1) == [9, 88, 7])
assert(m.row(2) == [5, 3, 2])
assert(m.row(3) == [6, 6])
assert(m.column(1) == [9, 5, 6]) 
assert(m.column(2) == [88, 3, 6])
assert(m.column(3) == [7, 2])