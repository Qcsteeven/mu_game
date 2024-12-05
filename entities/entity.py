from abc import ABC, abstractmethod
from ..map.room import Room
from ..objects.objects import Object
from ..management.game_manager import GameManager
from typing import Never

class Entity(ABC):

    def __init__(self, game_manager : GameManager, room: Room):
        self._name : str = "Entity"
        self._health : int = 100
        self._inventory : list[Room | Never]  = []
        self._damage : int = 1
        self._subscribers : list[Room | 'Entity' | Object | Never] = []
        self._position : tuple[int] =  (0,0)
        self._room = room
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

    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value : tuple[int]):
        self._position = value       
        