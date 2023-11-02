from PyQt5.QtWidgets import QWidget
from UI.PlayWindowUI import Ui_playWidget


class PlayWindow(QWidget, Ui_playWidget):
    def __init__(self):
        print("PlayWindow class initialized")
        super().__init__()

        self.setupUi(self)

        self.show()

        self._clicking_on_buttons()

    def _clicking_on_buttons(self):
        self.backButton.clicked.connect(self.close)
