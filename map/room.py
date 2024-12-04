from abc import ABC, abstractmethod
class Room(ABC):
            def __init__(self, isSafe: bool, creations: list[Entity], objects: list[Objects], roomEffect: list[roomEffect]):
                self.isSafe = isSafe
                self.creations = creations
                self.objects = objects
                self.roomEffect = roomEffect
        
            @abstractmethod
            def update(self) -> None:
                    pass
            @abstractmethod
            def applyEffect(self) -> None:
                    pass
            @abstractmethod
            def dischargeEffect(self) -> None:
                    pass

class  Armory(Room):
    type = "Armory"
    def update(self):
           for creation in self.creations:
                  creation.update()

           for obj in self.objects:
                  obj.update()
          
           for effect in self.roomEffect:
                  effect.update()


class  Shop(Room):
    type = "Shop"
    def update(self):
           for creation in self.creations:
                  creation.update()

           for obj in self.objects:
                  obj.update()


class  Dangeon(Room):
    type = "Dangeon"
    def update(self):
           for creation in self.creations:
                  creation.update()

           for obj in self.objects:
                  obj.update()
          
    def applyEffect(self):
           for effect in self.roomEffect:
                  effect.update()

    def dischargeEffect(self):
           self.roomEffect = None

