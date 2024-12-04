class Player:
    def __init__(self, game_manager : GameManager, name : str, health : int, damage : int, room: Room, inventory: list[Object], subscribers: list[Room | Entity | Object]):
        super().__init__(game_manager, name, health, damage, room, inventory, subscribers)
        self._money = 0
        
    def action(self, entity : Entity, kind : str, *args, **kwargs) -> None:
        match (kind):
            case ("attack"):
                self.attack(entity, *args, **kwargs)
            case ("buy"):
                self.buy(entity, *args, **kwargs)
            case ("move"):
                self.move(*args, **kwargs)
            case (_):
                print("Хммм... Я так не умею")

    def attack(self, entity : Entity, damage : int) -> None:
        if entity.health - damage > 0:
            entity.health -= damage
        else:
            entity.health = 0
            entity.notify("kill", entity)

    def buy(self, entity : Entity, thing : str):
        new_thing = entity.trading(self._money, thing)
        if new_thing:
            self.inventory.append(new_thing)
            self._money -= new_thing.cost
    
    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, value : int):
        self._money = value
