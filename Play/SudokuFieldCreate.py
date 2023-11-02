class SudokuFieldCreate:
    def __init__(self):
        self.end_field = []  # field that program generates first(wining field)

        self.current_field = []  # field that will not have all cells(field that user will see)

