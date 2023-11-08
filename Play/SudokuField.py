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
        self.delete_option = False  # is deleting option activated
        self.win = False  # if the game is won

    def game_tick(self) -> None:
        """Pressing on the cell - one tick.\n
            Points that realized here:\n
            checking is move available;
            writing number;
            checking win and so on"""
        self.update_field()
        self.check_win()

        self._print_variables()

    def update_field(self) -> None:
        """Updating self.current_field"""
        if self.number_selected:
            self.current_field[self.y][self.x] = self.number_selected
        if self.delete_option:
            self.current_field[self.y][self.x] = None

    def check_win(self) -> None:
        """Checking is combination winning"""
        for y, line in enumerate(self.current_field):
            for x, item in enumerate(line):
                if item is None:
                    self.win = False
                    return
                if self.end_field[y][x] != int(item):
                    self.win = False
                    return
        self.win = True

    def available_move(self) -> bool:
        """Checking is move available"""

        # When number selected
        if self.number_selected and self.current_field[self.y][self.x] is None:
            return True

        # When clear button clicked
        if self.delete_option and isinstance(self.current_field[self.y][self.x], str):
            return True

        # Bad ways
        return False

    def update_variables(self, x: int | None = None,
                         y: int | None = None,
                         number_selected: str | None = None,
                         delete_pressed: bool = False) -> None:
        """Update all variable for future interaction"""
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if number_selected is not None:
            self.number_selected = number_selected
            self.delete_option = False
        if delete_pressed:
            self.delete_option = not self.delete_option
            self.number_selected = None

    def _print_current_field(self) -> None:
        """Just printing self.current_field in normal format(for testing)"""
        for i in range(9):
            print(self.current_field[i])

    def _print_end_field(self):
        """Just printing self.end_field in normal format(for testing)"""
        for i in range(9):
            print(self.end_field[i])

    def _print_variables(self):
        print('++++++++++++++++++++++++++++')
        self._print_current_field()
        print('============================')
        self._print_end_field()
        print('++++++++++++++++++++++++++++')
        print(f'current_number={self.number_selected}, x={self.x}, y={self.y}, delete_option={self.delete_option}')
