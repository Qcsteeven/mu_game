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
    def action(self, entity : 'Entity', kind : str) -> None:
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
    
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value : str):
        self._name = value

    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value : int):
        self._health = value

    
    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, value : Room):
        self._room = value
        

    @property
    def inventory(self):
        return self.inventory
        
    @inventory.setter
    def inventory(self, value : list[Object]):
        self._inventory = value
        
    
    @property
    def damage(self):
        return self._damage

    @damage.setter
    def danage(self, value : int):
        self.damage = value
        
    
    @property
    def subscribers(self):
        return self._subscribers
    
    @subscribers.setter
    def subscribers(self, value : list[Room | 'Entity' | Object]):
        self._subscribers = value  
