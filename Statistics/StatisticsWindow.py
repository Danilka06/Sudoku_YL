from PyQt5.QtWidgets import QWidget
from UI.SettingsWindowUI import Ui_settingsWidget


class StatisticsWindow(QWidget, Ui_settingsWidget):
    def __init__(self):
        print("StatisticsWindow class initialized")
        super().__init__()
        
        self.setupUi(self)

        self.show()

        self._clicking_on_buttons()

    def _clicking_on_buttons(self):
        self.backButton.clicked.connect(self.close)
