class Effect:
    """
    Класс для применения эффектов комнат. Реализован через метод __call__, что позволяет
    объектам этого класса вызываться как функции.
    """
    def __init__(self):
        """
        Конструктор класса Effect. Пока не инициализирует никаких параметров.
        """
        pass

    def __call__(self, room):
        """
        Применяет эффект к комнате на основе свойства `room_effect`.

        :param room: Комната, к которой применяется эффект.
        """
        if room.room_effect == "dark":
            # Эффект: Снижение вероятности попадания по врагу.
            print("вероятность попадания по врагу снижена на 70%")

        if room.room_effect == "treasury":
            # Эффект: Сокровищница найдена.
            print("вот это удача: Вы нашли сокровищницу")

        if room.room_effect == "healing":
            # Эффект: Комната с возможностью восстановления здоровья.
            print("ура: Наконец-то я могу подлечить свои раны")

        if room.room_effect == "lock":
            # Эффект: Запертая комната, требуется ключ.
            print("Хмм, эта комната заперта-нужно найти ключ")
