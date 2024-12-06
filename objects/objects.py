import json
from abc import ABC, abstractmethod
import random

# Базовый класс
class Object(ABC):
    def __init__(self, item_type, name, description, quality, price):
        self.item_type = item_type
        self.name = name
        self.description = description
        self.quality = quality
        self.price = price

    @abstractmethod
    def create_object(self):
        pass


# Класс Potion
class Potion(Object):
    def __init__(self, item_type, name, description, quality, healing, price):
        super().__init__(item_type, name, description, quality, price)
        self.healing = healing

    def create_object(self):
        return {
            "type": self.item_type,
            "name": self.name,
            "description": self.description,
            "quality": self.quality,
            "healing": self.healing,
            "price": self.price
        }


# Класс Armor
class Armor(Object):
    def __init__(self, item_type, name, description, quality, defense, price):
        super().__init__(item_type, name, description, quality, price)
        self.defense = defense

    def create_object(self):
        return {
            "type": self.item_type,
            "name": self.name,
            "description": self.description,
            "quality": self.quality,
            "defense": self.defense,
            "price": self.price
        }


# Класс Weapon
class Weapon(Object):
    def __init__(self, item_type, name, description, quality, attack, price):
        super().__init__(item_type, name, description, quality, price)
        self.attack = attack

    def create_object(self):
        return {
            "type": self.item_type,
            "name": self.name,
            "description": self.description,
            "quality": self.quality,
            "attack": self.attack,
            "price": self.price
        }

def load_set_items_npc_json(stri : str, filename : str):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    items = []
    for item_type, objects in data["items"].items():
        if item_type == 'armor' or item_type == 'sword':
            for obj in objects:
                if (obj['quality'] == stri):
                    if item_type == "armor":
                        items.append(Armor("armor", obj["name"], obj["description"], obj["quality"], obj["defense"],
                                           obj["price"]))
                    else:
                        items.append(Weapon("sword", obj["name"], obj["description"], obj["quality"], obj["attack"],
                                            obj["price"]))
    return items
# Функция загрузки данных из JSON
def load_items_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    items = []
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


def return_item():
    items = load_items_from_json("../management/text.json")
    return random.choice(items).create_object()


# Пример использования
if __name__ == "__main__":
    items = load_items_from_json("../management/text.json")
    for item in items:
        print(item.create_object())
