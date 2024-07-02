# Объявляем класс WordString
class WordString:
    # Инициализируем класс с параметром string и разбиваем эту строку на слова
    def __init__(self, string=""):
        self._string = string
        self._words = string.split()

    # Определяем свойство string для получения значения строки
    @property
    def string(self):
        return self._string

    # Определяем сеттер для свойства string, который также обновляет список слов
    @string.setter
    def string(self, value):
        self._string = value
        self._words = value.split()

    # Определяем метод __len__, который возвращает количество слов в строке
    def __len__(self):
        return len(self._words)

    # Определяем метод __call__, который возвращает слово по его индексу
    def __call__(self, indx):
        return self._words[indx] if indx < len(self._words) else ""

