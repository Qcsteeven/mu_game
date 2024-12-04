from room import *
import random
class Map:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance=super(Map,cls).__new__(cls)
        return cls._instance

    def __init__(self, pattern, Entities):
        leng = len(pattern)
        self._map = ['']*leng
        for i in range(leng):
            self._map[i]=pattern[i].copy()
        for i in range(leng):
            for j in range(len(self._map[i])):
                if self._map[i][j]=='s':
                    self._map[i][j]=Room(True,["Shop"], [], [])
                elif self._map[i][j]=='d':
                    enemy = Entities[random.randint(0,len(Entities))]
                    self._map[i][j]=Room(False,[enemy],[],[])
                else:
                    issafe = random.randint(0,1)
                    if issafe == 1:
                        self._map[i][j] = Room(True, ["Shop"], [], [])
                    else:
                        enemy = Entities[random.randint(0, len(Entities))]
                        self._map[i][j] = Room(False, [enemy], [], [])
