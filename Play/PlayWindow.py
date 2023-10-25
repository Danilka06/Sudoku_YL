from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class PlayWindow(QWidget):
    def __init__(self):
        print("PlayWindow class initialized")
        super().__init__()
        uic.loadUi('UI/PlayWindowUI.ui', self)

        self.show()

        self._clicking_on_buttons()

    def _clicking_on_buttons(self):
        self.backButton.clicked.connect(self.close)
