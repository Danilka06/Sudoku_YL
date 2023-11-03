class SudokuFieldCreate:
    def __init__(self):
        self.end_field = []  # field that program generates first(wining field)
        self.current_field = []  # field that will not have all cells(field that user will see)

        self.fill_field_with_spaces()

    def fill_field_with_spaces(self):
        for _ in range(9):
            self.end_field.append(['0' for _ in range(9)])

        self.current_field = self.end_field

    # TODO: create ramdom matrix
