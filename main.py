import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MenuWindowUI.ui', self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MenuWindow()
    ex.show()
    sys.exit(app.exec())
