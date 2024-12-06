import random


class Effect:
    effects_room = ["dark", "treasury", "healing", "lock"]

    def __init__(self):
        pass

    def __call__(self, cls):
        class WrapperCls(cls):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                our_effect = random.choice(Effect.effects_room)
                self.room_effect = our_effect
        return WrapperCls
