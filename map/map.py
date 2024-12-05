from map.room import *
import random


class Map:
    _instance = None
    _isCreated = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Map, cls).__new__(cls)
        return cls._instance

    def __init__(self, pattern, Entities):
        if Map._isCreated == True:
            return
        Map._isCreated = True
        leng = len(pattern)
        self._map = [''] * leng
        for i in range(leng):
            self._map[i] = pattern[i].copy()
        for i in range(leng):
            for j in range(len(self._map[i])):
                if self._map[i][j] == 's':
                    self._map[i][j] = Room(True, ["Shop"], [], [])
                elif self._map[i][j] == 'd':
                    enemy = random.choice(Entities)
                    self._map[i][j] = Room(False, [enemy], [], [])
                else:
                    issafe = random.randint(0, 1)
                    if issafe == 1:
                        self._map[i][j] = Room(True, ["Shop"], [], [])
                    else:
                        enemy = random.choice(Entities)
                        self._map[i][j] = Room(False, [enemy], [], [])

    def get_room(self, x_pos, y_pos):
        return self._map[x_pos][y_pos]
