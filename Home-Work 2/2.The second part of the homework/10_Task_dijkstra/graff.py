# Объявляем класс Vertex
class Vertex:
    # Инициализируем класс с пустым списком связей
    def __init__(self):
        self._links = []

    # Определяем свойство links для доступа к списку связей
    @property
    def links(self):
        return self._links


# Объявляем класс Link
class Link:
    # Инициализируем класс с параметрами v1, v2 и dist
    def __init__(self, v1: Vertex, v2: Vertex, dist: float):
        self.v1 = v1
        self.v2 = v2
        self.dist = dist


# Объявляем класс LinkedGraph
class LinkedGraph:
    # Инициализируем класс с пустым списком вершин и связей
    def __init__(self):
        self._vertex = []
        self._links = []

    # Добавляем новую связь в граф
    def add_link(self, link: Link):
        self._links.append(link)
        if link.v1 not in self._vertex:
            self._vertex.append(link.v1)
        if link.v2 not in self._vertex:
            self._vertex.append(link.v2)

    # Находим кратчайший путь от вершины v1 до вершины v6
    def find_path(self, v1: Vertex, v6: Vertex):
        # Здесь должен быть ваш код для поиска пути
        pass


# Объявляем класс Station, который наследуется от класса Vertex
class Station(Vertex):
    # Инициализируем класс с параметром name
    def __init__(self, name: str):
        super().__init__()
        self.name = name


# Объявляем класс LinkMetro, который наследуется от класса Link
class LinkMetro(Link):
    # Инициализируем класс с параметрами v1, v2 и dist
    def __init__(self, v1: Station, v2: Station, dist: float):
        super().__init__(v1, v2, dist)
