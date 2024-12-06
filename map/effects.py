import random


# Декоратор для добавления случайного эффекта к комнате
class Effect:
    # Список возможных эффектов, которые могут быть применены к комнате
    effects_room = ["dark", "treasury", "healing", "lock"]

    def __init__(self):
        pass  # Конструктор не делает ничего, так как нам не нужны параметры

    def __call__(self, cls):
        """
        Метод __call__ позволяет использовать объект класса Effect как декоратор.
        Он оборачивает переданный класс (cls) в новый класс-обёртку.
        """
        # Класс-обёртка для добавления эффекта к оригинальному классу
        class WrapperCls(cls):
            def __init__(self, *args, **kwargs):
                # Инициализация родительского класса
                super().__init__(*args, **kwargs)
                # Выбор случайного эффекта из списка
                our_effect = random.choice(Effect.effects_room)
                # Добавление эффекта в качестве атрибута объекта комнаты
                self.room_effect = our_effect

        # Возвращаем обёрнутый класс
        return WrapperCls
