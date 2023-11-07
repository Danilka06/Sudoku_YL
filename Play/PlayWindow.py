from PyQt5.QtWidgets import QWidget, QPushButton
from UI.PlayWindowUI import Ui_playWidget

from Play.SudokuField import SudokuField


class PlayWindow(QWidget, Ui_playWidget):
    """Class based on QWidget to operate with all buttons"""

    def __init__(self):
        print("PlayWindow class initialized")
        super().__init__()

        self.setupUi(self)  # loading design
        self.show()  # open window

        self.sudokuField = SudokuField()

        self._fill_in_field()

        self._clicking_on_buttons()

    def _clicking_on_buttons(self) -> None:
        self.backButton.clicked.connect(self.close)
        self.clearButton.clicked.connect(self.clearButton_pressed)

        self.fieldGroup.buttonClicked.connect(self.fieldGroup_clicked)
        self.numberSelectGroup.buttonClicked.connect(self.numberSelectGroup_clicked)

    def clearButton_pressed(self) -> None:
        pass  # TODO

    def fieldGroup_clicked(self, button: QPushButton) -> None:
        button_name = button.objectName()  # name of pressed button
        y, x = int(button_name[-3]), int(button_name[-1])  # x and y from button name

        self.sudokuField.update_variables(x=x, y=y)  # Update variables in field class

        if self.sudokuField.available_move():
            print("available move")
            self.sudokuField.game_tick()
            button.setText(str(self.sudokuField.number_selected))

    def numberSelectGroup_clicked(self, button: QPushButton) -> None:
        # self.sudokuField.number_selected = button.objectName()[-1]
        self.sudokuField.update_variables(number_selected=button.objectName()[-1])
        print(f"selected number = {self.sudokuField.number_selected}")

    def _fill_in_field(self):
        """Execute on startup and set text to all buttons from given current field"""
        for button in self.fieldGroup.buttons():
            button_name = button.objectName()
            y, x = int(button_name[-3]), int(button_name[-1])

            cell = self.sudokuField.current_field[y][x]
            if cell is not None:
                button.setText(str(cell))
