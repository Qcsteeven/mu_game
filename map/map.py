from __future__ import annotations
from typing import TYPE_CHECKING

# Импортируем классы только для проверки типов
if TYPE_CHECKING:
    from management.game_manager import GameManager  # Менеджер игры
from map.room import *  # Импорт классов комнат
import random
from entities.npc import trader, robber  # НПС (торговец и грабитель)


# Класс карты для управления расположением и типами комнат
class Map:
    _instance = None  # Синглтон: хранит единственный экземпляр класса
    _isCreated = False  # Флаг для проверки, создан ли объект

    def __new__(cls, *args, **kwargs):
        # Реализация синглтона: если объект не создан, создаем его
        if cls._instance is None:
            cls._instance = super(Map, cls).__new__(cls)
        return cls._instance

    def __init__(self, pattern: list[list[str]], game_manager: GameManager):
        # Если объект уже создан, повторная инициализация игнорируется
        if Map._isCreated:
            return
        Map._isCreated = True

        # Копируем шаблон карты (матрица символов)
        leng = len(pattern)
        self.pattern = [[] for _ in range(leng)]
        for i in range(leng):
            self.pattern[i] = pattern[i].copy()

        # Размеры карты
        self.rows = leng
        self.cols = len(pattern[0])

        # Генерация карты на основе шаблона
        self._map = [[] for _ in range(leng)]
        for i in range(leng):
            for j in range(len(pattern[i])):
                if pattern[i][j] == 's':
                    # Если комната — магазин
                    shop = Shop(True, [], [], [])
                    tr = trader(game_manager)  # Создаем торговца
                    tr.room = shop
                    shop.creations.append(tr)  # Добавляем торговца в список созданий комнаты
                    self._map[i].append(shop)
                elif pattern[i][j] == 'a':
                    # Если комната — оружейная
                    armory = Armory(True, [], [], [])
                    self._map[i].append(armory)
                elif pattern[i][j] == 'd':
                    # Если комната — темница
                    dungeon = Dungeon(False, [], [], [])
                    rb = robber(game_manager, random.choice(["common", "rare", "epic"]))  # Грабитель с рандомным качеством
                    rb.room = dungeon
                    dungeon.creations.append(rb)  # Добавляем грабителя в список созданий
                    self._map[i].append(dungeon)
                elif pattern[i][j] == "B":
                    # Если комната — комната босса
                    self._map[i].append(BossRoom(True, [], [], []))
                elif pattern[i][j] == '-':
                    # Если комната — пустая
                    self._map[i].append(EmptyRoom(True, [], [], []))

        # Отмечаем начальную комнату как посещённую
        self._map[0][0].visited = True

    # Получение объекта комнаты по координатам
    def get_room(self, x_pos: int, y_pos: int):
        return self._map[x_pos][y_pos]

    # Проверка доступных направлений из текущей комнаты
    def avail_directions(self, x_pos: int, y_pos: int):
        up = 1 if x_pos > 0 else 0  # Проверка, можно ли двигаться вверх
        down = 1 if x_pos < self.rows - 1 else 0  # Проверка, можно ли двигаться вниз
        left = 1 if y_pos > 0 else 0  # Проверка, можно ли двигаться влево
        right = 1 if y_pos < self.cols - 1 else 0  # Проверка, можно ли двигаться вправо
        return up, down, left, right

    # Получение размеров карты
    def map_size(self):
        return self.rows, self.cols

    # Отображение карты для игрока
    def show_map(self, pos) -> None:
        x, y = pos  # Текущая позиция игрока
        arr = [['?'] * self.cols for i in range(self.rows)]  # Изначально все комнаты скрыты
        for i in range(self.rows):
            for j in range(self.cols):
                if self._map[i][j].visited:
                    arr[i][j] = self.pattern[i][j]  # Показываем посещённые комнаты
        arr[x][y] = "X"  # Отмечаем текущую позицию игрока
        for i in arr:
            print(*i)  # Вывод карты на экран

    # Отметить комнату как посещённую
    def make_visited(self, pos_x: int, pos_y: int) -> None:
        self._map[pos_x][pos_y].visited = True
