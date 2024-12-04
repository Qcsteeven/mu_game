def decorator_effect_person(action):
    def wrapper(self, *args, **kwargs):
        if self.type_room == "dark":
            print("вероятность попадания по врагу снижена на 70%")

        if self.type_room == "treasury":
            print("вот это удача: Вы нашли сокровищницу")

        if self.type_room == "healing":
            print("ура: Наконец-то я могу подлечить свои раны")

        if self.type_room == "lock":
            print("Хмм, эта комната заперта-нужно найти ключ")

        return action(self)
    return wrapper


class Effect:
    def __init__(self, type_room):
        self.type_room = type_room
