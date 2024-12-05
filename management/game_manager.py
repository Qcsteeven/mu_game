import json
import random
from map.config_room import Adapter
from map.create_map import PatCreator
from map.map import Map
from entities.player import Player
from entities.npc import robber 


class GameManager:
    _instance = None  # Приватное поле для хранения единственного экземпляра
    isCreated = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if GameManager.isCreated:
            return
        GameManager.isCreated = True
        settings = Adapter.adapt("config.json")
        pattern = PatCreator.create_2d_array(settings["rows"],settings["cols"],settings["d_count"])
        self._entities = [robber(GameManager)]
        self._map = Map(pattern, self._entities)
        try:
            with open('text.JSON', 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.ending_phrases = data.get("ending", [])
        except FileNotFoundError:
            print("Файл с данными не найден.")
        except json.JSONDecodeError:
            print("Ошибка при чтении JSON файла.")
        
        self.player = Player(self)
        self.player.room = self._map.get_room(0, 0)
        self.menu()
        
    def menu(self):
        print("Приветствуем в игре mu_game")
        name = input("Выберите имя: ")
        self.player.name = name
        while True:
            direction = input("Выберите направление движения (направо\налево\вверх\вниз): ")
            self.player.action("move", "step", direction)

    def update(self, notify_message : str, *args, **kwargs):
        match (notify_message):
            case ("lose"):
                if self.ending_phrases:
                    phrase = random.choice(self.ending_phrases)["dialogue"]
                else:
                    print("Нет доступных концовочных фраз.")
            case ("move"):
                self.change_player_position(*args, **kwargs)
    
    def change_player_position(self, position, *args):
        size_x, size_y = self._map.map_size()
        if position != ():
            x, y = position
            if -1 < x and x < size_x  and -1 < y and y < size_y:
                self.player.position = position
                self._map.show_map(position)
            
            
