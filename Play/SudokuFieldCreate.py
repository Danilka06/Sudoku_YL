import random
from random import randint as rnd


class SudokuFieldCreate:
    """Class for creating entirely random sudoku field"""

    def __init__(self) -> None:
        self.end_field = []  # field that program generates first(wining field)
        self.current_field = []  # field that will not have all cells(field that user will see)

        self.row = list(range(1, 10))  # first row of field (1-9 numbers)

        self.field_size = 9  # field size
        self.area1, self.area2 = None, None  # indexes of two large swapping areas
        self.small_area1, self.small_area2 = None, None  # indexes of two small swapping areas
        self.re = True  # I don't know what the fuck this is.
        # TODO: understand what mean self.re
        # TODO: check everything dependent on the variable self.re

        self._fill_field_with_shifted_rows()  # creating started field

        self.shuffle_field(iterations=50)  # shuffle field

        self.current_field = self.end_field

        self._delete_some_cells()

    def shuffle_field(self, iterations: int) -> None:
        """Shuffling rows and columns to create entirely random sudoku field"""
        shuffling_functions = [self.swap,
                               self.swap_small_rows,
                               self.swap_small_columns,
                               self.swap_rows,
                               self.swap_columns]
        for i in range(1, iterations):
            random.choice(shuffling_functions)()

    def swap(self) -> None:
        """Swaps rows and columns"""
        self.end_field = [list(i) for i in list(zip(*self.end_field))]

    def swap_small_rows(self) -> None:
        """Swapping 2 small rows"""
        if self.re or self.small_area1 is None:
            self.get_random_small_area()
        self.end_field[self.small_area1], self.end_field[self.small_area2] = \
            self.end_field[self.small_area2], self.end_field[self.small_area1]

    def swap_small_columns(self) -> None:
        """Swap 2 small columns"""
        if self.re:
            self.get_random_small_area()
        self.swap()
        self.swap_small_rows()
        self.swap()

    def swap_rows(self) -> None:
        """Swap 2 large rows"""
        self.get_random_area()
        self.re = False
        for i in range(3):
            self.swap_small_rows()
        self.re = True

    def swap_columns(self) -> None:
        """Swaps 2 large columns"""
        self.get_random_area()
        self.re = False
        self.swap()
        self.swap_rows()
        self.swap()
        self.re = True

    def get_random_area(self) -> None:
        """Generating indexes of large columns and rows"""
        self.area1 = rnd(0, self.field_size // 3 - 1)
        self.area2 = rnd(0, self.field_size // 3 - 1)
        while self.area1 == self.area2:
            self.area2 = rnd(0, self.field_size // 3 - 1)

    def get_random_small_area(self) -> None:
        """Generating indexes of columns and rows"""
        self.small_area1 = rnd(0, self.field_size // 3 - 1)
        self.small_area2 = rnd(0, self.field_size // 3 - 1)
        area = rnd(0, self.field_size // 3 - 1)
        while self.small_area1 == self.small_area2:
            self.small_area2 = rnd(0, self.field_size // 3 - 1)
        self.small_area1, self.small_area2 = area * 3 + self.small_area1, area * 3 + self.small_area2

    def _fill_field_with_shifted_rows(self) -> None:
        """Filling field with shifted rows"""
        for i in range(1, self.field_size + 1):
            self.end_field.append(self.row)
            if i % 3 == 0:
                self.row = self.row[4:self.field_size:] + self.row[0:4:]
            else:
                self.row = self.row[3:self.field_size:] + self.row[0:3:]

    def _print_end_field(self) -> None:
        """Printing self.end_field"""
        for line in self.end_field:
            print(line)

    def _fill_field_with_none(self) -> None:
        """Just filling field with zeros(for testing)"""
        for _ in range(9):
            self.end_field.append([None for _ in range(9)])

        self.current_field = self.end_field

    def _delete_some_cells(self):
        self.end_field[8][2] = None
        self.end_field[8][5] = None
        self.end_field[7][4] = None
