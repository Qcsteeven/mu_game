import json
from abc import ABC, abstractmethod


# Базовый класс
class Object(ABC):
    def __init__(self, name, description, quality, price):
        self.name = name
        self.description = description
        self.quality = quality
        self.price = price

    @abstractmethod
    def create_object(self):
        pass


# Класс Potion
class Potion(Object):
    def __init__(self, name, description, quality, healing, price):
        super().__init__(name, description, quality, price)
        self.healing = healing

    def create_object(self):
        return {
            "name": self.name,
            "description": self.description,
            "quality": self.quality,
            "healing": self.healing,
            "price": self.price
        }


# Класс Armor
class Armor(Object):
    def __init__(self, name, description, quality, defense, price):
        super().__init__(name, description, quality, price)
        self.defense = defense

    def create_object(self):
        return {
            "name": self.name,
            "description": self.description,
            "quality": self.quality,
            "defense": self.defense,
            "price": self.price
        }


# Класс Weapon
class Weapon(Object):
    def __init__(self, name, description, quality, attack, price):
        super().__init__(name, description, quality, price)
        self.attack = attack

    def create_object(self):
        return {
            "name": self.name,
            "description": self.description,
            "quality": self.quality,
            "attack": self.attack,
            "price": self.price
        }


# Функция загрузки данных из JSON
def load_items_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    items = []
    for item_type, objects in data["items"].items():
        for obj in objects:
            if item_type == "healing_potion":
                items.append(Potion(obj["name"], obj["description"], obj["quality"], obj["healing"], obj["price"]))
            elif item_type == "armor":
                items.append(Armor(obj["name"], obj["description"], obj["quality"], obj["defense"], obj["price"]))
            elif item_type == "sword":
                items.append(Weapon(obj["name"], obj["description"], obj["quality"], obj["attack"], obj["price"]))

    return items


# Пример использования
if __name__ == "__main__":
    items = load_items_from_json("../management/text.json")
    for item in items:
        print(item.create_object())
