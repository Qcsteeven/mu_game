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
        self._money = 100
    
    def action(self, kind : str, *args, **kwargs) -> None:
        if len(args) > 0 and isinstance(args[0], Entity):
            self.subscribe(args[0])
        match (kind):
            case ("attack"):
                self.attack(*args, **kwargs)
            case ("buy"):
                self.buy(*args, **kwargs)
            case ("sell"):
                self.sell(*args, **kwargs)
            case ("move"):
                self.move(*args, **kwargs)
            case ("show"):
                self.show_inventory(*args, **kwargs)
            case ("use"):
                self.use_inventory(*args, **kwargs)
            case (_):
                print("Хммм... Я так не умею")
        if len(args) > 0 and type(args[0]) is Entity:
            self.unsubscribe(args[0])
    
    def use_inventory(self, item : str = None) -> None:
        if item and item in self._inventory:
            match (item.item_type):
                case ("healing_potion"):
                    self.health += item.healing
                case ("armor"):
                    self.armor += item.defense
                case ("sword"):
                    self.damage += item.attack
                case (_):
                    print("Я не умею использовать такой предмет")
        else:
            print("Такого у меня нет(")
            
    def show_inventory(self) -> None:
        for item in self._inventory:
            print(f"Название предмета: {item.name}")
            print(f"Описание предмета: {item.description}")
            print(f"Тип предмета: {item.item_type}")
            match (item.item_type):
                case ("healing_potion"):
                    print(f"Исцеление: {item.healing}")
                case ("armor"):
                    print(f"Броня: {item.defense}")
                case ("sword"):
                    print(f"Урон: {item.attack}")
                case (_):
                    pass
            print(f"Качество: {item.quality}")
            print(f"Цена: {item.price}")
            input("Для того, чтобы увидеть следуюший предмет, нажмите Enter")
        else:
            print("Инвентарь закончился")
        
    def attack(self, entity : 'Entity') -> None:
        if entity.health - self._damage > 0:
            entity.health -= self._damage
            print(f"У {entity.name} осталось {entity.health} здоровья")
            self.notify("hit", entity)
        else:
            entity.health = 0
            self.notify("kill", entity)
            
    def sell(self, entity : 'Entity', thing : str) -> None:
        money = entity.sell(thing, self.inventory)
        th = None
        for elem in self.inventory:
            if thing == elem.name:
                th = elem
        if money:
            self._money += money
            self.inventory.remove(th)        

    def buy(self, entity : 'Entity', thing : str) -> None:
        new_thing = entity.trading(self._money, thing)
        if new_thing:
            self.inventory.append(new_thing)
            self._money -= new_thing.price

    def move(self, kind : str, *args, **kwargs) -> None:
        new_pos = tuple()
        if kind == "step":
            direction = args[0]
            match (direction):
                case ("left"):
                    new_pos = (self.position[0], self.position[1] - 1)
                case ("right"):
                    new_pos = (self.position[0], self.position[1] + 1)
                case ("up"):
                    new_pos = (self.position[0] - 1, self.position[1])
                case ("down"):
                    new_pos = (self.position[0] + 1, self.position[1])
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
