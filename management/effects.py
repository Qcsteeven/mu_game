class Effect:
    def __init__(self):
        pass

    def __call__(self, room):
        if room.room_effect == "dark":
            print("вероятность попадания по врагу снижена на 70%")

        if room.room_effect == "treasury":
            print("вот это удача: Вы нашли сокровищницу")

        if room.room_effect == "healing":
            print("ура: Наконец-то я могу подлечить свои раны")

        if room.room_effect == "lock":
            print("Хмм, эта комната заперта-нужно найти ключ")

            