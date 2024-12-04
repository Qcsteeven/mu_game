class Room:
    def __init__(self, isSafe: bool, creations: list[Entity], objects: list[Objects], roomEffect: list[roomEffect]):
        self.isSafe = isSafe
        self.creations = creations
        self.objects = objects
        self.roomEffect = roomEffect

    
    def update(self):
        pass
    
    def applyEffect(self):
        pass

    def dischargeEffect(self):
        pass
