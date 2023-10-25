import sys

from Menu import MenuWindow

from PyQt5.QtWidgets import QApplication


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MenuWindow.MenuWindow()
    ex.show()
    sys.exit(app.exec())
