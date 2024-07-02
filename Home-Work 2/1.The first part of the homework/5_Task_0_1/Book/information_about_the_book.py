# Объявляем класс Book
class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        # Инициализируем атрибуты класса
        self.title = title  # заголовок книги
        self.author = author  # автор книги
        self.pages = pages  # количество страниц
        self.year = year  # год издания

    # Магический метод __setattr__ для проверки типов присваиваемых данных
    def __setattr__(self, name, value):
        # Если атрибут - это title или author, проверяем, что значение - это строка
        if name == 'title' or name == 'author':
            if not isinstance(value, str):
                # Если значение не является строкой, генерируем исключение
                raise TypeError("Неверный тип присваиваемых данных.")
        # Если атрибут - это pages или year, проверяем, что значение - это целое число
        elif name == 'pages' or name == 'year':
            if not isinstance(value, int):
                # Если значение не является целым числом, генерируем исключение
                raise TypeError("Неверный тип присваиваемых данных.")
        # Если типы данных корректны, присваиваем значение атрибуту
        self.__dict__[name] = value

# Создаем объект book класса Book с заданными параметрами
book = Book('OOP', 'JK', 123, 2022)
