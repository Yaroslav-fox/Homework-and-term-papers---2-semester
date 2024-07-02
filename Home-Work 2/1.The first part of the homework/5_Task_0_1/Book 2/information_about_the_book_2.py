# Объявляем класс Book
class Book:
    # Инициализируем класс с параметрами title, author и pages
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Определяем метод __str__, который возвращает строковое представление объекта класса
    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"
