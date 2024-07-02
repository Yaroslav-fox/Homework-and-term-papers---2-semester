# Импортируем класс book в отдельный файл с настройками для проверки работоспособности кода
from information_about_the_book import Book

# Создание объекта book с корректными данными
book1 = Book('OOP', 'JK', 123, 2022)
print(book1.title)  # должно вывести: OOP
print(book1.author)  # должно вывести: JK
print(book1.pages)  # должно вывести: 123
print(book1.year)  # должно вывести: 2022

# Попытка присвоить некорректные данные
try:
    book1.title = 123  # должно вызвать исключение TypeError
except TypeError:
    print("Неверный тип присваиваемых данных.")

try:
    book1.pages = 'one hundred and twenty-three'  # должно вызвать исключение TypeError
except TypeError:
    print("Неверный тип присваиваемых данных.")