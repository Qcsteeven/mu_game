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
    """
    Базовый класс для всех неигровых персонажей (NPC).
    """

    def __init__(self, game_manager: GameManager):
        """
        Конструктор для NPC.

        :param game_manager: Экземпляр GameManager, управляющий игрой.
        """
        super().__init__(game_manager)

    def action(self, entity: 'Entity', kind: str) -> None:
        """
        Заглушка для действия NPC. Должен быть переопределен в дочерних классах.
        """
        pass

    def use_inventory(self) -> Object:
        """
        Заглушка для использования инвентаря NPC. Должен быть переопределен в дочерних классах.
        """
        pass


class trader(NPC):
    """
    Класс для торговца в игре.
    """
    type = "trader"  # Тип NPC.

    def __init__(self, game_manager: GameManager):
        """
        Конструктор для торговца.

        :param game_manager: Экземпляр GameManager, управляющий игрой.
        """
        super().__init__(game_manager)
        self._name = "Trader"  # Имя торговца.
        # Загрузка инвентаря из JSON-файла.
        self.inventory = load_items_from_json('management/text.JSON')

    def update(self, *args, **kwargs):
        """
        Метод обновления для торговца. Пока не используется.
        """
        pass

    def action(self, entity: 'Entity', kind: str) -> None:
        """
        Заглушка для действия торговца.
        """
        pass

    def use_inventory(self) -> Object:
        """
        Заглушка для использования инвентаря торговца.
        """
        pass

    def trading(self, money, name_bread):
        """
        Метод для покупки предмета у торговца.

        :param money: Количество денег у игрока.
        :param name_bread: Название предмета.
        :return: Объект, если покупка успешна, иначе None.
        """
        thing = None
        for i in self.inventory:
            if i.name == name_bread:
                thing = i
        if thing and thing.price <= money:
            confirm = input(
                f'Вы точно хотите купить {name_bread} за {thing.price} РУБЛЕЙ (чтобы подтвердить введите "Да") ')
            if confirm.lower() != 'да':
                return None
            self.inventory.remove(thing)
            print(f"Поздравляю с покупкой {name_bread}")
            return thing
        else:
            if thing:
                print(f'Вам не хватает {thing.price - money}')
            else:
                print(f'Вы что-то путаете, у меня нет {name_bread}')
            return None

    def sell(self, name_thing: str, inventory: list[Object]):
        """
        Метод для продажи предмета торговцу.

        :param name_thing: Название предмета.
        :param inventory: Инвентарь игрока.
        :return: Сумма, полученная за продажу.
        """
        thing = None
        for elem in inventory:
            if name_thing == elem.name:
                thing = elem

        confirm = input(
            f'Вы точно хотите продать {name_thing} за {thing.price // 1.2} РУБЛЕЙ (чтобы подтвердить введите "Да") ')
        if confirm.lower() == 'да':
            self.inventory.append(thing)
            return thing.price // 1.2
        else:
            return 0

    def show_inventory(self):
        """
        Метод для отображения инвентаря торговца.
        """
        num = 1
        for i in self.inventory:
            print(f' {i.name} стоит {i.price} руб. ', end=' |_|_| ')
            num += 1
            if not (num % 5):
                print()


class robber(NPC):
    """
    Класс для разбойника в игре.
    """
    type = "robber"  # Тип NPC.

    def __init__(self, game_manager: GameManager, rarity: str):
        """
        Конструктор для разбойника.

        :param game_manager: Экземпляр GameManager.
        :param rarity: Редкость предметов в инвентаре разбойника.
        """
        super().__init__(game_manager)
        self._name = "Skeleton"  # Имя разбойника.
        # Загрузка инвентаря из JSON-файла с учетом редкости.
        self.inventory = load_set_items_npc_json(rarity, 'management/text.JSON')
        for i in self.inventory:
            if i.item_type == 'armor':
                self._armor = i.defense
            if i.item_type == 'sword':
                self._damage = i.attack

    def action(self, entity: 'Entity', kind: str) -> None:
        """
        Заглушка для действия разбойника.
        """
        pass

    def use_inventory(self) -> Object:
        """
        Заглушка для использования инвентаря разбойника.
        """
        pass

    def underattack(self, entity: 'Entity'):
        """
        Метод, описывающий атаку на сущность.

        :param entity: Сущность, на которую совершается атака.
        """
        entity.health -= self.damage
        print(f"{entity.name} нанес вам удар")
        print(f"У вас осталось {entity.health} здоровья")
        if entity.health <= 0:
            entity.notify("lose")

    def kill(self, entity: 'Entity'):
        """
        Метод для передачи инвентаря убитой сущности разбойнику.

        :param entity: Убитая сущность.
        """
        entity.inventory += self.inventory

    def update(self, notify_message, *args, **kwargs):
        """
        Метод обновления состояния разбойника.

        :param notify_message: Тип уведомления.
        """
        match notify_message:
            case "kill":
                self.kill(args[0])
            case "hit":
                self.underattack(args[0])
