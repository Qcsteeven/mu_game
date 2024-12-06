import json
import random
from map.config_room import Adapter
from map.create_map import PatCreator
from map.map import Map
from entities.player import Player
from entities.npc import robber
from management.effects import Effect

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
        self.px, self.py = 0, 0
        settings = Adapter.adapt("config.json")
        self.pattern = PatCreator.create_2d_array(settings["rows"], settings["cols"], settings["d_count"])
        self._entities = [robber(GameManager, "epic")]
        self._map = Map(self.pattern, self._entities)
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

    def check_player_position(self):
        x, y = self.player.position
        current_room = self._map.get_room(x, y)

        directions_tuple = self._map.avail_directions(x, y)

        directions_map = ["вверх", "вниз", "влево", "вправо"]

        available_directions = [
            direction for i, direction in enumerate(directions_map) if directions_tuple[i]
        ]

        if available_directions:
            print("Вы можете пойти: " + " и ".join(available_directions) + ".")
        else:
            print("Вы не можете никуда пойти.")

    def observe_room(self):
        x, y = self.player.position
        current_room = self._map.get_room(x, y)
        print("Тип комнаты, в которую вы вошли: ", current_room.type)
        print("Ваша комната наполнена существами ", *[elem.name for elem in current_room.creations])

    def new_game(self):
        print("Добро пожаловать в подземелье")
        print("Выберите имя: ")
        name = input()
        self.player.name = name

    def menu(self):
        while True:
            print("Выберите действие: walk, attack, trade, show")
            action = input()
            match action:
                case ("walk"):
                    print("Выберите направление, куда вы хотите пойти: ")
                    direction = input()
                    self.player.action("move", "step", direction)
                case ("attack"):
                    self.start_fight()
                case ("trade"):
                    if self.player.room.creations[0].type == "trader":
                        act = input("Вы хотите что-то купить или продать? (sell / buy) ")
                        if act == "buy":
                            self.player.room.creations[0].show_inventory()
                        else: 
                            self.player.show_inventory()
                        thing = input("Название предмета: ")
                        self.player.action(act, self.player.room.creations[0], thing)
                case ("show"):
                    self.player.action("show")
                case ("use"):
                    item = input("Название предмета:")
                    self.player.action("use", item)
            self.check_player_position()
            self.observe_room()

    def update(self, notify_message: str, *args, **kwargs):
        match (notify_message):
            case ("lose"):
                if self.ending_phrases:
                    phrase = random.choice(self.ending_phrases)["dialogue"]
                else:
                    print("Нет доступных концовочных фраз.")
            case ("move"):
                self.change_player_position(*args, **kwargs)
            case ("kill"):
                pass

    def start_fight(self):
        enemy = self.player.room.creations[0]
        print(f"Драка с {enemy.name}")
        self.player.action("attack", self.player.room.creations[0])
        

    def change_player_position(self, position, *args):
        size_x, size_y = self._map.map_size()

        if position != ():
            x, y = position
            
            
            if self.pattern[x][y] == 'B':
                vibor = input("Вы хотите зайти в покои босса (yes, no)? ").strip()
                if vibor.lower() == 'yes':
                    pass
                elif vibor.lower() == 'no':
                    print("Вы не рискнули посетить покои босса")
                    return 

            if -1 < x and x < size_x and -1 < y and y < size_y:
                
                self._map.make_visited(x, y)
                self.player.position = position
                self.player.room = self._map.get_room(x, y)
                eff = Effect()
                eff(self.player.room)
                self._map.show_map(position)
                self.px = x
                self.py = y
