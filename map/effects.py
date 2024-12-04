import random
from random import choice

class Effect:
    effect_room = ["dark", "treasury", "healing", "lock"]

    def __init__(self, type_room):
        self.type_room = type_room

    # number_room - номер комнаты, на которую нужно накинуть определенный эффект-type_room
    def apple_effect_room(self, graph : list[[]], type_room, number_room = -1):

        for i in range(0, len(graph)):
            for j in range(0, len(graph[i])):
                graph[i][j] = random.choice(Effect.effect_room)

        if number_room != -1:
            graph[number_room] = type_room

        print(*graph)
