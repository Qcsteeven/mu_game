from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from management.game_manager import GameManager
    from map.room import Room
    from objects.objects import Object
from entities.entity import Entity
from objects.objects import *
import os


class NPC(Entity):
    def __init__(self, game_manager: GameManager):
        super().__init__(game_manager)

    def action(self, entity: 'Entity', kind: str) -> None:
        pass

    def use_inventory(self) -> Object:
        pass


class trader(NPC):
    type = "trader"
    
    def __init__(self, game_manager: GameManager):
        super().__init__(game_manager)
        self._name = "Trader"
        self.inventory = load_items_from_json('management/text.JSON')
        
    def update(self, *args, **kwargs):
        pass
        

    def action(self, entity: 'Entity', kind: str) -> None:
        pass

    def use_inventory(self) -> Object:
        pass

    def trading(self, money, name_bread):
        thing = None
        for i in self.inventory:
            if i.name == name_bread:
                thing = i
        if (not thing is None) and thing.price <= money:
            confirm = input(
                f'Вы точно хотите купить {name_bread} за {thing.price // 1.2} '
                f'РУБЛЕЙ (чтобы подтвердить введите "Да")')
            if confirm.lower() != 'да':
                return None
            self.inventory.remove(thing)
            print(f"Поздравляю с покупкой {name_bread}")
            return thing
        else:
            if thing in self.inventory:
                print(f'Вам не хватает {thing.price - money}')
            else:
                print(f'Вы что-то путаете у меня нет {name_bread}')
            return None

    def sell(self, name_thing : str, inventory : list[Object]):
        thing = None
        for elem in inventory:
            if name_thing == elem.name:
                thing = elem
        
        confirm = input(
            f'вы точно хотите продать {name_thing} за {thing.price // 1.2} РУБЛЕЙ (что бы подтвердить в ведите "Да")')
        if confirm.lower() == 'да':
            self.inventory = self.inventory + [thing]
            return thing.price // 1.2
        else:
            return 0

    def show_inventory(self):
        num = 1
        for i in self.inventory:
            print(f' {i.name} стоит {i.price} руб. ', end=' |_|_| ')
            num += 1
            if not (num % 5):
                print()


class robber(NPC):
    type = "robber"
    
    def __init__(self, game_manager : GameManager, rarity : str):
        super().__init__(game_manager)
        self._name = "Skeleton"
        self.inventory = load_set_items_npc_json(rarity, 'management/text.JSON')
        for i in self.inventory:
            if i.item_type == 'armor':
                self._armor = i.defense
            if i.item_type == 'sword':
                self._damage = i.attack
                
    def action(self, entity: 'Entity', kind: str) -> None:
        pass

    def use_inventory(self) -> Object:
        pass

    def underattack(self, entity: 'Entity'):
        entity.health -= self.damage
        print(f"{entity.name} нанёс вам удар")
        print(f"У вас осталось {entity.health} здоровья")
        if entity.health <= 0:
            entity.notify("lose")

    def kill(self, entity: 'Entity'):
        entity.inventory = entity.inventory + self.inventory
        

    def update(self, notify_message, *args, **kwargs):
        match (notify_message):
            case ("kill"):
                self.kill(args[0])
            case ("hit"):
                self.underattack(args[0])
                