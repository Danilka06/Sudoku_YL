class SudokuFieldCreate:
    """Class for creating entirely random sudoku field"""
    def __init__(self) -> None:
        self.end_field = []  # field that program generates first(wining field)
        self.current_field = []  # field that will not have all cells(field that user will see)

        self._fill_field_with_spaces()

    def _fill_field_with_spaces(self) -> None:
        """Just filling field with zeros(for testing)"""
        for _ in range(9):
            self.end_field.append(['0' for _ in range(9)])

        self.current_field = self.end_field

    # TODO: create ramdom matrix
