from random import randint as rnd


class SudokuDelete:
    def __init__(self, matrix):
        self.matrix = matrix
        self.difficulty_level = 3

        self._difficulty_level()
        self.delete_matrix()

    def _difficulty_level(self):
        match self.difficulty_level:
            case 1:
                # self.difficulty_level = rnd(1, 2)
                self.difficulty_level = rnd(31, 35)
            case 2:
                self.difficulty_level = rnd(26, 30)
            case 3:
                self.difficulty_level = rnd(20, 25)
            case _:
                self.difficulty_level = 81

    def delete_matrix(self):
        while self.difficulty_level > 0:
            x, y = rnd(0, 8), rnd(0, 8)
            if self.matrix[y][x] != '':
                self.matrix[y][x] = ''
                self.difficulty_level -= 1
