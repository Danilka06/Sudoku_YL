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

        self._clicking_on_buttons()

        self.sudokuField = SudokuField()

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

        if self.sudokuField.available_move():
            self.sudokuField.game_tick(x, y)
            button.setText(str(self.sudokuField.number_selected))

    def numberSelectGroup_clicked(self, button: QPushButton) -> None:
        self.sudokuField.number_selected = button.objectName()[-1]
        print(self.sudokuField.number_selected)
