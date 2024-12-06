class Effect:
    def __init__(self):
        pass

    def __call__(self, action):
        def wrapper(self, *args, **kwargs):
            if self.room.room_effect == "dark":
                print("вероятность попадания по врагу снижена на 70%")

            if self.room.room_effect == "treasury":
                print("вот это удача: Вы нашли сокровищницу")

            if self.room.room_effect == "healing":
                print("ура: Наконец-то я могу подлечить свои раны")

            if self.room.room_effect == "lock":
                print("Хмм, эта комната заперта-нужно найти ключ")

            return action(self, *args, **kwargs)

        return wrapper
