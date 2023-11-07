from Play.SudokuFieldCreate import SudokuFieldCreate


class SudokuField:
    """Class for saving data of sudoku field and manipulate with it"""

    def __init__(self) -> None:
        sudoku_field_create = SudokuFieldCreate()
        self.end_field = sudoku_field_create.end_field  # wining field
        self.current_field = sudoku_field_create.current_field  # current field

        self.x = None
        self.y = None
        self.number_selected = None  # number that selected for input from the line below field

    def game_tick(self) -> None:
        """Pressing on the cell - one tick.\n
            Points that realized here:\n
            checking is move available;
            writing number;
            checking win and so on"""
        self.update_field()
        self.check_win()

        self._print_current_field()

    def update_field(self) -> None:
        """Updating self.current_field"""
        print(f'SudokuField.update_field: current_number={self.number_selected}, x={self.x}, y={self.y}')
        self.current_field[self.y][self.x] = self.number_selected

    def check_win(self) -> None:
        """Checking is combination winning"""
        pass  # TODO

    def available_move(self) -> bool:
        """Checking is move available"""
        if self.number_selected is not None and self.current_field[self.y][self.x] is None:
            return True
        return False

    def update_variables(self, x: int | None = None,
                         y: int | None = None,
                         number_selected: str | None = None) -> None:
        """Update all variable for future interaction"""
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if number_selected is not None:
            self.number_selected = number_selected

    def _print_current_field(self) -> None:
        """Just printing self.current_field in normal format(for testing)"""
        for i in range(9):
            print(self.current_field[i])
