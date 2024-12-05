from entity import Entity
from management.game_manager import GameManager
from map.room import Room
from objects.objects import Object

class NPC(Entity):
	def __init__(self, game_manager: GameManager, room: Room):
		super().__init__(game_manager, room)
		print(f'появился {Entity.name}')
	def action(self, entity : Entity, kind : str) -> None:
		pass
	def use_inventory(self) -> Object:
		pass
	
	
class trader(NPC):
	def __init__(self, game_manager : GameManager, room: Room):
		super().__init__(game_manager, room)
	
	def action(self, entity : Entity, kind : str) -> None:
		pass

	def use_inventory(self) -> Object:
		pass
	def trading(self, money, name_bread):
		if name_bread in self.inventory and self.inventory[name_bread].cost <= money:
			tmp = self.inventory[name_bread]
			self.inventory.remove(name_bread)
			print(f"Поздравляю с покупкой {name_bread}")
			return tmp
		else:
			if name_bread in self.inventory:
				print(f'Ты что то путаешь у меня нет {name_bread}')
			else:
				print(f'Тебе не хватает {self.inventory[name_bread].cost - money}')
			return None

class robber(NPC):
	def action(self, entity : Entity, kind : str) -> None:
		pass
	def use_inventory(self) -> Object:
		pass
	def underattack(self, entity : Entity, damage : int):
		entity.health =- damage
		if entity.health <= 0:
			entity.notify("lose")
		