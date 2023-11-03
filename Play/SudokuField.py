from Play.SudokuFieldCreate import SudokuFieldCreate


class SudokuField:
    """Class for saving data of sudoku field and manipulate with it"""
    def __init__(self) -> None:
        sudoku_field_create = SudokuFieldCreate()
        self.end_field = sudoku_field_create.end_field  # wining field
        self.current_field = sudoku_field_create.current_field  # current field

        self.number_selected = None  # number that selected for input from the line below field

    def game_tick(self, x: int, y: int) -> None:
        """Pressing on the cell - one tick.\n
            Points that realized here:\n
            checking is move available;
            writing number;
            checking win and so on"""
        self.update_field(x, y)
        self.check_win()

        self._print_current_field()

    def update_field(self, x: int, y: int) -> None:
        """Updating self.current_field"""
        print(f'SudokuField.update_field: current_number={self.number_selected}, x={x}, y={y}')
        self.current_field[y][x] = self.number_selected

    def check_win(self) -> None:
        """Checking is combination winning"""
        pass  # TODO

    def available_move(self) -> bool:
        """Checking is move available"""
        if self.number_selected is not None:
            return True
        return False

    def _print_current_field(self) -> None:
        """Just printing self.current_field in normal format(for testing)"""
        for i in range(9):
            print(self.current_field[i])
