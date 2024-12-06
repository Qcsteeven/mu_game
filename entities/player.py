from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from management.game_manager import GameManager
    from map.room import Room
    from objects.objects import Object
from entities.entity import Entity


class Player(Entity):
    """
    Класс для управления действиями игрока в игре.
    """

    def __init__(self, game_manager: GameManager):
        """
        Конструктор игрока.

        :param game_manager: Экземпляр GameManager, управляющий игрой.
        """
        super().__init__(game_manager)
        self._money = 100  # Изначальная сумма денег у игрока.

    def action(self, kind: str, *args, **kwargs) -> None:
        """
        Выполняет действие игрока.

        :param kind: Тип действия (например, "attack", "move").
        :param args: Дополнительные аргументы для действия.
        :param kwargs: Дополнительные именованные аргументы для действия.
        """
        if len(args) > 0 and isinstance(args[0], Entity):
            self.subscribe(args[0])  # Подписка на изменения объекта.
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
        if len(args) > 0 and isinstance(args[0], Entity):
            self.unsubscribe(args[0])  # Отписка после выполнения действия.

    def use_inventory(self, item: str = None) -> None:
        """
        Использует предмет из инвентаря.

        :param item: Название предмета для использования.
        """
        if item and item in self._inventory:
            match (item.item_type):
                case ("healing_potion"):
                    self.health += item.healing  # Лечение.
                case ("armor"):
                    self.armor += item.defense  # Усиление брони.
                case ("sword"):
                    self.damage += item.attack  # Усиление атаки.
                case (_):
                    print("Я не умею использовать такой предмет")
        else:
            print("Такого у меня нет(")

    def show_inventory(self) -> None:
        """
        Отображает содержимое инвентаря игрока.
        """
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
            input("Для того, чтобы увидеть следующий предмет, нажмите Enter")
        else:
            print("Инвентарь закончился")

    def attack(self, entity: 'Entity') -> None:
        """
        Атакует указанную сущность.

        :param entity: Сущность, на которую совершается атака.
        """
        if entity.health - self._damage > 0:
            entity.health -= self._damage
            print(f"У {entity.name} осталось {entity.health} здоровья")
            self.notify("hit", entity)
        else:
            entity.health = 0
            self.notify("kill", entity)

    def sell(self, entity: 'Entity', thing: str) -> None:
        """
        Продает предмет торговцу.

        :param entity: Сущность, осуществляющая покупку.
        :param thing: Название предмета.
        """
        money = entity.sell(thing, self.inventory)
        th = None
        for elem in self.inventory:
            if thing == elem.name:
                th = elem
        if money:
            self._money += money
            self.inventory.remove(th)

    def buy(self, entity: 'Entity', thing: str) -> None:
        """
        Покупает предмет у сущности.

        :param entity: Сущность, осуществляющая продажу.
        :param thing: Название предмета.
        """
        new_thing = entity.trading(self._money, thing)
        if new_thing:
            self.inventory.append(new_thing)
            self._money -= new_thing.price

    def move(self, kind: str, *args, **kwargs) -> None:
        """
        Перемещает игрока.

        :param kind: Тип перемещения ("step" или абсолютное перемещение).
        :param args: Аргументы перемещения (например, направление или координаты).
        """
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
        """
        Геттер для денег игрока.
        """
        return self._money

    @money.setter
    def money(self, value: int):
        """
        Сеттер для денег игрока.
        """
        self._money = value
