from Play.SudokuFieldCreate import SudokuFieldCreate


class SudokuField:
    def __init__(self):
        sudoku_field_create = SudokuFieldCreate()
        self.end_field = sudoku_field_create.end_field  # wining field

        self.current_field = sudoku_field_create.current_field  # current field

    def game_tick(self, current_number: int, x: int, y: int) -> None:
        """Pressing on the cell - one tick.\n
            Points that realized here:\n
            checking is move available;
            writing number;
            checking win and so on"""
        self.update_field(current_number, x, y)
        self.check_win()

    def update_field(self, current_number: int, x: int, y: int):
        print(f'SudokuField.update_field: current_number={current_number}, x={x}, y={y}')

    def check_win(self):
        pass
