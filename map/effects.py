import random
from collections import defaultdict
from typing import Callable


class Effect:
    effects_room = ["dark", "treasury", "healing", "lock"]

    def __init__(self, dict_rooms_determined_effect : dict):
        self.dict_rooms_determined_effect = dict_rooms_determined_effect # комнаты, которые точно будут с этим эффектом

    def __call__(self, func : Callable)->Callable:
        def wrapper(rooms : list[list]):
            for i in range(0, len(rooms)):
                for j in range(0, len(rooms[i])):
                    rooms[i][j] = random.choice(Effect.effects_room)
               #     rooms[i][j].applyEffect()  # обновляем эффект для каждой комнаты

            # заполняем комнаты с определенным эффектом
            for number_room in self.dict_rooms_determined_effect.keys():
                rooms[number_room - 1][0] = self.dict_rooms_determined_effect.get(number_room)
               # rooms[number_room].applyEffect()

            return func(self)

        return wrapper

my_dict = {1: "dark", 2: "treasury", 3: "healing", 4: "lock"}
my_rooms = [[None, None, None], [None, None, None], [None, None, None]]

@Effect(my_dict)
def apply_effect(rooms : list[list]):
    print("эффекты")

apply_effect(my_rooms)
