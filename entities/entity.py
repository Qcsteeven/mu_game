from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from map.room import Room
    from objects.objects import Object
    from management.game_manager import GameManager

from abc import ABC, abstractmethod


class Entity(ABC):
    """
    Абстрактный базовый класс для всех сущностей в игре.
    """

    def __init__(self, game_manager: GameManager):
        """
        Конструктор класса Entity.

        :param game_manager: Экземпляр класса GameManager, управляющий игрой.
        """
        self._name: str = "Entity"  # Имя сущности.
        self._health: int = 100  # Здоровье сущности.
        self._inventory: list[Object] = []  # Инвентарь сущности.
        self._damage: int = 1  # Урон, наносимый сущностью.
        self._subscribers: list[GameManager | Room | 'Entity' | Object] = [game_manager]  # Подписчики для уведомлений.
        self._position: tuple[int] = (0, 0)  # Координаты сущности на карте.
        self._armor: int = 0  # Защита сущности.
        self._room: Room | None = None  # Комната, в которой находится сущность.
        self.game_manager = game_manager  # Ссылка на управляющий объект игры.

    @abstractmethod
    def action(self, entity: 'Entity', kind: str) -> None:
        """
        Абстрактный метод для выполнения действия. Должен быть реализован в дочерних классах.

        :param entity: Целевая сущность.
        :param kind: Тип действия.
        """
        pass

    @abstractmethod
    def use_inventory(self) -> Object:
        """
        Абстрактный метод для использования объекта из инвентаря. Должен быть реализован в дочерних классах.

        :return: Используемый объект.
        """
        pass

    def subscribe(self, subscriber: GameManager | 'Entity' | Room | Object) -> None:
        """
        Добавляет объект в список подписчиков.

        :param subscriber: Объект, подписывающийся на уведомления.
        """
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: GameManager | 'Entity' | Room | Object) -> None:
        """
        Удаляет объект из списка подписчиков.

        :param subscriber: Объект, отписывающийся от уведомлений.
        """
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def notify(self, action: str, *args, **kwargs) -> None:
        """
        Уведомляет всех подписчиков о событии.

        :param action: Тип события.
        :param args: Дополнительные аргументы.
        :param kwargs: Дополнительные именованные аргументы.
        """
        for elem in self._subscribers:
            elem.update(action, *args, **kwargs)

    # Свойства с геттерами и сеттерами для удобного управления атрибутами сущности.

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = value

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, value: Room):
        self._room = value

    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value: list[Object]):
        self._inventory = value

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value: int):
        self._damage = value

    @property
    def subscribers(self):
        return self._subscribers

    @subscribers.setter
    def subscribers(self, value: list[Room | 'Entity' | Object]):
        self._subscribers = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value: tuple[int]):
        self._position = value

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, value: int):
        self._armor = value
