from __future__ import annotations
from typing import TYPE_CHECKING

# Проверка типов для предотвращения циклического импорта
if TYPE_CHECKING:
    from entities.entity import Entity  # Класс сущностей (например, враги, NPC)
    from objects.objects import Object  # Класс объектов (например, предметы)
    from map.room import Room  # Комнаты
from map.effects import Effect  # Эффекты в комнате
from abc import ABC, abstractmethod

# Базовый абстрактный класс для всех типов комнат
class Room(ABC):
    def __init__(self, isSafe: bool, creations: list[Entity], objects: list[Object], room_effects: list[Effect], room_effect=None):
        # Указывает, безопасна ли комната (нет врагов и ловушек)
        self.isSafe = isSafe
        # Список созданий в комнате (например, враги, NPC)
        self.creations = creations
        # Список объектов, находящихся в комнате
        self.objects = objects
        # Активный эффект в комнате (например, бафф или дебафф)
        self.room_effect = room_effect

        # Флаг, указывающий, была ли комната посещена
        self.visited = False

    # Метод для обновления состояния комнаты (реализуется в подклассах)
    @abstractmethod
    def update(self) -> None:
        pass

    # Метод для применения эффектов комнаты (реализуется в подклассах)
    @abstractmethod
    def apply_effect(self) -> None:
        pass

    # Метод для удаления эффекта из комнаты (реализуется в подклассах)
    @abstractmethod
    def discharge_effect(self) -> None:
        pass


# Класс "Оружейная", наследующий базовый класс Room
class Armory(Room):
    type = "Armory"  # Тип комнаты

    def update(self, notify_message: str, *args, **kwargs):
        # Обработка различных уведомлений
        match notify_message:
            case "move":
                self.hello_message(*args, **kwargs)  # Отправка приветственного сообщения
            case _:
                pass

    def hello_message(self, player: Player):
        # Приветствие при входе в оружейную
        if self == player.room:
            print("Добро пожаловать в оружейную")

    def apply_effect(self) -> None:
        pass

    def discharge_effect(self) -> None:
        pass


# Класс "Магазин", наследующий базовый класс Room
class Shop(Room):
    type = "Shop"  # Тип комнаты

    def update(self, notify_message: str, *args, **kwargs):
        # Обработка различных уведомлений
        match notify_message:
            case "move":
                self.hello_message(*args, **kwargs)  # Отправка приветственного сообщения
            case _:
                pass

    def hello_message(self, player: Player):
        # Приветствие при входе в магазин
        if self == player.room:
            print("Добро пожаловать в магазин")

    def apply_effect(self) -> None:
        pass

    def discharge_effect(self) -> None:
        pass


# Класс "Темница" с применением эффекта
@Effect()  # Применение эффекта к комнате
class Dungeon(Room):
    type = "Dungeon"  # Тип комнаты

    def update(self):
        # Обновление состояния созданий в комнате
        for creation in self.creations:
            creation.update()

        # Обновление состояния объектов в комнате
        for obj in self.objects:
            obj.update()

    def apply_effect(self):
        # Применение всех эффектов комнаты
        for effect in self.roomEffect:
            effect.update()

    def discharge_effect(self):
        # Удаление текущего эффекта из комнаты
        self.room_effect = None


# Класс "Пустая комната"
class EmptyRoom(Room):
    type = "EmptyRoom"  # Тип комнаты

    def update(self, notify_message: str, *args, **kwargs):
        # Обработка различных уведомлений
        match notify_message:
            case "move":
                self.hello_message(*args, **kwargs)  # Отправка приветственного сообщения
            case _:
                pass

    def hello_message(self, player: Player):
        # Приветствие при входе в пустую комнату
        if self == player.room:
            print("Вы попали в пустую комнату")

    def apply_effect(self) -> None:
        pass

    def discharge_effect(self) -> None:
        pass


# Класс "Комната босса"
class BossRoom(Room):
    type = "BossRoom"  # Тип комнаты

    def update(self, notify_message: str, *args, **kwargs):
        # Обработка различных уведомлений
        match notify_message:
            case "move":
                self.hello_message(*args, **kwargs)  # Отправка приветственного сообщения
            case _:
                pass

    def hello_message(self, player: Player):
        # Приветствие при входе в комнату босса
        if self == player.room:
            print("Вы попали в покои босса")

    def apply_effect(self) -> None:
        pass

    def discharge_effect(self) -> None:
        pass
