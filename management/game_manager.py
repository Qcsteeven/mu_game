import json
import random


class GameManager:
    _instance = None  # Приватное поле для хранения единственного экземпляра
    isCreated = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, settings=None):
        if GameManager.isCreated:
            return
        GameManager.isCreated = True
        # self._map = Map(settings)
        # self._entities = []
        self._map = ["Карта"]
        try:
            with open('text.JSON', 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.ending_phrases = data.get("ending", [])
        except FileNotFoundError:
            print("Файл с данными не найден.")
        except json.JSONDecodeError:
            print("Ошибка при чтении JSON файла.")

    def update(self, notify_message, *args, **kwargs):
        # В зависимости от сообщения, сделать какое-то взаимодействие игры и персонажа
        match notify_message:
            case "lose":
                if self.ending_phrases:
                    phrase = random.choice(self.ending_phrases)["dialogue"]
                    print(phrase)
                else:
                    print("Нет доступных концовочных фраз.")
