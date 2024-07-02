# Импортируем модуль random для генерации случайных чисел
import random

# Объявляем класс RandomPassword
class RandomPassword:
    # Инициализируем класс с параметрами psw_chars, min_length и max_length
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    # Определяем метод __call__, который генерирует пароль
    def __call__(self):
        # Выбираем случайную длину пароля в заданном диапазоне
        length = random.randint(self.min_length, self.max_length)
        # Генерируем пароль из случайных символов
        return ''.join(random.choice(self.psw_chars) for _ in range(length))
