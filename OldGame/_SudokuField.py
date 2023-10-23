import random
from random import randint as rnd


class SudokuField:
    def __init__(self, length_matrix: int) -> None:
        # Матрица
        self.matrix = []

        # Первая строка матрицы
        self.row = list(range(1, 10))

        # Размер матрицы
        self.length = length_matrix

        # Переменные
        self.area1, self.area2 = None, None
        self.small_area1, self.small_area2 = None, None
        self.re = True

        # Сдвиг матрицы
        self.shift_matrix()

        # Перемешивание матрицы
        self.shuffle()

    def shuffle(self) -> None:
        """Создание уникальной матрицы ответов"""
        iterations = 50
        mix_func = [self.swap,
                    self.swap_rows_small,
                    self.swap_columns_small,
                    self.swap_rows,
                    self.swap_columns]
        for i in range(1, iterations):
            random.choice(mix_func)()

    def swap(self) -> None:
        """Меняет местами строки и столбцы"""
        self.matrix = [list(i) for i in list(zip(*self.matrix))]

    def swap_rows_small(self) -> None:
        """Замена 2 маленьких рядов"""
        if self.re or self.small_area1 is None:
            self.get_random_small_area()
        self.matrix[self.small_area1], self.matrix[self.small_area2] = \
            self.matrix[self.small_area2], self.matrix[self.small_area1]

    def swap_columns_small(self) -> None:
        """Замена 2 маленьких столбцов"""
        if self.re:
            self.get_random_small_area()
        self.swap()
        self.swap_rows_small()
        self.swap()

    def swap_rows(self) -> None:
        """Замена 2 рядов"""
        self.get_random_area()
        self.re = False
        for i in range(3):
            self.swap_rows_small()
        self.re = True

    def swap_columns(self) -> None:
        """Замена 2 столбцов"""
        self.get_random_area()
        self.re = False
        self.swap()
        self.swap_rows()
        self.swap()
        self.re = True

    def get_random_area(self) -> None:
        """Генерация индексов больших столбцов и строк"""
        self.area1 = rnd(0, self.length // 3 - 1)
        self.area2 = rnd(0, self.length // 3 - 1)
        while self.area1 == self.area2:
            self.area2 = rnd(0, self.length // 3 - 1)

    def get_random_small_area(self) -> None:
        """Генерация индексов столбца и строки"""
        self.small_area1 = rnd(0, self.length // 3 - 1)
        self.small_area2 = rnd(0, self.length // 3 - 1)
        area = rnd(0, self.length // 3 - 1)
        while self.small_area1 == self.small_area2:
            self.small_area2 = rnd(0, self.length // 3 - 1)
        self.small_area1, self.small_area2 = area * 3 + self.small_area1, area * 3 + self.small_area2

    def shift_matrix(self) -> None:
        """Сдвиг матрицы"""
        for i in range(1, self.length + 1):
            self.matrix.append(self.row)
            if i % 3 == 0:
                self.row = self.row[4:self.length:] + self.row[0:4:]
            else:
                self.row = self.row[3:self.length:] + self.row[0:3:]

    def output(self) -> None:
        for line in self.matrix:
            print(line)
