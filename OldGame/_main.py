from random import randint as rnd
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QButtonGroup, QWidget, QLabel
from PyQt5 import QtGui

import _config as config
from _SudokuField import SudokuField
from _SudokuDelete import SudokuDelete
from _config import *


class Sudoku(QMainWindow):
    def __init__(self):
        super().__init__()

        #  Ширина и высота судоку (9*9)
        self.width_matrix, self.length_matrix = config.width_matrix, config.length_matrix

        #  Отступы от края по x и y
        self.indent_x, self.indent_y = config.indent_x, config.indent_y

        #  Размер кнопок
        self.side = config.side

        #  Список кнопок
        self.btn_matrix = []

        #  Группы кнопок
        self.btn_group = QButtonGroup()  # Кнопки поля
        self.answer_btn_group = QButtonGroup()  # Кнопки ответов

        # Выбранное число
        self.active_number = None

        # Нажата ли кнопка delete
        self.delete_choice = None

        # Matrix
        # Матрица готового решения
        self.matrix_answer = []
        # Матрица нынешнего состояния поля
        self.matrix = []

        # Сложность уровня
        self.difficulty_level = None

        # initUI (^-^)
        self.initUI()

    def initUI(self) -> None:
        uic.loadUi('_sudoku_ui.ui', self)

        #  Создания матрицы поля, в которой будут значения
        self.generate_matrix()

        #  Создание поля из кнопок
        self.sudoku_field()

        #  Создание кнопок ответов
        self.number_buttons()

        # win button
        self.win = QLabel(self)

        # Создание кнопки delete
        self.delete_btn = QPushButton('Стереть', self)
        self.delete_btn.resize(150, 40)
        self.delete_btn.setFont(QtGui.QFont("Arial", 8))
        self.delete_btn.move(150, 550)
        self.delete_btn.clicked.connect(self.delete_number)
        #  Подключения групп кнопок к функции

        self.btn_group.buttonClicked.connect(self.pressed)
        # При нажатии на кнопку поля, будет вызываться функция pressed и туда будет передаваться нажатая кнопка

        self.answer_btn_group.buttonClicked.connect(self.answer_pressed)
        # При нажатии на кнопку ответов, будет вызываться функция set_number и туда будет передаваться нажатая кнопка

    def generate_matrix(self):
        """Генерация матрицы значений"""
        #  Обычная матрица, но изначально в каждой позиции находиться значение None
        self.matrix = [['' for _ in range(self.width_matrix)] for __ in range(self.width_matrix)]
        something_in_the_way = SudokuField(9).matrix
        print(id(something_in_the_way), 'smt in the way')
        field = [[something_in_the_way[y][x] for x in range(len(something_in_the_way[y]))] for y in range(len(something_in_the_way))]
        print(id(field), "field")
        self.matrix_answer = [[something_in_the_way[y][x] for x in range(len(something_in_the_way[y]))] for y in range(len(something_in_the_way))]
        self.output(self.matrix_answer)
        print('==========================')
        self.matrix = SudokuDelete(field).matrix
        # self.output(self.matrix)
        # print('+++++++++++++++++++++++++')
        # self.output(self.matrix_answer)
        print(id(self.matrix_answer), 'id - matrix_answer')
        print(id(self.matrix), 'id - matrix')
        print(id(field), 'id - field')

    def sudoku_field(self) -> None:
        """Создание поля из кнопок"""
        x_pos, y_pos = self.indent_x, self.indent_y
        for i in range(self.width_matrix):
            self.btn_matrix.append([])
            x_pos = self.indent_x
            width = 1
            for j in range(self.length_matrix):

                #  Создание кнопки с текстом ""
                k = QPushButton(str(self.matrix[i][j]), self)
                # k.setObjectName(i, j))
                #  Если это третья кнопка - меняем отступ (width) на 2
                if (j + 1) % 3 == 0:
                    width = 2

                #  Указание ее значений - шрифт, размер шрифта, размер кнопки и css, позиция
                k.setFont(QtGui.QFont("Arial", 10))
                k.resize(self.side, self.side)
                k.setStyleSheet('color: black; background-color: white; border: none')

                #  Двигает кнопку
                k.move(x_pos, y_pos)

                #  Изменяет x_pos
                x_pos += self.side + width

                #  Возвращает отступ
                width = 1

                #  Добавление кнопки в группу кнопок
                self.btn_group.addButton(k)
                self.btn_matrix[i].append(k)

            #  Та же самая схема, только по y
            if (i + 1) % 3 == 0:
                width = 2
            else:
                width = 1

            y_pos += self.side + width

    def number_buttons(self) -> None:
        """Создание кнопок ответов"""

        x, y = 50, 500
        for i in range(1, 10):
            #  создание кнопки с цифрой i
            number_btn = QPushButton(str(i), self)

            #  Изменение размеров и перемещение
            number_btn.resize(self.side, self.side)
            number_btn.move(x, y)

            #  Добавление в группу
            self.answer_btn_group.addButton(number_btn)

            x += self.side + 1

    def pressed(self, btn) -> None:
        """Вызывается если кнопка на поле нажата и принимает btn - нажатую кнопку"""

        y, x = self.find_button_index(btn)

        if self.delete_choice and isinstance(self.matrix[y][x], str):
            print('====')
            print(self.matrix[y][x])
            print('====')

            self.matrix[y][x] = ''
            self.white_color(y, x)
            btn.setText('')
        elif not self.delete_choice:
            self.can_pressed(y, x)
            self.matrix[y][x] = self.active_number
            btn.setText(self.active_number)
            if self.check_win():
                self.when_win()

        # print('amogus')
        # self.output(self.matrix)
        # print('sussus')
        # self.output(self.matrix_answer)
        # print('suuuuuussuuuuus')

    def can_pressed(self, y: int, x: int) -> None:
        """Проверка на корректность постановки цифры"""
        # В строке
        for i in self.matrix[y]:
            if i == self.active_number:
                self.red_color(y, x)
                print("Строка", self.delete_choice)

        # В столбце
        for line in self.matrix:
            if line[x] == self.active_number:
                self.red_color(y, x)
                print("Столбец", self.delete_choice)

        # В квадрате
        i, j = y // 3 * 3, x // 3 * 3
        for i in range(i, i + 3):
            for j in range(j, j + 3):
                if self.active_number == self.matrix[i][j]:
                    self.red_color(y, x)
                    print("Квадрат", self.delete_choice)
                    break
            j = x // 3 * 3

    def check_win(self):
        amongus = True
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                if self.matrix[y][x] == '' or int(self.matrix[y][x]) != self.matrix_answer[y][x]:
                    amongus = False
        return amongus

    def when_win(self):
        self.win.move(10, 10)
        self.win.resize(500, 500)
        self.win.setText("           You\n          won!!!")
        self.win.setStyleSheet("color: white")
        self.win.setFont(QtGui.QFont("Arial", 20))
        self.win.setVisible(True)

        for btn in self.btn_group.buttons():
            btn.setVisible(False)
        for btn in self.answer_btn_group.buttons():
            btn.setVisible(False)
        self.delete_btn.setVisible(False)

    def find_button_index(self, button) -> tuple[int, int]:
        """Возвращает индекс нажатой кнопки"""
        for y in self.btn_matrix:
            if button in y:
                return self.btn_matrix.index(y), y.index(button)

    def answer_pressed(self, btn) -> None:
        """Вызывается если кнопка ответов нажата и принимает btn - нажатую кнопку"""
        self.active_number = btn.text()
        self.delete_choice = False

    def delete_number(self) -> None:
        """Вызывается если нажата кнопка delete"""
        self.active_number = None
        self.delete_choice = True

    def red_color(self, y, x) -> None:
        """Перекраска клетки в красный"""
        self.btn_matrix[y][x].setStyleSheet(
            f'color: white; '
            f'background-color: red; '
            f'border: none')

    def white_color(self, y, x) -> None:
        """Перекраска клетки в белый"""
        self.btn_matrix[y][x].setStyleSheet(
            f'color: black; '
            f'background-color: white; '
            f'border: none')

    def output(self, _matrix) -> None:
        for line in _matrix:
            print(line)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Sudoku()
    window.show()
    sys.exit(app.exec())
