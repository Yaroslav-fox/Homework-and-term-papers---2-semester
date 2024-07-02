# Определение класса Data, который представляет пакет данных
class Data:
    # Инициализатор класса, который принимает данные и IP-адрес
    def __init__(self, data, ip):
        self.data = data  # Сохранение данных
        self.ip = ip  # Сохранение IP-адреса

    # Метод для представления объекта Data в виде строки
    def __str__(self):
        return f"Data(data={self.data}, ip={self.ip})"

    # Метод для представления объекта Data при выводе списка объектов
    __repr__ = __str__

# Определение класса Server, который представляет сервер
class Server:
    ip_counter = 1  # Счетчик IP-адресов

    # Инициализатор класса
    def __init__(self):
        self.ip = Server.ip_counter  # Присвоение уникального IP-адреса серверу
        Server.ip_counter += 1  # Увеличение счетчика IP-адресов
        self.buffer = []  # Создание буфера для хранения принятых пакетов данных

    # Метод для отправки данных
    def send_data(self, data, router):
        router.buffer.append((self.ip, data))  # Добавление данных в буфер роутера

    # Метод для получения данных
    def get_data(self):
        received = self.buffer  # Сохранение принятых данных
        self.buffer = []  # Очистка буфера
        return received  # Возврат принятых данных

    # Метод для получения IP-адреса сервера
    def get_ip(self):
        return self.ip

# Определение класса Router, который представляет роутер
class Router:
    # Инициализатор класса
    def __init__(self):
        self.buffer = []  # Создание буфера для хранения пакетов данных
        self.servers = {}  # Создание словаря для хранения серверов

    # Метод для присоединения сервера к роутеру
    def link(self, server):
        self.servers[server.get_ip()] = server  # Добавление сервера в словарь

    # Метод для отсоединения сервера от роутера
    def unlink(self, server):
        del self.servers[server.get_ip()]  # Удаление сервера из словаря

    # Метод для отправки данных
    def send_data(self):
        for sender_ip, data in self.buffer:  # Обход всех пакетов данных в буфере
            receiver = self.servers[data.ip]  # Получение получателя данных
            receiver.buffer.append((sender_ip, data))  # Добавление данных в буфер получателя
        self.buffer = []  # Очистка буфера

