import random

from collections import defaultdict
from typing import Callable


class Effect:
    effects_room = ["dark", "treasury", "healing", "lock"]

    def __init__(self):
        pass

    def __call__(self, func):
        def wrapper(self, *args, **kwargs):
            our_effect = random.choice(Effect.effects_room)
            self.roomEffect = our_effect

            return func(self, *args, **kwargs)

        return wrapper
