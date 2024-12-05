import json
from abc import ABC, abstractmethod


# Базовый класс
class ObjectCreator(ABC):
    def __init__(self, name, description, quality):
        self.name = name
        self.description = description
        self.quality = quality

    @abstractmethod
    def create_object(self):
        pass


# Класс Potion
class Potion(ObjectCreator):
    def __init__(self, name, description, quality, healing):
        super().__init__(name, description, quality)
        self.healing = healing

    def create_object(self):
        return {
            "name": self.name,
            "description": self.description,
            "quality": self.quality,
            "healing": self.healing
        }


# Класс Armor
class Armor(ObjectCreator):
    def __init__(self, name, description, quality, defense):
        super().__init__(name, description, quality)
        self.defense = defense

    def create_object(self):
        return {
            "name": self.name,
            "description": self.description,
            "quality": self.quality,
            "defense": self.defense
        }


# Класс Weapon
class Weapon(ObjectCreator):
    def __init__(self, name, description, quality, attack):
        super().__init__(name, description, quality)
        self.attack = attack

    def create_object(self):
        return {
            "name": self.name,
            "description": self.description,
            "quality": self.quality,
            "attack": self.attack
        }


# Функция загрузки данных из JSON
def load_items_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    items = []
    for item_type, objects in data["items"].items():
        for obj in objects:
            if item_type == "healing_potion":
                items.append(Potion(obj["name"], obj["description"], obj["quality"], obj["healing"]))
            elif item_type == "armor":
                items.append(Armor(obj["name"], obj["description"], obj["quality"], obj["defense"]))
            elif item_type == "sword":
                items.append(Weapon(obj["name"], obj["description"], obj["quality"], obj["attack"]))

    return items


# Пример использования
if __name__ == "__main__":
    items = load_items_from_json("../management/text.json")
    for item in items:
        print(item.create_object())
