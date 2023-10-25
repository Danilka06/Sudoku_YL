from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class StatisticsWindow(QWidget):
    def __init__(self):
        print("StatisticsWindow class initialized")
        super().__init__()
        uic.loadUi('UI/StatisticsWindowUI.ui', self)

        self.show()

        self._clicking_on_buttons()

    def _clicking_on_buttons(self):
        self.backButton.clicked.connect(self.close)
