class Player:
    def __init__(self, game_manager : GameManager, health : int, damage : int, room: Room, inventory: list[Object], subscribers: list[Room | Entity | Object]):
        super().__init__(game_manager, health, damage, room, inventory, subscribers)
        
    def action(self, entity : Entity, kind : str, *args, **kwargs) -> None:
        match (kind):
            case ("attack"):
                self.attack(entity, *args, **kwargs)
            case (_):
                print("Ничего не произошло")
                
    def attack(self, entity, *args, **kwargs):
        pass
