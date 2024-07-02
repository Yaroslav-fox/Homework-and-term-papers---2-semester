# Импортируем класс WordString в отдельный файл для проверки работоспособности кода
from word_string import WordString

# Создаем объект класса WordString без параметров
words = WordString()

# Устанавливаем строку для объекта words
words.string = "Python ООП Программирование"

# Получаем количество слов в строке
n = len(words)

# Получаем первое слово в строке
first = "" if n == 0 else words(0)

# Выводим строку и информацию о ней
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
