from map.room import *
import random
from entities.entity import Entity

class Map:
    _instance = None
    _isCreated = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Map, cls).__new__(cls)
        return cls._instance

    def __init__(self, pattern: list[list[str]], Entities: list[Entity]):
        if Map._isCreated == True:
            return
        Map._isCreated = True
        leng = len(pattern)
        self.pattern = [[] for _ in range(leng)]
        for i in range(leng):
            self.pattern[i] = pattern[i].copy()
        self.rows = leng
        self.cols = len(pattern[0])
        self._map = [[] for _ in range(leng)]
        for i in range(leng):
            for j in range(len(pattern[i])):
                if pattern[i][j] == 's':
                    self._map[i].append(Shop(True, [], [], []))
                elif pattern[i][j] == 'a':
                    self._map[i].append(Armory(True, [], [], []))
                elif pattern[i][j] == 'd':
                    enemy = random.choice(Entities)
                    self._map[i].append(Dungeon(False, [enemy], [], []))
                elif pattern[i][j] == "B":
                    self._map[i].append(BossRoom(True, [], [], []))
                elif pattern[i][j] == '-':
                    self._map[i].append(EmptyRoom(True, [], [], []))
                
        self._map[0][0].visited = True

    def get_room(self, x_pos: int, y_pos: int):
        return self._map[x_pos][y_pos]

    def avail_directions(self, x_pos: int, y_pos: int):
        up = 1 if x_pos > 0 else 0
        down = 1 if x_pos < self.rows - 1 else 0
        left = 1 if y_pos > 0 else 0
        right = 1 if y_pos < self.rows - 1 else 0
        return up, down, left, right

    def map_size(self):
        return self.rows, self.cols

    def show_map(self, x, y) -> None:
        arr = [['?'] * self.cols for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                if self._map[i][j].visited:
                    arr[i][j] = self.pattern[i][j]
        
        arr[x][y] = "X"
        for i in arr:
            print(*i)

    def make_visited(self, pos_x: int, pos_y: int) -> None:
        self._map[pos_x][pos_y].visited = True
