from Play.PlayWindow import PlayWindow
from Statistics.StatisticsWindow import StatisticsWindow
from Settings.SettingsWindow import SettingsWindow
from UI.MenuWindowUI import Ui_SudokuUI

from PyQt5.QtWidgets import QMainWindow


class MenuWindow(QMainWindow, Ui_SudokuUI):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self._clicking_on_buttons()

    def _clicking_on_buttons(self):
        """When someone button is pressed create new Widget and save it to the variable"""
        self.playButton.clicked.connect(self._create_playWindow)
        self.statisticsButton.clicked.connect(self._create_statisticsWindow)
        self.settingsButton.clicked.connect(self._create_settingsWindow)

    def _create_playWindow(self):
        self.playWindow = PlayWindow()

    def _create_statisticsWindow(self):
        self.statisticsWindow = StatisticsWindow()

    def _create_settingsWindow(self):
        self.settingsWindow = SettingsWindow()

    def close_playWindow(self):
        print('closing')
        self.playWindow.close()

    def close_statisticsWindow(self):
        self.statisticsWindow.close()

    def close_settingsWindow(self):
        self.settingsWindow.close()
