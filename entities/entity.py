from abc import ABC, abstractmethod
from ..map.room import Room
from ..objects.objects import Object
from ..management.game_manager import GameManager


class Entity(ABC):

    def __init__(self, game_manager: GameManager, health: int, damage: int, room: Room, inventory: list[Object],
                 subscribers: list[Room | Entity | Object]):
        self._health = health
        self._room = room
        self._inventory = inventory
        self._damage = damage
        self._subscribers = subscribers
        self.game_manager = game_manager

    @abstractmethod
    def action(self, entity: Entity, kind: str):
        pass
