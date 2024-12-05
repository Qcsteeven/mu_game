from abc import ABC, abstractmethod

from entities.entity import Entity
from objects.objects import Object
from map.room import Room
from map.effects import Effect

class Room(ABC):
    def __init__(self, isSafe: bool, creations: list[Entity], objects: list[Objects], room_effect: list[Effect]):
       self.isSafe = isSafe
       self.creations = creations
       self.objects = objects
       self.room_effect = room_effect
        
    @abstractmethod
    def update(self) -> None:
       pass
       
    @abstractmethod
    def apply_effect(self) -> None:
       pass
       
    @abstractmethod
    def discharge_effect(self) -> None:
       pass

class Armory(Room):
    type = "Armory"

    def update(self):

       for creation in self.creations:
           creation.update()

       for obj in self.objects:
           obj.update()
          
       for effect in self.roomEffect:
           effect.update()


class Shop(Room):
    type = "Shop"

    def update(self):

       for creation in self.creations:
           creation.update()

       for obj in self.objects:
           obj.update()


class Dungeon(Room):
    type = "Dungeon"
    def update(self):
       for creation in self.creations:
            creation.update()

       for obj in self.objects:
            obj.update()

    @Effect()
    def apply_effect(self):
       for effect in self.roomEffect:
            effect.update()

    def discharge_effect(self):
       self.roomEffect = None

