# Импортируем класс: Data, Server, Router в отдельный файл для тестирования программы
from Conect_the_server_and_router import Data
from Conect_the_server_and_router import Server
from Conect_the_server_and_router import Router

# Создаем роутер
router = Router()

# Создаем серверы
sv1 = Server()
sv2 = Server()
sv3 = Server()

# Соединяем серверы с роутером
router.link(sv1)
router.link(sv2)
router.link(sv3)

# Отправляем данные от sv1 к sv2 и sv3
sv1.send_data(Data("Hello, Server 2", sv2.get_ip()), router)
sv1.send_data(Data("Hello, Server 3", sv3.get_ip()), router)

# Отправляем данные от sv2 к sv1
sv2.send_data(Data("Hello, Server 1", sv1.get_ip()), router)

# Отправляем данные от sv3 к sv2
sv3.send_data(Data("Hello, Server 2", sv2.get_ip()), router)

# Роутер пересылает все пакеты
router.send_data()

# Получаем данные на серверах
print(sv1.get_data())  # Должно вывести: [(2, Data(data=Hello, Server 1, ip=1))]
print(sv2.get_data())  # Должно вывести: [(1, Data(data=Hello, Server 2, ip=2)), (3, Data(data=Hello, Server 2, ip=2))]
print(sv3.get_data())  # Должно вывести: [(1, Data(data=Hello, Server 3, ip=3))]