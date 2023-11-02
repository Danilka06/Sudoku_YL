from PyQt5.QtWidgets import QWidget, QPushButton
from UI.PlayWindowUI import Ui_playWidget

from Play.SudokuField import SudokuField


class PlayWindow(QWidget, Ui_playWidget):
    def __init__(self):
        print("PlayWindow class initialized")
        super().__init__()

        self.setupUi(self)

        self.show()

        self._clicking_on_buttons()

        self.number_selected = 0
        self.field = SudokuField()

    def _clicking_on_buttons(self):
        self.backButton.clicked.connect(self.close)
        self.clearButton.clicked.connect(self.clearButton_pressed)

        self.fieldGroup.buttonClicked.connect(self.fieldGroup_clicked)
        self.numberSelectGroup.buttonClicked.connect(self.numberSelectGroup_clicked)

    def clearButton_pressed(self):
        pass

    def fieldGroup_clicked(self, button: QPushButton):
        button_name = button.objectName()  # name of pressed button
        y, x = int(button_name[-3]), int(button_name[-1])  # x and y from button name

        self.field.game_tick(self.number_selected, x, y)

    def numberSelectGroup_clicked(self):
        pass
