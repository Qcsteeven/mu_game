from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from management.game_manager import GameManager
    from map.room import Room
    from objects.objects import Object
from entities.entity import Entity 

class Player(Entity):
    def __init__(self, game_manager : GameManager):
        super().__init__(game_manager)
        self._money = 0
        
    def action(self, kind : str, *args, **kwargs) -> None:
        if type(args[0]) is Entity:
            self.subscribe(entity)
        match (kind):
            case ("attack"):
                self.attack(*args, **kwargs)
            case ("buy"):
                self.buy(*args, **kwargs)
            case ("sell"):
                self.sell(*args, **kwargs)
            case ("move"):
                self.move(*args, **kwargs)
            case (_):
                print("Хммм... Я так не умею")
        if type(args[0]) is Entity:
            self.unsubscribe(entity)
    
    def use_inventory(self) -> None:
        pass
        
    def attack(self, entity : 'Entity', damage : int) -> None:
        if entity.health - damage > 0:
            entity.health -= damage
        else:
            entity.health = 0
            entity.notify("kill", entity)
            
    def sell(self, entity : 'Entity', thing : Object):
        money = entity.sell(thing)
        if money:
            self._money += money
            self.inventaty.remove(thing)        

    def buy(self, entity : 'Entity', thing : str) -> None:
        new_thing = entity.trading(self._money, thing)
        if new_thing:
            self.inventory.append(new_thing)
            self._money -= new_thing.cost
            
    def move(self, kind : str, *args, **kwargs):
        new_pos = tuple()
        if kind == "step":
            direction = args[0]
            match (direction):
                case ("left"):
                    new_pos = (self.position[0] - 1, self.position[1])
                case ("right"):
                    new_pos = (self.position[0] + 1, self.position[1])
                case ("up"):
                    new_pos = (self.position[0], self.position[1] + 1)
                case ("down"):
                    new_pos = (self.position[0], self.position[1] - 1)
                case (_):
                    print("Вы остались на месте")
        else:
            new_pos = (args[0], args[1])
        self.notify("move", new_pos, self)
            
        
    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, value : int):
        self._money = value
