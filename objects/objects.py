import json
from abc import ABC, abstractmethod
import random


# Базовый класс, представляющий объект. Все игровые объекты (зелья, броня, оружие) наследуют этот класс.
class Object(ABC):
    def __init__(self, item_type, name, description, quality, price):
        # Инициализация общих свойств объекта.
        self.item_type = item_type  # Тип объекта (например, зелье, броня, оружие).
        self.name = name  # Название объекта.
        self.description = description  # Описание объекта.
        self.quality = quality  # Качество объекта (например, "обычное", "редкое").
        self.price = price  # Цена объекта.

    @abstractmethod
    def create_object(self):
        # Абстрактный метод для создания объекта. Должен быть реализован в подклассах.
        pass


# Класс, представляющий зелье.
class Potion(Object):
    def __init__(self, item_type, name, description, quality, healing, price):
        super().__init__(item_type, name, description, quality, price)
        self.healing = healing  # Лечебный эффект зелья.

    def create_object(self):
        # Возвращает словарь, представляющий свойства зелья.
        return {
            "type": self.item_type,
            "name": self.name,
            "description": self.description,
            "quality": self.quality,
            "healing": self.healing,
            "price": self.price
        }


# Класс, представляющий броню.
class Armor(Object):
    def __init__(self, item_type, name, description, quality, defense, price):
        super().__init__(item_type, name, description, quality, price)
        self.defense = defense  # Защитные характеристики брони.

    def create_object(self):
        # Возвращает словарь, представляющий свойства брони.
        return {
            "type": self.item_type,
            "name": self.name,
            "description": self.description,
            "quality": self.quality,
            "defense": self.defense,
            "price": self.price
        }


# Класс, представляющий оружие.
class Weapon(Object):
    def __init__(self, item_type, name, description, quality, attack, price):
        super().__init__(item_type, name, description, quality, price)
        self.attack = attack  # Атакующие характеристики оружия.

    def create_object(self):
        # Возвращает словарь, представляющий свойства оружия.
        return {
            "type": self.item_type,
            "name": self.name,
            "description": self.description,
            "quality": self.quality,
            "attack": self.attack,
            "price": self.price
        }


# Функция для загрузки и фильтрации предметов из JSON-файла по качеству.
def load_set_items_npc_json(stri: str, filename: str):
    # Открытие JSON-файла с данными о предметах.
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    items = []  # Список для хранения объектов.
    # Проходим по всем предметам, группированным по их типам.
    for item_type, objects in data["items"].items():
        if item_type == 'armor' or item_type == 'sword':  # Учитываются только броня и мечи.
            for obj in objects:
                if obj['quality'] == stri:  # Фильтруем по указанному качеству.
                    if item_type == "armor":
                        items.append(Armor("armor", obj["name"], obj["description"], obj["quality"], obj["defense"],
                                           obj["price"]))
                    else:
                        items.append(Weapon("sword", obj["name"], obj["description"], obj["quality"], obj["attack"],
                                            obj["price"]))
    return items


# Функция для загрузки всех предметов из JSON-файла.
def load_items_from_json(filename):
    # Открытие JSON-файла.
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    items = []  # Список для хранения объектов.
    # Обрабатываем каждый предмет, добавляя его в соответствующий класс.
    for item_type, objects in data["items"].items():
        for obj in objects:
            if item_type == "healing_potion":
                items.append(Potion("healing_potion", obj["name"], obj["description"], obj["quality"], obj["healing"],
                                    obj["price"]))
            elif item_type == "armor":
                items.append(Armor("armor", obj["name"], obj["description"], obj["quality"], obj["defense"],
                                   obj["price"]))
            elif item_type == "sword":
                items.append(Weapon("sword", obj["name"], obj["description"], obj["quality"], obj["attack"],
                                    obj["price"]))
    return items


# Функция для случайного выбора предмета из списка.
def return_item():
    items = load_items_from_json("../management/text.json")  # Загрузка предметов из файла.
    return random.choice(items).create_object()  # Возвращает случайный объект в виде словаря.


# Пример использования программы.
if __name__ == "__main__":
    items = load_items_from_json("../management/text.json")  # Загрузка всех предметов из файла.
    for item in items:
        print(item.create_object())  # Вывод информации о каждом объекте.
