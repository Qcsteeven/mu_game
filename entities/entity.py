from abc import ABC, abstractmethod
from ..map.room import Room 
from ..objects.objects import Object
from ..management.game_manager import GameManager

class Entity(ABC):

    def __init__(self, game_manager : GameManager, name : str, health : int, damage : int, room: Room, inventory: list[Object], subscribers: list[Room | 'Entity' | Object]):
        self._name = name
        self._health = health
        self._room = room
        self._inventory = inventory
        self._damage = damage
        self._subscribers = subscribers
        self.game_manager = game_manager

    @abstractmethod
    def action(self, entity : Entity, kind : str) -> None:
        pass

    @abstractmethod
    def use_inventory(self) -> Object:
        pass

    def subscribe(self, subscriber : GameManager | 'Entity' | Room | Object) -> None:
        self._subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber : GameManager | 'Entity' | Room | Object) -> None:
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)
    
    def notify(self, action : str) -> None:
        for elem in self._subscribers:
            elem.update(action)
    
        
        
