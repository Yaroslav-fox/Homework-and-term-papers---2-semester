# Импортируем класс Book в отдельный файл для проверки работоспособности кода
from information_about_the_book_2 import Book

# Создаем список lst_in с информацией о книге
lst_in = ['Python', 'JK', '1024']
# Создаем объект book класса Book с параметрами из списка lst_in
book = Book(*lst_in)
# Выводим строковое представление объекта book
print(book)