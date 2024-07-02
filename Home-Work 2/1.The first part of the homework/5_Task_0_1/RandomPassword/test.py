# Импортируем класс RandomPassword в отдельный файл для проверки работоспособности программы
from random_password import RandomPassword

# Создаем переменные с вводом, с клавиатуры
x = int(input("Минимальная длинна пароля:", ))
y = int(input("Максимальная длинна пароля:", ))
z = int(input("Колличество паролей:", ))

# Создаем объект rnd класса RandomPassword с параметрами который выберит пользователь
rnd = RandomPassword("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*", x, y)

# Создаем список lst_pass из того колличества сгенерированных паролей который выберит пользователь
lst_pass = [rnd() for _ in range(z)]

# Выводим сгенерированные пароли
for i, password in enumerate(lst_pass):
    print(f"Пароль {i+1}: {password}")