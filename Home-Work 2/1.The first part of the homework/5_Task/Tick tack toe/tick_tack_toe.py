# Импортируем модуль random для генерации случайных чисел
import random

# Объявляем класс Cell
class Cell:
    def __init__(self):
        # Инициализируем свойство value значением 0
        self.value = 0

    # Метод __bool__ для проверки, свободна ли клетка
    def __bool__(self):
        # Возвращает True, если клетка свободна (value = 0), иначе False
        return self.value == 0

# Объявляем класс TicTacToe
class TicTacToe:
    # Определяем константы для обозначения свободной клетки, крестика и нолика
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        # Инициализируем игровое поле 3x3 клетками
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]

    # Метод __getitem__ для получения значения клетки по индексам
    def __getitem__(self, indices):
        i, j = indices
        # Если индексы выходят за пределы игрового поля, генерируем исключение
        if not (0 <= i < 3 and 0 <= j < 3):
            raise IndexError('некорректно указанные индексы')
        # Возвращаем значение клетки
        return self.pole[i][j].value

    # Маетод __setitem__ для установки значения клетки по индексам
    def __setitem__(self, indices, value):
        i, j = indices
        # Если индексы выходят за пределы игрового поля, генерируем исключение
        if not (0 <= i < 3 and 0 <= j < 3):
            raise IndexError('некорректно указанные индексы')
        # Устанавливаем значение клетки
        self.pole[i][j].value = value

    # Метод для инициализации игры
    def init(self):
        # Очищаем игровое поле, устанавливая значение каждой клетки равным FREE_CELL
        for i in range(3):
            for j in range(3):
                self.pole[i][j].value = self.FREE_CELL

    # Метод для отображения игрового поля
    def show(self):
        # Выводим каждую клетку игрового поля
        for i in range(3):
            for j in range(3):
                print(self.pole[i][j].value, end=' ')
            print()

    # Метод для реализации хода человека
    def human_go(self):
        # Запрашиваем координаты свободной клетки и ставим туда крестик
        i, j = map(int, input("Введите координаты клетки: ").split())
        self[i, j] = self.HUMAN_X

    # Метод для реализации хода компьютера
    def computer_go(self):
        # Ставим нолик в случайную свободную клетку
        i, j = random.choice([(i, j) for i in range(3) for j in range(3) if self[i, j] == self.FREE_CELL])
        self[i, j] = self.COMPUTER_O

    # Метод для проверки победы игрока
    def check_win(self, player):
        # Определяем все возможные позиции для победы
        win_positions = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        # Проверяем, есть ли выигрышная комбинация для заданного игрока
        for positions in win_positions:
            if all(self[i, j] == player for i, j in positions):
                return True
        return False

    # Свойство для проверки победы человека
    @property
    def is_human_win(self):
        return self.check_win(self.HUMAN_X)

    # Свойство для проверки победы компьютера
    @property
    def is_computer_win(self):
        return self.check_win(self.COMPUTER_O)

    # Свойство для проверки ничьей
    @property
    def is_draw(self):
        return all(self[i, j] != self.FREE_CELL for i in range(3) for j in range(3))

    # Магический метод __bool__ для проверки, окончена ли игра
    def __bool__(self):
        return not (self.is_human_win or self.is_computer_win or self.is_draw)
